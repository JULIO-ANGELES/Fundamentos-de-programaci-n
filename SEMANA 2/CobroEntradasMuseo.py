# Nombre: Julio Cesar Angeles Mendoza (IDS)
# Matrícula: 07313141
# Fecha: 20/08/2026
# Actividad evaluable 2: Cobro de entradas del museo

#constantes
PRECIO_MENOR = 30
PRECIO_ADULTO = 45

DESCUENTO_ADULTO_MAYOR = 0.12
DESCUENTO_PROFESOR = 0.10
DESCUENTO_ESTUDIANTE = 0.10

cantidad_visitantes =int(input("Ingresa la cantidad de visitantes:"))
contador = 1
total = 0

while contador <= cantidad_visitantes:
    print(f"\nVisitante {contador}")
    edad = int(input("ingrese la edad:"))

    if edad < 3:
        precio = 0
        print("Menor de 3 años, sin cargo")
        print("Precio del boleto: $0.00")

        contador += 1
        continue
    elif edad <= 17:
        precio = PRECIO_MENOR
    else:
        precio = PRECIO_ADULTO

    print("Selecciona el tipo de visitante: ")
    print("1.Adulto mayor")
    print("2.Profesor")
    print("3.Estudiante")
    print("4.Ninguno")

    tipo = int(input("Selecciona una Opcion:"))

    if tipo == 1:
        descuento = precio * DESCUENTO_ADULTO_MAYOR
    elif tipo == 2:
        descuento = precio * DESCUENTO_PROFESOR
    elif tipo == 3:
        descuento = precio * DESCUENTO_ESTUDIANTE
    else:
         descuento = 0
    precio_final = precio - descuento

    print(f"precio del boleto: ${precio:.2f}")
    print(f"Descuento: ${descuento:.2f}")
    print(f"Total a pagar: ${precio_final:.2f}")

    total += precio_final
    contador += 1

    if contador > cantidad_visitantes:
         break

print("\nTotal de todos los visitantes:")
print(f" ${total:.2f}")