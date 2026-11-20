/**
 * AceroMAX API — Servidor de pagos con MercadoPago Checkout Pro
 *
 * Este servicio maneja:
 * - Creación de preferencias de pago (Checkout Pro)
 * - Recepción de webhooks de MercadoPago
 * - Lógica de envío (gratis en Cd. Victoria > $1,000)
 *
 * Deploy: Render.com (web service Node.js)
 */

require('dotenv').config();
const express = require('express');
const cors = require('cors');
const { MercadoPagoConfig, Preference, Payment } = require('mercadopago');
const nodemailer = require('nodemailer');

const app = express();
const PORT = process.env.PORT || 3001;
const FRONTEND_URL = process.env.FRONTEND_URL || 'https://aceromax.mx';

// ============================================================
// Configuración de MercadoPago
// ============================================================
const mpClient = new MercadoPagoConfig({
  accessToken: process.env.MP_ACCESS_TOKEN,
  options: { timeout: 5000 }
});

const preferenceClient = new Preference(mpClient);
const paymentClient = new Payment(mpClient);

// ============================================================
// Configuración de Email (Nodemailer)
// ============================================================
const NOTIFY_EMAIL = process.env.NOTIFY_EMAIL || 'acero2@aceromax.mx';

const emailTransporter = nodemailer.createTransport({
  service: 'gmail',
  auth: {
    user: process.env.SMTP_USER,       // acero2@aceromax.mx
    pass: process.env.SMTP_PASSWORD    // App Password de Google
  }
});

/**
 * Envía correo de notificación de venta al equipo AceroMAX
 */
async function enviarCorreoVenta(info, items) {
  if (!process.env.SMTP_USER || !process.env.SMTP_PASSWORD) {
    console.log('[Email] SMTP no configurado, saltando notificación por correo');
    return;
  }

  const fecha = new Date(info.date).toLocaleString('es-MX', {
    timeZone: 'America/Monterrey',
    dateStyle: 'long',
    timeStyle: 'short'
  });

  const metodos = {
    'credit_card': 'Tarjeta de crédito',
    'debit_card': 'Tarjeta de débito',
    'account_money': 'Dinero en cuenta MercadoPago',
    'ticket': 'Pago en efectivo (OXXO)',
    'bank_transfer': 'Transferencia bancaria (SPEI)',
    'atm': 'Cajero automático'
  };
  const metodo = metodos[info.payment_method] || info.payment_method;

  // Construir tabla de productos si hay items
  let productosHTML = '';
  if (items && items.length > 0) {
    const filas = items
      .filter(i => i.id !== 'envio')
      .map(i => `
        <tr>
          <td style="padding:8px 12px;border-bottom:1px solid #eee;">${i.title}</td>
          <td style="padding:8px 12px;border-bottom:1px solid #eee;text-align:center;">${i.quantity}</td>
          <td style="padding:8px 12px;border-bottom:1px solid #eee;text-align:right;">$${(i.unit_price * i.quantity).toLocaleString('es-MX', {minimumFractionDigits:2})}</td>
        </tr>
      `).join('');

    const envioItem = items.find(i => i.id === 'envio');
    const envioHTML = envioItem
      ? `<tr style="background:#f0fdf4;">
          <td style="padding:8px 12px;" colspan="2"><strong>Envío</strong></td>
          <td style="padding:8px 12px;text-align:right;">$${envioItem.unit_price.toLocaleString('es-MX', {minimumFractionDigits:2})}</td>
        </tr>`
      : `<tr style="background:#f0fdf4;">
          <td style="padding:8px 12px;" colspan="2"><strong>Envío</strong></td>
          <td style="padding:8px 12px;text-align:right;color:#25D366;font-weight:bold;">GRATIS</td>
        </tr>`;

    productosHTML = `
      <table style="width:100%;border-collapse:collapse;margin:16px 0;">
        <thead>
          <tr style="background:#1B2A4A;color:#fff;">
            <th style="padding:10px 12px;text-align:left;">Producto</th>
            <th style="padding:10px 12px;text-align:center;">Cant.</th>
            <th style="padding:10px 12px;text-align:right;">Subtotal</th>
          </tr>
        </thead>
        <tbody>
          ${filas}
          ${envioHTML}
          <tr style="background:#1B2A4A;color:#fff;">
            <td style="padding:10px 12px;" colspan="2"><strong>TOTAL</strong></td>
            <td style="padding:10px 12px;text-align:right;font-size:1.1em;"><strong>$${info.amount.toLocaleString('es-MX', {minimumFractionDigits:2})} MXN</strong></td>
          </tr>
        </tbody>
      </table>
    `;
  }

  const html = `
    <div style="font-family:'Segoe UI',system-ui,sans-serif;max-width:600px;margin:0 auto;">
      <div style="background:#1B2A4A;color:#fff;padding:20px 24px;border-radius:8px 8px 0 0;">
        <h1 style="margin:0;font-size:22px;">&#x2705; Nueva Venta en AceroMAX</h1>
        <p style="margin:6px 0 0;opacity:0.85;font-size:14px;">${fecha}</p>
      </div>

      <div style="background:#fff;padding:24px;border:1px solid #e5e7eb;border-top:none;">
        <div style="background:#f0fdf4;border-left:4px solid #25D366;padding:16px;border-radius:0 8px 8px 0;margin-bottom:20px;">
          <div style="font-size:28px;font-weight:800;color:#1B2A4A;">$${info.amount.toLocaleString('es-MX', {minimumFractionDigits:2})} MXN</div>
          <div style="color:#666;font-size:14px;margin-top:4px;">Pago aprobado — ${metodo}</div>
        </div>

        <table style="width:100%;font-size:14px;margin-bottom:16px;">
          <tr><td style="padding:6px 0;color:#666;">ID de pago:</td><td style="padding:6px 0;font-weight:600;">${info.id}</td></tr>
          <tr><td style="padding:6px 0;color:#666;">Referencia:</td><td style="padding:6px 0;font-weight:600;">${info.external_reference}</td></tr>
          <tr><td style="padding:6px 0;color:#666;">Email cliente:</td><td style="padding:6px 0;font-weight:600;">${info.payer_email || 'No proporcionado'}</td></tr>
          <tr><td style="padding:6px 0;color:#666;">Estado:</td><td style="padding:6px 0;font-weight:600;color:#25D366;">APROBADO &#x2713;</td></tr>
        </table>

        ${productosHTML}

        <div style="text-align:center;margin-top:20px;">
          <a href="https://www.mercadopago.com.mx/activities" style="display:inline-block;background:#2563EB;color:#fff;padding:12px 28px;border-radius:8px;text-decoration:none;font-weight:700;font-size:14px;">Ver en MercadoPago</a>
        </div>
      </div>

      <div style="background:#f9fafb;padding:16px 24px;border:1px solid #e5e7eb;border-top:none;border-radius:0 0 8px 8px;text-align:center;">
        <p style="margin:0;font-size:12px;color:#9ca3af;">AceroMAX — Blvd. Tamaulipas 3700, Cd. Victoria, Tam. — (834) 110-0942</p>
      </div>
    </div>
  `;

  try {
    await emailTransporter.sendMail({
      from: `"AceroMAX Ventas" <${process.env.SMTP_USER}>`,
      to: NOTIFY_EMAIL,
      subject: `💰 Nueva venta $${info.amount.toLocaleString('es-MX', {minimumFractionDigits:2})} MXN — ${metodo}`,
      html: html
    });
    console.log(`[Email] Notificación enviada a ${NOTIFY_EMAIL}`);
  } catch (emailError) {
    console.error('[Email] Error enviando correo:', emailError.message);
  }
}

// ============================================================
// Middleware
// ============================================================

// CORS — permitir solo orígenes autorizados
const allowedOrigins = [
  FRONTEND_URL,
  'https://aceromax.mx',
  'https://www.aceromax.mx',
  'http://localhost:3000',
  'http://localhost:5500',
  'http://127.0.0.1:5500'
];

app.use(cors({
  origin: function (origin, callback) {
    // Permitir requests sin origin (como mobile apps o curl)
    if (!origin) return callback(null, true);
    if (allowedOrigins.some(allowed => origin.startsWith(allowed))) {
      return callback(null, true);
    }
    callback(new Error('No permitido por CORS'));
  },
  methods: ['GET', 'POST'],
  allowedHeaders: ['Content-Type', 'Authorization']
}));

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Log de requests en desarrollo
if (process.env.NODE_ENV !== 'production') {
  app.use((req, res, next) => {
    console.log(`[${new Date().toISOString()}] ${req.method} ${req.path}`);
    next();
  });
}

// ============================================================
// Rutas
// ============================================================

/**
 * GET /api/health
 * Health check para Render y monitoreo
 */
app.get('/api/health', (req, res) => {
  res.json({
    status: 'ok',
    service: 'aceromax-api',
    timestamp: new Date().toISOString(),
    mp_configured: !!process.env.MP_ACCESS_TOKEN
  });
});

/**
 * GET /api/public-key
 * Retorna la public key de MercadoPago para el frontend
 */
app.get('/api/public-key', (req, res) => {
  if (!process.env.MP_PUBLIC_KEY) {
    return res.status(500).json({ error: 'Public key no configurada' });
  }
  res.json({ publicKey: process.env.MP_PUBLIC_KEY });
});

/**
 * POST /api/create-preference
 * Crea una preferencia de pago en MercadoPago Checkout Pro
 *
 * Body esperado:
 * {
 *   items: [{ id, title, quantity, unit_price, picture_url }],
 *   shipping: { cost, zone },
 *   payer: { name, email, phone }
 * }
 */
app.post('/api/create-preference', async (req, res) => {
  try {
    const { items, shipping, payer } = req.body;

    // --- Validación básica ---
    if (!items || !Array.isArray(items) || items.length === 0) {
      return res.status(400).json({ error: 'Se requiere al menos un producto' });
    }

    for (const item of items) {
      if (!item.title || !item.quantity || !item.unit_price) {
        return res.status(400).json({
          error: 'Cada producto necesita: title, quantity, unit_price'
        });
      }
      if (item.unit_price <= 0 || item.quantity <= 0) {
        return res.status(400).json({ error: 'Precio y cantidad deben ser positivos' });
      }
    }

    // --- Construir items para MercadoPago ---
    const mpItems = items.map(item => ({
      id: item.id || `prod-${Date.now()}`,
      title: item.title,
      description: item.description || `${item.title} — AceroMAX`,
      quantity: Number(item.quantity),
      unit_price: Number(item.unit_price),
      currency_id: 'MXN',
      picture_url: item.picture_url
        ? `${FRONTEND_URL}${item.picture_url}`
        : `${FRONTEND_URL}/images/logo.png`
    }));

    // --- Calcular costo de envío ---
    let shippingCost = 0;
    const shippingZone = shipping?.zone || 'victoria';

    if (shipping && typeof shipping.cost === 'number') {
      shippingCost = shipping.cost;
    } else {
      // Calcular según zona y subtotal
      const subtotal = mpItems.reduce((sum, i) => sum + (i.unit_price * i.quantity), 0);

      switch (shippingZone) {
        case 'victoria':
          shippingCost = subtotal >= 1000 ? 0 : 200;
          break;
        case 'tamaulipas-norte':
          shippingCost = 450;
          break;
        case 'tamaulipas-sur':
          shippingCost = 350;
          break;
        default:
          // Fuera de Tamaulipas: se cotiza por WhatsApp, no debería llegar aquí
          shippingCost = 0;
      }
    }

    // Si hay costo de envío, agregarlo como item
    if (shippingCost > 0) {
      mpItems.push({
        id: 'envio',
        title: `Envío a ${formatZoneName(shippingZone)}`,
        description: 'Costo de envío AceroMAX',
        quantity: 1,
        unit_price: shippingCost,
        currency_id: 'MXN'
      });
    }

    // --- Datos del comprador ---
    const payerData = {};
    if (payer) {
      if (payer.name) payerData.name = payer.name;
      if (payer.email) payerData.email = payer.email;
      if (payer.phone) {
        payerData.phone = {
          area_code: '834',
          number: payer.phone.replace(/\D/g, '')
        };
      }
    }

    // --- URL del webhook ---
    const apiUrl = process.env.API_URL || `https://aceromaxweb.onrender.com`;
    const notificationUrl = `${apiUrl}/api/webhook`;

    // --- Crear preferencia ---
    const preferenceBody = {
      items: mpItems,
      payer: Object.keys(payerData).length > 0 ? payerData : undefined,
      back_urls: {
        success: `${FRONTEND_URL}/checkout/resultado/?status=approved`,
        failure: `${FRONTEND_URL}/checkout/resultado/?status=rejected`,
        pending: `${FRONTEND_URL}/checkout/resultado/?status=pending`
      },
      auto_return: 'approved',
      statement_descriptor: 'ACEROMAX',
      notification_url: notificationUrl,
      external_reference: `order-${Date.now()}`,
      expires: false,
      payment_methods: {
        // Permitir hasta 12 meses sin intereses en compras grandes
        installments: 12,
        // No excluir ningún método — aceptar todo lo disponible en MX:
        // Tarjetas crédito/débito, OXXO, SPEI, Banamex, Santander, BBVA,
        // Cuenta de Mercado Pago, Meses sin Tarjeta
      },
      shipments: {
        cost: shippingCost,
        mode: 'not_specified'
      },
      metadata: {
        source: 'aceromax-web',
        shipping_zone: shippingZone,
        shipping_cost: shippingCost
      }
    };

    console.log(`[Preferencia] Creando con ${items.length} productos, envío: $${shippingCost} (${shippingZone})`);

    const preference = await preferenceClient.create({ body: preferenceBody });

    console.log(`[Preferencia] Creada: ${preference.id}`);

    res.json({
      id: preference.id,
      init_point: preference.init_point,
      sandbox_init_point: preference.sandbox_init_point
    });

  } catch (error) {
    console.error('[Error] Crear preferencia:', error.message || error);
    res.status(500).json({
      error: 'Error al crear la preferencia de pago',
      detail: process.env.NODE_ENV !== 'production' ? error.message : undefined
    });
  }
});

/**
 * POST /api/webhook
 * Recibe notificaciones de MercadoPago sobre pagos
 *
 * MercadoPago envía:
 * - topic: "payment" | "merchant_order"
 * - id: ID del recurso
 */
app.post('/api/webhook', async (req, res) => {
  try {
    const { type, data, action } = req.body;

    console.log(`[Webhook] Recibido: type=${type}, action=${action}, data=${JSON.stringify(data)}`);

    // MercadoPago envía notificaciones con type "payment"
    if (type === 'payment' && data?.id) {
      const paymentId = data.id;

      try {
        // Consultar detalles del pago
        const payment = await paymentClient.get({ id: paymentId });

        const info = {
          id: payment.id,
          status: payment.status,
          status_detail: payment.status_detail,
          amount: payment.transaction_amount,
          currency: payment.currency_id,
          payment_method: payment.payment_method_id,
          payer_email: payment.payer?.email,
          external_reference: payment.external_reference,
          date: payment.date_approved || payment.date_created
        };

        console.log(`[Pago] ${info.status}: $${info.amount} MXN — ${info.payment_method} — Ref: ${info.external_reference}`);

        // --- Notificar al equipo de AceroMAX ---
        if (payment.status === 'approved') {
          console.log(`[Pago APROBADO] $${info.amount} MXN`);
          console.log(`  Método: ${info.payment_method}`);
          console.log(`  Email: ${info.payer_email}`);
          console.log(`  Referencia: ${info.external_reference}`);

          // Obtener items de la preferencia si es posible
          let items = [];
          try {
            if (payment.additional_info?.items) {
              items = payment.additional_info.items;
            }
          } catch (e) { /* silent */ }

          // Enviar correo de notificación
          await enviarCorreoVenta(info, items);
        }

      } catch (paymentError) {
        console.error(`[Webhook] Error consultando pago ${paymentId}:`, paymentError.message);
      }
    }

    // Siempre responder 200 para que MercadoPago no reintente
    res.sendStatus(200);

  } catch (error) {
    console.error('[Webhook] Error:', error.message);
    res.sendStatus(200); // Responder 200 de todas formas
  }
});

/**
 * GET /api/order/:externalReference
 * Consultar estado de una orden por referencia externa
 */
app.get('/api/order/:ref', async (req, res) => {
  try {
    // Buscar pagos por external_reference
    const response = await fetch(
      `https://api.mercadopago.com/v1/payments/search?external_reference=${req.params.ref}`,
      {
        headers: {
          'Authorization': `Bearer ${process.env.MP_ACCESS_TOKEN}`
        }
      }
    );

    const data = await response.json();

    if (data.results && data.results.length > 0) {
      const payment = data.results[0];
      res.json({
        status: payment.status,
        amount: payment.transaction_amount,
        method: payment.payment_method_id,
        date: payment.date_approved || payment.date_created
      });
    } else {
      res.status(404).json({ error: 'Orden no encontrada' });
    }

  } catch (error) {
    console.error('[Error] Consultar orden:', error.message);
    res.status(500).json({ error: 'Error al consultar la orden' });
  }
});

// ============================================================
// Helpers
// ============================================================

/**
 * Formatea el nombre de la zona de envío para mostrarlo en MercadoPago
 */
function formatZoneName(zone) {
  const zones = {
    'victoria': 'Ciudad Victoria',
    'tamaulipas-norte': 'Tamaulipas (Zona Norte)',
    'tamaulipas-sur': 'Tamaulipas (Zona Sur)',
    'fuera-estado': 'Fuera del estado'
  };
  return zones[zone] || zone;
}

// ============================================================
// Manejo de errores global
// ============================================================
app.use((err, req, res, next) => {
  console.error('[Error global]', err.message);
  res.status(500).json({ error: 'Error interno del servidor' });
});

// ============================================================
// Iniciar servidor
// ============================================================
app.listen(PORT, () => {
  console.log(`
╔══════════════════════════════════════════╗
║   AceroMAX API — MercadoPago Checkout    ║
║   Puerto: ${PORT}                            ║
║   Frontend: ${FRONTEND_URL}  ║
║   MP configurado: ${!!process.env.MP_ACCESS_TOKEN ? 'Sí' : 'No — revisar .env'}              ║
╚══════════════════════════════════════════╝
  `);
});

module.exports = app;
