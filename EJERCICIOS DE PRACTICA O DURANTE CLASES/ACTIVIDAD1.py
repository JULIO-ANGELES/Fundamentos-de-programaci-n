# Ejercicio 1: Algoritmo para preparar café
# Enunciado:** Escribe en lenguaje natural los pasos (algoritmo) para preparar una taza de café instantáneo. Deben ser precisos, definidos y finitos.
# Entrada:** Temperatura del agua, cantidad de café en cucharadas, presencia de azúcar.
# Salida:** Lista ordenada de pasos que termina con la taza de café lista para beber.

print = input("Ingrese la temperatura del agua (en grados Celsius): ")
print = input("Ingrese la cantidad de café en cucharadas: ")
azucar = input("¿Desea agregar azúcar? (sí/no): ")

print("----PASOS PARA PREPARAR CAFÉ INSTANTÁNEO----:")
print("1. Calentar el agua a la temperatura indicada.")
print("2. Colocar la cantidad de café en cucharadas en la taza.")
if azucar.lower() == "sí":
    print("3. Agregar azúcar al gusto.")
print("4. Verter el agua caliente en la taza con café y azúcar.")
print("5. Revolver bien la mezcla.")




