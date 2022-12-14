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

size=st.select_slider("Que tan seguido consumes productos de origen animal", options=["nunca","casi nunca", "ocasionalmente", "diariamente"],value=("nunca"))
 
st.write("nunca=0.1")
st.write("casi nunca=0.2")
st.write("ocasionalmente=1")
st.write("diariamente=2")

choice=st.selectbox("Porcentaje de tu comida no esta empaquetada",["100","75","50","25","0"])

st.write("100=0.09")
st.write("75=0.15")
st.write("50=0.25")
st.write("25=0.45")
st.write("0=0.75")

choice=st.selectbox("Como es tu casa",["independiente sin agua","independiente con agua","departamento con varios pisos","duplex,edificio","condominio de lujo"])

st.write("sin agua=0.2")
st.write("con agua=0.5")
st.write("varios pisos=0.3")
st.write("duplex=0.3")
st.write("condominio=0.8")

choice=st.selectbox("De que material esta construida",["Adobe","Madera","Paja","Ladrillo","Acero/otro"])
choice=st.selectbox("tamaño de la vivienda",["menor de 50","50-140","140-460","mayor de 460"])
size=st.select_slider("Que tan eficiente es el consumo de energia de tu hogar", options=["ineficiente","promedio", "por encima del promedio", "muy eficiente", "no tengo electricidad"],value=("no tengo electricidad"))
size=st.select_slider("Comparado con tus vecinos cuanta basura genera", options=["mucho menos","menos", "igual", "mas", "mucha mas"],value=("mucho menos"))
choice=st.number_input("Que distancia viaja en transporte publico cada semana (km)",0,100) 
