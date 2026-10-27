// Scroll suave con inercia (Lenis). Se desactiva si el sistema pide menos movimiento.
(function () {
  if (!window.Lenis || window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  var lenis = new Lenis({ lerp: 0.09, wheelMultiplier: 1, anchors: { offset: -84 } });
  window.lenis = lenis;
  function raf(t) { lenis.raf(t); requestAnimationFrame(raf); }
  requestAnimationFrame(raf);
  // Con el visor de fotos abierto, la página no se mueve
  document.querySelectorAll('dialog').forEach(function (d) {
    new MutationObserver(function () { d.open ? lenis.stop() : lenis.start(); }).observe(d, { attributes: true, attributeFilter: ['open'] });
  });
})();
