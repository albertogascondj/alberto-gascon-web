"""Regenera los datos estructurados (JSON-LD) y el sitemap.

Ejecutar después de cambiar data/fechas.js o los textos:  python3 tools/build.py
"""
import re, json, html, datetime, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = "https://albertogascon.com"
IG = "https://www.instagram.com/albertogascon_/"
EMAIL = "contacto@albertogascon.com"
TODAY = datetime.date.today()

def fechas():
    src = (ROOT / "data/fechas.js").read_text()
    body = src[src.index("window.FECHAS = [") + len("window.FECHAS = "):]
    body = body[:body.rindex("]") + 1]
    body = re.sub(r"(\w+):", r'"\1":', body)          # claves sin comillas -> JSON
    body = re.sub(r",\s*([\]}])", r"\1", body)          # comas finales
    return json.loads(body)

PERSON = {
    "@type": "Person", "@id": SITE + "/#alberto",
    "name": "Alberto Gascón", "jobTitle": "DJ", "birthDate": "2002", "birthPlace": {"@type": "Place", "name": "Teruel, España"},
    "description": "DJ de Teruel con base en Valencia, pinchando desde los 13 años y profesional desde hace 8, para discotecas, festivales, fiestas patronales, eventos privados y corporativos y bodas.",
    "url": SITE + "/", "image": SITE + "/assets/img/og.jpg", "email": EMAIL,
    "sameAs": [IG],
    "homeLocation": {"@type": "Place", "name": "Valencia, España"},
    "alumniOf": [
        {"@type": "EducationalOrganization", "name": "Comenius (Valencia)"},
        {"@type": "EducationalOrganization", "name": "Millenia Estudios (Valencia)"},
    ],
    "knowsAbout": ["DJ", "Sesiones de discoteca", "Fiestas patronales", "Bodas", "Técnico de sonido"],
}
AREAS = [{"@type": "AdministrativeArea", "name": n} for n in ["España", "Provincia de Teruel", "Valencia", "Aragón", "Comunidad Valenciana"]]
SERVICES = ["DJ para discotecas", "DJ para festivales", "DJ para fiestas patronales", "DJ para eventos privados y corporativos", "DJ para bodas", "Booking de DJs para fiestas"]
BUSINESS = {
    "@type": ["ProfessionalService", "EntertainmentBusiness"], "@id": SITE + "/#negocio",
    "name": "Alberto Gascón DJ", "url": SITE + "/", "image": SITE + "/assets/img/og.jpg", "logo": SITE + "/assets/img/icons/icon-512.png",
    "email": EMAIL, "sameAs": [IG], "founder": {"@id": SITE + "/#alberto"},
    "description": "Servicio de DJ en Teruel, Valencia, Aragón y toda España: discotecas, festivales, fiestas patronales, eventos privados y corporativos, bodas y booking de DJs.",
    "address": {"@type": "PostalAddress", "addressLocality": "Valencia", "addressRegion": "Valencia", "addressCountry": "ES"},
    "areaServed": AREAS,
    "knowsLanguage": "es",
    "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Servicios de DJ",
        "itemListElement": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": s, "areaServed": AREAS}} for s in SERVICES]},
}
WEBSITE = {"@type": "WebSite", "@id": SITE + "/#web", "url": SITE + "/", "name": "Alberto Gascón DJ", "inLanguage": "es-ES", "publisher": {"@id": SITE + "/#alberto"}}

def events(only_upcoming=True):
    out = []
    for f in fechas():
        d = datetime.date.fromisoformat(f["fecha"])
        if only_upcoming and d < TODAY:
            continue
        name = ("Alberto Gascón en " + f["sala"]) if not f.get("privado") else None
        if not name:
            continue
        ev = {"@type": "MusicEvent", "name": name, "startDate": f["fecha"],
              "eventStatus": "https://schema.org/EventScheduled",
              "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
              "location": {"@type": "Place", "name": f["sala"], "address": {"@type": "PostalAddress", "addressLocality": f["ciudad"], "addressCountry": "ES"}},
              "performer": {"@id": SITE + "/#alberto"}, "organizer": {"@type": "Organization", "name": f["sala"]},
              "image": SITE + "/assets/img/og.jpg", "url": SITE + "/tour.html",
              "description": "Alberto Gascón pincha en " + f["sala"] + " (" + f["ciudad"] + ")."}
        if f.get("entradas"):
            ev["offers"] = {"@type": "Offer", "url": f["entradas"], "availability": "https://schema.org/InStock"}
        out.append(ev)
    return out

def faq(page):
    qs = re.findall(r"<summary>(.*?)</summary><p>(.*?)</p>", page, flags=re.S)
    if not qs:
        return None
    return {"@type": "FAQPage", "@id": SITE + "/#preguntas", "mainEntity": [
        {"@type": "Question", "name": html.unescape(q), "acceptedAnswer": {"@type": "Answer", "text": html.unescape(re.sub("<.*?>", "", a))}} for q, a in qs]}

def inject(name, graph):
    f = ROOT / name
    s = f.read_text()
    data = json.dumps({"@context": "https://schema.org", "@graph": [g for g in graph if g]}, ensure_ascii=False, indent=1)
    block = '<!-- JSONLD -->\n<script type="application/ld+json">\n' + data + '\n</script>\n<!-- /JSONLD -->'
    s = re.sub(r"<!-- JSONLD -->.*?<!-- /JSONLD -->\n?", "", s, flags=re.S)
    s = s.replace("</head>", block + "\n</head>", 1)
    f.write_text(s)

idx = (ROOT / "index.html").read_text()
inject("index.html", [WEBSITE, PERSON, BUSINESS, faq(idx)] + events()[:3])
inject("tour.html", [WEBSITE, PERSON, {"@type": "ItemList", "name": "Próximas fechas de Alberto Gascón", "itemListElement": [
    {"@type": "ListItem", "position": i + 1, "item": e} for i, e in enumerate(events())]}])
inject("presskit.html", [WEBSITE, PERSON])

urls = [("/", "weekly", "1.0"), ("/tour.html", "weekly", "0.8"), ("/presskit.html", "monthly", "0.6")]
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(
    f"  <url><loc>{SITE}{u}</loc><lastmod>{TODAY.isoformat()}</lastmod><changefreq>{c}</changefreq><priority>{p}</priority></url>\n" for u, c, p in urls) + "</urlset>\n"
(ROOT / "sitemap.xml").write_text(sm)
print("JSON-LD y sitemap actualizados:", len(events()), "fechas próximas")
