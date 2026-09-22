/**
 * AceroMAX — Tu Espacio — Cloudflare Worker
 * Proxy para OpenAI Image Edit API (renderizado de pintura con IA)
 *
 * DEPLOY:
 * 1. Ve a dash.cloudflare.com > Workers & Pages > Create
 * 2. Nombre: "tuespacio-api"
 * 3. Pega este código en el editor
 * 4. Settings > Variables > Add:
 *    - OPENAI_API_KEY = tu clave de OpenAI (encrypt)
 * 5. (Opcional) Agrega KV Namespace "RATE_LIMIT" para rate limiting persistente
 * 6. El Worker URL será algo como: https://tuespacio-api.tu-cuenta.workers.dev
 * 7. Actualiza WORKER_URL en tuespacio/index.html con esa URL
 *
 * COSTOS OPENAI (aprox):
 * - gpt-image-1: ~$0.02-0.08 por imagen (depende de tamaño)
 * - Para un negocio local: ~5-20 renders/día = $0.10-1.60/día
 */

const ALLOWED_ORIGINS = [
  'https://aceromax.mx',
  'https://www.aceromax.mx',
  'http://localhost:3000', // dev
];

const RATE_LIMIT_PER_HOUR = 5;
const RATE_LIMIT_PER_DAY = 15;
const GLOBAL_DAILY_CAP = 200;
const MAX_IMAGE_SIZE_MB = 10;
const TIMEOUT_MS = 60000;

// In-memory rate limit (resets on Worker restart — for persistent, use KV)
const rateLimits = {};
let globalDailyCount = 0;
let globalDailyReset = Date.now() + 86400000;

function getCorsHeaders(origin) {
  if (ALLOWED_ORIGINS.includes(origin)) {
    return {
      'Access-Control-Allow-Origin': origin,
      'Access-Control-Allow-Methods': 'POST, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type',
      'Access-Control-Max-Age': '86400',
    };
  }
  return {};
}

function checkRateLimit(ip) {
  const now = Date.now();

  // Reset global daily cap
  if (now > globalDailyReset) {
    globalDailyCount = 0;
    globalDailyReset = now + 86400000;
  }

  if (globalDailyCount >= GLOBAL_DAILY_CAP) {
    return { allowed: false, reason: 'Límite global diario alcanzado. Intenta mañana.' };
  }

  if (!rateLimits[ip]) {
    rateLimits[ip] = { hourly: [], daily: [] };
  }

  const rl = rateLimits[ip];

  // Clean old entries
  rl.hourly = rl.hourly.filter(t => now - t < 3600000);
  rl.daily = rl.daily.filter(t => now - t < 86400000);

  if (rl.hourly.length >= RATE_LIMIT_PER_HOUR) {
    return { allowed: false, reason: `Máximo ${RATE_LIMIT_PER_HOUR} renders por hora. Espera un momento.` };
  }

  if (rl.daily.length >= RATE_LIMIT_PER_DAY) {
    return { allowed: false, reason: `Máximo ${RATE_LIMIT_PER_DAY} renders por día. Intenta mañana.` };
  }

  rl.hourly.push(now);
  rl.daily.push(now);
  globalDailyCount++;

  return { allowed: true };
}

function base64ToBlob(base64, mime) {
  const byteChars = atob(base64);
  const byteArrays = [];
  for (let offset = 0; offset < byteChars.length; offset += 512) {
    const slice = byteChars.slice(offset, offset + 512);
    const byteNumbers = new Array(slice.length);
    for (let i = 0; i < slice.length; i++) {
      byteNumbers[i] = slice.charCodeAt(i);
    }
    byteArrays.push(new Uint8Array(byteNumbers));
  }
  return new Blob(byteArrays, { type: mime });
}

export default {
  async fetch(request, env) {
    const origin = request.headers.get('Origin') || '';
    const corsHeaders = getCorsHeaders(origin);

    // Handle CORS preflight
    if (request.method === 'OPTIONS') {
      return new Response(null, { status: 204, headers: corsHeaders });
    }

    if (request.method !== 'POST') {
      return new Response(JSON.stringify({ error: 'Método no permitido' }), {
        status: 405,
        headers: { ...corsHeaders, 'Content-Type': 'application/json' },
      });
    }

    try {
      // Rate limiting
      const ip = request.headers.get('CF-Connecting-IP') || request.headers.get('X-Forwarded-For') || 'unknown';
      const rlCheck = checkRateLimit(ip);
      if (!rlCheck.allowed) {
        return new Response(JSON.stringify({ error: rlCheck.reason }), {
          status: 429,
          headers: { ...corsHeaders, 'Content-Type': 'application/json' },
        });
      }

      // Parse request
      const body = await request.json();
      const { image_base64, color_name, color_hex, acabado, mime_type } = body;

      if (!image_base64 || !color_name || !color_hex) {
        return new Response(JSON.stringify({ error: 'Faltan campos requeridos: image_base64, color_name, color_hex' }), {
          status: 400,
          headers: { ...corsHeaders, 'Content-Type': 'application/json' },
        });
      }

      // Size check
      const imageSizeBytes = (image_base64.length * 3) / 4;
      if (imageSizeBytes > MAX_IMAGE_SIZE_MB * 1024 * 1024) {
        return new Response(JSON.stringify({ error: `La imagen es demasiado grande. Máximo ${MAX_IMAGE_SIZE_MB}MB.` }), {
          status: 400,
          headers: { ...corsHeaders, 'Content-Type': 'application/json' },
        });
      }

      // Build the prompt
      const finish = acabado || 'mate';
      const prompt = `Repaint ONLY the walls in this photograph with "${color_name}" paint (approximately ${color_hex} hex color, ${finish} finish). ` +
        `Change ONLY the wall surfaces to this exact color. ` +
        `Keep absolutely everything else exactly as it is: all furniture, fixtures, floors, ceilings, doors, windows, light fixtures, shelving, decorative elements, and any objects in the room. ` +
        `The repainted walls should look photorealistic with natural lighting, subtle paint texture appropriate for a ${finish} finish, and correct shadows. ` +
        `Do not change the room layout, perspective, or any non-wall surface.`;

      // Convert base64 to blob
      const mimeType = mime_type || 'image/jpeg';
      const ext = mimeType.includes('png') ? 'png' : 'jpg';
      const imageBlob = base64ToBlob(image_base64, mimeType);

      // Build multipart form data for OpenAI
      const formData = new FormData();
      formData.append('model', 'gpt-image-1');
      formData.append('image[]', imageBlob, `photo.${ext}`);
      formData.append('prompt', prompt);
      formData.append('size', 'auto');
      formData.append('quality', 'medium');

      // Call OpenAI
      const controller = new AbortController();
      const timeout = setTimeout(() => controller.abort(), TIMEOUT_MS);

      const openaiResponse = await fetch('https://api.openai.com/v1/images/edits', {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${env.OPENAI_API_KEY}`,
        },
        body: formData,
        signal: controller.signal,
      });

      clearTimeout(timeout);

      if (!openaiResponse.ok) {
        const errorText = await openaiResponse.text();
        console.error('OpenAI error:', openaiResponse.status, errorText);
        let debugMsg = '';
        try { debugMsg = JSON.parse(errorText)?.error?.message || errorText.substring(0, 200); } catch(e) { debugMsg = errorText.substring(0, 200); }
        return new Response(JSON.stringify({
          error: 'Error al procesar la imagen. Intenta con otra foto.',
          debug: debugMsg,
          details: openaiResponse.status,
        }), {
          status: 502,
          headers: { ...corsHeaders, 'Content-Type': 'application/json' },
        });
      }

      const result = await openaiResponse.json();
      let editedImageBase64 = result.data?.[0]?.b64_json;

      // Si OpenAI devuelve URL en vez de b64, descargar y convertir
      if (!editedImageBase64 && result.data?.[0]?.url) {
        try {
          const imgResp = await fetch(result.data[0].url);
          const imgBuf = await imgResp.arrayBuffer();
          const bytes = new Uint8Array(imgBuf);
          let binary = '';
          for (let i = 0; i < bytes.length; i++) binary += String.fromCharCode(bytes[i]);
          editedImageBase64 = btoa(binary);
        } catch (e) {
          console.error('Error downloading image from URL:', e);
        }
      }

      if (!editedImageBase64) {
        return new Response(JSON.stringify({ error: 'No se recibió imagen del servicio de IA.' }), {
          status: 502,
          headers: { ...corsHeaders, 'Content-Type': 'application/json' },
        });
      }

      return new Response(JSON.stringify({
        image_base64: editedImageBase64,
        color_name,
        color_hex,
      }), {
        status: 200,
        headers: { ...corsHeaders, 'Content-Type': 'application/json' },
      });

    } catch (err) {
      if (err.name === 'AbortError') {
        return new Response(JSON.stringify({ error: 'Tiempo de espera agotado (60s). Intenta con una imagen más pequeña.' }), {
          status: 504,
          headers: { ...corsHeaders, 'Content-Type': 'application/json' },
        });
      }
      console.error('Worker error:', err);
      return new Response(JSON.stringify({ error: 'Error interno del servidor.' }), {
        status: 500,
        headers: { ...corsHeaders, 'Content-Type': 'application/json' },
      });
    }
  },
};
