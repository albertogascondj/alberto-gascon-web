"""Genera la versión en inglés de la web en en/ a partir de las páginas en español.

Se ejecuta solo al final de tools/build.py. Los textos en inglés están en tools/en.py.
Avisa de los textos en español que se hayan quedado sin traducir.
"""
import re, json, html, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import en

SITE = "https://albertogascon.com"
PAGES = {"index.html": "/", "tour.html": "/tour.html", "presskit.html": "/presskit.html"}
PAIRS = sorted(en.SEO + en.COMMON + en.INDEX + en.TOUR + en.PRESSKIT, key=lambda p: -len(p[0]))
SPANISH = re.compile(r"[áéíóúñ¿¡]|\b(de|del|el|la|los|las|con|para|en|y|que|tu|mi|sin|Ver|Más)\b")
# Nombres propios y textos que se quedan igual en inglés
KEEP = {"Alberto Gascón", "Los Que Faltaban, Teruel", "Fiestas del Ángel", "La Encerrona", "Los Que Faltaban", "Los Chachos",
        "Jardines de Tabarca", "Black", "Alberto Gascón · DJ", "Andorra (Teruel)", "© 2026 Alberto Gascón",
        "On Tour · Alberto Gascón DJ", "Press kit · Alberto Gascón DJ", "Ha pinchado"}


def switch(page):
    es = "../" + (page if page != "index.html" else "index.html")
    return f'<div class="lang" aria-label="Language"><a href="{es}" hreflang="es" lang="es" aria-label="Versión en español">ES</a><span aria-current="true">EN</span></div>'


def jsonld(s, page):
    m = re.search(r"(<script type=\"application/ld\+json\">\n)(.*?)(\n</script>)", s, flags=re.S)
    data = json.loads(m.group(2))

    def walk(v):
        if isinstance(v, dict):
            return {k: walk(x) for k, x in v.items()}
        if isinstance(v, list):
            return [walk(x) for x in v]
        if isinstance(v, str):
            if v in en.JSONLD:
                return en.JSONLD[v]
            if v == SITE + "/tour.html":
                return SITE + "/en/tour.html"
            v = re.sub(r"^Alberto Gascón en (.+)$", r"Alberto Gascón at \1", v)
            v = re.sub(r"^Alberto Gascón pincha en (.+)$", r"Alberto Gascón plays at \1", v)
        return v

    graph = []
    for g in data["@graph"]:
        if g.get("@type") == "FAQPage":
            qs = re.findall(r"<summary>(.*?)</summary><p>(.*?)</p>", s, flags=re.S)
            g = {"@type": "FAQPage", "@id": SITE + "/en/#preguntas", "inLanguage": "en", "mainEntity": [
                {"@type": "Question", "name": html.unescape(q), "acceptedAnswer": {"@type": "Answer", "text": html.unescape(re.sub("<.*?>", "", a))}} for q, a in qs]}
            graph.append(g)
        else:
            graph.append(walk(g))
    data["@graph"] = graph
    return s[:m.start(2)] + json.dumps(data, ensure_ascii=False, indent=1) + s[m.end(2):]


NAMES = re.compile(r"Jardines de Tabarca|La Encerrona|Los Que Faltaban|Los Chachos|Fiestas del Ángel|Gascón|Alcañiz|Giménez|Ángel|Aragón|[Pp]eñas|https?://\S+")


def spanish(t):
    return t not in KEEP and SPANISH.search(NAMES.sub("", t))


def leftovers(s):
    body = re.sub(r"<script.*?</script>|<style.*?</style>|<!--.*?-->", "", s, flags=re.S)
    found = set()
    for t in re.findall(r">([^<>]+)<", body):
        t = t.strip()
        if t and spanish(t):
            found.add(t)
    for t in re.findall(r'(?:alt|aria-label|title|placeholder|content)="([^"]+)"', body):
        if spanish(t) and t != "Versión en español":
            found.add(t)
    return sorted(found)


def main():
    out = ROOT / "en"
    out.mkdir(exist_ok=True)
    missing = {}
    for page, path in PAGES.items():
        s = (ROOT / page).read_text()
        s = s.replace('<html lang="es">', '<html lang="en">', 1)
        s = re.sub(r'<div class="lang" aria-label="Idioma">.*?</div>', switch(page), s, count=1)
        s = re.sub(r'<link rel="canonical" href="[^"]+">', f'<link rel="canonical" href="{SITE}/en{path}">', s, count=1)
        s = re.sub(r'<meta property="og:url" content="[^"]+">', f'<meta property="og:url" content="{SITE}/en{path}">', s, count=1)
        s = s.replace('<meta property="og:locale" content="es_ES">', '<meta property="og:locale" content="en_GB">\n<meta property="og:locale:alternate" content="es_ES">', 1)
        for a, b in PAIRS:
            s = s.replace(a, b)
        # Rutas relativas a archivos: en/ está un nivel por debajo
        s = re.sub(r'(?<=["\s,])(assets|data)/', r"../\1/", s)
        s = jsonld(s, page)
        (out / page).write_text(s)
        left = leftovers(s)
        if left:
            missing[page] = left
    for page, left in missing.items():
        print(f"  Sin traducir en en/{page}:")
        for t in left:
            print("   -", t[:110])
    print("Versión en inglés generada en en/" + (" (revisa los textos sin traducir)" if missing else ""))


main()
