#JULIO CESAR ANGELES MENDOZA (IDS) CALCULADORA DE TIEMPO DIGITAL 
#Desarrollar una **calculadora interactiva en Python** que permita registrar el
#tiempo diario (en horas o fracciones de hora) que una persona dedica a distintas
#plataformas digitales: redes sociales, mensajería, servicios de streaming,
#videojuegos, entre otras. El programa debe capturar los datos, procesarlos y
#mostrar un resumen claro y ordenado de los resultados.

nombre = input("introduzca su nombre:")

facebook = float(input("Ingrese el tiempo que dedica a Facebook (en horas): "))
instagram = float(input("Ingrese el tiempo que dedica a Instagram (en horas): "))
twitter = float(input("Ingrese el tiempo que dedica a Twitter (en horas): "))
youtube = float(input("Ingrese el tiempo que dedica a YouTube (en horas): "))
netflix = float(input("Ingrese el tiempo que dedica a Netflix (en horas): "))
whatsapp = float(input("Ingrese el tiempo que dedica a WhatsApp (en horas): "))
videojuegos = float(input("Ingrese el tiempo que dedica a Videojuegos (en horas): "))
estudio = float(input("Ingrese el tiempo que dedica a Estudio (en horas): "))
llamasas_o_reuniones = float(input("Ingrese el tiempo que dedica a Llamadas o Reuniones (en horas): "))

tiempo_total = facebook + instagram + twitter + youtube + estudio + netflix + whatsapp + videojuegos + llamasas_o_reuniones
porcentaje_total = (tiempo_total / 24) * 100

print("RESULTADOS:")
print(f"nombre: {nombre}")
print(f"Tiempo total dedicado a plataformas digitales: {tiempo_total:.2f} horas")
print(f"Porcentaje del día dedicado a plataformas digitales: {porcentaje_total:.2f}%")
