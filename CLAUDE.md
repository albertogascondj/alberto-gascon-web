# alberto-gascon-web

Web de **Alberto Gascón**, la faceta comercial: DJ para bodas, fiestas patronales, eventos privados, discotecas comerciales y booking de otros DJs (Teruel, Valencia, Aragón). No mezclar con CONIX (club, conixmusic.com) ni con CNX (estudio). Ver `../CLAUDE.md` para el contexto general.

- Responder en español de España. Tono profesional y cercano, tuteando.
- Marca: logo rojo de Alberto Gascón sobre fondo oscuro. Fuentes Chakra Petch (títulos), Barlow (texto), JetBrains Mono (datos).
- Nunca inventar datos, cifras ni clientes.

## Estructura

- `index.html`: portada. `tour.html`: On Tour. `presskit.html`: press kit.
- `assets/css/site.css`: estilos comunes. `assets/js/tour.js`: pinta las fechas.
- `data/fechas.js`: **lista de fechas** (una línea por fecha; la web separa próximas y pasadas sola). Tras cambiarla: `python3 tools/build.py`.
- `tools/build.py`: regenera JSON-LD (persona, servicio, FAQ, eventos) y `sitemap.xml`. `tools/seo_head.py`: títulos, descripciones y etiquetas OG de cada página.
- `SEO.md`: lo hecho y lo pendiente de SEO.
- `assets/presskit/alberto-gascon-logos.zip`: logos para descargar.
- `assets/img/`: imágenes optimizadas que usa la web.
- `assets/logos/`: logos originales (rojo, negro, blanco, rosa).
- `assets/fotos/`: fotos originales para la web (ver `LEEME.md`).

## Cómo se trabaja

- Copia local en `~/Documents/Cloude Apps/alberto-gascon-web`. Para verla: doble clic en `index.html`, o `python3 -m http.server 8000` en esta carpeta y abrir http://localhost:8000.
- Lo que se sube a la rama `main` de `albertogascondj/alberto-gascon-web` se publica solo en https://albertogascon.com (GitHub Pages, DNS en Cloudflare).
- Email de contacto: contacto@albertogascon.com (Cloudflare Email Routing).

## Pendiente

- Número de WhatsApp para el botón de contacto.
- Instagram: @albertogascon_ (ya enlazado).
- Fotos (en `assets/fotos/`).
- Prototipo online: https://claude.ai/artifact/E5chYQWZPdUfxiUyqbF37T
