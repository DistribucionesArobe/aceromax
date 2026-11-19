/**
 * AceroMAX Shopping Cart System
 * Self-contained cart module for aceromax.mx
 * Includes: state management, shipping logic, UI widget, event system
 */
(function () {
  'use strict';

  /* ========== CONSTANTS ========== */
  var STORAGE_KEY = 'aceromax_cart';
  var ZONE_KEY = 'aceromax_shipping_zone';
  var FREE_SHIPPING_MIN = 1000;
  var SHIPPING_RATES = {
    victoria: { under: 200, over: 0 },
    tamaulipas: { under: 450, over: 350 },
    otro: { under: null, over: null } // cotizar por WhatsApp
  };
  var WHATSAPP_NUMBER = '528348528236';
  var CHECKOUT_URL = '/checkout/';

  /* ========== CART STATE ========== */
  function loadCart() {
    try {
      var data = localStorage.getItem(STORAGE_KEY);
      return data ? JSON.parse(data) : [];
    } catch (e) {
      return [];
    }
  }

  function saveCart(cart) {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(cart));
    } catch (e) { /* silent */ }
  }

  function loadZone() {
    try {
      return localStorage.getItem(ZONE_KEY) || 'victoria';
    } catch (e) {
      return 'victoria';
    }
  }

  function saveZone(zone) {
    try {
      localStorage.setItem(ZONE_KEY, zone);
    } catch (e) { /* silent */ }
  }

  /* ========== EVENT SYSTEM ========== */
  function emit(eventName, detail) {
    var evt;
    try {
      evt = new CustomEvent(eventName, { detail: detail || {} });
    } catch (e) {
      evt = document.createEvent('CustomEvent');
      evt.initCustomEvent(eventName, true, true, detail || {});
    }
    document.dispatchEvent(evt);
  }

  /* ========== FORMATTING ========== */
  function formatPrice(n) {
    var num = parseFloat(n) || 0;
    return '$' + num.toFixed(2).replace(/\B(?=(\d{3})+(?!\d))/g, ',') + ' MXN';
  }

  /* ========== CORE API ========== */
  var cart = loadCart();

  function findIndex(id) {
    for (var i = 0; i < cart.length; i++) {
      if (String(cart[i].id) === String(id)) return i;
    }
    return -1;
  }

  function addItem(product) {
    if (!product || !product.id || !product.name || product.price == null) return;
    var idx = findIndex(product.id);
    var qty = parseInt(product.quantity, 10) || 1;
    if (idx >= 0) {
      cart[idx].quantity += qty;
    } else {
      cart.push({
        id: String(product.id),
        name: product.name,
        price: parseFloat(product.price),
        quantity: qty,
        image: product.image || '',
        category: product.category || '',
        sku: product.sku || ''
      });
    }
    saveCart(cart);
    emit('cart:item-added', { item: product });
    emit('cart:updated', { cart: cart });
    renderWidget();
    showAddedFeedback(product.name);
  }

  function removeItem(id) {
    var idx = findIndex(id);
    if (idx < 0) return;
    var removed = cart.splice(idx, 1)[0];
    saveCart(cart);
    emit('cart:item-removed', { item: removed });
    emit('cart:updated', { cart: cart });
    renderWidget();
  }

  function updateQuantity(id, qty) {
    qty = parseInt(qty, 10);
    if (qty < 1) { removeItem(id); return; }
    var idx = findIndex(id);
    if (idx < 0) return;
    cart[idx].quantity = qty;
    saveCart(cart);
    emit('cart:updated', { cart: cart });
    renderWidget();
  }

  function getCart() {
    return cart.slice();
  }

  function getTotal() {
    var total = 0;
    for (var i = 0; i < cart.length; i++) {
      total += cart[i].price * cart[i].quantity;
    }
    return Math.round(total * 100) / 100;
  }

  function getItemCount() {
    var count = 0;
    for (var i = 0; i < cart.length; i++) {
      count += cart[i].quantity;
    }
    return count;
  }

  function clearCart() {
    cart = [];
    saveCart(cart);
    emit('cart:updated', { cart: cart });
    renderWidget();
  }

  /* ========== SHIPPING ========== */
  function getShippingCost(zone, subtotal) {
    zone = zone || loadZone();
    subtotal = subtotal != null ? subtotal : getTotal();
    var rate = SHIPPING_RATES[zone];
    if (!rate) return null; // unknown zone
    if (rate.under === null) return null; // cotizar
    return subtotal >= FREE_SHIPPING_MIN ? rate.over : rate.under;
  }

  function getShippingLabel(zone, subtotal) {
    var cost = getShippingCost(zone, subtotal);
    if (cost === null) return 'Cotizar por WhatsApp';
    if (cost === 0) return 'GRATIS';
    return formatPrice(cost);
  }

  function getOrderTotal(zone) {
    var sub = getTotal();
    var ship = getShippingCost(zone, sub);
    if (ship === null) return null;
    return Math.round((sub + ship) * 100) / 100;
  }

  /* ========== CSS INJECTION ========== */
  function injectStyles() {
    if (document.getElementById('acero-cart-styles')) return;
    var style = document.createElement('style');
    style.id = 'acero-cart-styles';
    style.textContent = [
      /* Cart floating icon */
      '#acero-cart-fab{position:fixed;bottom:90px;right:20px;z-index:99998;width:56px;height:56px;border-radius:50%;background:#1B2A4A;color:#fff;border:none;cursor:pointer;box-shadow:0 4px 16px rgba(0,0,0,.3);display:flex;align-items:center;justify-content:center;transition:transform .2s,background .2s}',
      '#acero-cart-fab:hover{transform:scale(1.08);background:#2563EB}',
      '#acero-cart-fab svg{width:26px;height:26px;fill:none;stroke:currentColor;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}',
      '#acero-cart-badge{position:absolute;top:-4px;right:-4px;background:#E53E3E;color:#fff;font-size:11px;font-weight:700;min-width:20px;height:20px;line-height:20px;border-radius:10px;text-align:center;padding:0 5px;font-family:system-ui,-apple-system,sans-serif}',
      '#acero-cart-badge:empty,#acero-cart-badge[data-count="0"]{display:none}',

      /* Overlay */
      '#acero-cart-overlay{position:fixed;inset:0;background:rgba(0,0,0,.45);z-index:99999;opacity:0;visibility:hidden;transition:opacity .3s}',
      '#acero-cart-overlay.open{opacity:1;visibility:visible}',

      /* Panel */
      '#acero-cart-panel{position:fixed;top:0;right:0;bottom:0;width:400px;max-width:92vw;background:#fff;z-index:100000;box-shadow:-4px 0 24px rgba(0,0,0,.18);transform:translateX(100%);transition:transform .35s cubic-bezier(.4,0,.2,1);display:flex;flex-direction:column;font-family:system-ui,-apple-system,sans-serif}',
      '#acero-cart-panel.open{transform:translateX(0)}',

      /* Panel header */
      '.ac-panel-header{background:#1B2A4A;color:#fff;padding:16px 20px;display:flex;align-items:center;justify-content:space-between;flex-shrink:0}',
      '.ac-panel-header h3{margin:0;font-size:18px;font-weight:700}',
      '.ac-panel-close{background:none;border:none;color:#fff;font-size:28px;cursor:pointer;line-height:1;padding:0 4px;opacity:.8;transition:opacity .2s}',
      '.ac-panel-close:hover{opacity:1}',

      /* Free shipping banner */
      '.ac-ship-banner{background:linear-gradient(135deg,#25D366,#128C7E);color:#fff;padding:10px 16px;font-size:13px;font-weight:600;text-align:center;flex-shrink:0;display:flex;align-items:center;justify-content:center;gap:6px}',
      '.ac-ship-banner svg{width:18px;height:18px;fill:none;stroke:#fff;stroke-width:2;flex-shrink:0}',

      /* Cart items list */
      '.ac-items{flex:1;overflow-y:auto;padding:0}',
      '.ac-empty{padding:40px 20px;text-align:center;color:#6B7280}',
      '.ac-empty svg{width:48px;height:48px;stroke:#CBD5E1;fill:none;stroke-width:1.5;margin-bottom:12px}',
      '.ac-empty p{margin:0 0 4px;font-size:15px}',
      '.ac-empty small{color:#9CA3AF;font-size:13px}',

      /* Item row */
      '.ac-item{display:flex;gap:12px;padding:14px 16px;border-bottom:1px solid #F3F4F6;align-items:flex-start}',
      '.ac-item-img{width:60px;height:60px;border-radius:8px;object-fit:cover;background:#F3F4F6;flex-shrink:0}',
      '.ac-item-img-placeholder{width:60px;height:60px;border-radius:8px;background:#F3F4F6;display:flex;align-items:center;justify-content:center;flex-shrink:0}',
      '.ac-item-img-placeholder svg{width:28px;height:28px;stroke:#9CA3AF;fill:none;stroke-width:1.5}',
      '.ac-item-info{flex:1;min-width:0}',
      '.ac-item-name{font-size:14px;font-weight:600;color:#1B2A4A;margin:0 0 2px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}',
      '.ac-item-cat{font-size:11px;color:#9CA3AF;margin:0 0 6px;text-transform:uppercase;letter-spacing:.5px}',
      '.ac-item-price{font-size:14px;font-weight:700;color:#2563EB}',

      /* Quantity controls */
      '.ac-qty{display:flex;align-items:center;gap:0;border:1px solid #E5E7EB;border-radius:6px;overflow:hidden;margin-top:6px;width:fit-content}',
      '.ac-qty button{width:28px;height:28px;background:#F9FAFB;border:none;cursor:pointer;font-size:16px;font-weight:600;color:#374151;display:flex;align-items:center;justify-content:center;transition:background .15s}',
      '.ac-qty button:hover{background:#E5E7EB}',
      '.ac-qty span{width:32px;text-align:center;font-size:13px;font-weight:600;color:#1B2A4A}',

      /* Remove button */
      '.ac-item-remove{background:none;border:none;cursor:pointer;color:#D1D5DB;padding:4px;flex-shrink:0;transition:color .2s}',
      '.ac-item-remove:hover{color:#EF4444}',
      '.ac-item-remove svg{width:18px;height:18px;fill:none;stroke:currentColor;stroke-width:2}',

      /* Footer */
      '.ac-footer{border-top:2px solid #F3F4F6;padding:16px;flex-shrink:0;background:#FAFBFC}',

      /* Zone selector */
      '.ac-zone{margin-bottom:12px}',
      '.ac-zone label{display:block;font-size:12px;font-weight:600;color:#6B7280;margin-bottom:6px;text-transform:uppercase;letter-spacing:.5px}',
      '.ac-zone select{width:100%;padding:8px 12px;border:1px solid #E5E7EB;border-radius:6px;font-size:14px;color:#1B2A4A;background:#fff;cursor:pointer;appearance:auto}',

      /* Totals */
      '.ac-totals{display:flex;flex-direction:column;gap:6px;margin-bottom:14px}',
      '.ac-total-row{display:flex;justify-content:space-between;font-size:14px;color:#4B5563}',
      '.ac-total-row.shipping .val{color:#25D366;font-weight:600}',
      '.ac-total-row.shipping .val.paid{color:#4B5563;font-weight:400}',
      '.ac-total-row.shipping .val.quote{color:#F59E0B;font-weight:600;font-size:12px}',
      '.ac-total-row.grand{font-size:17px;font-weight:800;color:#1B2A4A;border-top:2px solid #E5E7EB;padding-top:8px;margin-top:4px}',

      /* Buttons */
      '.ac-btn-pay{display:block;width:100%;padding:14px;border:none;border-radius:8px;font-size:16px;font-weight:700;cursor:pointer;text-align:center;text-decoration:none;transition:background .2s,transform .15s}',
      '.ac-btn-pay:active{transform:scale(.98)}',
      '.ac-btn-pay.primary{background:#2563EB;color:#fff}',
      '.ac-btn-pay.primary:hover{background:#1D4ED8}',
      '.ac-btn-pay.whatsapp{background:#25D366;color:#fff;margin-top:8px;font-size:14px;padding:11px}',
      '.ac-btn-pay.whatsapp:hover{background:#1EBE5A}',
      '.ac-btn-continue{display:block;text-align:center;margin-top:10px;color:#6B7280;font-size:13px;text-decoration:none;cursor:pointer;border:none;background:none;width:100%}',
      '.ac-btn-continue:hover{color:#2563EB}',

      /* Added feedback toast */
      '#acero-cart-toast{position:fixed;bottom:160px;right:20px;z-index:100001;background:#1B2A4A;color:#fff;padding:12px 20px;border-radius:8px;font-size:14px;font-weight:600;box-shadow:0 4px 16px rgba(0,0,0,.2);opacity:0;transform:translateY(10px);transition:opacity .3s,transform .3s;pointer-events:none;font-family:system-ui,-apple-system,sans-serif;max-width:280px}',
      '#acero-cart-toast.show{opacity:1;transform:translateY(0)}',

      /* "Add to cart" buttons */
      '.ac-add-btn{display:inline-flex;align-items:center;gap:8px;padding:10px 20px;background:#2563EB;color:#fff;border:none;border-radius:8px;font-size:14px;font-weight:700;cursor:pointer;transition:background .2s,transform .15s;font-family:system-ui,-apple-system,sans-serif}',
      '.ac-add-btn:hover{background:#1D4ED8}',
      '.ac-add-btn:active{transform:scale(.96)}',
      '.ac-add-btn svg{width:18px;height:18px;fill:none;stroke:currentColor;stroke-width:2}',

      /* Responsive */
      '@media(max-width:480px){#acero-cart-fab{bottom:80px;right:14px;width:50px;height:50px}#acero-cart-fab svg{width:22px;height:22px}#acero-cart-panel{width:100vw;max-width:100vw}#acero-cart-toast{right:14px;bottom:142px;max-width:calc(100vw - 28px)}}'
    ].join('\n');
    document.head.appendChild(style);
  }

  /* ========== SVG ICONS ========== */
  var ICONS = {
    cart: '<svg viewBox="0 0 24 24"><circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/></svg>',
    truck: '<svg viewBox="0 0 24 24"><path d="M1 3h15v13H1z"/><path d="M16 8h4l3 3v5h-7V8z"/><circle cx="5.5" cy="18.5" r="2.5"/><circle cx="18.5" cy="18.5" r="2.5"/></svg>',
    x: '<svg viewBox="0 0 24 24"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>',
    trash: '<svg viewBox="0 0 24 24"><polyline points="3 6 5 6 21 6"/><path d="M19 6l-1.5 14a2 2 0 0 1-2 2h-7a2 2 0 0 1-2-2L5 6"/><path d="M10 11v6"/><path d="M14 11v6"/><path d="M9 6V4a1 1 0 0 1 1-1h4a1 1 0 0 1 1 1v2"/></svg>',
    emptyCart: '<svg viewBox="0 0 24 24"><circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/><line x1="1" y1="1" x2="23" y2="23" stroke-dasharray="2 3"/></svg>',
    box: '<svg viewBox="0 0 24 24"><path d="M21 16V8a2 2 0 0 0-1-1.73L12 2 4 6.27A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73L12 22l8-4.27A2 2 0 0 0 21 16z"/><polyline points="3.27 6.96 12 12.01 20.73 6.96"/><line x1="12" y1="22.08" x2="12" y2="12"/></svg>'
  };

  /* ========== UI RENDERING ========== */
  var panelOpen = false;

  function createWidget() {
    // Floating action button
    var fab = document.createElement('button');
    fab.id = 'acero-cart-fab';
    fab.setAttribute('aria-label', 'Carrito de compras');
    fab.innerHTML = ICONS.cart + '<span id="acero-cart-badge"></span>';
    fab.addEventListener('click', togglePanel);
    document.body.appendChild(fab);

    // Overlay
    var overlay = document.createElement('div');
    overlay.id = 'acero-cart-overlay';
    overlay.addEventListener('click', closePanel);
    document.body.appendChild(overlay);

    // Panel
    var panel = document.createElement('div');
    panel.id = 'acero-cart-panel';
    panel.setAttribute('role', 'dialog');
    panel.setAttribute('aria-label', 'Carrito de compras');
    document.body.appendChild(panel);

    // Toast
    var toast = document.createElement('div');
    toast.id = 'acero-cart-toast';
    document.body.appendChild(toast);
  }

  function togglePanel() {
    panelOpen ? closePanel() : openPanel();
  }

  function openPanel() {
    panelOpen = true;
    renderPanelContent();
    requestAnimationFrame(function () {
      document.getElementById('acero-cart-overlay').classList.add('open');
      document.getElementById('acero-cart-panel').classList.add('open');
    });
    document.body.style.overflow = 'hidden';
  }

  function closePanel() {
    panelOpen = false;
    document.getElementById('acero-cart-overlay').classList.remove('open');
    document.getElementById('acero-cart-panel').classList.remove('open');
    document.body.style.overflow = '';
  }

  function renderWidget() {
    var badge = document.getElementById('acero-cart-badge');
    if (badge) {
      var count = getItemCount();
      badge.textContent = count > 0 ? count : '';
      badge.setAttribute('data-count', count);
    }
    if (panelOpen) renderPanelContent();
  }

  function renderPanelContent() {
    var panel = document.getElementById('acero-cart-panel');
    if (!panel) return;

    var zone = loadZone();
    var subtotal = getTotal();
    var shipping = getShippingCost(zone, subtotal);
    var shippingLabel = getShippingLabel(zone, subtotal);
    var orderTotal = getOrderTotal(zone);
    var items = getCart();

    var html = '';

    // Header
    html += '<div class="ac-panel-header">';
    html += '<h3>Mi Carrito (' + getItemCount() + ')</h3>';
    html += '<button class="ac-panel-close" aria-label="Cerrar">&times;</button>';
    html += '</div>';

    // Free shipping banner
    html += '<div class="ac-ship-banner">' + ICONS.truck + ' Envío GRATIS en Cd. Victoria en compras mayores a $1,500</div>';

    // Items
    html += '<div class="ac-items">';
    if (items.length === 0) {
      html += '<div class="ac-empty">' + ICONS.emptyCart + '<p>Tu carrito está vacío</p><small>Agrega productos para comenzar</small></div>';
    } else {
      for (var i = 0; i < items.length; i++) {
        var it = items[i];
        html += '<div class="ac-item" data-item-id="' + it.id + '">';
        if (it.image) {
          html += '<img class="ac-item-img" src="' + escapeHtml(it.image) + '" alt="' + escapeHtml(it.name) + '" loading="lazy">';
        } else {
          html += '<div class="ac-item-img-placeholder">' + ICONS.box + '</div>';
        }
        html += '<div class="ac-item-info">';
        html += '<p class="ac-item-name" title="' + escapeHtml(it.name) + '">' + escapeHtml(it.name) + '</p>';
        if (it.category) html += '<p class="ac-item-cat">' + escapeHtml(it.category) + '</p>';
        html += '<div class="ac-item-price">' + formatPrice(it.price * it.quantity) + '</div>';
        html += '<div class="ac-qty">';
        html += '<button data-action="minus" data-id="' + it.id + '">−</button>';
        html += '<span>' + it.quantity + '</span>';
        html += '<button data-action="plus" data-id="' + it.id + '">+</button>';
        html += '</div>';
        html += '</div>';
        html += '<button class="ac-item-remove" data-action="remove" data-id="' + it.id + '" aria-label="Eliminar">' + ICONS.trash + '</button>';
        html += '</div>';
      }
    }
    html += '</div>';

    // Footer (only if items exist)
    if (items.length > 0) {
      html += '<div class="ac-footer">';

      // Zone selector
      html += '<div class="ac-zone">';
      html += '<label for="ac-zone-select">Zona de envío</label>';
      html += '<select id="ac-zone-select">';
      html += '<option value="victoria"' + (zone === 'victoria' ? ' selected' : '') + '>Ciudad Victoria</option>';
      html += '<option value="tamaulipas"' + (zone === 'tamaulipas' ? ' selected' : '') + '>Tamaulipas (otro municipio)</option>';
      html += '<option value="otro"' + (zone === 'otro' ? ' selected' : '') + '>Fuera de Tamaulipas</option>';
      html += '</select>';
      html += '</div>';

      // Totals
      html += '<div class="ac-totals">';
      html += '<div class="ac-total-row"><span>Subtotal</span><span>' + formatPrice(subtotal) + '</span></div>';

      var shipClass = 'val';
      if (shipping === 0) shipClass += ''; // green by default for free
      else if (shipping === null) shipClass += ' quote';
      else shipClass += ' paid';

      html += '<div class="ac-total-row shipping"><span>Envío</span><span class="' + shipClass + '">' + shippingLabel + '</span></div>';

      if (orderTotal !== null) {
        html += '<div class="ac-total-row grand"><span>Total</span><span>' + formatPrice(orderTotal) + '</span></div>';
      } else {
        html += '<div class="ac-total-row grand"><span>Total</span><span>Cotizar envío</span></div>';
      }
      html += '</div>';

      // Buttons
      if (zone === 'otro') {
        var waMsg = buildWhatsAppMessage();
        html += '<a href="https://wa.me/' + WHATSAPP_NUMBER + '?text=' + encodeURIComponent(waMsg) + '" target="_blank" rel="noopener" class="ac-btn-pay whatsapp">Cotizar envío por WhatsApp</a>';
      }
      html += '<a href="' + CHECKOUT_URL + '" class="ac-btn-pay primary">Ir a pagar</a>';
      html += '<button class="ac-btn-continue">Seguir comprando</button>';
      html += '</div>';
    }

    panel.innerHTML = html;

    // Wire events
    var closeBtn = panel.querySelector('.ac-panel-close');
    if (closeBtn) closeBtn.addEventListener('click', closePanel);

    var continueBtn = panel.querySelector('.ac-btn-continue');
    if (continueBtn) continueBtn.addEventListener('click', closePanel);

    var zoneSelect = panel.querySelector('#ac-zone-select');
    if (zoneSelect) {
      zoneSelect.addEventListener('change', function () {
        saveZone(this.value);
        renderPanelContent();
      });
    }

    // Quantity and remove buttons
    var buttons = panel.querySelectorAll('[data-action]');
    for (var b = 0; b < buttons.length; b++) {
      buttons[b].addEventListener('click', handleItemAction);
    }
  }

  function handleItemAction(e) {
    var btn = e.currentTarget;
    var action = btn.getAttribute('data-action');
    var id = btn.getAttribute('data-id');
    var idx = findIndex(id);
    if (idx < 0) return;

    if (action === 'minus') {
      updateQuantity(id, cart[idx].quantity - 1);
    } else if (action === 'plus') {
      updateQuantity(id, cart[idx].quantity + 1);
    } else if (action === 'remove') {
      removeItem(id);
    }
  }

  /* ========== WHATSAPP MESSAGE ========== */
  function buildWhatsAppMessage() {
    var items = getCart();
    var msg = 'Hola, me interesa hacer un pedido:\n\n';
    for (var i = 0; i < items.length; i++) {
      msg += '• ' + items[i].name + ' x' + items[i].quantity + ' — ' + formatPrice(items[i].price * items[i].quantity) + '\n';
    }
    msg += '\nSubtotal: ' + formatPrice(getTotal());
    msg += '\n\nNecesito cotización de envío fuera de Tamaulipas. Gracias.';
    return msg;
  }

  /* ========== ADDED FEEDBACK ========== */
  var toastTimer = null;
  function showAddedFeedback(name) {
    var toast = document.getElementById('acero-cart-toast');
    if (!toast) return;
    toast.textContent = '✓ ' + name + ' agregado al carrito';
    toast.classList.add('show');
    clearTimeout(toastTimer);
    toastTimer = setTimeout(function () {
      toast.classList.remove('show');
    }, 2500);
  }

  /* ========== HELPERS ========== */
  function escapeHtml(str) {
    var div = document.createElement('div');
    div.appendChild(document.createTextNode(str || ''));
    return div.innerHTML;
  }

  /* ========== INTEGRATION: data-attribute products ========== */
  function initProductButtons() {
    var els = document.querySelectorAll('[data-product-id]');
    for (var i = 0; i < els.length; i++) {
      var el = els[i];
      if (el.getAttribute('data-acero-cart-bound')) continue;
      el.setAttribute('data-acero-cart-bound', '1');

      // If the element itself is a button, wire click directly
      if (el.tagName === 'BUTTON' || el.tagName === 'A') {
        el.addEventListener('click', onDataProductClick);
      } else {
        // Look for or create a button inside
        var btn = el.querySelector('.ac-add-btn');
        if (!btn) {
          btn = createAddButton(readProductData(el));
          el.appendChild(btn);
        } else {
          btn.addEventListener('click', function (e) {
            var container = e.currentTarget.closest('[data-product-id]');
            if (container) addItem(readProductData(container));
          });
        }
      }
    }
  }

  function onDataProductClick(e) {
    e.preventDefault();
    addItem(readProductData(e.currentTarget));
  }

  function readProductData(el) {
    return {
      id: el.getAttribute('data-product-id'),
      name: el.getAttribute('data-product-name') || 'Producto',
      price: parseFloat(el.getAttribute('data-product-price')) || 0,
      image: el.getAttribute('data-product-image') || '',
      category: el.getAttribute('data-product-category') || '',
      sku: el.getAttribute('data-product-sku') || '',
      quantity: parseInt(el.getAttribute('data-product-qty'), 10) || 1
    };
  }

  function createAddButton(product) {
    var btn = document.createElement('button');
    btn.className = 'ac-add-btn';
    btn.innerHTML = ICONS.cart + ' Agregar al carrito';
    btn.addEventListener('click', function (e) {
      e.preventDefault();
      e.stopPropagation();
      addItem(product);
    });
    return btn;
  }

  /* ========== INITIALIZATION ========== */
  function init() {
    injectStyles();
    createWidget();
    renderWidget();
    initProductButtons();

    // Re-scan for new product buttons after dynamic content
    var observer;
    if (typeof MutationObserver !== 'undefined') {
      observer = new MutationObserver(function () { initProductButtons(); });
      observer.observe(document.body, { childList: true, subtree: true });
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  /* ========== PUBLIC API ========== */
  window.AceroCart = {
    addItem: addItem,
    removeItem: removeItem,
    updateQuantity: updateQuantity,
    getCart: getCart,
    getTotal: getTotal,
    getItemCount: getItemCount,
    clearCart: clearCart,
    getShippingCost: getShippingCost,
    getShippingLabel: getShippingLabel,
    getOrderTotal: getOrderTotal,
    openPanel: openPanel,
    closePanel: closePanel,
    togglePanel: togglePanel,
    createAddButton: createAddButton,
    initProductButtons: initProductButtons,
    formatPrice: formatPrice,
    WHATSAPP_NUMBER: WHATSAPP_NUMBER,
    FREE_SHIPPING_MIN: FREE_SHIPPING_MIN
  };

})();
