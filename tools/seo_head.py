"""Inserta las etiquetas SEO comunes en el <head> de cada página (entre los marcadores SEO)."""
import re, json, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = "https://albertogascon.com"
IG = "https://www.instagram.com/albertogascon_/"
PAGES = {
  "index.html": dict(path="/", title="DJ en Teruel y Valencia para fiestas y eventos | Alberto Gascón",
    desc="Alberto Gascón, DJ de Teruel con base en Valencia. Discotecas, festivales, fiestas patronales, eventos y bodas en toda España. Pinchando desde los 13, más de 200 bolos. Pide presupuesto."),
  "tour.html": dict(path="/tour.html", title="Próximas fechas de Alberto Gascón DJ | On Tour",
    desc="Próximas fechas de Alberto Gascón, DJ: discotecas, festivales y fiestas patronales en Teruel, Valencia y toda España. Consulta dónde pincha las próximas noches."),
  "presskit.html": dict(path="/presskit.html", title="Press kit de Alberto Gascón DJ | Bio, logos y rider",
    desc="Press kit de Alberto Gascón, DJ de Teruel y Valencia: biografía corta y larga, logos en alta, rider técnico y contacto para promotores, salas y comisiones de fiestas."),
}
for name, p in PAGES.items():
    f = ROOT / name
    s = f.read_text()
    url = SITE + p["path"]
    block = f'''<!-- SEO -->
<title>{p["title"]}</title>
<meta name="description" content="{p["desc"]}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="author" content="Alberto Gascón">
<meta property="og:type" content="website">
<meta property="og:locale" content="es_ES">
<meta property="og:site_name" content="Alberto Gascón DJ">
<meta property="og:title" content="{p["title"]}">
<meta property="og:description" content="{p["desc"]}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/assets/img/og.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="apple-touch-icon" href="/assets/img/icons/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<!-- /SEO -->'''
    s = re.sub(r'<!-- SEO -->.*?<!-- /SEO -->', '', s, flags=re.S)
    s = re.sub(r'<title>.*?</title>\n', '', s)
    s = re.sub(r'<meta name="description"[^>]*>\n', '', s)
    s = s.replace('<meta name="claude:viewport-fit-sides" content="cover">', block + '\n<meta name="claude:viewport-fit-sides" content="cover">', 1)
    f.write_text(s)
    print("ok", name)
