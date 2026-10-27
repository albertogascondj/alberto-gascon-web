// Pinta las fechas de data/fechas.js en cualquier elemento con [data-tour].
// data-tour="proximas" | "pasadas", data-limit="3" para limitar.
(function () {
  var MESES = ['ene', 'feb', 'mar', 'abr', 'may', 'jun', 'jul', 'ago', 'sep', 'oct', 'nov', 'dic'];
  var DIAS = ['dom', 'lun', 'mar', 'mié', 'jue', 'vie', 'sáb'];
  var hoy = new Date(); hoy.setHours(0, 0, 0, 0);
  var lista = (window.FECHAS || []).map(function (f) {
    var p = String(f.fecha).split('-');
    return Object.assign({}, f, { d: new Date(+p[0], +p[1] - 1, +p[2]) });
  }).filter(function (f) { return !isNaN(f.d); });
  var proximas = lista.filter(function (f) { return f.d >= hoy; }).sort(function (a, b) { return a.d - b.d; });
  var pasadas = lista.filter(function (f) { return f.d < hoy; }).sort(function (a, b) { return b.d - a.d; });
  function esc(s) { return String(s == null ? '' : s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function fila(f, pasada) {
    var sala = f.privado ? (f.tipo || 'Evento privado') : f.sala;
    var accion = pasada ? '<span class="t-tag">Hecho</span>'
      : f.entradas ? '<a class="t-tag hot" href="' + esc(f.entradas) + '" target="_blank" rel="noopener">Entradas →</a>'
      : f.privado ? '<span class="t-tag">Privado</span>' : '<span class="t-tag">Entrada libre o en taquilla</span>';
    return '<li class="t-row' + (pasada ? ' past' : '') + '">' +
      '<div class="t-date"><b>' + f.d.getDate() + '</b><span>' + MESES[f.d.getMonth()] + ' ' + f.d.getFullYear() + '</span><small>' + DIAS[f.d.getDay()] + (f.hora ? ' · ' + esc(f.hora) : '') + '</small></div>' +
      '<div class="t-main"><span class="t-venue">' + esc(sala) + '</span><span class="t-city">' + esc(f.ciudad) + (f.tipo && !f.privado ? ' · ' + esc(f.tipo) : '') + '</span></div>' +
      '<div class="t-act">' + accion + '</div></li>';
  }
  document.querySelectorAll('[data-tour]').forEach(function (el) {
    var pasada = el.dataset.tour === 'pasadas';
    var items = pasada ? pasadas : proximas;
    if (el.dataset.limit) items = items.slice(0, +el.dataset.limit);
    if (!items.length) {
      var empty = el.dataset.empty;
      if (empty === 'hide') { var box = el.closest('[data-tour-box]'); if (box) box.hidden = true; return; }
      el.innerHTML = '<li class="t-empty"><b>' + (pasada ? 'Aún no hay fechas en el archivo.' : 'Nuevas fechas muy pronto.') + '</b><span>' + (pasada ? '' : '¿Quieres que tu sala o tus fiestas sean la próxima? <a href="index.html#presupuesto">Escríbeme</a>.') + '</span></li>';
      return;
    }
    el.innerHTML = items.map(function (f) { return fila(f, pasada); }).join('');
  });
  document.querySelectorAll('[data-tour-count]').forEach(function (el) { el.textContent = proximas.length; });
})();
