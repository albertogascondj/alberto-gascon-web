// Movimiento común a todas las páginas: scroll suave, apariciones y vídeos.
(function () {
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Scroll suave con inercia (Lenis). En el móvil se queda el scroll nativo.
  if (window.Lenis && !reduce) {
    var lenis = new Lenis({ lerp: 0.09, wheelMultiplier: 1, anchors: { offset: -84 } });
    window.lenis = lenis;
    (function raf(t) { lenis.raf(t); requestAnimationFrame(raf); })(0);
    // Con el visor de fotos abierto, la página no se mueve
    document.querySelectorAll('dialog').forEach(function (d) {
      new MutationObserver(function () { d.open ? lenis.stop() : lenis.start(); }).observe(d, { attributes: true, attributeFilter: ['open'] });
    });
  }

  // Menú del móvil
  var nav = document.getElementById('nav'), burger = nav && nav.querySelector('.burger');
  if (burger) {
    var setMenu = function (open) {
      nav.classList.toggle('open', open);
      burger.setAttribute('aria-expanded', open);
      burger.setAttribute('aria-label', open ? 'Cerrar menú' : 'Abrir menú');
      document.documentElement.style.overflow = open ? 'hidden' : '';
      if (window.lenis) open ? lenis.stop() : lenis.start();
    };
    burger.addEventListener('click', function () { setMenu(!nav.classList.contains('open')); });
    nav.querySelectorAll('ul a').forEach(function (a) { a.addEventListener('click', function () { setMenu(false); }); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') setMenu(false); });
  }

  // Apariciones en navegadores sin animaciones ligadas al scroll (Safari de iPhone, Firefox)
  var css = window.CSS && CSS.supports && CSS.supports('animation-timeline: view()');
  if (!css && !reduce && 'IntersectionObserver' in window) {
    document.documentElement.classList.add('io');
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } });
    }, { rootMargin: '0px 0px -8% 0px' });
    document.querySelectorAll('.reveal, .grow').forEach(function (el) { io.observe(el); });
  }

  // Vídeos (sin sonido): suenan solo mientras se ven. Si el móvil bloquea la
  // reproducción automática (p. ej. modo de bajo consumo), arrancan al primer toque.
  var vids = Array.prototype.slice.call(document.querySelectorAll('video'));
  if (!vids.length) return;
  function play(v) { v.muted = true; var p = v.play(); if (p) p.catch(function () {}); }
  var seen = new Set();
  if ('IntersectionObserver' in window) {
    var vo = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { seen.add(en.target); play(en.target); } else { seen.delete(en.target); en.target.pause(); }
      });
    }, { threshold: .2 });
    vids.forEach(function (v) { vo.observe(v); });
  } else vids.forEach(play);
  function wake() { seen.forEach(play); }
  ['touchstart', 'pointerdown', 'scroll'].forEach(function (ev) { window.addEventListener(ev, wake, { passive: true, once: true }); });
})();
