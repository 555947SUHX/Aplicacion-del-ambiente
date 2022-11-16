import streamlit as st

st.title('AYUDANOS A CUIDAR EN MEDIO AMBIENTE')
st.image("https://i.ytimg.com/vi/dGAMdXY3zX8/maxresdefault.jpg", width=300)
st.subheader("*$¿Qué$ $es$ $el$ $calentamiento$ $global?$*")
st.write("La Revolución Industrial fue el punto de inflexión en el que las emisiones de gases de efecto invernadero (GEI) arrojadas a la atmósfera empezaron a dispararse. Empezó a crecer la población y aumentó la demanda y producción de energía (obtenidas mayoritariamente a través de combustibles fósiles), lo que dio lugar a un nuevo modelo de producción y de consumo. El principal resultado fue el aumento global de la temperatura: de 1,1°C entre 1850 y 2017. En este articulo resumimos en qué situación nos encontramos en 2022.")


st.caption("-huella de carbono")
st.write("Mitigar los efectos del calentamiento global significa adaptar su estilo de vida a la situación actual, reduciendo y limitando las emisiones de gases de efecto invernadero. Para ello, el primer paso es tomar conciencia de su propia huella de carbono.")
st.write("El cálculo de la huella de carbono es el primer paso para reducirla: identificar las principales fuentes de emisiones de gases de efecto invernadero en nuestra vida cotidiana y adaptar así nuestro estilo de vida para minimizar su impacto de carbono en el medio ambiente; La reducción de las emisiones de gases de efecto invernadero es muy importante para luchar contra el calentamiento global: optimizar el consumo de energía, reducir nuestra huella digital de carbono y promover el transporte sostenible; La compensación de sus emisiones de carbono mediante la financiación de proyectos ambientales con el fin de reducir las emisiones de gases de efecto invernadero a la atmósfera y avanzar así hacia la neutralidad del carbono.")

st.sidebar.header("La contaminacion")
st.sidebar.subheader('El daño que hacen en el planeta')
st.sidebar.write("Se entiende por contaminación ambiental cuando existe la presencia de sustancias nocivas en el agua, aire o suelo.")
st.sidebar.image("https://plusambiental.com/wp-content/uploads/2021/11/contaminacion-ambiental-todo.jpg")

st.sidebar.write("$tipos$ $de$ $contaminación$")

col1, col2 = st.columns([1,2])

col1.header("Causas")
col2.header("Consecuencias")

st.header("$¿Qué$ $es$ $la$ $huella$ $ecologica?$")
st.write("El objetivo de reducir la huella ecológica es esencial debido al nivel de consumo de los recursos naturales y de la energía, la creación de desechos y las emisiones contaminantes por parte del ser humano. Se trata de tener claras nuestras necesidades reales y lo que requiere la naturaleza para su subsistencia. Hay que mantener presente que esta debe regenerarse y que, en ocasiones, tarda mucho tiempo en hacerlo.")



st.header("Reduce tu huella ecologica")


if st.sidebar.button("hidrica"):
  col1.write("Vertidos de aguas negras, Derrames de petróleo, Productos fitosanitarios, Deforestación, Aumento de temperatura")
  col2.write("Deterioro de la biodiversidad, Contaminación de la cadena alimentaria, Escasez de agua potable, Enfermedades, Mortalidad infantil")
  st.write("Ajustar el consumo de agua en casa")
  st.write("Las buenas prácticas en el hogar nunca están demás. Las duchas cortas, cerrar los caños cuando no se está usando, reducir el nivel de agua en las lavadoras, arreglar las llaves y tuberías de los lavaderos para que no goteen y regar las plantas cuando llueve son acciones que pueden parecer insignificantes, pero que en el tiempo ayudan en gran medida a reducir la huella hídrica y contribuir al cuidado del medio ambiente.")
  st.write("Reduce el consumo de carne")
  st.write("Aunque no lo parezca, cada kilogramo de carne bovina produce un gasto de más de 15 mil litros de agua, o sea unos 40 camiones cisterna3. Esto se debe a su alimentación: hay que considerar toda el agua necesaria para la producción de los pastos, cereales, etc, que el animal va a consumir durante toda su vida4. Es por ello que, para reducir la huella hídrica, es mejor consumir otro tipo de alimentos que nos permita alcanzar nuestros requerimientos nutricionales diarios.")
  st.write("Elije alimentos orgánicos")
  st.write("Muchos de los alimentos de cultivo que se consumen diariamente mantienen un proceso de producción que requieren riego constante. Algunos cereales, por ejemplo, emplean más de 1500 litros de agua en un solo kilogramo5. Por otra parte, los productos procesados también generan un gran impacto, ya que pasan por una cadena de limpieza y precocción. En ese sentido, el consumir alimentos orgánicos nos ayudará a reducir la huella hídrica debido a que los suelos en los que son sembrados permiten que se filtre y retengan eficientemente más agua, y no necesitan de ningún proceso ambientalmente perjudicial para su empaquetado6.")
  st.write("Revisa el etiquetado de la ropa")
  st.write("Actualmente, la industria textil es otro sector que consume grandes cantidades de agua para la fabricación de ropa. Informes hechos por El Corte Inglés, Fundación Botín y el Instituto Aitex indican que la ropa de los jóvenes es la que presenta mayor huella hídrica, pues su manufacturación requiere 15 mil litros de agua: las zapatillas requieren 4400 litros; un pantalón jean, 3000 litros; una camisa, 1000 litros; y un polo, 1200 litros7. Este gasto se debe al uso de algodón como insumo principal para las prendas. Ante esto, existen marcas certificadas que están empezando a ofrecer ropa en base a materiales reciclados y aguas residuales tratadas.")

if st.sidebar.button("del suelo"):
  col1.write("-Almacenamiento incorrecto de productos y/o residuos en actividades industriales, Vertidos de residuos incontrolados, Deposición de contaminantes atmosféricos")
  col2.write("Daños a la salud, Peores cultivos, Cambio climático, Contaminación de agua y aire, Desaparición de especies, Desertificación")
  st.write("Transporte sostenible")
  st.write("Se pueden utilizar alternativas sostenibles a los medios de transporte más contaminantes (motos y coches), como son la bicicleta, el transporte público, los patines o caminar. No conducir vehículos contaminantes puede llegar a reducir la huella ecológica de una persona hasta en un 20%.") 
  st.write("Evita comprar productos con aceite de palma.")
  st.write("¿Te encanta desayunar bollería, galletas o cereales? ¿No imaginas un aperitivo sin patatas fritas? Mira bien los ingredientes de estos alimentos y si llevan aceite de palma, ¡descártalos! La palma y la soja están causando la deforestación de grandes zonas en selvas vírgenes en Indonesia, Brasil o Camerún. Además, es un cultivo muy agresivo con el suelo.")
  st.write("Evita comprar platos precocinados.")
  st.write("Contienen conservantes, colorantes o antiapelmazantes para mejorar su conservación y una gran cantidad de azúcar, para el cual se emplea mucha agua al producirlo. Prueba a preparar tus propias comidas, sándwiches o zumos, reducirás el consumo de azúcares, embalajes y plásticos.")

if st.sidebar.button("ambiental"):
  col1.write("Contaminantes químicos, Agentes físicos, Contaminantes biológicos")
  col2.write("Diversos tipos de contaminación, Daños en el estado de salud de los seres humanos, Desaparición de la capa de ozono, Daños en los ecosistemas")
  st.write("el crecimiento de la población, en la actualidad por el gran crecimiento de las familias, se han visto un vgran consumo en recursos y estos se ah estado sobre explotando")
  st.write("la pérdida de suelo fértil ya que estos se han estado contaminando o se quieran para construir, tomando en cuenta que solo unas partes son aptas para la agricultura")
  st.write("la deforestación esta tambien va relacionada con la sobre explotacion porque talamos mas arboles de los que se plantan y se dejan crecer")
  st.write("el aumento del consumo, esto va de la mano por el aumento de la poblacion.")


st.sidebar.write("participantes :")
st.sidebar.write("Pela Abigail Rodriguez Muñoz")
st.sidebar.write("Curso de Programnación")
st.sidebar.write("Facultad de Ciencias Quimicas, Univerdidad Autonoma de chihuahua")
st.sidebar.write("Docente: Jose Manuel Napoles Duarte")

st.title("Calculadora de huella ecologica")
number=st.slider("personas con las que vives",1,10)

suma = 0
diccionario1 = {"nunca":0.1,"casi nunca":0.2, "ocasionalmente":1, "diariamente":2}
option = st.selectbox(
    'Que tan seguido consumes productos de origen animal',
    diccionario1)

st.write('You selected:', diccionario1[option])

suma = suma + diccionario1[option]

diccionario2 = {"100":0.09,"75":0.15, "50":0.25, "25":0.45, "0":0.75}
option = st.selectbox(
    'Porcentaje de tu comida que no esta empaquetada ',
    diccionario2)

st.write('You selected:', diccionario2[option])

suma = suma + diccionario2[option]

diccionario3 = {"independiente sin agua":0.2,"independiente con agua":0.5, "departamento con varios pisos":0.3, "duplex,edificio":0.3, "condominio de lujo":0.8}
option = st.selectbox(
    'Como es tu casa',
    diccionario3)

st.write('You selected:', diccionario3[option])

suma = suma + diccionario3[option]

diccionario4 = {"Adobe":0.01,"Madera":0.2, "Paja":0.02, "Ladrillo":0.8, "Acero/otro":0.5}
option = st.selectbox(
    'De que material esta construida',
    diccionario4)

st.write('You selected:', diccionario4[option])

suma = suma + diccionario4[option]

diccionario5 = {"menor de 50":0.15,"50-140":0.3, "140-460":0.4, "mayor de 460":0.9}
option = st.selectbox(
    'tamaño de la vivienda',
    diccionario5)

st.write('You selected:', diccionario5[option])

suma = suma + diccionario5[option]

diccionario6 = {"ineficiente":0.05,"promedio":0.3, "por encima del promedio":0.4, "muy eficiente":0.7,"no tengo electricidad": 0}
option = st.selectbox(
    'Que tan eficiente es el consumo de energia de tu hogar',
    diccionario6)

st.write('You selected:', diccionario6[option])

suma = suma + diccionario6[option]

diccionario7 = {"mucho menos":0.01,"menos":0.2, "igual":0.5, "mas":0.8, "mucha mas": 2}
option = st.selectbox(
    'Comparado con tus vecinos cuanta basura genera',
    diccionario7)

st.write('You selected:', diccionario7[option])

suma = suma + diccionario7[option]

st.header("tu huella ecologica es de:")
st.header(suma)
st.write("HAG")

st.header("si todos vivieran como tu necesitariamos:")

planetas = (suma/3)
st.header(planetas)
st.image("https://img.freepik.com/vector-premium/planeta-tierra-arboles-estilo-dibujos-animados_1308-81386.jpg?w=2000", width=200)
st.write("planetas")
