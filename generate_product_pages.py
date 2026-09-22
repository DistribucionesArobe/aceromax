import os

GA4 = """<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-HTPSHZR7NT"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-HTPSHZR7NT');
</script>"""

products = [
  {
    "slug": "tablaroca",
    "name": "Tablaroca",
    "title": "Tablaroca en Ciudad Victoria | Precio y Venta | AceroMAX",
    "desc": "Venta de tablaroca en Ciudad Victoria, Tamaulipas. Ultralight USG 1/2\" y 5/8\", resistente a humedad, FIRECODE. Precio al mayoreo y menudeo. 2 sucursales, entrega a domicilio.",
    "keywords": "tablaroca ciudad victoria, tablaroca precio victoria, venta tablaroca tamaulipas, tablaroca cerca de mi, donde comprar tablaroca ciudad victoria, tablaroca al mayoreo victoria, placa de yeso victoria, drywall ciudad victoria, tablaroca barata victoria",
    "h1": "Tablaroca en Ciudad Victoria",
    "intro": "¿Buscas <strong>tablaroca en Ciudad Victoria</strong>? En AceroMAX somos el distribuidor #1 de tablaroca USG Ultralight en la región. Manejamos todos los tipos: regular, resistente a humedad (RH), resistente al fuego (FIRECODE), y en espesores de 1/2\" y 5/8\". Precio competitivo al mayoreo y menudeo.",
    "details": "La tablaroca (también conocida como placa de yeso, drywall o panel de yeso) es el material más utilizado para muros divisorios, plafones falsos y acabados interiores en construcción moderna. En Ciudad Victoria y Tamaulipas, AceroMAX es el principal proveedor de tablaroca con más de 20 años de experiencia surtiendo a constructores, contratistas y público en general.",
    "uses": ["Muros divisorios interiores", "Plafones falsos residenciales y comerciales", "Remodelaciones y ampliaciones", "Cielos rasos en oficinas y comercios", "Acabados interiores en construcción nueva", "Divisiones en naves industriales"],
    "variants": ["Tablaroca Ultralight USG 1/2\" (12.7mm) — 1.22 x 2.44m", "Tablaroca Ultralight USG 5/8\" (15.9mm) — 1.22 x 2.44m", "Tablaroca RH resistente a humedad — para baños y cocinas", "Tablaroca FIRECODE resistente al fuego — para muros cortafuego", "Tablaroca regular estándar"],
    "brands": ["USG"],
    "faqs": [
      ("¿Cuánto cuesta la tablaroca en Ciudad Victoria?", "El precio de la tablaroca en Ciudad Victoria varía según el tipo y cantidad. La Ultralight USG 1/2\" tiene un precio aproximado de $240 MXN por pieza. Cotiza tu cantidad exacta por WhatsApp para precio actualizado y descuento por volumen."),
      ("¿Cuántas piezas de tablaroca necesito?", "Calcula los m² de pared o techo y divide entre 2.97 (área de cada lámina 1.22x2.44m). Agrega 10% de desperdicio. Ejemplo: 50 m² ÷ 2.97 = 17 piezas + 2 extra = 19 piezas. Llámanos y te ayudamos con el cálculo."),
      ("¿Entregan tablaroca a domicilio en Ciudad Victoria?", "Sí. Entregamos tablaroca a tu obra en Ciudad Victoria, Güémez, Jiménez, Padilla y Llera. Camión propio con capacidad para pedidos grandes y pequeños."),
    ],
    "related": [("/productos/durock/", "Durock"), ("/productos/plafones/", "Plafones"), ("/tablaroca-durock/", "Catálogo Tablaroca y Durock"), ("/marcas/usg/", "Marca USG")],
  },
  {
    "slug": "durock",
    "name": "Durock",
    "title": "Durock en Ciudad Victoria | Panel de Cemento USG | AceroMAX",
    "desc": "Venta de Durock USG en Ciudad Victoria, Tamaulipas. Panel de cemento para exteriores, baños, fachadas y áreas húmedas. Distribuidor oficial. Entrega a domicilio.",
    "keywords": "durock ciudad victoria, durock precio victoria, panel de cemento victoria, durock USG tamaulipas, venta durock victoria, durock para baños, durock para fachadas, durock cerca de mi",
    "h1": "Durock en Ciudad Victoria",
    "intro": "¿Necesitas <strong>Durock en Ciudad Victoria</strong>? En AceroMAX somos distribuidor oficial de Durock USG, el panel de cemento líder para exteriores y áreas húmedas. Resistente al agua, al fuego y al impacto.",
    "details": "El Durock (panel de cemento USG) es la solución profesional para zonas donde la tablaroca regular no funciona: baños con regadera directa, cocinas industriales, fachadas exteriores y muros perimetrales. A diferencia de la tablaroca de yeso, el Durock no se deteriora con la humedad ni con la exposición al exterior.",
    "uses": ["Fachadas exteriores de casas y edificios", "Baños con regadera directa", "Cocinas comerciales e industriales", "Muros perimetrales expuestos a lluvia", "Áreas de alberca y spa", "Bases para recubrimiento cerámico en zonas húmedas"],
    "variants": ["Durock USG 1/2\" (12.7mm) — 1.22 x 2.44m", "Durock USG 5/8\" (15.9mm) — 1.22 x 2.44m", "Durock Next Gen (nueva generación, más ligero)"],
    "brands": ["USG"],
    "faqs": [
      ("¿Cuál es la diferencia entre tablaroca y Durock?", "La tablaroca es de yeso y es para interiores secos. El Durock es de cemento Portland y resiste agua, humedad y exteriores. En Ciudad Victoria, donde hay calor y lluvia, usamos Durock para exteriores y baños, tablaroca para interiores."),
      ("¿Se puede usar Durock en fachadas?", "Sí, el Durock es ideal para fachadas en Ciudad Victoria. Resiste sol, lluvia y cambios de temperatura. Se puede acabar con estuco, pintura texturizada o recubrimiento cerámico."),
      ("¿Dónde comprar Durock en Ciudad Victoria?", "En AceroMAX, distribuidor oficial USG. Tenemos Durock en existencia permanente. 2 sucursales en Ciudad Victoria con entrega a domicilio."),
    ],
    "related": [("/productos/tablaroca/", "Tablaroca"), ("/tablaroca-durock/", "Catálogo completo"), ("/marcas/usg/", "Marca USG")],
  },
  {
    "slug": "plafones",
    "name": "Plafones",
    "title": "Plafones en Ciudad Victoria | Plafón Acústico y Decorativo | AceroMAX",
    "desc": "Venta de plafones en Ciudad Victoria, Tamaulipas. Plafón acústico USG, plafón decorativo, plafón de PVC y fibra mineral. Para oficinas, clínicas, comercios. Entrega a domicilio.",
    "keywords": "plafones ciudad victoria, plafón acústico victoria, plafón USG tamaulipas, plafón decorativo victoria, cielo raso ciudad victoria, plafón PVC victoria, venta plafones tamaulipas, plafón precio victoria",
    "h1": "Plafones en Ciudad Victoria",
    "intro": "¿Buscas <strong>plafones en Ciudad Victoria</strong>? En AceroMAX somos distribuidor oficial de plafones USG y Megapanel. Plafones acústicos, decorativos y funcionales para oficinas, clínicas, escuelas, comercios y casas.",
    "details": "Los plafones (también llamados cielo raso o falso plafón) son paneles que se instalan debajo del techo real para mejorar la estética, reducir ruido, ocultar instalaciones y mejorar el aislamiento térmico. En Ciudad Victoria, donde el calor es intenso, un buen plafón puede reducir significativamente la temperatura interior.",
    "uses": ["Oficinas y corporativos", "Clínicas y consultorios médicos", "Escuelas y universidades", "Tiendas y centros comerciales", "Restaurantes y cafeterías", "Residencias y casas habitación"],
    "variants": ["Plafón Radar Climaplus USG 2x2 pies", "Plafón Olympia Micro USG 2x2 pies", "Plafón Ceramic Climaplus USG 2x4 pies", "Plafón de PVC decorativo", "Plafón de fibra mineral", "Suspensión (riel principal, cruceta, ángulo perimetral)"],
    "brands": ["USG", "Megapanel"],
    "faqs": [
      ("¿Cuánto cuesta el plafón en Ciudad Victoria?", "El precio del plafón varía según el modelo. Los plafones USG Radar van desde $45 MXN por pieza (2x2 pies). Cotiza por WhatsApp para precio actualizado según modelo y cantidad."),
      ("¿Qué plafón es mejor para oficinas?", "Para oficinas en Ciudad Victoria recomendamos el plafón USG Radar Climaplus: absorbe ruido, resiste humedad y tiene acabado profesional. Incluimos la suspensión (rieles) y asesoría de instalación."),
      ("¿Venden la suspensión para plafón?", "Sí. Manejamos el sistema completo de suspensión: riel principal, crucetas, ángulo perimetral, alambre galvanizado y ganchos. Todo compatible con plafones USG 2x2 y 2x4 pies."),
    ],
    "related": [("/plafones/", "Catálogo Plafones"), ("/marcas/usg/", "Marca USG"), ("/marcas/megapanel/", "Megapanel")],
  },
  {
    "slug": "lamina-galvanizada",
    "name": "Lámina Galvanizada",
    "title": "Lámina Galvanizada en Ciudad Victoria | Todos los Calibres | AceroMAX",
    "desc": "Venta de lámina galvanizada en Ciudad Victoria, Tamaulipas. Calibres 22, 24, 26, 28. Acanalada, lisa, pintro. Ternium original. Techumbres, bardas, naves. Entrega a domicilio.",
    "keywords": "lámina galvanizada ciudad victoria, lámina calibre 26 victoria, lámina para techo victoria, lámina acanalada tamaulipas, lámina precio ciudad victoria, venta lámina victoria, lámina Ternium victoria, lámina para barda",
    "h1": "Lámina Galvanizada en Ciudad Victoria",
    "intro": "¿Buscas <strong>lámina galvanizada en Ciudad Victoria</strong>? En AceroMAX somos distribuidor oficial de lámina Ternium en todos los calibres. Acanalada, lisa, pintro y zintro-alum para techumbres, bardas, naves y cerramientos.",
    "details": "La lámina galvanizada es uno de los materiales más versátiles en construcción: sirve para techos, bardas perimetrales, cerramientos de naves industriales, cobertizos y fachadas. En AceroMAX manejamos lámina Ternium original en calibres del 22 al 28, con largos estándar y cortes especiales bajo pedido.",
    "uses": ["Techumbres residenciales y comerciales", "Bardas perimetrales", "Naves industriales y bodegas", "Cobertizos y cocheras", "Cerramientos temporales y permanentes", "Fachadas con lámina pintada"],
    "variants": ["Lámina acanalada R-72 cal. 26 (la más vendida)", "Lámina acanalada cal. 24 (mayor resistencia)", "Lámina acanalada cal. 22 (uso industrial)", "Lámina KR-18 (perfil trapezoidal)", "Lámina lisa galvanizada", "Lámina pintro (pintada) en colores", "Lámina zintro-alum (alta durabilidad)"],
    "brands": ["Ternium", "Prolamsa"],
    "faqs": [
      ("¿Cuánto cuesta la lámina galvanizada en Ciudad Victoria?", "El precio varía según calibre y largo. La lámina cal. 26 es la más económica y popular para techumbres residenciales. Cotiza por WhatsApp con el calibre y largo que necesitas para precio exacto."),
      ("¿Qué calibre de lámina necesito para mi techo?", "Para techos residenciales: cal. 26 o 28. Para techumbres comerciales: cal. 24. Para naves industriales: cal. 22. En AceroMAX te asesoramos según tu claro (distancia entre apoyos)."),
      ("¿Tienen lámina pintada de colores?", "Sí, manejamos lámina pintro Ternium en rojo, azul, verde, blanco, gris y más colores. Ideal para fachadas y techumbres con acabado estético."),
    ],
    "related": [("/laminas/", "Catálogo Láminas"), ("/marcas/ternium/", "Marca Ternium"), ("/productos/galvateja/", "Galvateja"), ("/productos/aceroteja/", "Aceroteja")],
  },
  {
    "slug": "fierro",
    "name": "Fierro",
    "title": "Fierro en Ciudad Victoria | Venta de Fierro y Acero | AceroMAX",
    "desc": "Venta de fierro en Ciudad Victoria, Tamaulipas. Fierro estructural, ángulo, solera, redondo, cuadrado, placa. Todos los calibres y medidas. 2 sucursales, entrega a obra.",
    "keywords": "fierro ciudad victoria, venta de fierro victoria, fierro precio tamaulipas, fierro estructural victoria, ángulo de fierro, solera de fierro, redondo de fierro, cuadrado de fierro, fierro para herrería victoria",
    "h1": "Fierro en Ciudad Victoria",
    "intro": "¿Buscas <strong>fierro en Ciudad Victoria</strong>? En AceroMAX tenemos todo tipo de fierro y acero estructural: ángulo, solera, redondo, cuadrado, placa, y perfiles. Para herrería, construcción, fabricación y proyectos industriales.",
    "details": "El fierro (acero al carbón) es fundamental para herrería, estructuras metálicas, puertas, ventanas, rejas y fabricación en general. En AceroMAX manejamos fierro en todas las presentaciones: ángulo de 1/2\" a 4\", solera de 1/2\" a 3\", redondo de 1/4\" a 2\", cuadrado, placa y más.",
    "uses": ["Herrería: puertas, ventanas, rejas, barandales", "Estructuras metálicas", "Fabricación de muebles de fierro", "Marcos y bastidores", "Refuerzos estructurales", "Escaleras y pasamanos"],
    "variants": ["Ángulo de fierro: 1/2\" a 4\", cal. 3/16\" y 1/4\"", "Solera de fierro: 1/2\" a 3\", varios espesores", "Redondo liso: 1/4\" a 2\"", "Cuadrado: 3/8\" a 1\"", "Placa de acero: 1/8\" a 1\", varios anchos", "Lámina negra: cal. 10, 12, 14", "Perfil T: varias medidas"],
    "brands": ["Ternium", "Deacero"],
    "faqs": [
      ("¿Dónde comprar fierro en Ciudad Victoria?", "En AceroMAX, 2 sucursales en Ciudad Victoria. Manejamos ángulo, solera, redondo, cuadrado, placa y todos los perfiles de fierro. Cortamos a medida."),
      ("¿Venden fierro por kilo o por pieza?", "Vendemos fierro por pieza (largos de 6 metros estándar) y por corte a medida. Para volumen, cotizamos por tonelada con precio preferencial."),
      ("¿Hacen cortes de fierro a medida?", "Sí, cortamos fierro, ángulo, solera y placa a la medida que necesites. Solo dinos las dimensiones."),
    ],
    "related": [("/acero-estructural/", "Acero Estructural"), ("/productos/vigas/", "Vigas"), ("/productos/canal-de-acero/", "Canal de Acero")],
  },
  {
    "slug": "vigas",
    "name": "Vigas",
    "title": "Vigas IPR en Ciudad Victoria | Viga de Acero Estructural | AceroMAX",
    "desc": "Venta de vigas IPR e IPS en Ciudad Victoria, Tamaulipas. Acero estructural para construcción, naves industriales, entrepisos. Todas las medidas. Entrega a obra.",
    "keywords": "vigas ciudad victoria, vigas IPR victoria, viga de acero tamaulipas, vigas para construcción victoria, viga IPR precio, vigas estructurales victoria, viga IPS, viga H victoria",
    "h1": "Vigas IPR en Ciudad Victoria",
    "intro": "¿Necesitas <strong>vigas en Ciudad Victoria</strong>? En AceroMAX manejamos vigas IPR (perfil I de patín ancho), IPS (perfil I de patín angosto) y vigas H para construcción estructural, naves industriales y entrepisos.",
    "details": "Las vigas IPR son elementos estructurales fundamentales para soportar cargas en construcciones de acero. Se usan como trabes principales, columnas, marcos rígidos y refuerzos en edificios, naves industriales y puentes. En AceroMAX trabajamos con vigas de acero estructural de primera calidad.",
    "uses": ["Trabes principales en naves industriales", "Columnas de acero", "Entrepisos metálicos", "Marcos rígidos para edificios", "Puentes y pasarelas", "Refuerzos estructurales"],
    "variants": ["Viga IPR 4\" a 24\" (W4 a W24)", "Viga IPS 3\" a 12\"", "Viga H estándar", "Largos: 6m, 9m, 12m (bajo pedido)"],
    "brands": ["Ternium"],
    "faqs": [
      ("¿Dónde comprar vigas IPR en Ciudad Victoria?", "En AceroMAX. Manejamos vigas IPR de 4\" a 24\" en existencia y bajo pedido. Cotiza con medidas exactas por WhatsApp para precio y disponibilidad."),
      ("¿Cuánto cuesta una viga IPR?", "El precio de vigas IPR se cotiza por kilo. Varía según el peralte (4\", 6\", 8\", etc.) y el largo. Cotiza tu necesidad exacta por WhatsApp para precio del día."),
    ],
    "related": [("/acero-estructural/", "Acero Estructural"), ("/productos/fierro/", "Fierro"), ("/productos/canal-de-acero/", "Canal de Acero")],
  },
  {
    "slug": "pintura",
    "name": "Pintura",
    "title": "Pintura en Ciudad Victoria | Vinílica, Esmalte, Impermeabilizante | AceroMAX",
    "desc": "Venta de pintura en Ciudad Victoria, Tamaulipas. Vinílica, esmalte, impermeabilizante, texturizado. Marcas DOAL y Alvamex. Toda la gama de colores. 2 sucursales.",
    "keywords": "pintura ciudad victoria, venta pintura victoria, pintura precio tamaulipas, pintura vinílica victoria, impermeabilizante ciudad victoria, esmalte victoria, pintura para casa victoria, pintura barata victoria, tienda de pinturas victoria",
    "h1": "Pintura en Ciudad Victoria",
    "intro": "¿Buscas <strong>pintura en Ciudad Victoria</strong>? En AceroMAX somos distribuidores oficiales de Pinturas DOAL y Alvamex. Vinílicas, esmaltes, impermeabilizantes, texturizados y selladores. Toda la gama de colores para interior y exterior.",
    "details": "La pintura es el acabado final que define la estética de cualquier proyecto. En AceroMAX manejamos dos líneas complementarias: DOAL para acabados premium y Alvamex para la mejor relación calidad-precio. Te asesoramos en la selección del producto correcto según tu superficie y condiciones de uso.",
    "uses": ["Interiores de casas y departamentos", "Fachadas exteriores", "Oficinas y locales comerciales", "Impermeabilización de techos", "Acabados texturizados", "Protección anticorrosiva de estructuras metálicas"],
    "variants": ["Pintura vinílica interior (DOAL / Alvamex)", "Pintura vinílica exterior alto rendimiento", "Esmalte alquidálico (para metal y madera)", "Impermeabilizante acrílico (3, 5, 10 años)", "Texturizado para fachadas", "Sellador para muros nuevos", "Primer anticorrosivo", "Barniz para madera"],
    "brands": ["DOAL", "Alvamex"],
    "faqs": [
      ("¿Dónde comprar pintura en Ciudad Victoria?", "En AceroMAX, distribuidor oficial DOAL y Alvamex. Tenemos toda la gama de colores en vinílicas, esmaltes, impermeabilizantes y más. 2 sucursales en Ciudad Victoria."),
      ("¿Cuánta pintura necesito para mi casa?", "1 litro de vinílica rinde aprox. 10-12 m² por mano. Para un cuarto de 3x4m con 2.5m de altura necesitas aprox. 7 litros (2 manos). Llámanos con las medidas y te calculamos."),
      ("¿Tienen igualación de colores?", "Sí, contamos con sistema de colorimetría para igualar cualquier color que traigas como muestra. Lo preparamos en minutos."),
    ],
    "related": [("/pinturas/", "Catálogo Pinturas"), ("/marcas/doal/", "Marca DOAL"), ("/marcas/alvamex/", "Marca Alvamex")],
  },
  {
    "slug": "malla-ciclonica",
    "name": "Malla Ciclónica",
    "title": "Malla Ciclónica en Ciudad Victoria | Galvanizada y Plastificada | AceroMAX",
    "desc": "Venta de malla ciclónica en Ciudad Victoria, Tamaulipas. Galvanizada y plastificada. Alturas de 1.00m a 3.00m. Deacero original. Rollos y por metro. Entrega a domicilio.",
    "keywords": "malla ciclónica ciudad victoria, malla ciclónica precio victoria, venta malla ciclónica tamaulipas, malla galvanizada victoria, malla para cerco victoria, cerca de malla victoria, malla ciclónica por metro victoria",
    "h1": "Malla Ciclónica en Ciudad Victoria",
    "intro": "¿Necesitas <strong>malla ciclónica en Ciudad Victoria</strong>? En AceroMAX somos distribuidor oficial Deacero. Malla ciclónica galvanizada y plastificada en alturas de 1.00m a 3.00m. Rollos completos o por metro.",
    "details": "La malla ciclónica (también llamada malla de alambre o cerca de malla) es la solución más popular para cercar terrenos, jardines, canchas deportivas y perímetros industriales. Fabricada con alambre galvanizado tejido en forma de diamante, ofrece visibilidad, ventilación y seguridad.",
    "uses": ["Cercado de terrenos y predios", "Canchas deportivas", "Perímetros industriales y comerciales", "Jardines y áreas verdes", "Corrales y áreas para animales", "Cercas temporales de obra"],
    "variants": ["Malla ciclónica galvanizada cal. 12.5 — 1.50m x 20m", "Malla ciclónica galvanizada cal. 12.5 — 2.00m x 20m", "Malla ciclónica galvanizada cal. 12.5 — 2.50m x 20m", "Malla ciclónica galvanizada cal. 12.5 — 3.00m x 20m", "Malla ciclónica plastificada (verde) — varias alturas", "Postes para malla ciclónica (tubo galvanizado)"],
    "brands": ["Deacero"],
    "faqs": [
      ("¿Cuánto cuesta la malla ciclónica en Ciudad Victoria?", "El precio varía según la altura y el calibre. La malla de 2.00m cal. 12.5 es la más popular. Cotiza por WhatsApp con los metros lineales que necesitas para precio exacto."),
      ("¿Venden malla ciclónica por metro?", "Sí, vendemos malla ciclónica por metro lineal y en rollos completos de 20 metros. También tenemos postes, tensores y accesorios para instalación completa."),
      ("¿Instalan la malla ciclónica?", "Podemos recomendarte instaladores de confianza en Ciudad Victoria. Vendemos el material completo: malla, postes, tensores, alambre y accesorios."),
    ],
    "related": [("/mallas/", "Catálogo Mallas"), ("/marcas/deacero/", "Marca Deacero"), ("/productos/malla-borreguera/", "Malla Borreguera")],
  },
  {
    "slug": "rejacero",
    "name": "Rejacero",
    "title": "Rejacero en Ciudad Victoria | Reja de Acero Electrosoldada | AceroMAX",
    "desc": "Venta de rejacero en Ciudad Victoria, Tamaulipas. Reja de acero electrosoldada para cercado perimetral, fachadas y seguridad. Varios diseños y alturas. Entrega a domicilio.",
    "keywords": "rejacero ciudad victoria, reja de acero victoria, rejacero precio tamaulipas, reja electrosoldada victoria, cerca de rejacero, rejacero para casa victoria, panel de rejacero victoria",
    "h1": "Rejacero en Ciudad Victoria",
    "intro": "¿Buscas <strong>rejacero en Ciudad Victoria</strong>? En AceroMAX tenemos reja de acero electrosoldada (rejacero) para cercado perimetral, fachadas y seguridad. Más resistente que la malla ciclónica, con mejor estética.",
    "details": "El rejacero es un panel de reja electrosoldada de acero galvanizado, mucho más rígido y seguro que la malla ciclónica tradicional. Es ideal para fraccionamientos, industrias, escuelas y cualquier perímetro que requiera mayor seguridad y apariencia profesional.",
    "uses": ["Cercado perimetral de fraccionamientos", "Seguridad industrial", "Escuelas y centros deportivos", "Fachadas decorativas", "Estacionamientos", "Áreas residenciales de alta seguridad"],
    "variants": ["Rejacero estándar (panel electrosoldado)", "Rejacero de alta seguridad (anti-escala)", "Rejacero decorativo con puntas", "Postes y accesorios para rejacero"],
    "brands": ["Deacero"],
    "faqs": [
      ("¿Qué ventaja tiene el rejacero sobre la malla ciclónica?", "El rejacero es mucho más rígido, difícil de cortar o escalar, tiene mejor apariencia estética y mayor durabilidad. Es la opción preferida para fraccionamientos y empresas en Ciudad Victoria."),
      ("¿Cuánto cuesta el rejacero en Ciudad Victoria?", "El precio depende de la altura y el diseño del panel. Cotiza por WhatsApp con los metros lineales y la altura que necesitas."),
    ],
    "related": [("/mallas/", "Catálogo Mallas"), ("/productos/malla-ciclonica/", "Malla Ciclónica"), ("/marcas/deacero/", "Marca Deacero")],
  },
  {
    "slug": "malla-borreguera",
    "name": "Malla Borreguera",
    "title": "Malla Borreguera en Ciudad Victoria | Malla Ganadera | AceroMAX",
    "desc": "Venta de malla borreguera (ganadera) en Ciudad Victoria, Tamaulipas. Para corrales, potreros y cercado de ganado. Varias alturas y aberturas. Deacero original.",
    "keywords": "malla borreguera ciudad victoria, malla ganadera victoria, malla para borregos tamaulipas, malla para ganado victoria, cerca ganadera victoria, malla borreguera precio victoria",
    "h1": "Malla Borreguera en Ciudad Victoria",
    "intro": "¿Necesitas <strong>malla borreguera en Ciudad Victoria</strong>? En AceroMAX tenemos malla ganadera Deacero para corrales, potreros, establos y cercado de ganado menor. Diseño de abertura graduada que impide el paso de animales pequeños.",
    "details": "La malla borreguera (también llamada malla ganadera o malla para ganado menor) tiene una abertura graduada: más cerrada abajo y más abierta arriba, lo que impide que borregos, cabras y crías se escapen o queden atorados. Es el estándar en ganadería en Tamaulipas.",
    "uses": ["Corrales para borregos y cabras", "Potreros y agostaderos", "Cercado de ranchos", "Establos y áreas de confinamiento", "Protección de huertos y cultivos", "Cercado de aves de corral"],
    "variants": ["Malla borreguera 1.20m x 50m (12/100/15)", "Malla borreguera 1.50m x 50m", "Malla borreguera reforzada", "Grapas y postes para malla ganadera"],
    "brands": ["Deacero"],
    "faqs": [
      ("¿Cuánto cuesta la malla borreguera en Ciudad Victoria?", "El precio depende de la altura y el rollo. La presentación más común es 1.20m x 50m. Cotiza por WhatsApp para precio actualizado."),
      ("¿Cuál es la diferencia entre malla borreguera y ciclónica?", "La malla borreguera tiene abertura graduada (más chica abajo, más grande arriba) para contener ganado menor. La ciclónica tiene abertura uniforme en diamante. Para ganado siempre recomendamos borreguera."),
    ],
    "related": [("/mallas/", "Catálogo Mallas"), ("/productos/malla-ciclonica/", "Malla Ciclónica"), ("/marcas/deacero/", "Marca Deacero")],
  },
  {
    "slug": "puertas-multipanel",
    "name": "Puertas Multipanel",
    "title": "Puertas Multipanel en Ciudad Victoria | Puertas de Madera | AceroMAX",
    "desc": "Venta de puertas multipanel en Ciudad Victoria, Tamaulipas. Puertas de madera para interiores y exteriores. Varios diseños, colores y medidas. 2 sucursales.",
    "keywords": "puertas multipanel ciudad victoria, puertas de madera victoria, puertas para casa victoria, puertas interiores victoria, puertas precio victoria, venta de puertas tamaulipas, puertas multipanel precio",
    "h1": "Puertas Multipanel en Ciudad Victoria",
    "intro": "¿Buscas <strong>puertas multipanel en Ciudad Victoria</strong>? En AceroMAX tenemos puertas multipanel de madera en múltiples diseños, colores y medidas. Para entradas principales, recámaras, baños y oficinas.",
    "details": "Las puertas multipanel son puertas de madera moldeada con paneles en relieve que ofrecen una estética elegante y moderna. Son más resistentes que las puertas tambor y vienen en variedad de diseños: 2 paneles, 4 paneles, 6 paneles, con o sin visor.",
    "uses": ["Entradas principales de casas", "Recámaras", "Baños", "Oficinas y despachos", "Locales comerciales", "Departamentos"],
    "variants": ["Puerta multipanel 2 paneles", "Puerta multipanel 4 paneles", "Puerta multipanel 6 paneles", "Puerta multipanel con visor", "Puerta tambor económica", "Marcos y chambrana"],
    "brands": [],
    "faqs": [
      ("¿Cuánto cuesta una puerta multipanel en Ciudad Victoria?", "El precio depende del diseño y la medida. Tenemos desde puertas tambor económicas hasta multipanel premium. Cotiza por WhatsApp para precio según modelo."),
      ("¿Incluyen marco y chambrana?", "Vendemos puertas sueltas y kits completos con marco, chambrana y bisagras. Pregunta por el kit completo para mejor precio."),
    ],
    "related": [("/puertas-ferreteria/", "Puertas y Ferretería"), ("/productos/ferreteria/", "Ferretería")],
  },
  {
    "slug": "ferreteria",
    "name": "Ferretería",
    "title": "Ferretería en Ciudad Victoria | Herramientas y Accesorios | AceroMAX",
    "desc": "Ferretería en Ciudad Victoria, Tamaulipas. Herramientas Truper, Makita, DeWalt. Tornillería, clavos, silicón, cinta, brocas, discos, lijas. Todo para tu obra. 2 sucursales.",
    "keywords": "ferretería ciudad victoria, ferretería cerca de mi victoria, ferretería tamaulipas, herramientas ciudad victoria, tornillos victoria, clavos victoria, accesorios construcción victoria, ferretería en general victoria",
    "h1": "Ferretería en Ciudad Victoria",
    "intro": "¿Buscas <strong>ferretería en Ciudad Victoria</strong>? En AceroMAX tenemos ferretería completa: herramientas Truper, Makita y DeWalt, tornillería, clavos, silicón, cintas, brocas, discos, lijas, candados y todo lo que necesitas para tu obra o remodelación.",
    "details": "Nuestra sección de ferretería complementa los materiales de construcción pesada. Tenemos desde un clavo hasta una rotomartillo profesional. Todo en un solo lugar para que no pierdas tiempo buscando en varias tiendas.",
    "uses": ["Construcción de obra nueva", "Remodelaciones", "Herrería y soldadura", "Plomería básica", "Electricidad básica", "Mantenimiento del hogar"],
    "variants": ["Herramienta manual Truper (llaves, pinzas, martillos)", "Herramienta eléctrica Makita y DeWalt", "Tornillería (pijas, tornillos, tuercas, roldanas)", "Clavos (concreto, acero, madera)", "Silicón y adhesivos", "Brocas y discos de corte", "Lijas y abrasivos", "Cinta de aislar, masking, ducto", "Candados y cerraduras"],
    "brands": ["Truper", "Makita", "DeWalt"],
    "faqs": [
      ("¿Dónde hay ferretería en Ciudad Victoria?", "AceroMAX tiene 2 sucursales con ferretería completa: Hombres Ilustres 510 y Naciones Unidas 1155. Herramientas Truper, Makita, DeWalt y toda la tornillería y accesorios."),
      ("¿Tienen herramienta eléctrica profesional?", "Sí, somos distribuidores oficiales de Makita y DeWalt. Toda la línea profesional con garantía de fábrica."),
    ],
    "related": [("/puertas-ferreteria/", "Puertas y Ferretería"), ("/marcas/truper/", "Truper"), ("/marcas/makita/", "Makita"), ("/marcas/dewalt/", "DeWalt")],
  },
  {
    "slug": "canal-de-acero",
    "name": "Canal de Acero",
    "title": "Canal de Acero en Ciudad Victoria | Canal Estructural CPS | AceroMAX",
    "desc": "Venta de canal de acero en Ciudad Victoria, Tamaulipas. Canal estructural CPS, canal monten, canal U. Para techos, estructuras y naves. Todas las medidas.",
    "keywords": "canal de acero ciudad victoria, canal estructural victoria, canal CPS victoria, canal monten tamaulipas, canal para techo victoria, canal U victoria, perfil canal victoria",
    "h1": "Canal de Acero en Ciudad Victoria",
    "intro": "¿Necesitas <strong>canal de acero en Ciudad Victoria</strong>? En AceroMAX manejamos canal estructural CPS, canal monten y canal U en todas las medidas. Para estructuras de techos, entrepisos, marcos y refuerzos.",
    "details": "El canal de acero (perfil C o canal estructural) es uno de los elementos más utilizados en construcción metálica. Sirve como larguero en techumbres, marco para muros de tablaroca, soporte de plafones y elemento estructural ligero.",
    "uses": ["Largueros para techumbres", "Marcos para muros de tablaroca", "Soporte de plafones", "Estructuras ligeras", "Entrepisos metálicos", "Carrocerías"],
    "variants": ["Canal CPS 2\" a 12\"", "Canal monten 4\" a 12\"", "Canal U estándar", "Canal de tablaroca (poste y canal USG)", "Largos: 6m estándar"],
    "brands": ["Prolamsa", "Ternium"],
    "faqs": [
      ("¿Dónde comprar canal de acero en Ciudad Victoria?", "En AceroMAX. Manejamos canal CPS, monten y U en todas las medidas. 2 sucursales en Ciudad Victoria con entrega a obra."),
      ("¿Cuál es la diferencia entre canal CPS y monten?", "El canal CPS tiene los labios doblados hacia adentro (mayor rigidez). El monten tiene labios hacia afuera. Ambos se usan como largueros, pero el CPS resiste más torsión."),
    ],
    "related": [("/acero-estructural/", "Acero Estructural"), ("/productos/vigas/", "Vigas"), ("/productos/fierro/", "Fierro")],
  },
  {
    "slug": "varilla",
    "name": "Varilla",
    "title": "Varilla en Ciudad Victoria | Varilla Corrugada Deacero | AceroMAX",
    "desc": "Venta de varilla corrugada en Ciudad Victoria, Tamaulipas. Deacero original del #2 al #8, grado 42 y 60. Para castillos, cadenas, losas. Entrega a obra.",
    "keywords": "varilla ciudad victoria, varilla corrugada victoria, varilla precio victoria, varilla 3/8 victoria, varilla Deacero tamaulipas, varilla para construcción victoria, venta varilla victoria, varilla grado 42",
    "h1": "Varilla Corrugada en Ciudad Victoria",
    "intro": "¿Buscas <strong>varilla en Ciudad Victoria</strong>? En AceroMAX somos distribuidor oficial Deacero. Varilla corrugada del #2 al #8, grado 42 y grado 60, que cumple con norma NMX-C-407. Para castillos, cadenas, losas y cimentaciones.",
    "details": "La varilla corrugada es el refuerzo esencial en toda estructura de concreto: castillos, cadenas, trabes, losas, zapatas y cimentaciones. En AceroMAX manejamos varilla Deacero original certificada, la marca #1 en aceros largos de México.",
    "uses": ["Castillos y cadenas de cerramiento", "Losas de concreto armado", "Zapatas y cimentaciones", "Trabes y contratrabes", "Escaleras de concreto", "Muros de contención"],
    "variants": ["Varilla #2 (1/4\") — para estribos", "Varilla #3 (3/8\") — la más usada en casa habitación", "Varilla #4 (1/2\") — castillos y cadenas reforzadas", "Varilla #5 (5/8\") — estructuras medianas", "Varilla #6 (3/4\") — estructuras pesadas", "Varilla #8 (1\") — cimentaciones profundas", "Grado 42 (4200 kg/cm²)", "Grado 60 (6000 kg/cm²)"],
    "brands": ["Deacero"],
    "faqs": [
      ("¿Cuánto cuesta la varilla en Ciudad Victoria?", "El precio de la varilla varía diariamente según el mercado del acero. La varilla 3/8 (la más usada) se cotiza por pieza de 12 metros. Manda tu lista por WhatsApp para precio del día."),
      ("¿Qué varilla necesito para mi casa?", "Para casa habitación estándar: varilla #3 (3/8\") para castillos y cadenas, varilla #2 (1/4\") para estribos. Para estructuras de 2+ pisos: varilla #4 (1/2\") mínimo. Consulta a tu ingeniero estructural."),
      ("¿La varilla Deacero cumple con norma?", "Sí, toda la varilla Deacero que vendemos cumple con NMX-C-407 y viene certificada. Como distribuidor oficial, garantizamos producto original de fábrica."),
    ],
    "related": [("/varilla-cemento/", "Varilla y Cemento"), ("/productos/cemento/", "Cemento"), ("/marcas/deacero/", "Marca Deacero")],
  },
  {
    "slug": "cemento",
    "name": "Cemento",
    "title": "Cemento en Ciudad Victoria | Cemento Apasco 50 kg | AceroMAX",
    "desc": "Venta de cemento en Ciudad Victoria, Tamaulipas. Cemento Apasco (Holcim) 50 kg. Existencia permanente. Entrega a obra desde 1 tonelada. Precio competitivo.",
    "keywords": "cemento ciudad victoria, cemento precio victoria, cemento Apasco victoria, cemento 50 kg victoria, venta cemento tamaulipas, cemento Holcim victoria, cemento para obra victoria, cemento barato victoria",
    "h1": "Cemento en Ciudad Victoria",
    "intro": "¿Necesitas <strong>cemento en Ciudad Victoria</strong>? En AceroMAX somos distribuidor oficial de Cemento Apasco (Holcim). Sacos de 50 kg con existencia permanente. Precio competitivo al menudeo y por volumen. Entrega directa a tu obra.",
    "details": "El cemento es el insumo básico de toda construcción. En AceroMAX manejamos Cemento Apasco (Holcim), una de las marcas más reconocidas mundialmente. Garantizamos producto fresco (fecha reciente de fabricación) y almacenamiento correcto para mantener la calidad.",
    "uses": ["Colado de losas, castillos y cadenas", "Mezcla para pegar block y ladrillo", "Firmes y pisos de concreto", "Banquetas y guarniciones", "Cimentaciones y zapatas", "Aplanados y acabados"],
    "variants": ["Cemento gris Apasco 50 kg (uso general)", "Cemento Apasco Extra (alta resistencia temprana)", "Mortero Apasco (mezcla lista para pegar)", "Pegablock Apasco"],
    "brands": ["Apasco"],
    "faqs": [
      ("¿Cuánto cuesta el saco de cemento en Ciudad Victoria?", "El precio del cemento varía semanalmente. Cotiza por WhatsApp para precio del día. Tenemos descuento por volumen (5+ toneladas)."),
      ("¿Entregan cemento a domicilio?", "Sí, entregamos cemento a tu obra en Ciudad Victoria y municipios vecinos. Pedidos desde 1 tonelada (20 sacos). Camión propio."),
      ("¿Cuántos sacos de cemento necesito para un firme?", "Para un firme de 10cm de espesor, necesitas aprox. 1 saco de cemento por cada 2 m². Para 50 m² = 25 sacos + arena y grava. Te ayudamos con el cálculo exacto."),
    ],
    "related": [("/varilla-cemento/", "Varilla y Cemento"), ("/productos/varilla/", "Varilla"), ("/marcas/apasco/", "Marca Apasco")],
  },
  {
    "slug": "lambrin",
    "name": "Lambrín",
    "title": "Lambrín en Ciudad Victoria | Lambrín de PVC y Madera | AceroMAX",
    "desc": "Venta de lambrín en Ciudad Victoria, Tamaulipas. Lambrín de PVC, madera y tablaroca para muros y plafones decorativos. Varios colores y texturas. 2 sucursales.",
    "keywords": "lambrín ciudad victoria, lambrín PVC victoria, lambrín de madera victoria, lambrín para techo victoria, lambrín decorativo tamaulipas, lambrín precio victoria, venta lambrín victoria",
    "h1": "Lambrín en Ciudad Victoria",
    "intro": "¿Buscas <strong>lambrín en Ciudad Victoria</strong>? En AceroMAX tenemos lambrín de PVC, madera y materiales compuestos para muros decorativos y plafones. Acabados que transforman cualquier espacio con instalación rápida.",
    "details": "El lambrín es un recubrimiento decorativo que se instala sobre muros o techos existentes para mejorar la estética y el aislamiento. Los lambrines de PVC son especialmente populares en Ciudad Victoria por su resistencia a la humedad y facilidad de limpieza.",
    "uses": ["Plafones decorativos en casas", "Muros decorativos en recámaras", "Recubrimiento de baños y cocinas (PVC)", "Fachadas interiores de comercios", "Oficinas y consultorios", "Restaurantes y cafeterías"],
    "variants": ["Lambrín de PVC liso (varios colores)", "Lambrín de PVC tipo madera", "Lambrín de madera natural", "Lambrín de MDF", "Accesorios de instalación (perfiles de remate)"],
    "brands": [],
    "faqs": [
      ("¿Cuánto cuesta el lambrín en Ciudad Victoria?", "El precio del lambrín varía según el material y acabado. El lambrín de PVC es el más económico. Cotiza por WhatsApp con los metros cuadrados que necesitas."),
      ("¿El lambrín de PVC resiste la humedad?", "Sí, el lambrín de PVC es 100% resistente al agua. Es ideal para baños, cocinas y áreas húmedas en Ciudad Victoria."),
    ],
    "related": [("/productos/plafones/", "Plafones"), ("/productos/tablaroca/", "Tablaroca")],
  },
  {
    "slug": "material-decoracion",
    "name": "Material de Decoración",
    "title": "Material de Decoración en Ciudad Victoria | Acabados y Recubrimientos | AceroMAX",
    "desc": "Material de decoración en Ciudad Victoria, Tamaulipas. Lambrín, molduras, cornisas, plafones decorativos, paneles 3D, texturizados. Para remodelaciones y acabados.",
    "keywords": "material de decoración ciudad victoria, decoración de interiores victoria, acabados para casa victoria, molduras victoria, cornisas victoria, paneles decorativos tamaulipas, remodelación victoria",
    "h1": "Material de Decoración en Ciudad Victoria",
    "intro": "¿Buscas <strong>material de decoración en Ciudad Victoria</strong>? En AceroMAX tenemos lambrines, molduras, cornisas, plafones decorativos, pinturas texturizadas y materiales para acabados interiores que transforman cualquier espacio.",
    "details": "La decoración interior va más allá de la pintura. Con los materiales correctos puedes crear ambientes modernos, elegantes o rústicos según tu gusto. En AceroMAX combinamos materiales de construcción con acabados decorativos para que encuentres todo en un solo lugar.",
    "uses": ["Remodelación de salas y recámaras", "Acabados en oficinas y consultorios", "Decoración de restaurantes y comercios", "Plafones decorativos", "Muros de acento", "Fachadas interiores"],
    "variants": ["Lambrín de PVC decorativo", "Molduras y cornisas de poliestireno", "Plafones decorativos (PVC y fibra mineral)", "Pintura texturizada DOAL", "Paneles 3D para muros", "Tablaroca para nichos y diseños especiales"],
    "brands": ["DOAL", "Alvamex", "USG"],
    "faqs": [
      ("¿Tienen material decorativo en Ciudad Victoria?", "Sí, en AceroMAX manejamos lambrines, molduras, plafones decorativos, pinturas texturizadas y materiales para acabados. 2 sucursales en Ciudad Victoria."),
      ("¿Qué material recomiendan para un muro de acento?", "Para muros de acento en Ciudad Victoria recomendamos lambrín de PVC tipo madera o paneles 3D. Son fáciles de instalar y dan un cambio dramático al espacio."),
    ],
    "related": [("/productos/lambrin/", "Lambrín"), ("/productos/pintura/", "Pintura"), ("/productos/plafones/", "Plafones")],
  },
  {
    "slug": "galvateja",
    "name": "Galvateja",
    "title": "Galvateja en Ciudad Victoria | Teja de Acero Galvanizado | AceroMAX",
    "desc": "Venta de galvateja en Ciudad Victoria, Tamaulipas. Teja de acero galvanizado con apariencia de teja de barro. Ligera, resistente, fácil instalación. Varios colores.",
    "keywords": "galvateja ciudad victoria, galvateja precio victoria, teja de acero victoria, teja galvanizada tamaulipas, galvateja para techo, galvateja colores, venta galvateja victoria",
    "h1": "Galvateja en Ciudad Victoria",
    "intro": "¿Buscas <strong>galvateja en Ciudad Victoria</strong>? En AceroMAX tenemos galvateja: lámina de acero galvanizado con perfil de teja tradicional. La estética de la teja de barro con la resistencia y ligereza del acero. Varios colores disponibles.",
    "details": "La galvateja es una lámina de acero galvanizado o pintro con perfil que simula la teja de barro tradicional. Pesa una fracción de la teja real, se instala más rápido, no se quiebra y dura décadas sin mantenimiento. Es la tendencia en techumbres residenciales de Ciudad Victoria.",
    "uses": ["Techumbres residenciales con estilo colonial", "Terrazas y pérgolas", "Cocheras con acabado premium", "Remodelación de techos existentes", "Fachadas decorativas", "Casas de campo y ranchos"],
    "variants": ["Galvateja pintro rojo", "Galvateja pintro terracota", "Galvateja pintro café", "Galvateja galvanizada natural", "Galvateja calibre 26", "Caballete y accesorios"],
    "brands": ["Ternium"],
    "faqs": [
      ("¿Cuánto cuesta la galvateja en Ciudad Victoria?", "El precio de la galvateja varía según el color y calibre. Cotiza por WhatsApp con los m² de techo para precio exacto incluyendo caballete y accesorios."),
      ("¿La galvateja es mejor que la teja de barro?", "La galvateja es más ligera (tu estructura necesita menos refuerzo), no se quiebra, no absorbe agua, se instala 3 veces más rápido y dura más. Solo la teja de barro supera en autenticidad visual."),
      ("¿En qué colores viene la galvateja?", "Manejamos galvateja en rojo, terracota, café, gris y galvanizado natural. El rojo y terracota son los más populares en Ciudad Victoria."),
    ],
    "related": [("/laminas/", "Catálogo Láminas"), ("/productos/aceroteja/", "Aceroteja"), ("/productos/lamina-galvanizada/", "Lámina Galvanizada")],
  },
  {
    "slug": "aceroteja",
    "name": "Aceroteja",
    "title": "Aceroteja en Ciudad Victoria | Teja Metálica Premium | AceroMAX",
    "desc": "Venta de aceroteja en Ciudad Victoria, Tamaulipas. Teja metálica premium con acabado tipo teja artesanal. Alta durabilidad, ligera, varios colores. Para techos residenciales.",
    "keywords": "aceroteja ciudad victoria, aceroteja precio victoria, teja metálica victoria, teja de acero premium tamaulipas, aceroteja para techo, venta aceroteja victoria",
    "h1": "Aceroteja en Ciudad Victoria",
    "intro": "¿Buscas <strong>aceroteja en Ciudad Victoria</strong>? En AceroMAX tenemos aceroteja, la teja metálica premium con acabado tipo teja artesanal. Máxima durabilidad, mínimo mantenimiento y la estética más elegante para tu techumbre.",
    "details": "La aceroteja es la versión premium de las tejas metálicas. Con un perfil más pronunciado y acabados de alta definición, logra una apariencia prácticamente idéntica a la teja de barro artesanal. Es la elección preferida para residencias de alto nivel y proyectos arquitectónicos en Ciudad Victoria.",
    "uses": ["Residencias de alto nivel", "Proyectos arquitectónicos especiales", "Restaurantes y hoteles boutique", "Casas de campo premium", "Remodelación de techos coloniales", "Edificios comerciales con estilo clásico"],
    "variants": ["Aceroteja acabado terracota", "Aceroteja acabado rojo colonial", "Aceroteja acabado café antiguo", "Aceroteja acabado gris piedra", "Caballete y accesorios de remate"],
    "brands": ["Ternium"],
    "faqs": [
      ("¿Cuál es la diferencia entre galvateja y aceroteja?", "La aceroteja tiene un perfil más pronunciado y acabados de mayor definición que la galvateja. Es la opción premium. La galvateja es más económica pero con excelente resultado. Ambas son de acero galvanizado."),
      ("¿Cuánto dura la aceroteja?", "La aceroteja tiene una vida útil de 30+ años con mantenimiento mínimo. La garantía de acabado puede ser de 10 a 25 años según el fabricante."),
    ],
    "related": [("/laminas/", "Catálogo Láminas"), ("/productos/galvateja/", "Galvateja"), ("/productos/lamina-galvanizada/", "Lámina Galvanizada")],
  },
]


def gen_product_page(p):
    uses_html = "\n".join([f'<li style="padding:8px 0;border-bottom:1px solid #f0f0f0;">{u}</li>' for u in p["uses"]])
    variants_html = "\n".join([f'<li style="padding:12px 16px;border-bottom:1px solid #f0f0f0;display:flex;align-items:center;gap:12px;"><span style="color:var(--primary);font-weight:700;">✓</span>{v}</li>' for v in p["variants"]])
    brands_html = " · ".join([f'<a href="/marcas/{b.lower()}/" style="color:var(--primary);font-weight:600;">{b}</a>' for b in p["brands"]]) if p["brands"] else "Varias marcas"
    faqs_schema = ",\n".join([
        f'{{"@type":"Question","name":"{q}","acceptedAnswer":{{"@type":"Answer","text":"{a}"}}}}'
        for q, a in p["faqs"]
    ])
    faqs_html = "\n".join([
        f'<div class="faq-item"><button class="faq-question">{q}</button><div class="faq-answer"><p>{a}</p></div></div>'
        for q, a in p["faqs"]
    ])
    related_html = "\n".join([
        f'<a href="{url}" class="category-card"><h3>{name}</h3><p>Ver más →</p></a>'
        for url, name in p["related"]
    ])

    return f'''<!DOCTYPE html>
<html lang="es-MX">
<head>
{GA4}
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{p["title"]}</title>
<meta name="description" content="{p["desc"]}">
<meta name="keywords" content="{p["keywords"]}">
<meta name="robots" content="index, follow, max-image-preview:large">
<link rel="canonical" href="https://aceromax.mx/productos/{p["slug"]}/">
<meta property="og:title" content="{p["title"]}">
<meta property="og:description" content="{p["desc"]}">
<meta property="og:url" content="https://aceromax.mx/productos/{p["slug"]}/">
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
  "name":"AceroMAX — {p["name"]} en Ciudad Victoria",
  "image":"https://aceromax.mx/images/logo.png",
  "url":"https://aceromax.mx/productos/{p["slug"]}/",
  "telephone":"+528341100942",
  "priceRange":"$$",
  "address":[{{
    "@type":"PostalAddress","streetAddress":"Hombres Ilustres 510, Col. Adolfo López Mateos","addressLocality":"Ciudad Victoria","addressRegion":"Tamaulipas","postalCode":"87020","addressCountry":"MX"
  }},{{
    "@type":"PostalAddress","streetAddress":"Naciones Unidas 1155, Fracc. Naciones Unidas","addressLocality":"Ciudad Victoria","addressRegion":"Tamaulipas","postalCode":"87049","addressCountry":"MX"
  }}],
  "geo":{{"@type":"GeoCoordinates","latitude":23.7369,"longitude":-99.1411}},
  "areaServed":[
    {{"@type":"City","name":"Ciudad Victoria"}},
    {{"@type":"City","name":"Güémez"}},
    {{"@type":"City","name":"Jiménez"}},
    {{"@type":"City","name":"Padilla"}},
    {{"@type":"City","name":"Llera"}},
    {{"@type":"State","name":"Tamaulipas"}}
  ]
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
{{"@type":"ListItem","position":2,"name":"Productos","item":"https://aceromax.mx/productos/"}},
{{"@type":"ListItem","position":3,"name":"{p["name"]}","item":"https://aceromax.mx/productos/{p["slug"]}/"}}
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
<li><a href="https://wa.me/528348528236?text=Hola%2C%20quiero%20cotizar%20{p["name"].lower().replace(" ", "%20")}" class="nav-cta" target="_blank" rel="noopener">Cotizar por WhatsApp</a></li>
</ul>
</div></nav>

<section class="page-hero" style="background:linear-gradient(135deg, var(--dark) 0%, #16213e 100%); color:white; padding:60px 0;">
<div class="container">
<p style="color:var(--accent);font-weight:600;margin-bottom:8px;">VENTA EN CIUDAD VICTORIA</p>
<h1 style="font-size:2.4rem;font-weight:900;margin-bottom:16px;">{p["h1"]}</h1>
<p style="font-size:1.1rem;color:#ccd;max-width:700px;">Distribuidor en Ciudad Victoria, Tamaulipas. Venta al mayoreo y menudeo. 2 sucursales con entrega a domicilio en la región.</p>
<p style="margin-top:12px;font-size:0.95rem;color:var(--accent);">Marcas: {" · ".join(p["brands"]) if p["brands"] else "Varias marcas disponibles"}</p>
<div style="margin-top:24px;display:flex;gap:12px;flex-wrap:wrap;">
<a href="https://wa.me/528348528236?text=Hola%2C%20quiero%20cotizar%20{p["name"].lower().replace(" ", "%20")}" class="btn btn-whatsapp" target="_blank" rel="noopener">
<svg width="20" height="20" viewBox="0 0 24 24" fill="white"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347z"/></svg>
Cotizar {p["name"]}
</a>
<a href="tel:+528341100942" class="btn btn-outline">Llamar: 834 110 0942</a>
</div>
</div>
</section>

<section style="padding:60px 0;">
<div class="container" style="max-width:900px;">
<div style="display:grid;grid-template-columns:1fr 1fr;gap:40px;">
<div>
<h2 style="font-size:1.6rem;font-weight:800;color:var(--dark);margin-bottom:16px;">{p["name"]} en Ciudad Victoria</h2>
<p style="font-size:1.05rem;line-height:1.8;margin-bottom:16px;">{p["intro"]}</p>
<p style="font-size:1rem;line-height:1.8;color:#555;">{p["details"]}</p>
</div>
<div>
<h3 style="font-size:1.2rem;font-weight:700;color:var(--dark);margin-bottom:16px;">Usos principales</h3>
<ul style="list-style:none;padding:0;">{uses_html}</ul>
</div>
</div>
</div>
</section>

<section class="bg-gray" style="padding:60px 0;">
<div class="container">
<div class="section-title"><h2>Presentaciones Disponibles</h2><p>Stock en nuestras 2 sucursales de Ciudad Victoria</p></div>
<div style="max-width:800px;margin:0 auto;background:white;border-radius:12px;padding:32px;box-shadow:0 2px 12px rgba(0,0,0,0.04);">
<ul style="list-style:none;padding:0;">{variants_html}</ul>
<p style="margin-top:20px;text-align:center;color:#666;font-size:0.9rem;">Marcas: {brands_html}</p>
<div style="margin-top:24px;text-align:center;">
<a href="https://wa.me/528348528236?text=Hola%2C%20quiero%20cotizar%20{p["name"].lower().replace(" ", "%20")}" class="btn btn-whatsapp" target="_blank" rel="noopener">Cotizar {p["name"]} por WhatsApp</a>
</div>
</div>
</div>
</section>

<section style="padding:60px 0;">
<div class="container">
<div class="section-title"><h2>Preguntas Frecuentes — {p["name"]} en Ciudad Victoria</h2></div>
<div class="faq-list">{faqs_html}</div>
</div>
</section>

<section class="bg-gray" style="padding:48px 0;">
<div class="container">
<div class="section-title"><h2>Relacionados</h2></div>
<div style="display:grid;grid-template-columns:repeat(auto-fill, minmax(220px, 1fr));gap:16px;max-width:800px;margin:0 auto;">
{related_html}
</div>
</div>
</section>

<section class="cta-section">
<div class="container">
<h2>¿Necesitas {p["name"].lower()} en Ciudad Victoria?</h2>
<p>Cotiza al instante por WhatsApp. Manda tu lista y recibe precio en minutos. Entrega a domicilio.</p>
<div class="cta-buttons">
<a href="https://wa.me/528348528236?text=Hola%2C%20quiero%20cotizar%20{p["name"].lower().replace(" ", "%20")}" class="btn btn-whatsapp" target="_blank" rel="noopener">
<svg width="20" height="20" viewBox="0 0 24 24" fill="white"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347z"/></svg>
Cotizar por WhatsApp
</a>
<a href="tel:+528341100942" class="btn btn-outline" style="border-color:rgba(255,255,255,0.4);color:white;">Llamar: 834 110 0942</a>
</div>
</div>
</section>

<section style="padding:48px 0;">
<div class="container">
<div class="section-title"><h2>Nuestras Sucursales</h2></div>
<div class="locations-grid">
<div class="location-card"><div class="location-info">
<h3>Sucursal Matriz</h3>
<p>Hombres Ilustres 510, Col. Adolfo López Mateos, CP 87020</p>
<p><a href="tel:+528341100942">834 110 0942</a> | Lun-Vie 8:00-18:00 | Sáb 8:00-14:00</p>
</div></div>
<div class="location-card"><div class="location-info">
<h3>Sucursal Naciones Unidas</h3>
<p>Naciones Unidas 1155, Fracc. Naciones Unidas, CP 87049</p>
<p><a href="tel:+528343132000">834 313 2000</a> | Lun-Vie 8:00-18:00 | Sáb 8:00-14:00</p>
</div></div>
</div>
</div>
</section>

<footer><div class="container">
<div class="footer-grid">
<div class="footer-col"><h4>AceroMAX</h4><p>Distribuidor oficial de materiales de construcción en Ciudad Victoria, Tamaulipas.</p></div>
<div class="footer-col"><h4>Productos</h4>
<a href="/acero-estructural/">Acero</a><a href="/ptr-perfiles/">PTR</a><a href="/laminas/">Láminas</a><a href="/tablaroca-durock/">Tablaroca</a><a href="/varilla-cemento/">Varilla</a><a href="/losacero/">Losacero</a></div>
<div class="footer-col"><h4>Más</h4>
<a href="/mallas/">Mallas</a><a href="/plafones/">Plafones</a><a href="/pinturas/">Pinturas</a><a href="/puertas-ferreteria/">Ferretería</a><a href="/marcas/">Marcas</a><a href="/contacto/">Contacto</a></div>
<div class="footer-col"><h4>Contacto</h4>
<a href="tel:+528341100942">834 110 0942</a><a href="tel:+528343132000">834 313 2000</a><a href="https://wa.me/528348528236">WhatsApp: 834 852 82 36</a><p>Ciudad Victoria, Tamaulipas</p></div>
</div><div class="footer-bottom"><p>&copy; 2026 AceroMAX — {p["name"]} en Ciudad Victoria, Tamaulipas.</p></div></div></footer>

<div class="wa-float"><a href="https://wa.me/528348528236?text=Hola%2C%20quiero%20cotizar%20{p["name"].lower().replace(" ", "%20")}" target="_blank" rel="noopener">
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


# Generate all product pages
for p in products:
    dirpath = f"productos/{p['slug']}"
    os.makedirs(dirpath, exist_ok=True)
    filepath = f"{dirpath}/index.html"
    with open(filepath, 'w') as f:
        f.write(gen_product_page(p))
    print(f"✓ {filepath}")

print(f"\n{len(products)} product pages generated")
