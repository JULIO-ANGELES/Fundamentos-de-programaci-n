# PROTOTIPO INICIAL DEL PORYECTO (AVANCE) JULIO CESAR ANGELES MENDOZA (IDS)
# Control de Ocupación del Gimnasio Universitario

print("==========================================")
print(" CONTROL DE OCUPACION DEL GIMNASIO")
print("          UNIVERSITARIO")
print("==========================================")

# aqui se piden los datos (primera parte)
capacidad_maxima = int(input("Ingrese la capacidad maxima del gimnasio: "))

while capacidad_maxima <= 0:
    print("La capacidad debe ser mayor a cero.")
    capacidad_maxima = int(input("Ingrese nuevamente la capacidad: "))

horario = input("Ingrese el horario a analizar: ")
usuarios_presentes = int(input("Ingrese la cantidad de usuarios presentes: "))

# aqui se validan los datos ingresados
while usuarios_presentes < 0 or usuarios_presentes > capacidad_maxima:
    print("Cantidad de usuarios no valida.")
    usuarios_presentes = int(input("Ingrese nuevamente la cantidad: "))

#aqui se procesan los datos de capacidad del gym
espacios_disponibles = capacidad_maxima - usuarios_presentes
porcentaje_ocupacion = (usuarios_presentes / capacidad_maxima) * 100

# Aqui se clasifica la ocupacion del gym
if porcentaje_ocupacion <= 50:
    nivel_ocupacion = "BAJA"

elif porcentaje_ocupacion <= 75:
    nivel_ocupacion = "MODERADA"

elif porcentaje_ocupacion <= 90:
    nivel_ocupacion = "ALTA"

else:
    nivel_ocupacion = "CRITICA"

# Aqui se muestran los resultados despues de todo lo anteriormente procesado

print("------------- RESULTADO -------------")
print("Horario:", horario)
print("Usuarios presentes:", usuarios_presentes)
print("Espacios disponibles:", espacios_disponibles)
print("Porcentaje de ocupacion:", round(porcentaje_ocupacion, 2), "%")
print("Nivel de ocupacion:", nivel_ocupacion)

if usuarios_presentes == capacidad_maxima:
    print("ALERTA: El gimnasio alcanzo su capacidad maxima.")