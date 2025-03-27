# Proyecto: [Nombre del Proyecto]
# Estudiante: [Nombre del Estudiante]
# Fecha de Inicio: [dd/mm/aaaa]
# Fecha de Entrega: [dd/mm/aaaa]
# Descripción: Este archivo contiene el punto de entrada principal del proyecto.
# Recuerda incluir tu nombre completo, la fecha en la que iniciaste el proyecto y la fecha estimada de entrega.
# Esto ayuda a mantener un registro claro del trabajo realizado.
from analisis_datos import *

lista_compras = generar_lista_compras()

precios = [valor for producto, valor in lista_compras]

print(precios)

print(lista_compras)

print('La media de precio que pague fue:', media(precios))

print('la mediana de la compra es:', mediana(precios))

