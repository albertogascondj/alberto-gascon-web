"""Textos de la versión en inglés (/en/).

Cada pareja es (texto en español tal y como está en el HTML, texto en inglés).
tools/i18n.py copia las páginas en español a en/ y cambia cada texto por su traducción.
Si cambias un texto en español, cámbialo también aquí (i18n.py avisa de lo que quede sin traducir).
"""

# Títulos y descripciones (tools/seo_head.py)
SEO = [
    ("DJ en Teruel y Valencia para fiestas y eventos | Alberto Gascón",
     "DJ in Valencia and Teruel, Spain, for parties and events | Alberto Gascón"),
    ("Alberto Gascón, DJ de Teruel con base en Valencia. Discotecas, festivales, fiestas patronales, eventos y bodas en toda España. Pinchando desde los 13, más de 400 bolos. Pide presupuesto.",
     "Alberto Gascón is a DJ from Teruel based in Valencia, Spain. Clubs, festivals, town fiestas, events and weddings all over Spain. DJing since age 13, over 400 gigs. Ask for a quote."),
    ("Próximas fechas de Alberto Gascón DJ | On Tour",
     "Upcoming dates for Alberto Gascón DJ | On Tour"),
    ("Próximas fechas de Alberto Gascón, DJ: discotecas, festivales y fiestas patronales en Teruel, Valencia y toda España. Consulta dónde pincha las próximas noches.",
     "Upcoming dates for Alberto Gascón, DJ: clubs, festivals and town fiestas in Teruel, Valencia and across Spain. See where he's playing next."),
    ("Press kit de Alberto Gascón DJ | Bio, logos y rider",
     "Alberto Gascón DJ press kit | Bio, logos and rider"),
    ("Press kit de Alberto Gascón, DJ de Teruel y Valencia: biografía corta y larga, logos en alta, rider técnico y contacto para promotores, salas y comisiones de fiestas.",
     "Press kit for Alberto Gascón, DJ from Teruel and Valencia, Spain: short and long bio, high-res logos, technical rider and booking contact for promoters, venues and festival committees."),
]

# Partes comunes: menú, pie, selector de idioma
COMMON = [
    ('aria-label="Inicio"', 'aria-label="Home"'),
    ('aria-label="Abrir menú"', 'aria-label="Open menu"'),
    ('>Servicios</a>', '>Services</a>'),
    ('>Sobre mí</a>', '>About</a>'),
    ('>Sesiones</a>', '>Sessions</a>'),
    ('>Ficha</a>', '>Fact sheet</a>'),
    ('>Presupuesto <span class="arr">→</span></a>', '>Book <span class="arr">→</span></a>'),
    ('>Contratar <span class="arr">→</span></a>', '>Book <span class="arr">→</span></a>'),
    ('<span class="label">Redes</span>', '<span class="label">Social</span>'),
    ('aria-label="Instagram de Alberto Gascón"', 'aria-label="Alberto Gascón on Instagram"'),
    ('aria-label="YouTube de Alberto Gascón"', 'aria-label="Alberto Gascón on YouTube"'),
    ('>Volver a la web</a>', '>Back to the main page</a>'),
]

INDEX = [
    # Portada
    ('<span>Discotecas · Festivales · Fiestas patronales · Eventos · Bodas</span><span>Desplazamiento a toda España</span>',
     '<span>Clubs · Festivals · Town fiestas · Events · Weddings</span><span>Available all over Spain</span>'),
    ('alt="Alberto Gascón, DJ en Teruel y Valencia"', 'alt="Alberto Gascón, DJ in Teruel and Valencia"'),
    ('<span class="line-mask"><span>DJ en Teruel y Valencia</span></span>',
     '<span class="line-mask"><span>DJ in Valencia and Teruel</span></span>'),
    ('<span class="line-mask"><span>para fiestas que <em>no se olvidan</em>.</span></span>',
     '<span class="line-mask"><span>for parties <em>nobody forgets</em>.</span></span>'),
    ('>Pide presupuesto <span class="arr">→</span></a>', '>Get a quote <span class="arr">→</span></a>'),
    ('>Qué hago</a>', '>What I do</a>'),
    ('<i></i>Desliza</div>', '<i></i>Scroll</div>'),
    ('aria-label="Alberto Gascón pinchando en Los Que Faltaban, Teruel"', 'aria-label="Alberto Gascón playing at Los Que Faltaban, Teruel"'),
    ('<span class="rec"></span>En directo · Los Que Faltaban, Teruel', '<span class="rec"></span>Live · Los Que Faltaban, Teruel'),
    ('<span>Discotecas</span><span class="star">✦</span><span>Festivales</span><span class="star">✦</span><span>Fiestas patronales</span><span class="star">✦</span><span>Eventos corporativos</span><span class="star">✦</span><span>Bodas</span><span class="star">✦</span>',
     '<span>Clubs</span><span class="star">✦</span><span>Festivals</span><span class="star">✦</span><span>Town fiestas</span><span class="star">✦</span><span>Corporate events</span><span class="star">✦</span><span>Weddings</span><span class="star">✦</span>'),

    # Servicios
    ('<p class="eyebrow">Servicios</p><h2>Música para que <span class="out">nadie</span> se siente</h2>',
     '<p class="eyebrow">Services</p><h2>Music so <span class="out">nobody</span> sits down</h2>'),
    ('<h3>Discotecas</h3><div><p>Sesiones para salas y discotecas comerciales: éxitos, remember y lo que esté sonando ahora, leyendo la pista en cada momento.</p><div class="tags"><span>Comercial</span><span>Remember</span><span>Actualidad</span></div>',
     '<h3>Clubs</h3><div><p>Sets for venues and commercial clubs: hits, throwbacks and whatever is playing right now, reading the dance floor all night.</p><div class="tags"><span>Commercial</span><span>Throwbacks</span><span>Current hits</span></div>'),
    ('<h3>Festivales</h3><div><p>He pinchado en MotoGP en Motorland Alcañiz y en Cheste. Sé trabajar con producción, horarios cerrados y mucho público.</p><div class="tags"><span>Festivales</span><span>Grandes eventos</span><span>Producción</span></div>',
     '<h3>Festivals</h3><div><p>I\'ve played MotoGP at Motorland Alcañiz and at Cheste. I know how to work with production teams, tight schedules and big crowds.</p><div class="tags"><span>Festivals</span><span>Large events</span><span>Production</span></div>'),
    ('<h3>Fiestas patronales</h3><div><p>Verbenas, peñas y noches grandes de fiestas. Llevo años en las de la provincia de Teruel y sé lo que pide la plaza a cada hora.</p><div class="tags"><span>Verbenas</span><span>Peñas</span><span>Plaza</span></div>',
     '<h3>Town fiestas</h3><div><p>Open-air dances, peñas (local party crews) and the big nights of a town\'s fiestas. I\'ve played the ones in the province of Teruel for years and I know what the square wants at every hour.</p><div class="tags"><span>Open-air dances</span><span>Peñas</span><span>Town square</span></div>'),
    ('<h3>Eventos privados y corporativos</h3><div><p>Cenas y fiestas de empresa, aniversarios, inauguraciones y celebraciones privadas, con música adaptada a tu gente.</p><div class="tags"><span>Empresas</span><span>Cumpleaños</span><span>Inauguraciones</span></div>',
     '<h3>Private and corporate events</h3><div><p>Company dinners and parties, anniversaries, openings and private celebrations, with music chosen for your guests.</p><div class="tags"><span>Companies</span><span>Birthdays</span><span>Openings</span></div>'),
    ('<h3>Bodas</h3><div><p>Desde el cóctel hasta el último tema de la barra libre. Preparamos juntos la música de los momentos clave, con remixes hechos para vosotros (la entrada, el primer baile, la tarta…), y yo leo la pista el resto de la noche.</p><div class="tags"><span>Cóctel</span><span>Primer baile</span><span>Remixes a medida</span><span>Barra libre</span></div>',
     '<h3>Weddings</h3><div><p>From the cocktail hour to the last song of the open bar. We plan the music for the key moments together, with remixes made just for you (the entrance, the first dance, the cake…), and I read the dance floor for the rest of the night.</p><div class="tags"><span>Cocktail hour</span><span>First dance</span><span>Custom remixes</span><span>Open bar</span></div>'),

    # Sobre mí
    ('alt="Alberto Gascón con el micrófono en la mano durante una sesión"', 'alt="Alberto Gascón holding the microphone during a set"'),
    ('<p class="eyebrow">Sobre mí</p>', '<p class="eyebrow">About me</p>'),
    ('<p class="lead">DJ de <b>Teruel</b> afincado en <b>Valencia</b>. Pincho desde los <b>13 años</b> y llevo <b>8 como profesional</b> en discotecas, festivales, fiestas patronales, eventos privados y bodas de toda España.</p>',
     '<p class="lead">DJ from <b>Teruel</b>, based in <b>Valencia</b>, Spain. I started DJing at <b>13</b> and I\'ve been <b>a professional for 8 years</b>, playing clubs, festivals, town fiestas, private events and weddings all over Spain.</p>'),
    ('<p class="body">Además de DJ soy técnico de sonido: estudié el Grado Superior de Sonido para Audiovisuales y Espectáculos en Comenius y Producción Musical e Ingeniería de Sonido en Millenia Estudios. Eso se nota en cómo suena el equipo y en que los imprevistos técnicos se resuelven sin que la fiesta pare.</p>',
     '<p class="body">As well as a DJ, I\'m a sound technician: I took the Higher Diploma in Sound for Audiovisual and Live Shows at Comenius and studied Music Production and Sound Engineering at Millenia Estudios. You can hear it in how the system sounds, and technical hiccups get fixed without the party stopping.</p>'),
    ('<span>Años tenía cuando empecé a pinchar</span>', '<span>My age when I started DJing</span>'),
    ('<span>Años como profesional</span>', '<span>Years as a professional</span>'),
    ('</sup></b><span>Bolos</span>', '</sup></b><span>Gigs</span>'),

    # Cabinas
    ('<p class="eyebrow">Dónde he pinchado</p><h2>Algunas <span class="out">cabinas</span></h2>',
     '<p class="eyebrow">Where I\'ve played</p><h2>Some of the <span class="out">booths</span></h2>'),
    ('<span class="name">Fiestas del Ángel</span><span class="where">Teruel</span>', '<span class="name">Fiestas del Ángel</span><span class="where">Teruel</span>'),
    ('<span class="name">Fiestas patronales</span><span class="where">Provincia de Teruel</span>',
     '<span class="name">Town fiestas</span><span class="where">Province of Teruel</span>'),

    # Galería
    ('<p class="eyebrow">En cabina</p><h2>Así se vive <span class="out">desde dentro</span></h2>',
     '<p class="eyebrow">In the booth</p><h2>What it feels like <span class="out">from inside</span></h2>'),
    ('>Más en Instagram <span class="arr">→</span></a>', '>More on Instagram <span class="arr">→</span></a>'),
    ('aria-label="Clip de Alberto Gascón en el escenario con luces"', 'aria-label="Clip of Alberto Gascón on stage with lights"'),
    ('Ampliar foto: ', 'Enlarge photo: '),
    ('Alberto Gascón pinchando en el escenario de unas fiestas, con el público delante', 'Alberto Gascón playing on a fiesta stage with the crowd in front'),
    ('Alberto Gascón en cabina con la Denon DJ Prime 4 en unas fiestas de Teruel', 'Alberto Gascón in the booth with the Denon DJ Prime 4 at a fiesta in Teruel'),
    ('Alberto Gascón pinchando en la plaza durante unas fiestas', 'Alberto Gascón playing in the town square during a fiesta'),
    ('Vista de la carpa llena de gente desde la cabina de Alberto Gascón', 'View of the packed marquee from Alberto Gascón\'s booth'),
    ('Alberto Gascón en un escenario con pantalla de luces rojas', 'Alberto Gascón on a stage with a red LED screen'),
    ('Alberto Gascón pinchando en un escenario de festival', 'Alberto Gascón playing on a festival stage'),
    ('Alberto Gascón en la cabina de unas fiestas en Teruel', 'Alberto Gascón in the booth at a fiesta in Teruel'),
    ('Alberto Gascón en el escenario, foto en blanco y negro', 'Alberto Gascón on stage, black and white photo'),
    ('Alberto Gascón en el escenario de unas fiestas, con banderines y público', 'Alberto Gascón on a fiesta stage with bunting and crowd'),
    ('aria-label="Foto ampliada"', 'aria-label="Enlarged photo"'),
    ('aria-label="Foto anterior"', 'aria-label="Previous photo"'),
    ('aria-label="Foto siguiente"', 'aria-label="Next photo"'),
    ('aria-label="Cerrar"', 'aria-label="Close"'),

    # Sesiones
    ('<p class="eyebrow">Sesiones</p><h2>Última <span class="out">sesión</span></h2>',
     '<p class="eyebrow">Sessions</p><h2>Latest <span class="out">set</span></h2>'),
    ('>Canal de YouTube <span class="arr">→</span></a>', '>YouTube channel <span class="arr">→</span></a>'),
    ('title="Sesión de Alberto Gascón y Alex Giménez en Jardines de Tabarca"', 'title="Alberto Gascón and Alex Giménez live at Jardines de Tabarca"'),
    ('<p>Con Alex Giménez · 1 hora</p>', '<p>With Alex Giménez · 1 hour</p>'),
    ('>Ver en YouTube ↗</a>', '>Watch on YouTube ↗</a>'),

    # On Tour
    ('<p class="eyebrow">On Tour</p><h2>Próximas <span class="out">fechas</span></h2>',
     '<p class="eyebrow">On Tour</p><h2>Upcoming <span class="out">dates</span></h2>'),
    ('>Todas las fechas <span class="arr">→</span></a>', '>All dates <span class="arr">→</span></a>'),

    # Cómo trabajo
    ('<p class="eyebrow">Cómo trabajo</p><h2>De la primera llamada <span class="out">a la pista</span></h2>',
     '<p class="eyebrow">How I work</p><h2>From the first call <span class="out">to the dance floor</span></h2>'),
    ('<b>Me escribes</b><p>Fecha, lugar y tipo de evento. Con eso ya te digo si estoy libre.</p>',
     '<b>You get in touch</b><p>Date, place and type of event. That\'s all I need to tell you if I\'m free.</p>'),
    ('<b>Presupuesto</b><p>Te paso precio cerrado según horas, equipo y desplazamiento.</p>',
     '<b>Quote</b><p>You get a fixed price based on hours, equipment and travel.</p>'),
    ('<b>Contrato</b><p>Reservamos la fecha por escrito para que los dos estemos tranquilos.</p>',
     '<b>Contract</b><p>We book the date in writing so we both have peace of mind.</p>'),
    ('<b>El día</b><p>Llego con tiempo, monto, pruebo y la fiesta empieza a su hora.</p>',
     '<b>The day</b><p>I arrive early, set up, sound-check and the party starts on time.</p>'),

    # Rider
    ('<p class="eyebrow">Para organizadores</p><h2>Rider <span class="out">técnico</span></h2>',
     '<p class="eyebrow">For organisers</p><h2>Technical <span class="out">rider</span></h2>'),
    ('>Ver press kit <span class="arr">→</span></a>', '>See press kit <span class="arr">→</span></a>'),
    ('<span class="tag">Opción 1</span><h3>Llevo mi equipo</h3><ul><li><span>Controladora <b>Denon DJ Prime 4</b> propia.</span></li><li><span>Solo necesito mesa estable, toma de corriente y conexión al equipo de sonido.</span></li></ul>',
     '<span class="tag">Option 1</span><h3>I bring my own gear</h3><ul><li><span>My own <b>Denon DJ Prime 4</b> controller.</span></li><li><span>All I need is a sturdy table, a power socket and a connection to the sound system.</span></li></ul>'),
    ('<span class="tag">Opción 2</span><h3>Cabina del organizador</h3>',
     '<span class="tag">Option 2</span><h3>Organiser\'s booth</h3>'),
    ('<li><span>Reproductores <b>Pioneer CDJ-3000</b> o superiores.</span></li><li><span>Mesa <b>DJM-900NXS2</b>, <b>DJM-A9</b> o <b>DJM-V10</b>.</span></li>',
     '<li><span><b>Pioneer CDJ-3000</b> players or better.</span></li><li><span><b>DJM-900NXS2</b>, <b>DJM-A9</b> or <b>DJM-V10</b> mixer.</span></li>'),

    # Preguntas frecuentes
    ('<p class="eyebrow">Preguntas frecuentes</p><h2>Lo que <span class="out">me preguntan</span></h2>',
     '<p class="eyebrow">FAQ</p><h2>What people <span class="out">ask me</span></h2>'),
    ('<summary>¿Dónde pinchas? ¿Te desplazas?</summary><p>Sí, me desplazo a toda España. Soy de Teruel y vivo en Valencia, así que la mayoría de mis bolos son en Teruel, Valencia y Aragón, pero si tu evento está en otra provincia, escríbeme y lo organizamos.</p>',
     '<summary>Where do you play? Do you travel?</summary><p>Yes, I travel all over Spain. I\'m from Teruel and live in Valencia, so most of my gigs are in Teruel, Valencia and Aragón, but if your event is somewhere else, drop me a line and we\'ll sort it out.</p>'),
    ('<summary>¿Qué tipo de eventos haces?</summary><p>Discotecas y salas comerciales, festivales, fiestas patronales y verbenas, eventos privados y de empresa, y bodas. He pinchado en MotoGP Motorland Alcañiz, MotoGP Cheste, La Encerrona, Los Que Faltaban, Los Chachos, Black y las Fiestas del Ángel de Teruel.</p>',
     '<summary>What kind of events do you do?</summary><p>Commercial clubs and venues, festivals, town fiestas and open-air dances, private and company events, and weddings. I\'ve played MotoGP Motorland Alcañiz, MotoGP Cheste, La Encerrona, Los Que Faltaban, Los Chachos, Black and the Fiestas del Ángel in Teruel.</p>'),
    ('<summary>¿Llevas tu propio equipo de DJ?</summary><p>Sí. Puedo llevar mi Denon DJ Prime 4. Si la sala ya tiene cabina, trabajo con Pioneer CDJ-3000 o superiores y mesa DJM-900NXS2, DJM-A9 o DJM-V10.</p>',
     '<summary>Do you bring your own DJ gear?</summary><p>Yes. I can bring my Denon DJ Prime 4. If the venue already has a booth, I work with Pioneer CDJ-3000 or better and a DJM-900NXS2, DJM-A9 or DJM-V10 mixer.</p>'),
    ('<summary>¿Cuánto cuesta contratar un DJ para unas fiestas o un evento?</summary><p>Depende de las horas, del equipo que haga falta y del desplazamiento. Cuéntame la fecha, el lugar y el tipo de evento y te paso un precio cerrado sin compromiso.</p>',
     '<summary>How much does it cost to book a DJ for a fiesta or an event?</summary><p>It depends on the hours, the equipment needed and the travel. Tell me the date, the place and the type of event and I\'ll send you a fixed price, no strings attached.</p>'),
    ('<summary>¿Puedes encargarte de todos los DJs de nuestras fiestas?</summary><p>Sí. Para comisiones de fiestas, ayuntamientos y salas organizo el cartel con DJs de la zona de confianza, con un solo contacto para todas las noches.</p>',
     '<summary>Can you handle all the DJs for our fiestas?</summary><p>Yes. For festival committees, town councils and venues I put together the line-up with trusted local DJs, with a single contact for every night.</p>'),
    ('<summary>¿Cuánta experiencia tienes?</summary><p>Pincho desde los 13 años y llevo 8 como DJ profesional, con más de 400 bolos. Tengo 24 años y además soy técnico de sonido: estudié en Comenius y en Millenia Estudios (Valencia).</p>',
     '<summary>How much experience do you have?</summary><p>I\'ve been DJing since I was 13 and professionally for 8 years, with over 400 gigs. I\'m 24 and I\'m also a sound technician: I studied at Comenius and Millenia Estudios (Valencia).</p>'),

    # Booking
    ('<h2>¿Buscas DJ para <span class="out">tus fiestas</span>?</h2>', '<h2>Need DJs for <span class="out">your fiestas</span>?</h2>'),
    ('<p>Para comisiones de fiestas, ayuntamientos y salas: el cartel lo monta <b>Salvaje Booking</b>, mi agencia, con DJs en los que confío. Un solo contacto para todas las noches.</p>',
     '<p>For festival committees, town councils and venues: <b>Salvaje Booking</b>, my agency, puts the line-up together with DJs I trust. One contact for every night.</p>'),
    ('>Ir a Salvaje Booking <span class="arr">→</span></a>', '>Go to Salvaje Booking <span class="arr">→</span></a>'),

    # Presupuesto
    ('<p class="eyebrow">Presupuesto</p>', '<p class="eyebrow">Get a quote</p>'),
    ('<h2>¿Tienes <span class="out">un evento</span>?</h2>', '<h2>Got <span class="out">an event</span>?</h2>'),
    ('<p>Mis contrataciones las lleva <b>Salvaje Booking</b>, mi agencia. Rellena el formulario con la fecha y el lugar, o escríbeles directamente, y te contestan con disponibilidad y presupuesto.</p>',
     '<p>My bookings are handled by <b>Salvaje Booking</b>, my agency. Fill in the form with the date and place, or email them directly, and they\'ll get back to you with availability and a quote.</p>'),
    ('<div class="channel"><span>Agencia</span>', '<div class="channel"><span>Agency</span>'),
    ('<label for="f-name">Nombre</label>', '<label for="f-name">Name</label>'),
    ('placeholder="Tu nombre"', 'placeholder="Your name"'),
    ('<label for="f-tel">Teléfono</label>', '<label for="f-tel">Phone</label>'),
    ('placeholder="600 000 000"', 'placeholder="+34 600 000 000"'),
    ('<label for="f-type">Tipo de evento</label>', '<label for="f-type">Type of event</label>'),
    ('<option>Discoteca</option><option>Festival</option><option>Fiestas patronales</option><option>Evento privado</option><option>Evento corporativo</option><option>Boda</option><option>Booking de DJs</option><option>Otro</option>',
     '<option>Club</option><option>Festival</option><option>Town fiesta</option><option>Private event</option><option>Corporate event</option><option>Wedding</option><option>DJ booking</option><option>Other</option>'),
    ('<label for="f-date">Fecha</label>', '<label for="f-date">Date</label>'),
    ('<label for="f-venue">Localidad</label>', '<label for="f-venue">Town / city</label>'),
    ('placeholder="Ej. Teruel"', 'placeholder="e.g. Valencia"'),
    ('<label for="f-guests">Invitados (aprox.)</label>', '<label for="f-guests">Guests (approx.)</label>'),
    ('<label for="f-msg">Mensaje</label>', '<label for="f-msg">Message</label>'),
    ('placeholder="Horario, si hay equipo de sonido en el sitio, música que os gusta…"',
     'placeholder="Timings, whether there\'s a sound system on site, music you like…"'),
    ('>Pedir presupuesto <span class="arr">→</span></button>', '>Ask for a quote <span class="arr">→</span></button>'),
    ('Se ha abierto tu correo con la petición ya escrita para Salvaje Booking. Solo tienes que enviarla. Si no se abre, escribe a contacto@salvajebooking.com.',
     'Your email app has opened with the request already written for Salvaje Booking. Just hit send. If it didn\'t open, write to contacto@salvajebooking.com.'),

    # Pie
    ('<span>DJ para discotecas, festivales y eventos · Teruel · Valencia · Toda España</span>',
     '<span>DJ for clubs, festivals and events · Teruel · Valencia · All over Spain</span>'),
    ('>Arriba ↑</a>', '>Back to top ↑</a>'),

    # Formulario (correo que se abre)
    ("campos = [['Nombre', 'name'], ['Teléfono', 'tel'], ['Tipo de evento', 'type'], ['Fecha', 'date'], ['Localidad', 'venue'], ['Invitados', 'guests'], ['Mensaje', 'msg']]",
     "campos = [['Name', 'name'], ['Phone', 'tel'], ['Type of event', 'type'], ['Date', 'date'], ['Town / city', 'venue'], ['Guests', 'guests'], ['Message', 'msg'], ['Language', 'lang']]"),
    ("var cuerpo = 'Artista: Alberto Gascón\\n'", "var cuerpo = 'Artist: Alberto Gascón\\n'"),
    ("'Petición de presupuesto · Alberto Gascón · ' + (f.elements.type.value || 'evento')",
     "'Quote request (English) · Alberto Gascón · ' + (f.elements.type.value || 'event')"),
    ("(f.elements[c[1]].value || '-')", "((f.elements[c[1]] || {}).value || (c[1] === 'lang' ? 'English' : '-'))"),
]

TOUR = [
    ('<p>Dónde puedes verme pinchar las próximas noches: discotecas, festivales y fiestas. Los eventos privados y las bodas aparecen sin detalles.</p>',
     '<p>Where you can catch me playing over the coming nights: clubs, festivals and fiestas. Private events and weddings are listed without details.</p>'),
    ('</b> próximas fechas</span>', '</b> upcoming dates</span>'),
    ('<p class="eyebrow">Próximas fechas</p>', '<p class="eyebrow">Upcoming dates</p>'),
    ('<p class="eyebrow">Archivo</p>', '<p class="eyebrow">Archive</p>'),
    ('<h2>Fechas <span class="out">pasadas</span></h2>', '<h2>Past <span class="out">dates</span></h2>'),
]

PRESSKIT = [
    ('<p class="eyebrow">Para promotores, salas y comisiones</p>', '<p class="eyebrow">For promoters, venues and committees</p>'),
    ('<p>Todo lo que necesitas para anunciar y contratar a Alberto Gascón: biografía lista para copiar, logos en alta, rider técnico y contacto directo.</p>',
     '<p>Everything you need to announce and book Alberto Gascón: a ready-to-copy bio, high-res logos, technical rider and direct contact.</p>'),
    ('>Descargar logos <span class="arr">↓</span></a>', '>Download logos <span class="arr">↓</span></a>'),
    ('>Ver biografía</a>', '>Read the bio</a>'),

    # Ficha
    ('<p class="eyebrow">Ficha rápida</p><h2>En <span class="out">30 segundos</span></h2>',
     '<p class="eyebrow">Fact sheet</p><h2>In <span class="out">30 seconds</span></h2>'),
    ('<dt>Nombre artístico</dt>', '<dt>Stage name</dt>'),
    ('<dd>Valencia (de Teruel)</dd>', '<dd>Valencia, Spain (from Teruel)</dd>'),
    ('<dt>Zona de trabajo</dt><dd>Toda España (sobre todo Teruel, Valencia y Aragón)</dd>',
     '<dt>Area</dt><dd>All over Spain (mainly Teruel, Valencia and Aragón)</dd>'),
    ('<dt>Experiencia</dt><dd>Pincha desde los 13 · 8 años como profesional · +400 bolos</dd>',
     '<dt>Experience</dt><dd>DJing since 13 · 8 years as a professional · 400+ gigs</dd>'),
    ('<dt>Edad</dt><dd>24 años (2002)</dd>', '<dt>Age</dt><dd>24 (born 2002)</dd>'),
    ('<dt>Formato</dt><dd>Discotecas · Festivales · Fiestas patronales · Eventos privados y corporativos · Bodas</dd>',
     '<dt>Formats</dt><dd>Clubs · Festivals · Town fiestas · Private and corporate events · Weddings</dd>'),
    ('<dt>Equipo</dt><dd>Denon DJ Prime 4 propia, o CDJ-3000 + DJM</dd>', '<dt>Equipment</dt><dd>His own Denon DJ Prime 4, or CDJ-3000 + DJM</dd>'),
    ('<dd>4 latas de Coca-Cola con cubitera de hielo · 4 botellas de agua</dd>', '<dd>4 cans of Coca-Cola in an ice bucket · 4 bottles of water</dd>'),
    ('<dt>Formación</dt><dd>Técnico de sonido (Comenius · Millenia Estudios)</dd>', '<dt>Training</dt><dd>Sound technician (Comenius · Millenia Estudios)</dd>'),
    ('<dt>Contratación</dt>', '<dt>Bookings</dt>'),

    # Bio
    ('<p class="eyebrow">Biografía</p><h2>Lista para <span class="out">copiar</span></h2>',
     '<p class="eyebrow">Biography</p><h2>Ready to <span class="out">copy</span></h2>'),
    ('<span class="tag">Versión corta</span>', '<span class="tag">Short version</span>'),
    ('<span class="tag">Versión larga</span>', '<span class="tag">Long version</span>'),
    ('data-copy="bio-corta">Copiar</button>', 'data-copy="bio-corta">Copy</button>'),
    ('data-copy="bio-larga">Copiar</button>', 'data-copy="bio-larga">Copy</button>'),
    ('<p>Alberto Gascón (Teruel, 2002) es DJ afincado en Valencia. Pincha desde los 13 años y lleva 8 como profesional, con más de 400 bolos en discotecas, festivales, fiestas patronales, eventos privados y bodas, con cabinas como MotoGP Motorland Alcañiz, MotoGP Cheste o La Encerrona. Técnico de sonido de formación, cuida tanto la pista como cómo suena.</p>',
     '<p>Alberto Gascón (Teruel, 2002) is a DJ based in Valencia, Spain. He has been DJing since he was 13 and professionally for 8 years, with over 400 gigs at clubs, festivals, town fiestas, private events and weddings, including MotoGP Motorland Alcañiz, MotoGP Cheste and La Encerrona. A trained sound technician, he looks after the dance floor and the sound in equal measure.</p>'),
    ('<p>Alberto Gascón (Teruel, 2002) es DJ afincado en Valencia. Empezó a pinchar con 13 años y lleva 8 como profesional, con más de 400 actuaciones entre discotecas, festivales, fiestas patronales, eventos privados y corporativos y bodas. Trabaja sobre todo en Teruel, Valencia y Aragón y se desplaza a toda España.</p>',
     '<p>Alberto Gascón (Teruel, 2002) is a DJ based in Valencia, Spain. He started DJing at 13 and has been a professional for 8 years, with over 400 shows across clubs, festivals, town fiestas, private and corporate events and weddings. He works mainly in Teruel, Valencia and Aragón and travels all over Spain.</p>'),
    ('<p>Ha pinchado en MotoGP Motorland Alcañiz y en MotoGP Cheste, en La Encerrona, Los Que Faltaban y Los Chachos de Teruel, en Black (Andorra, Teruel), en las Fiestas del Ángel y en las fiestas patronales de la provincia de Teruel.</p>',
     '<p>He has played MotoGP Motorland Alcañiz and MotoGP Cheste, La Encerrona, Los Que Faltaban and Los Chachos in Teruel, Black (Andorra, Teruel), the Fiestas del Ángel and the town fiestas of the province of Teruel.</p>'),
    ('<p>Además de DJ es técnico de sonido: estudió el Grado Superior de Sonido para Audiovisuales y Espectáculos en Comenius y Producción Musical e Ingeniería de Sonido en Millenia Estudios, en Valencia. Trabaja con su propia Denon DJ Prime 4 o en cabinas con CDJ-3000 y mesas DJM.</p>',
     '<p>As well as a DJ, he is a sound technician: he took the Higher Diploma in Sound for Audiovisual and Live Shows at Comenius and studied Music Production and Sound Engineering at Millenia Estudios in Valencia. He plays on his own Denon DJ Prime 4 or in booths with CDJ-3000s and DJM mixers.</p>'),

    # Logos
    ('<p class="eyebrow">Identidad</p><h2>Logos en <span class="out">alta</span></h2>',
     '<p class="eyebrow">Identity</p><h2>High-res <span class="out">logos</span></h2>'),
    ('>Todos en ZIP <span class="arr">↓</span></a>', '>All as ZIP <span class="arr">↓</span></a>'),
    ('alt="Logo rosa"></div><div class="meta"><span>Rosa · PNG</span>', 'alt="Pink logo"></div><div class="meta"><span>Pink · PNG</span>'),
    ('alt="Logo rojo"></div><div class="meta"><span>Rojo · PNG</span>', 'alt="Red logo"></div><div class="meta"><span>Red · PNG</span>'),
    ('alt="Logo blanco"></div><div class="meta"><span>Blanco · PNG</span>', 'alt="White logo"></div><div class="meta"><span>White · PNG</span>'),
    ('alt="Logo negro"></div><div class="meta"><span>Negro · PNG</span>', 'alt="Black logo"></div><div class="meta"><span>Black · PNG</span>'),
    (' download>Descargar</a>', ' download>Download</a>'),

    # Fotos
    ('<p class="eyebrow">Fotos</p><h2>Fotos de <span class="out">prensa</span></h2>',
     '<p class="eyebrow">Photos</p><h2>Press <span class="out">photos</span></h2>'),
    ('alt="Retrato de Alberto Gascón sobre fondo blanco, pensado para carteles"', 'alt="Portrait of Alberto Gascón on a white background, made for posters"'),
    ('<span>Retrato para cartelería (fondo blanco)</span>', '<span>Poster portrait (white background)</span>'),
    ('alt="Alberto Gascón en el escenario de unas fiestas, con el público delante"', 'alt="Alberto Gascón on a fiesta stage with the crowd in front"'),
    ('<span>Escenario con público</span>', '<span>Stage with crowd</span>'),
    ('<span>En cabina · Teruel</span>', '<span>In the booth · Teruel</span>'),
    ('<span>Con micrófono</span>', '<span>With microphone</span>'),
    ('<span>Plaza llena</span>', '<span>Packed square</span>'),
    ('<span>Escenario · pantalla roja</span>', '<span>Stage · red screen</span>'),
    ('<span>Escenario de festival</span>', '<span>Festival stage</span>'),
    ('<span>Blanco y negro</span>', '<span>Black and white</span>'),
    ('alt="Alberto Gascón en cabina con la Denon DJ Prime 4"', 'alt="Alberto Gascón in the booth with the Denon DJ Prime 4"'),
    ('<span>Escenario con banderines</span>', '<span>Stage with bunting</span>'),
    ('<span>Vista desde cabina</span>', '<span>View from the booth</span>'),
    ('<span>Fotos en alta resolución para carteles, prensa y redes.</span>', '<span>High-resolution photos for posters, press and social media.</span>'),
    ('>Descargar todas (ZIP · 6 MB) <span class="arr">→</span></a>', '>Download all (ZIP · 6 MB) <span class="arr">→</span></a>'),

    # Rider
    ('<span class="tag">Opción 1</span><h3>Lleva su equipo</h3><ul><li><span>Controladora <b>Denon DJ Prime 4</b> propia.</span></li><li><span>Necesita mesa estable, toma de corriente y conexión al equipo de sonido.</span></li></ul>',
     '<span class="tag">Option 1</span><h3>He brings his own gear</h3><ul><li><span>His own <b>Denon DJ Prime 4</b> controller.</span></li><li><span>Needs a sturdy table, a power socket and a connection to the sound system.</span></li></ul>'),
    ('<span class="tag">Hospitality</span><h3>En cabina</h3><ul><li><span><b>4 latas de Coca-Cola</b> con su cubitera de hielo.</span></li><li><span><b>4 botellas de agua</b>.</span></li></ul>',
     '<span class="tag">Hospitality</span><h3>In the booth</h3><ul><li><span><b>4 cans of Coca-Cola</b> in an ice bucket.</span></li><li><span><b>4 bottles of water</b>.</span></li></ul>'),

    # Trayectoria
    ('<p class="eyebrow">Trayectoria</p><h2>Ha <span class="out">pinchado en</span></h2>',
     '<p class="eyebrow">Track record</p><h2>Has <span class="out">played at</span></h2>'),
    ('<span>Fiestas patronales<small>Provincia de Teruel</small></span>', '<span>Town fiestas<small>Province of Teruel</small></span>'),

    # Contacto
    ('<p class="eyebrow">Contratación</p>', '<p class="eyebrow">Bookings</p>'),
    ('<h2>¿Lo quieres <span class="out">en tu cartel</span>?</h2>', '<h2>Want him <span class="out">on your line-up</span>?</h2>'),
    ('<p>Sus contrataciones las lleva Salvaje Booking. Escribe a <a href="mailto:contacto@salvajebooking.com">contacto@salvajebooking.com</a> con fecha, sala y horario y te contestan con disponibilidad y presupuesto.</p>',
     '<p>His bookings are handled by Salvaje Booking. Email <a href="mailto:contacto@salvajebooking.com">contacto@salvajebooking.com</a> with the date, venue and set time and they\'ll get back to you with availability and a quote.</p>'),
    ('>Pedir presupuesto <span class="arr">→</span></a>', '>Ask for a quote <span class="arr">→</span></a>'),

    # Botón copiar
    ("b.textContent = 'Copiada'; setTimeout(function () { b.textContent = 'Copiar'; }, 1800);",
     "b.textContent = 'Copied'; setTimeout(function () { b.textContent = 'Copy'; }, 1800);"),
    ("b.textContent = 'Seleccionada';", "b.textContent = 'Selected';"),
]

# Datos estructurados (JSON-LD): textos exactos
JSONLD = {
    "Teruel, España": "Teruel, Spain",
    "Valencia, España": "Valencia, Spain",
    "DJ de Teruel con base en Valencia, pinchando desde los 13 años y profesional desde hace 8, para discotecas, festivales, fiestas patronales, eventos privados y corporativos y bodas.":
        "DJ from Teruel based in Valencia, Spain, DJing since age 13 and professionally for 8 years, for clubs, festivals, town fiestas, private and corporate events and weddings.",
    "Sesiones de discoteca": "Club sets",
    "Fiestas patronales": "Town fiestas",
    "Bodas": "Weddings",
    "Técnico de sonido": "Sound technician",
    "España": "Spain",
    "Provincia de Teruel": "Province of Teruel",
    "Comunidad Valenciana": "Valencian Community",
    "DJ para discotecas": "DJ for clubs",
    "DJ para festivales": "DJ for festivals",
    "DJ para fiestas patronales": "DJ for town fiestas",
    "DJ para eventos privados y corporativos": "DJ for private and corporate events",
    "DJ para bodas": "Wedding DJ",
    "Booking de DJs para fiestas": "DJ booking for fiestas",
    "Servicio de DJ en Teruel, Valencia, Aragón y toda España: discotecas, festivales, fiestas patronales, eventos privados y corporativos, bodas y booking de DJs.":
        "DJ service in Teruel, Valencia, Aragón and all over Spain: clubs, festivals, town fiestas, private and corporate events, weddings and DJ booking.",
    "Servicios de DJ": "DJ services",
    "Próximas fechas de Alberto Gascón": "Upcoming dates for Alberto Gascón",
}
