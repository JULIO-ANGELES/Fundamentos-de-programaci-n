#JULIO CESAR ANGELES MENDOZA (IDS) CALCULADORA DE TIEMPO DIGITAL 
#Desarrollar una **calculadora interactiva en Python** que permita registrar el
#tiempo diario (en horas o fracciones de hora) que una persona dedica a distintas
#plataformas digitales: redes sociales, mensajería, servicios de streaming,
#videojuegos, entre otras. El programa debe capturar los datos, procesarlos y
#mostrar un resumen claro y ordenado de los resultados.

nombre = input("introduzca su nombre:")

Redes_sociales = float(input("Ingrese el tiempo que dedica a redes sociales (en horas): "))
streaming = float(input("Ingrese el tiempo que dedica a streaming (en horas): "))
mensajeria = float(input("Ingrese el tiempo que dedica a Mensajería (en horas): "))
videojuegos = float(input("Ingrese el tiempo que dedica a Videojuegos (en horas): "))
estudio_en_linea = float(input("Ingrese el tiempo que dedica a Estudio en línea (en horas): "))


tiempo_total = Redes_sociales + streaming + mensajeria + videojuegos + estudio_en_linea
porcentaje_total = (tiempo_total / 24) * 100

print("----RESULTADOS----:")
print(f"nombre: {nombre}")
print(f"Tiempo total dedicado a plataformas digitales: {tiempo_total:.2f} horas")
print(f"Porcentaje del día dedicado a plataformas digitales: {porcentaje_total:.2f}%")