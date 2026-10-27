# SEO de albertogascon.com

## Hecho en la web (27-10-2026)

- Títulos y descripciones pensados para búsquedas tipo "DJ en Teruel", "DJ Valencia", "DJ fiestas patronales Teruel".
- H1 de portada: "DJ en Teruel y Valencia para fiestas que no se olvidan".
- Datos estructurados (schema.org): persona (Alberto Gascón, DJ), servicio profesional con zona de trabajo y catálogo de servicios, preguntas frecuentes y cada fecha de On Tour como evento musical.
- Sección de preguntas frecuentes en la portada (Google y los asistentes de IA citan mucho este formato).
- Imagen para compartir en WhatsApp/redes, favicon, `site.webmanifest`, URL canónica.
- `sitemap.xml`, `robots.txt` (abierto a Google, Bing y a los rastreadores de ChatGPT, Claude, Perplexity y Gemini) y `llms.txt` con el resumen para IA.
- Carga más rápida de la cabecera (logo prioritario y animación de entrada más corta).
- Página 404 propia.

## Lo que tiene que hacer Alberto (por orden de impacto)

1. **Perfil de Empresa de Google** (business.google.com). Es lo que más pesa para salir en "DJ cerca de mí" y en el mapa.
   - Nombre: Alberto Gascón DJ. Categoría principal: "DJ". Secundarias: "Servicio de entretenimiento para bodas", "Animador de fiestas".
   - Negocio de zona de servicio (sin dirección pública): Teruel, Valencia, Aragón.
   - Web albertogascon.com, fotos reales en cabina (mínimo 10) y publicaciones con cada fecha.
2. **Reseñas en Google**: pide una reseña a cada comisión de fiestas, sala o pareja después del bolo. Que mencionen el pueblo y el tipo de evento ("DJ fiestas de Manzanera").
3. **Google Search Console** (search.google.com/search-console): añadir albertogascon.com (verificación por DNS en Cloudflare, se hace en 2 minutos) y enviar `https://albertogascon.com/sitemap.xml`.
4. **Bing Webmaster Tools** (bing.com/webmasters): importar desde Search Console. Bing alimenta a ChatGPT y Copilot.
5. **Instagram @albertogascon_**: poner albertogascon.com en la bio y en cada fecha publicada.
6. **Enlaces desde otros sitios**: pedir a salas, festivales y ayuntamientos que enlacen la web en sus carteles online; darse de alta en directorios de bodas (Bodas.net, Zankyou) si quiere bodas.

## Siguiente fase (contenido)

- Páginas por servicio y zona con texto propio: "DJ para fiestas patronales en Teruel", "DJ en Valencia para discotecas", "DJ para bodas en Teruel".
- Una crónica corta tras cada bolo grande (MotoGP Cheste, Electropura…) con fotos.
- Fotos reales con nombre descriptivo (`dj-fiestas-manzanera-2026.jpg`) y texto alternativo.

## Mantenimiento

Después de cambiar `data/fechas.js` o textos: `python3 tools/build.py` (regenera los datos estructurados y el sitemap).
