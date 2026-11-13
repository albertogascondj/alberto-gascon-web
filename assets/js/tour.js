// Pinta las fechas de data/fechas.js en cualquier elemento con [data-tour].
// data-tour="proximas" | "pasadas", data-limit="3" para limitar.
(function () {
  // Textos en español o en inglés según el idioma de la página (<html lang>)
  var EN = document.documentElement.lang === 'en';
  var MESES = EN ? ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'] : ['ene', 'feb', 'mar', 'abr', 'may', 'jun', 'jul', 'ago', 'sep', 'oct', 'nov', 'dic'];
  var DIAS = EN ? ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat'] : ['dom', 'lun', 'mar', 'mié', 'jue', 'vie', 'sáb'];
  var T = EN ? {
    privado: 'Private event', ver: 'View ', mapa: 'on the map', pin: 'Map', hecho: 'Done', entradas: 'Tickets →',
    sinArchivo: 'No past dates yet.', pronto: 'New dates coming soon.',
    cta: 'Want your venue or festival to be next? <a href="index.html#presupuesto">Get in touch</a>.',
    tipos: { 'Discoteca': 'Club', 'Festival': 'Festival', 'Fiestas patronales': 'Town festival', 'Evento privado': 'Private event', 'Evento corporativo': 'Corporate event', 'Boda': 'Wedding' }
  } : {
    privado: 'Evento privado', ver: 'Ver ', mapa: 'en el mapa', pin: 'Mapa', hecho: 'Hecho', entradas: 'Entradas →',
    sinArchivo: 'Aún no hay fechas en el archivo.', pronto: 'Nuevas fechas muy pronto.',
    cta: '¿Quieres que tu sala o tus fiestas sean la próxima? <a href="index.html#presupuesto">Escríbeme</a>.', tipos: {}
  };
  function tipo(t) { return T.tipos[t] || t; }
  var hoy = new Date(); hoy.setHours(0, 0, 0, 0);
  var lista = (window.FECHAS || []).map(function (f) {
    var p = String(f.fecha).split('-');
    return Object.assign({}, f, { d: new Date(+p[0], +p[1] - 1, +p[2]) });
  }).filter(function (f) { return !isNaN(f.d); });
  var proximas = lista.filter(function (f) { return f.d >= hoy; }).sort(function (a, b) { return a.d - b.d; });
  var pasadas = lista.filter(function (f) { return f.d < hoy; }).sort(function (a, b) { return b.d - a.d; });
  function esc(s) { return String(s == null ? '' : s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function fila(f, pasada) {
    var sala = f.privado ? (tipo(f.tipo) || T.privado) : f.sala;
    var donde = f.mapa || ((f.privado ? '' : f.sala + ', ') + f.ciudad);
    var pin = '<a class="t-pin" href="https://www.google.com/maps/search/?api=1&query=' + encodeURIComponent(donde) + '" target="_blank" rel="noopener" aria-label="' + T.ver + esc(donde) + ' ' + T.mapa + '">' +
      '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 22s7-6.2 7-12a7 7 0 1 0-14 0c0 5.8 7 12 7 12z" fill="currentColor"/><circle cx="12" cy="10" r="2.6" fill="var(--ink)"/></svg><span>' + T.pin + '</span></a>';
    var accion = pasada ? '<span class="t-tag">' + T.hecho + '</span>'
      : (f.entradas ? '<a class="t-tag hot" href="' + esc(f.entradas) + '" target="_blank" rel="noopener">' + T.entradas + '</a>' : '') + pin;
    return '<li class="t-row' + (pasada ? ' past' : '') + '">' +
      '<div class="t-date"><b>' + f.d.getDate() + '</b><span>' + MESES[f.d.getMonth()] + ' ' + f.d.getFullYear() + '</span><small>' + DIAS[f.d.getDay()] + (f.hora ? ' · ' + esc(f.hora) : '') + '</small></div>' +
      '<div class="t-main"><span class="t-venue">' + esc(sala) + '</span><span class="t-city">' + esc(f.ciudad) + (f.tipo && !f.privado ? ' · ' + esc(tipo(f.tipo)) : '') + '</span></div>' +
      '<div class="t-act">' + accion + '</div></li>';
  }
  document.querySelectorAll('[data-tour]').forEach(function (el) {
    var pasada = el.dataset.tour === 'pasadas';
    var items = pasada ? pasadas : proximas;
    if (el.dataset.limit) items = items.slice(0, +el.dataset.limit);
    if (!items.length) {
      var empty = el.dataset.empty;
      if (empty === 'hide') { var box = el.closest('[data-tour-box]'); if (box) box.hidden = true; return; }
      el.innerHTML = '<li class="t-empty"><b>' + (pasada ? T.sinArchivo : T.pronto) + '</b><span>' + (pasada ? '' : T.cta) + '</span></li>';
      return;
    }
    el.innerHTML = items.map(function (f) { return fila(f, pasada); }).join('');
  });
  document.querySelectorAll('[data-tour-count]').forEach(function (el) { el.textContent = proximas.length; });
})();
