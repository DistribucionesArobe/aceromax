import os

GA4 = """<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-HTPSHZR7NT"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-HTPSHZR7NT');
</script>"""

brands = [
  {
    "slug": "usg",
    "name": "USG",
    "fullname": "USG (United States Gypsum)",
    "title": "Distribuidor Oficial USG en Ciudad Victoria | Tablaroca, Durock, Plafones | AceroMAX",
    "desc": "Distribuidor oficial USG en Ciudad Victoria, Tamaulipas. Tablaroca Ultralight, Durock, plafones acústicos, perfiles, redimix y accesorios. 2 sucursales, entrega a domicilio. Cotiza por WhatsApp.",
    "keywords": "USG ciudad victoria, distribuidor USG tamaulipas, tablaroca USG victoria, durock USG ciudad victoria, plafones USG tamaulipas, venta tablaroca USG, ultralight USG precio, distribuidor autorizado USG",
    "category": "Construcción Ligera",
    "products": ["Tablaroca Ultralight 1/2\"", "Tablaroca Ultralight 5/8\"", "Tablaroca RH (resistente a humedad)", "Tablaroca FIRECODE (resistente al fuego)", "Durock 1/2\" panel de cemento", "Plafón Radar Climaplus", "Plafón Olympia Micro", "Plafón Ceramic Climaplus", "Perfiles USG: postes y canales", "Redimix USG", "Perfacinta USG", "Pijas y tornillos USG", "Basecoat USG", "Esquinero metálico y vinílico"],
    "intro": "AceroMAX es distribuidor oficial y concesionario autorizado de <strong>USG</strong> en Ciudad Victoria, Tamaulipas. Manejamos la línea completa de productos USG para construcción ligera: tablaroca Ultralight, paneles Durock, plafones acústicos y todos los accesorios para instalación profesional.",
    "why": "Como concesionarios directos de USG, compramos de fábrica sin intermediarios. Esto significa precios más bajos que la competencia, producto original garantizado y asesoría técnica especializada en sistemas de construcción ligera.",
    "faqs": [
      ("¿Dónde comprar tablaroca USG en Ciudad Victoria?", "En AceroMAX, distribuidor oficial USG con 2 sucursales en Ciudad Victoria: Hombres Ilustres 510 y Naciones Unidas 1155. Manejamos toda la línea USG: Ultralight, RH, FIRECODE, Durock, plafones, perfiles y accesorios."),
      ("¿Cuál es la diferencia entre tablaroca Ultralight y regular USG?", "La Tablaroca Ultralight USG es 30% más ligera que la regular, facilitando transporte e instalación sin perder resistencia. Es la más vendida en Ciudad Victoria para muros divisorios y plafones residenciales y comerciales."),
      ("¿Tienen plafones acústicos USG en Ciudad Victoria?", "Sí. Manejamos toda la línea de plafones USG: Radar Climaplus, Olympia Micro y Ceramic Climaplus. Ideales para oficinas, clínicas, escuelas y comercios en Ciudad Victoria y la región."),
    ],
    "related_categories": [("Tablaroca y Durock", "/tablaroca-durock/"), ("Plafones", "/plafones/")],
  },
  {
    "slug": "prolamsa",
    "name": "Prolamsa",
    "fullname": "Prolamsa (Productos Laminados de Monterrey)",
    "title": "Distribuidor Oficial Prolamsa en Ciudad Victoria | PTR, Perfiles, Tubería | AceroMAX",
    "desc": "Distribuidor oficial Prolamsa en Ciudad Victoria, Tamaulipas. PTR, perfiles tubulares, tubería estructural, postes para cerca. Todos los calibres y medidas. Entrega a domicilio.",
    "keywords": "Prolamsa ciudad victoria, distribuidor Prolamsa tamaulipas, PTR Prolamsa victoria, perfiles Prolamsa, tubería estructural ciudad victoria, PTR precio victoria, distribuidor autorizado Prolamsa",
    "category": "Acero Estructural",
    "products": ["PTR (perfil tubular rectangular) todos los calibres", "Tubería estructural redonda", "Tubería cuadrada", "Postes para cerca", "Perfil estructural HSS", "Tubería industrial", "Polines", "Perfil omega"],
    "intro": "AceroMAX es distribuidor oficial y concesionario autorizado de <strong>Prolamsa</strong> en Ciudad Victoria, Tamaulipas. Manejamos la línea completa de perfiles tubulares: PTR, tubería redonda, cuadrada, postes para cerca y perfil estructural en todos los calibres y medidas.",
    "why": "Prolamsa es el fabricante #1 de perfiles tubulares en México. Como concesionarios directos, tenemos acceso a toda la gama de medidas, calibres del 10 al 18, y largos estándar de 6 metros. Stock permanente en las medidas más demandadas.",
    "faqs": [
      ("¿Dónde comprar PTR Prolamsa en Ciudad Victoria?", "En AceroMAX, distribuidor oficial Prolamsa. Tenemos PTR en todas las medidas desde 1\"x1\" hasta 6\"x6\", calibres 10 a 18. 2 sucursales en Ciudad Victoria con entrega a domicilio."),
      ("¿Qué calibres de PTR manejan en AceroMAX?", "Manejamos PTR Prolamsa en calibres 10, 11, 12, 14, 16 y 18. Los más vendidos para construcción en Ciudad Victoria son calibre 14 y 12 en medidas 2x2, 2x4 y 3x3 pulgadas."),
      ("¿Hacen cortes de PTR a medida?", "Sí. En AceroMAX hacemos cortes de PTR y perfiles a la medida que necesites. Solo dinos las dimensiones y te lo preparamos. Cotiza por WhatsApp al 834 852 82 36."),
    ],
    "related_categories": [("PTR y Perfiles", "/ptr-perfiles/"), ("Acero Estructural", "/acero-estructural/"), ("Losacero", "/losacero/")],
  },
  {
    "slug": "deacero",
    "name": "Deacero",
    "fullname": "Deacero",
    "title": "Distribuidor Oficial Deacero en Ciudad Victoria | Varilla, Mallas, Alambre | AceroMAX",
    "desc": "Distribuidor oficial Deacero en Ciudad Victoria, Tamaulipas. Varilla corrugada, malla ciclónica, malla electrosoldada, alambre galvanizado, alambre de púas. Entrega a domicilio.",
    "keywords": "Deacero ciudad victoria, distribuidor Deacero tamaulipas, varilla Deacero victoria, malla ciclónica Deacero, alambre galvanizado, malla electrosoldada, distribuidor autorizado Deacero",
    "category": "Varilla y Mallas",
    "products": ["Varilla corrugada #2 al #8", "Varilla grado 42 y grado 60", "Malla ciclónica galvanizada", "Malla electrosoldada 6x6", "Alambre galvanizado cal. 14, 16, 18", "Alambre recocido", "Alambre de púas", "Clavo galvanizado", "Grapas", "Castillo armado"],
    "intro": "AceroMAX es distribuidor oficial y concesionario autorizado de <strong>Deacero</strong> en Ciudad Victoria, Tamaulipas. Manejamos toda la línea de productos Deacero: varilla corrugada, mallas, alambres y derivados del acero para construcción y uso perimetral.",
    "why": "Deacero es el fabricante de aceros largos más grande de México. Como concesionarios directos, garantizamos producto certificado que cumple con norma NMX-C-407, precios competitivos por volumen y stock permanente en las medidas más comunes.",
    "faqs": [
      ("¿Dónde comprar varilla Deacero en Ciudad Victoria?", "En AceroMAX, distribuidor oficial Deacero. Manejamos varilla corrugada del #2 al #8, grado 42 y 60. 2 sucursales en Ciudad Victoria con entrega a obra."),
      ("¿Qué tipos de malla manejan de Deacero?", "Manejamos malla ciclónica galvanizada (1.50m a 3.00m), malla electrosoldada 6x6 para losas, y malla gallinera. Todo producto Deacero original con certificado."),
      ("¿Venden alambre por rollo o por kilo?", "Vendemos alambre galvanizado y recocido Deacero tanto por rollo completo como por kilo. Calibres 14, 16 y 18 en existencia permanente."),
    ],
    "related_categories": [("Varilla y Cemento", "/varilla-cemento/"), ("Mallas", "/mallas/")],
  },
  {
    "slug": "ternium",
    "name": "Ternium",
    "fullname": "Ternium México",
    "title": "Distribuidor Oficial Ternium en Ciudad Victoria | Láminas, Losacero, Acero | AceroMAX",
    "desc": "Distribuidor oficial Ternium en Ciudad Victoria, Tamaulipas. Láminas galvanizadas, losacero, acero estructural. Todos los calibres. 2 sucursales, entrega a domicilio.",
    "keywords": "Ternium ciudad victoria, distribuidor Ternium tamaulipas, lámina galvanizada Ternium, losacero Ternium victoria, acero Ternium, lámina calibre 26 victoria, distribuidor autorizado Ternium",
    "category": "Láminas y Acero",
    "products": ["Lámina galvanizada cal. 22, 24, 26, 28", "Lámina pintada (pintro)", "Lámina acanalada R-72", "Lámina KR-18", "Losacero calibre 22", "Lámina lisa galvanizada", "Lámina zintro-alum", "Acero estructural: IPR, IPS, canal, ángulo"],
    "intro": "AceroMAX es distribuidor oficial de <strong>Ternium</strong> en Ciudad Victoria, Tamaulipas. Manejamos la línea completa de láminas galvanizadas, losacero y acero estructural Ternium para techumbres, naves industriales y construcción pesada.",
    "why": "Ternium es el productor de acero plano más importante de México. Como distribuidores oficiales, tenemos acceso a toda la gama de calibres y acabados, precios de fábrica y entregas de camión completo o parciales.",
    "faqs": [
      ("¿Dónde comprar lámina galvanizada Ternium en Ciudad Victoria?", "En AceroMAX, distribuidor oficial Ternium. Tenemos lámina galvanizada en calibres 22, 24, 26 y 28. Medidas estándar y cortes especiales. 2 sucursales en Ciudad Victoria."),
      ("¿Qué es el losacero y para qué sirve?", "El losacero Ternium es una lámina acanalada que sirve como cimbra perdida y refuerzo para colado de losas de entrepiso. Elimina la cimbra de madera, ahorra tiempo y concreto. Disponible en calibre 22."),
      ("¿Manejan lámina pintada Ternium?", "Sí, manejamos lámina pintada (pintro) Ternium en varios colores: rojo, azul, verde, blanco, gris. Ideal para fachadas, bardas y techumbres con acabado estético."),
    ],
    "related_categories": [("Láminas", "/laminas/"), ("Losacero", "/losacero/"), ("Acero Estructural", "/acero-estructural/")],
  },
  {
    "slug": "apasco",
    "name": "Apasco",
    "fullname": "Apasco (Holcim México)",
    "title": "Distribuidor Oficial Apasco en Ciudad Victoria | Cemento, Mortero | AceroMAX",
    "desc": "Distribuidor oficial de Cemento Apasco (Holcim) en Ciudad Victoria, Tamaulipas. Cemento gris 50 kg, mortero, pegablock. Existencia permanente, entrega a obra.",
    "keywords": "Apasco ciudad victoria, cemento Apasco victoria, distribuidor cemento tamaulipas, Holcim ciudad victoria, cemento 50 kg victoria, precio cemento victoria, distribuidor autorizado Apasco",
    "category": "Cemento",
    "products": ["Cemento gris Apasco 50 kg", "Cemento Apasco Extra (alta resistencia)", "Mortero Apasco", "Pegablock Apasco", "Cemento blanco"],
    "intro": "AceroMAX es distribuidor oficial de <strong>Cemento Apasco (Holcim)</strong> en Ciudad Victoria, Tamaulipas. Manejamos cemento gris 50 kg con existencia permanente, mortero y productos especializados para todo tipo de obra.",
    "why": "Apasco (Holcim) es una de las cementeras líderes a nivel mundial. Como distribuidores oficiales en Ciudad Victoria, garantizamos producto fresco de fecha reciente, precio competitivo y entrega directa a tu obra.",
    "faqs": [
      ("¿Dónde comprar cemento Apasco en Ciudad Victoria?", "En AceroMAX, distribuidor oficial Apasco (Holcim). Tenemos cemento gris 50 kg en existencia permanente. 2 sucursales en Ciudad Victoria con entrega a obra."),
      ("¿Cuánto cuesta el cemento en Ciudad Victoria?", "El precio del cemento Apasco varía según la cantidad. Cotiza por WhatsApp al 834 852 82 36 para precio del día. Tenemos descuento por volumen para constructoras y contratistas."),
      ("¿Entregan cemento a domicilio?", "Sí. Entregamos cemento Apasco a tu obra en Ciudad Victoria, Güémez, Jiménez, Padilla y Llera. Pedidos desde 1 tonelada hasta camiones completos."),
    ],
    "related_categories": [("Varilla y Cemento", "/varilla-cemento/")],
  },
  {
    "slug": "doal",
    "name": "DOAL",
    "fullname": "Pinturas DOAL",
    "title": "Distribuidor Oficial Pinturas DOAL en Ciudad Victoria | Vinílicas, Esmaltes | AceroMAX",
    "desc": "Distribuidor oficial de Pinturas DOAL en Ciudad Victoria, Tamaulipas. Vinílicas, esmaltes, impermeabilizantes, texturizados. Toda la gama de colores. 2 sucursales.",
    "keywords": "DOAL ciudad victoria, pinturas DOAL tamaulipas, distribuidor pinturas victoria, vinílica DOAL, esmalte DOAL, impermeabilizante, pintura precio victoria, distribuidor autorizado DOAL",
    "category": "Pinturas",
    "products": ["Pintura vinílica DOAL (interior/exterior)", "Esmalte alquidálico DOAL", "Impermeabilizante DOAL", "Texturizado DOAL", "Sellador DOAL", "Barniz DOAL", "Primer anticorrosivo"],
    "intro": "AceroMAX es distribuidor oficial de <strong>Pinturas DOAL</strong> en Ciudad Victoria, Tamaulipas. Ofrecemos la línea completa de pinturas vinílicas, esmaltes, impermeabilizantes, texturizados y productos especializados para acabados profesionales.",
    "why": "DOAL es una marca mexicana con presencia en el noreste del país, reconocida por su cubriente superior y rendimiento. Como distribuidores oficiales, ofrecemos toda la gama de colores, asesoría en selección de producto y precios de distribuidor.",
    "faqs": [
      ("¿Dónde comprar pintura DOAL en Ciudad Victoria?", "En AceroMAX, distribuidor oficial DOAL. Tenemos toda la línea: vinílicas, esmaltes, impermeabilizantes, texturizados y selladores. 2 sucursales en Ciudad Victoria."),
      ("¿Tienen sistema de colorimetría DOAL?", "Sí, podemos preparar el color exacto que necesitas con el sistema de colorimetría DOAL. Trae tu muestra y te la igualamos en minutos."),
      ("¿Cuál pintura DOAL recomiendan para exteriores?", "Para exteriores en Ciudad Victoria recomendamos la línea DOAL de alto rendimiento exterior, resistente a rayos UV y lluvia. Combinada con impermeabilizante DOAL para máxima protección."),
    ],
    "related_categories": [("Pinturas", "/pinturas/")],
  },
  {
    "slug": "alvamex",
    "name": "Alvamex",
    "fullname": "Pinturas Alvamex",
    "title": "Distribuidor Oficial Pinturas Alvamex en Ciudad Victoria | Línea Económica | AceroMAX",
    "desc": "Distribuidor oficial de Pinturas Alvamex en Ciudad Victoria, Tamaulipas. Línea económica y rendidora para interiores y exteriores. Toda la gama de colores.",
    "keywords": "Alvamex ciudad victoria, pinturas Alvamex tamaulipas, pintura económica victoria, distribuidor Alvamex, pintura barata ciudad victoria, distribuidor autorizado Alvamex",
    "category": "Pinturas",
    "products": ["Pintura vinílica Alvamex", "Esmalte Alvamex", "Impermeabilizante Alvamex", "Sellador Alvamex", "Texturizado Alvamex"],
    "intro": "AceroMAX es distribuidor oficial de <strong>Pinturas Alvamex</strong> en Ciudad Victoria, Tamaulipas. Línea económica con excelente rendimiento y cubriente para interiores y exteriores. Toda la gama de colores disponible.",
    "why": "Alvamex ofrece la mejor relación calidad-precio en pinturas para proyectos con presupuesto ajustado sin sacrificar acabado. Como distribuidores oficiales, tenemos precios de fábrica.",
    "faqs": [
      ("¿Dónde comprar pintura Alvamex en Ciudad Victoria?", "En AceroMAX, distribuidor oficial Alvamex. Manejamos vinílicas, esmaltes, impermeabilizantes y selladores. 2 sucursales en Ciudad Victoria."),
      ("¿Es buena la pintura Alvamex?", "Sí, Alvamex ofrece excelente rendimiento a precio accesible. Es la mejor opción para proyectos grandes donde se necesita cubrir muchos metros cuadrados con buen acabado."),
    ],
    "related_categories": [("Pinturas", "/pinturas/")],
  },
  {
    "slug": "megapanel",
    "name": "Megapanel",
    "fullname": "Megapanel",
    "title": "Distribuidor Oficial Megapanel en Ciudad Victoria | Panel Aislante | AceroMAX",
    "desc": "Distribuidor oficial de Megapanel en Ciudad Victoria, Tamaulipas. Panel aislante para techos, muros y fachadas. Térmico, acústico y estructural. Naves industriales y casas.",
    "keywords": "Megapanel ciudad victoria, panel aislante tamaulipas, distribuidor Megapanel victoria, panel sandwich victoria, panel térmico, distribuidor autorizado Megapanel, naves industriales victoria",
    "category": "Paneles Aislantes",
    "products": ["Panel aislante para techo", "Panel aislante para muro", "Panel aislante para fachada", "Panel frigorífico", "Accesorios de fijación Megapanel"],
    "intro": "AceroMAX es distribuidor oficial de <strong>Megapanel</strong> en Ciudad Victoria, Tamaulipas. Panel aislante de alto desempeño para techos, muros y fachadas. Solución todo en uno: térmico, acústico y estructural.",
    "why": "Megapanel reduce tiempos de construcción hasta 60% vs. sistemas tradicionales. Es la solución ideal para naves industriales, bodegas, cámaras frías, oficinas y vivienda moderna en Ciudad Victoria y la región.",
    "faqs": [
      ("¿Dónde comprar Megapanel en Ciudad Victoria?", "En AceroMAX, distribuidor oficial Megapanel. Manejamos paneles para techo, muro y fachada. Cotiza tu proyecto por WhatsApp al 834 852 82 36."),
      ("¿Para qué sirve el Megapanel?", "Megapanel es un panel aislante tipo sándwich que funciona como estructura, aislante térmico y acabado al mismo tiempo. Ideal para naves industriales, bodegas, oficinas y casas modernas."),
    ],
    "related_categories": [("Plafones", "/plafones/"), ("Láminas", "/laminas/")],
  },
  {
    "slug": "truper",
    "name": "Truper",
    "fullname": "Truper",
    "title": "Distribuidor Oficial Truper en Ciudad Victoria | Herramienta Manual | AceroMAX",
    "desc": "Distribuidor oficial Truper en Ciudad Victoria, Tamaulipas. Herramienta manual profesional: llaves, pinzas, martillos, desarmadores, niveles, cintas. Calidad mexicana.",
    "keywords": "Truper ciudad victoria, herramienta Truper tamaulipas, distribuidor Truper victoria, ferretería Truper, llaves Truper, pinzas Truper, distribuidor autorizado Truper",
    "category": "Herramientas",
    "products": ["Llaves mixtas y de tubo Truper", "Pinzas Truper (electricista, mecánica, presión)", "Martillos Truper", "Desarmadores Truper", "Niveles Truper", "Cintas métricas Truper", "Candados Truper", "Seguetas y arcos Truper", "Escaleras Truper", "Carretillas Truper"],
    "intro": "AceroMAX es distribuidor oficial de <strong>Truper</strong> en Ciudad Victoria, Tamaulipas. La marca mexicana #1 en herramienta manual. Llaves, pinzas, martillos, desarmadores, niveles, cintas y toda la línea de ferretería profesional.",
    "why": "Truper es la marca de herramienta más reconocida de México, con garantía de por vida en muchos productos. Como distribuidores oficiales, ofrecemos toda la línea a precios de distribuidor con garantía directa.",
    "faqs": [
      ("¿Dónde comprar herramienta Truper en Ciudad Victoria?", "En AceroMAX, distribuidor oficial Truper. Tenemos toda la línea de herramienta manual: llaves, pinzas, martillos, desarmadores, niveles y más. 2 sucursales en Ciudad Victoria."),
      ("¿Truper tiene garantía?", "Sí, Truper ofrece garantía de por vida en muchos de sus productos. Como distribuidor oficial, procesamos la garantía directamente."),
    ],
    "related_categories": [("Puertas y Ferretería", "/puertas-ferreteria/")],
  },
  {
    "slug": "makita",
    "name": "Makita",
    "fullname": "Makita",
    "title": "Distribuidor Oficial Makita en Ciudad Victoria | Herramienta Eléctrica | AceroMAX",
    "desc": "Distribuidor oficial Makita en Ciudad Victoria, Tamaulipas. Taladros, rotomartillos, sierras, pulidoras, atornilladores inalámbricos. Garantía directa.",
    "keywords": "Makita ciudad victoria, herramienta Makita tamaulipas, distribuidor Makita victoria, taladro Makita, rotomartillo Makita, sierra Makita, distribuidor autorizado Makita, herramienta eléctrica victoria",
    "category": "Herramientas Eléctricas",
    "products": ["Taladro percutor Makita", "Rotomartillo Makita SDS-Plus", "Sierra circular Makita", "Pulidora/esmeriladora Makita", "Atornillador de impacto inalámbrico", "Taladro inalámbrico 18V LXT", "Caladora Makita", "Compresor Makita", "Generador Makita", "Baterías y cargadores Makita"],
    "intro": "AceroMAX es distribuidor oficial de <strong>Makita</strong> en Ciudad Victoria, Tamaulipas. Herramienta eléctrica de calidad japonesa: taladros, rotomartillos, sierras, pulidoras, atornilladores inalámbricos y toda la línea profesional.",
    "why": "Makita es sinónimo de durabilidad y precisión, con más de 100 años de experiencia. Como distribuidores oficiales, ofrecemos garantía directa de fábrica, precios de distribuidor y asesoría para elegir la herramienta correcta.",
    "faqs": [
      ("¿Dónde comprar herramienta Makita en Ciudad Victoria?", "En AceroMAX, distribuidor oficial Makita. Tenemos taladros, rotomartillos, sierras, pulidoras, atornilladores inalámbricos y toda la línea. 2 sucursales en Ciudad Victoria."),
      ("¿Makita tiene garantía en AceroMAX?", "Sí. Como distribuidor oficial, la garantía Makita aplica directamente. Si tu herramienta presenta falla, nosotros gestionamos la garantía de fábrica."),
      ("¿Qué sistema de baterías Makita manejan?", "Manejamos el sistema 18V LXT de Makita, el más popular entre profesionales. Baterías de 3.0Ah, 5.0Ah y 6.0Ah compatibles con más de 200 herramientas."),
    ],
    "related_categories": [("Puertas y Ferretería", "/puertas-ferreteria/")],
  },
  {
    "slug": "dewalt",
    "name": "DeWalt",
    "fullname": "DeWalt",
    "title": "Distribuidor Oficial DeWalt en Ciudad Victoria | Herramienta Profesional | AceroMAX",
    "desc": "Distribuidor oficial DeWalt en Ciudad Victoria, Tamaulipas. Taladros, rotomartillos, sierras, atornilladores de impacto. Línea profesional con garantía directa.",
    "keywords": "DeWalt ciudad victoria, herramienta DeWalt tamaulipas, distribuidor DeWalt victoria, taladro DeWalt, rotomartillo DeWalt, sierra DeWalt, distribuidor autorizado DeWalt, herramienta profesional victoria",
    "category": "Herramientas Profesionales",
    "products": ["Taladro percutor DeWalt 20V MAX", "Rotomartillo DeWalt SDS-Plus", "Sierra circular DeWalt", "Atornillador de impacto DeWalt 20V", "Esmeriladora DeWalt", "Sierra reciprocante DeWalt", "Nivel láser DeWalt", "Combo kits DeWalt", "Baterías y cargadores 20V MAX", "Accesorios y brocas DeWalt"],
    "intro": "AceroMAX es distribuidor oficial de <strong>DeWalt</strong> en Ciudad Victoria, Tamaulipas. Herramienta profesional de grado industrial: taladros, rotomartillos, sierras, atornilladores de impacto y toda la plataforma 20V MAX.",
    "why": "DeWalt es la marca preferida de contratistas profesionales en todo el mundo. Como distribuidores oficiales en Ciudad Victoria, ofrecemos la línea completa con garantía de 3 años, servicio técnico y precios de distribuidor.",
    "faqs": [
      ("¿Dónde comprar herramienta DeWalt en Ciudad Victoria?", "En AceroMAX, distribuidor oficial DeWalt. Tenemos toda la línea profesional 20V MAX: taladros, rotomartillos, sierras, atornilladores de impacto y accesorios. 2 sucursales en Ciudad Victoria."),
      ("¿Cuántos años de garantía tiene DeWalt?", "DeWalt ofrece 3 años de garantía en herramienta, 1 año de servicio gratuito y 90 días de reembolso. Como distribuidor oficial, procesamos la garantía directamente."),
      ("¿DeWalt 20V MAX es compatible con FlexVolt?", "Sí, las baterías FlexVolt de 60V son retrocompatibles con todas las herramientas 20V MAX de DeWalt. Es la plataforma más versátil del mercado."),
    ],
    "related_categories": [("Puertas y Ferretería", "/puertas-ferreteria/")],
  },
]

def gen_page(b):
    products_html = "\n".join([f'<li>{p}</li>' for p in b["products"]])
    faqs_schema = ",\n".join([
        f'{{"@type":"Question","name":"{q}","acceptedAnswer":{{"@type":"Answer","text":"{a}"}}}}'
        for q, a in b["faqs"]
    ])
    faqs_html = "\n".join([
        f'<div class="faq-item"><button class="faq-question">{q}</button><div class="faq-answer"><p>{a}</p></div></div>'
        for q, a in b["faqs"]
    ])
    related_html = "\n".join([
        f'<a href="{url}" class="category-card"><h3>{name}</h3><p>Ver productos →</p></a>'
        for name, url in b["related_categories"]
    ])

    return f'''<!DOCTYPE html>
<html lang="es-MX">
<head>
{GA4}
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{b["title"]}</title>
<meta name="description" content="{b["desc"]}">
<meta name="keywords" content="{b["keywords"]}">
<meta name="robots" content="index, follow, max-image-preview:large">
<link rel="canonical" href="https://aceromax.mx/marcas/{b["slug"]}/">
<meta property="og:title" content="{b["title"]}">
<meta property="og:description" content="{b["desc"]}">
<meta property="og:url" content="https://aceromax.mx/marcas/{b["slug"]}/">
<meta property="og:type" content="website">
<meta property="og:locale" content="es_MX">
<meta name="geo.region" content="MX-TAM">
<meta name="geo.placename" content="Ciudad Victoria">
<meta name="geo.position" content="23.7369;-99.1411">
<meta name="ICBM" content="23.7369, -99.1411">
<link rel="stylesheet" href="/css/style.css">

<script type="application/ld+json">
{{
  "@context":"https://schema.org",
  "@type":"HardwareStore",
  "name":"AceroMAX — Distribuidor {b["name"]} en Ciudad Victoria",
  "image":"https://aceromax.mx/images/logo.png",
  "url":"https://aceromax.mx/marcas/{b["slug"]}/",
  "telephone":"+528341100942",
  "priceRange":"$$",
  "address":[{{
    "@type":"PostalAddress",
    "streetAddress":"Hombres Ilustres 510, Col. Adolfo López Mateos",
    "addressLocality":"Ciudad Victoria",
    "addressRegion":"Tamaulipas",
    "postalCode":"87020",
    "addressCountry":"MX"
  }},{{
    "@type":"PostalAddress",
    "streetAddress":"Naciones Unidas 1155, Fracc. Naciones Unidas",
    "addressLocality":"Ciudad Victoria",
    "addressRegion":"Tamaulipas",
    "postalCode":"87049",
    "addressCountry":"MX"
  }}],
  "geo":{{"@type":"GeoCoordinates","latitude":23.7369,"longitude":-99.1411}},
  "areaServed":[
    {{"@type":"City","name":"Ciudad Victoria"}},
    {{"@type":"City","name":"Güémez"}},
    {{"@type":"City","name":"Jiménez"}},
    {{"@type":"City","name":"Padilla"}},
    {{"@type":"City","name":"Llera"}},
    {{"@type":"State","name":"Tamaulipas"}}
  ],
  "brand":{{"@type":"Brand","name":"{b["name"]}"}},
  "openingHoursSpecification":[
    {{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday"],"opens":"08:00","closes":"18:00"}},
    {{"@type":"OpeningHoursSpecification","dayOfWeek":"Saturday","opens":"08:00","closes":"14:00"}}
  ],
  "sameAs":["https://www.facebook.com/aceromaxcdvictoria"]
}}
</script>

<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
{faqs_schema}
]}}
</script>

<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
{{"@type":"ListItem","position":1,"name":"Inicio","item":"https://aceromax.mx/"}},
{{"@type":"ListItem","position":2,"name":"Marcas","item":"https://aceromax.mx/marcas/"}},
{{"@type":"ListItem","position":3,"name":"{b["name"]}","item":"https://aceromax.mx/marcas/{b["slug"]}/"}}
]}}
</script>
</head>
<body>

<div class="topbar"><div class="container">
<div><a href="tel:+528341100942">834 110 0942</a> &nbsp;|&nbsp; <a href="tel:+528343132000">834 313 2000</a> &nbsp;|&nbsp; <a href="mailto:acero2@aceromax.mx">acero2@aceromax.mx</a></div>
<div>Lun-Vie 8:00-18:00 &nbsp;|&nbsp; Sab 8:00-14:00</div>
</div></div>

<nav><div class="container">
<a href="/" class="logo">Acero<span>MAX</span></a>
<button class="hamburger" onclick="document.querySelector('.nav-links').classList.toggle('active')" aria-label="Menú">&#9776;</button>
<ul class="nav-links">
<li><a href="/#productos">Productos</a></li>
<li><a href="/marcas/">Marcas</a></li>
<li><a href="/nosotros/">Nosotros</a></li>
<li><a href="/contacto/">Contacto</a></li>
<li><a href="https://wa.me/528348528236?text=Hola%2C%20quiero%20cotizar%20productos%20{b["name"]}" class="nav-cta" target="_blank" rel="noopener">Cotizar por WhatsApp</a></li>
</ul>
</div></nav>

<section class="page-hero" style="background:linear-gradient(135deg, var(--dark) 0%, #16213e 100%); color:white; padding:60px 0;">
<div class="container">
<p style="color:var(--accent);font-weight:600;margin-bottom:8px;">DISTRIBUIDOR OFICIAL</p>
<h1 style="font-size:2.4rem;font-weight:900;margin-bottom:16px;">{b["name"]} en Ciudad Victoria</h1>
<p style="font-size:1.15rem;color:#ccd;max-width:700px;">Concesionario autorizado {b["fullname"]}. {b["category"]} — venta, asesoría y entrega a domicilio en Ciudad Victoria, Tamaulipas y la región.</p>
<div style="margin-top:24px;display:flex;gap:12px;flex-wrap:wrap;">
<a href="https://wa.me/528348528236?text=Hola%2C%20quiero%20cotizar%20productos%20{b["name"]}" class="btn btn-whatsapp" target="_blank" rel="noopener">
<svg width="20" height="20" viewBox="0 0 24 24" fill="white"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347z"/></svg>
Cotizar {b["name"]}
</a>
<a href="tel:+528341100942" class="btn btn-outline">Llamar: 834 110 0942</a>
</div>
</div>
</section>

<div style="background:var(--primary);padding:12px 0;text-align:center;">
<div class="container" style="display:flex;justify-content:center;gap:32px;flex-wrap:wrap;color:white;font-weight:600;font-size:0.95rem;">
<span>Concesionario Oficial {b["name"]}</span>
<span>2 Sucursales en Cd. Victoria</span>
<span>Entrega a Domicilio</span>
<span>+20 Años de Experiencia</span>
</div>
</div>

<section style="padding:60px 0;">
<div class="container">
<div style="max-width:800px;margin:0 auto;">
<h2 style="font-size:1.8rem;font-weight:800;color:var(--dark);margin-bottom:20px;">Distribuidor Oficial {b["name"]} en Ciudad Victoria</h2>
<p style="font-size:1.05rem;line-height:1.8;margin-bottom:24px;">{b["intro"]}</p>
<p style="font-size:1.05rem;line-height:1.8;margin-bottom:24px;">{b["why"]}</p>
</div>
</div>
</section>

<section class="bg-gray" style="padding:60px 0;">
<div class="container">
<div class="section-title"><h2>Productos {b["name"]} Disponibles</h2><p>Stock permanente en nuestra(s) sucursal(es) de Ciudad Victoria</p></div>
<div style="max-width:800px;margin:0 auto;background:white;border-radius:12px;padding:32px;box-shadow:0 2px 12px rgba(0,0,0,0.04);">
<ul style="list-style:none;padding:0;">
{products_html.replace('<li>', '<li style="padding:12px 16px;border-bottom:1px solid #f0f0f0;font-size:1rem;display:flex;align-items:center;gap:12px;"><span style="color:var(--primary);font-weight:700;">✓</span>')}
</ul>
<div style="margin-top:24px;text-align:center;">
<a href="https://wa.me/528348528236?text=Hola%2C%20quiero%20cotizar%20productos%20{b["name"]}" class="btn btn-whatsapp" target="_blank" rel="noopener">Cotizar productos {b["name"]} por WhatsApp</a>
</div>
</div>
</div>
</section>

<section style="padding:60px 0;">
<div class="container">
<div class="section-title"><h2>Preguntas Frecuentes sobre {b["name"]} en Ciudad Victoria</h2></div>
<div class="faq-list">
{faqs_html}
</div>
</div>
</section>

<section class="bg-gray" style="padding:60px 0;">
<div class="container">
<div class="section-title"><h2>Categorías relacionadas</h2></div>
<div style="display:grid;grid-template-columns:repeat(auto-fill, minmax(250px, 1fr));gap:20px;max-width:800px;margin:0 auto;">
{related_html}
<a href="/marcas/" class="category-card"><h3>Todas las Marcas</h3><p>Ver todas →</p></a>
</div>
</div>
</section>

<section class="cta-section">
<div class="container">
<h2>¿Necesitas productos {b["name"]}?</h2>
<p>Cotiza al instante por WhatsApp. Manda tu lista y recibe precio en minutos.</p>
<div class="cta-buttons">
<a href="https://wa.me/528348528236?text=Hola%2C%20quiero%20cotizar%20productos%20{b["name"]}" class="btn btn-whatsapp" target="_blank" rel="noopener">
<svg width="20" height="20" viewBox="0 0 24 24" fill="white"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347z"/></svg>
Cotizar por WhatsApp
</a>
<a href="tel:+528341100942" class="btn btn-outline" style="border-color:rgba(255,255,255,0.4);color:white;">Llamar: 834 110 0942</a>
</div>
</div>
</section>

<section style="padding:60px 0;">
<div class="container">
<div class="section-title"><h2>Nuestras Sucursales en Ciudad Victoria</h2></div>
<div class="locations-grid">
<div class="location-card">
<iframe class="map-embed" src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3608.5!2d-99.1411!3d23.7369!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2zMjPCsDQ0JzEyLjgiTiA5OcKwMDgnMjguMCJX!5e0!3m2!1ses!2smx!4v1" allowfullscreen loading="lazy"></iframe>
<div class="location-info">
<h3>Sucursal Matriz</h3>
<p>Hombres Ilustres 510, Col. Adolfo López Mateos, CP 87020</p>
<p><a href="tel:+528341100942">834 110 0942</a></p>
<p>Lun-Vie 8:00-18:00 | Sáb 8:00-14:00</p>
</div>
</div>
<div class="location-card">
<iframe class="map-embed" src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3608.5!2d-99.155!3d23.745!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2zMjPCsDQ0JzQyLjAiTiA5OcKwMDknMTguMCJX!5e0!3m2!1ses!2smx!4v1" allowfullscreen loading="lazy"></iframe>
<div class="location-info">
<h3>Sucursal Naciones Unidas</h3>
<p>Naciones Unidas 1155, Fracc. Naciones Unidas, CP 87049</p>
<p><a href="tel:+528343132000">834 313 2000</a></p>
<p>Lun-Vie 8:00-18:00 | Sáb 8:00-14:00</p>
</div>
</div>
</div>
</div>
</section>

<footer><div class="container">
<div class="footer-grid">
<div class="footer-col"><h4>AceroMAX</h4><p>Distribuidor oficial de materiales de construcción en Ciudad Victoria, Tamaulipas. Más de 20 años al servicio de constructores.</p><p style="margin-top:12px;">Distribuidor oficial: USG, Prolamsa, Deacero, Ternium, Apasco, DOAL, Alvamex, Megapanel, Truper, Makita, DeWalt.</p></div>
<div class="footer-col"><h4>Productos</h4>
<a href="/acero-estructural/">Acero Estructural</a><a href="/ptr-perfiles/">PTR y Perfiles</a><a href="/laminas/">Láminas</a><a href="/tablaroca-durock/">Tablaroca y Durock</a><a href="/varilla-cemento/">Varilla y Cemento</a><a href="/losacero/">Losacero</a></div>
<div class="footer-col"><h4>Más</h4>
<a href="/mallas/">Mallas</a><a href="/plafones/">Plafones</a><a href="/pinturas/">Pinturas</a><a href="/puertas-ferreteria/">Puertas y Ferretería</a><a href="/marcas/">Marcas</a><a href="/nosotros/">Nosotros</a><a href="/contacto/">Contacto</a></div>
<div class="footer-col"><h4>Contacto</h4>
<a href="tel:+528341100942">834 110 0942</a><a href="tel:+528343132000">834 313 2000</a><a href="https://wa.me/528348528236">WhatsApp: 834 852 82 36</a><a href="mailto:acero2@aceromax.mx">acero2@aceromax.mx</a><p>Ciudad Victoria, Tamaulipas</p></div>
</div><div class="footer-bottom"><p>&copy; 2026 AceroMAX — Distribuidor oficial {b["name"]} en Ciudad Victoria, Tamaulipas.</p></div></div></footer>

<div class="wa-float"><a href="https://wa.me/528348528236?text=Hola%2C%20quiero%20cotizar%20productos%20{b["name"]}" target="_blank" rel="noopener">
<svg width="24" height="24" viewBox="0 0 24 24" fill="white"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347z"/></svg>
<span class="wa-text">Cotizar WhatsApp</span></a></div>

<script>
document.querySelectorAll('.faq-question').forEach(btn => {{
  btn.addEventListener('click', () => {{
    btn.parentElement.classList.toggle('open');
  }});
}});
</script>
</body>
</html>'''


# Generate all brand pages
for b in brands:
    path = f"marcas/{b['slug']}/index.html"
    with open(path, 'w') as f:
        f.write(gen_page(b))
    print(f"✓ {path}")

print(f"\n{len(brands)} brand pages generated")
