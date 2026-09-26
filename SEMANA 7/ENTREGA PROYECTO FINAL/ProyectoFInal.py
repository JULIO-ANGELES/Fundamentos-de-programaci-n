#Entrega Final del proyecto| Fundamentos de programación| Julio César Ángeles Mendoza|22/09/2026 (IDS)


# Entrega Final del Proyecto - Fundamentos de Programación
# Sistema de Control de Ocupación del Gimnasio Universitario

import time
import msvcrt
import pdb
import os
from datetime import datetime, date

# Hace que Python trabaje siempre desde la carpeta del programa
RUTA_PROYECTO = os.path.dirname(os.path.abspath(__file__))
os.chdir(RUTA_PROYECTO)

# CONFIGURACION GENERAL
# Archivos base utilizados para conservar la información.
archivos = {
    "usuarios": "usuarios.txt",
    "entradas": "entradas.txt",
    "salidas": "salidas.txt",
    "ocupacion": "ocupacion.txt"
}
DEBUG = False  # True activa PDB.
TIEMPO_INACTIVIDAD = 600  # 600 segundos = 10 minutos.

# FUNCIONES AUXILIARES
def formato_fecha(Fecha):
    # Convierte la tupla Fecha a dd/mm/aaaa.
    return f"{Fecha[0]:02d}/{Fecha[1]:02d}/{Fecha[2]}"

def validar_archivos_base():
    # Verifica que existan los cuatro archivos requeridos.
    faltantes = []
    for nombre_archivo in archivos.values():
        if not os.path.exists(nombre_archivo):
            faltantes.append(nombre_archivo)
    if faltantes:
        print("\nAdvertencia: faltan los siguientes archivos:")
        for nombre_archivo in faltantes:
            print("-", nombre_archivo)
        print("Algunas funciones pueden no estar disponibles.")
    else:
        print("\nArchivos base verificados correctamente.")

def actualizar_archivos():
    # Agrega al diccionario otros .txt creados en la carpeta.
    try:
        for nombre_archivo in os.listdir("."):
            if nombre_archivo.lower().endswith(".txt"):
                archivos[nombre_archivo[:-4].lower()] = nombre_archivo
    except OSError as error:
        print(f"Error al consultar los archivos: {error}")

def leer_lineas(nombre_archivo):
    # Lee un archivo y devuelve sus líneas.
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            return archivo.readlines()
    except FileNotFoundError:
        print(f"Error: No se encontró {nombre_archivo}.")
    except PermissionError:
        print(f"Error: No tienes permisos para leer {nombre_archivo}.")
    except OSError as error:
        print(f"Error al leer el archivo: {error}")
    return None

def anexar_registro(nombre_archivo, texto, Fecha):
    # El modo "a" conserva la información anterior.
    try:
        if not os.path.exists(nombre_archivo):
            raise FileNotFoundError
        with open(nombre_archivo, "a", encoding="utf-8") as archivo:
            archivo.write(f"Fecha: {formato_fecha(Fecha)} | {texto}\n")
        return True
    except FileNotFoundError:
        print(f"Error: No se encontró {nombre_archivo}.")
    except PermissionError:
        print(f"Error: No tienes permisos para modificar {nombre_archivo}.")
    except OSError as error:
        print(f"Error al guardar la información: {error}")
    return False

# 1. IDENTIFICACION DEL USUARIO
def solicitar_usuario():
    # No permite nombres o nicknames vacíos.
    while True:
        nombre = input("\nIngresa tu nombre o nickname: ").strip()
        if nombre:
            return nombre
        print("Error: Debes ingresar un nombre o nickname.")

# 2. BIENVENIDA DINAMICA
def mostrar_bienvenida(nombre_usuario):
    print("==========================================")
    print(" CONTROL DE OCUPACION DEL GIMNASIO")
    print("          UNIVERSITARIO")
    print("==========================================")
    print(f"\n¡Hola {nombre_usuario}! ¡BIENVENIDO AL SISTEMA DE CONTROL")
    print("DE OCUPACIÓN DEL GIMNASIO UNIVERSITARIO!\n")

# 3. PANTALLA DE CARGA
def pantalla_de_carga():
    # Simula una carga de cinco segundos.
    print("Cargando sistema", end="", flush=True)
    for i in range(5):
        time.sleep(1)
        print(".", end="", flush=True)
    print("\nSistema cargado correctamente.")

# 4. MENU COMO MATRIZ
# Cada fila contiene una opción y su descripción.
menu = [
    ["1", "Registrar usuario"],
    ["2", "Registrar entrada"],
    ["3", "Registrar salida"],
    ["4", "Consultar ocupacion"],
    ["5", "Leer archivo"],
    ["6", "Crear archivo"],
    ["7", "Escribir o anexar datos"],
    ["8", "Salir"]
]

def mostrar_menu():
    print("\n==========================================")
    print("              MENU PRINCIPAL")
    print("==========================================")
    for fila in menu:
        print(f"| {fila[0]} | {fila[1]}")
    print("==========================================")

# 5. CONTROL DE INACTIVIDAD
def controlar_inactividad():
    # Cada interacción reinicia el conteo de 10 minutos.
    print("Selecciona una opción: ", end="", flush=True)
    opcion = ""

    while True:
        hubo_actividad = False

        for segundo in range(TIEMPO_INACTIVIDAD):
            if msvcrt.kbhit():
                hubo_actividad = True

                while msvcrt.kbhit():
                    tecla = msvcrt.getwch()

                    if tecla == "\r":
                        print()
                        return opcion.strip()

                    elif tecla == "\b":
                        if opcion:
                            opcion = opcion[:-1]
                            print("\b \b", end="", flush=True)

                    elif tecla in ("\x00", "\xe0"):
                        if msvcrt.kbhit():
                            msvcrt.getwch()

                    else:
                        opcion += tecla
                        print(tecla, end="", flush=True)

                break

            time.sleep(1)

        if not hubo_actividad:
            print("\nHan transcurrido 10 minutos sin actividad.")
            return None

def preguntar_continuidad():
    # Después de la inactividad solo acepta si o no.
    while True:
        respuesta = input("¿Deseas continuar en el menú? Escribe si o no: ").strip().lower()

        if respuesta == "si":
            return True
        if respuesta == "no":
            return False

        print("Respuesta no válida. Escribe solamente si o no.")

# 6. CAPTURA Y VALIDACION DE FECHA
def capturar_fecha():
    # La fecha debe existir, estar en el periodo permitido y no ser futura.
    while True:
        try:
            texto = input("Ingresa la fecha de operación (dd/mm/aaaa): ").strip()
            fecha = datetime.strptime(texto, "%d/%m/%Y").date()
            fecha_inicio = date(2026, 1, 1)
            fecha_actual = date.today()

            if fecha < fecha_inicio:
                print("Error: La fecha es anterior al inicio de operaciones.")
                continue

            if fecha > fecha_actual:
                print("Error: No se permiten fechas futuras.")
                continue

            Fecha = (fecha.day, fecha.month, fecha.year)  # Tupla obligatoria.
            return Fecha

        except ValueError:
            print("Error: Ingresa una fecha válida en formato dd/mm/aaaa.")

# REGLAS DE NEGOCIO DEL GIMNASIO
def usuario_registrado(nombre):
    # Compara nombres completos para no confundir Ana con Ana Maria.
    lineas = leer_lineas("usuarios.txt")

    if lineas is None:
        return False

    for linea in lineas:
        if "Usuario: " in linea:
            usuario_archivo = linea.split("Usuario: ", 1)[1].strip()

            if usuario_archivo.lower() == nombre.lower():
                return True

    return False

def usuario_dentro(nombre):
    # Comprueba si el usuario tiene una entrada activa.
    entradas = leer_lineas("entradas.txt")
    salidas = leer_lineas("salidas.txt")

    if entradas is None or salidas is None:
        return None

    total_entradas = 0
    total_salidas = 0

    for linea in entradas:
        if "Entrada: " in linea:
            usuario = linea.split("Entrada: ", 1)[1].strip()

            if usuario.lower() == nombre.lower():
                total_entradas += 1

    for linea in salidas:
        if "Salida: " in linea:
            usuario = linea.split("Salida: ", 1)[1].strip()

            if usuario.lower() == nombre.lower():
                total_salidas += 1

    return total_entradas > total_salidas

# REGISTRAR USUARIO
def registrar_usuario(Fecha):
    # Evita campos vacíos y usuarios duplicados.
    print("\n---------- REGISTRAR USUARIO ----------")
    nombre = input("Ingresa el nombre del usuario: ").strip().title()

    if not nombre:
        print("Error: El nombre no puede estar vacío.")
        return

    if usuario_registrado(nombre):
        print("Error: El usuario ya se encuentra registrado.")
        return

    if DEBUG:
        pdb.set_trace()

    if anexar_registro("usuarios.txt", f"Usuario: {nombre}", Fecha):
        print(f"Usuario {nombre} registrado correctamente.")

# REGISTRAR ENTRADA
def registrar_entrada(Fecha):
    # Solo permite entrar a usuarios registrados sin entrada activa.
    print("\n---------- REGISTRAR ENTRADA ----------")
    nombre = input("Ingresa el nombre del usuario: ").strip().title()

    if not nombre:
        print("Error: El nombre no puede estar vacío.")
        return

    if not usuario_registrado(nombre):
        print("Error: El usuario debe registrarse antes de ingresar.")
        return

    dentro = usuario_dentro(nombre)

    if DEBUG:
        pdb.set_trace()

    if dentro is None:
        return

    if dentro:
        print("Error: El usuario ya tiene una entrada activa.")
        return

    if anexar_registro("entradas.txt", f"Entrada: {nombre}", Fecha):
        print(f"Entrada de {nombre} registrada correctamente.")

# REGISTRAR SALIDA
def registrar_salida(Fecha):
    # Solo permite salir si existe una entrada activa.
    print("\n---------- REGISTRAR SALIDA ----------")
    nombre = input("Ingresa el nombre del usuario: ").strip().title()

    if not nombre:
        print("Error: El nombre no puede estar vacío.")
        return

    if not usuario_registrado(nombre):
        print("Error: El usuario no se encuentra registrado.")
        return

    dentro = usuario_dentro(nombre)

    if dentro is None:
        return

    if not dentro:
        print("Error: El usuario no tiene una entrada activa.")
        return

    if anexar_registro("salidas.txt", f"Salida: {nombre}", Fecha):
        print(f"Salida de {nombre} registrada correctamente.")

# CONSULTAR OCUPACION
def consultar_ocupacion(Fecha):
    # Resta salidas a entradas de la fecha seleccionada.
    print("\n---------- CONSULTAR OCUPACION ----------")
    fecha = formato_fecha(Fecha)
    entradas = leer_lineas("entradas.txt")
    salidas = leer_lineas("salidas.txt")

    if entradas is None or salidas is None:
        return

    total_entradas = 0
    total_salidas = 0

    for linea in entradas:
        if fecha in linea:
            total_entradas += 1

    for linea in salidas:
        if fecha in linea:
            total_salidas += 1

    ocupacion = total_entradas - total_salidas

    if ocupacion < 0:
        ocupacion = 0

    print(f"Fecha: {fecha}")
    print(f"Entradas: {total_entradas}")
    print(f"Salidas: {total_salidas}")
    print(f"Ocupación actual: {ocupacion} personas")

    # Guarda un historial de las consultas.
    anexar_registro("ocupacion.txt", f"Ocupación: {ocupacion} personas", Fecha)

# 7. PERSISTENCIA: LEER ARCHIVOS
def leer_archivo():
    # Permite consultar cualquier archivo reconocido por el sistema.
    actualizar_archivos()
    print("\n---------- ARCHIVOS DISPONIBLES ----------")

    for nombre, archivo in archivos.items():
        print(f"{nombre} -> {archivo}")

    nombre = input("\nEscribe el nombre del archivo que deseas abrir: ").strip().lower()

    if nombre not in archivos:
        print("Error: El archivo seleccionado no existe.")
        return

    try:
        with open(archivos[nombre], "r", encoding="utf-8") as archivo:
            contenido = archivo.read()

        print("\n---------- CONTENIDO ----------")
        print(contenido if contenido else "El archivo está vacío.")

    except FileNotFoundError:
        print("Error: El archivo no fue encontrado.")

    except PermissionError:
        print("Error: No tienes permisos para abrir este archivo.")

    except OSError as error:
        print(f"Error al leer el archivo: {error}")

# PERSISTENCIA: CREAR ARCHIVO
def crear_archivo(Fecha):
    # Crea un .txt nuevo sin sobrescribir archivos existentes.
    print("\n---------- CREAR ARCHIVO ----------")
    nombre = input("Ingresa el nombre del nuevo archivo: ").strip().lower()

    if not nombre:
        print("Error: El nombre no puede estar vacío.")
        return

    caracteres_invalidos = '\\/:*?"<>|'

    if any(caracter in nombre for caracter in caracteres_invalidos):
        print("Error: El nombre contiene caracteres no permitidos.")
        return

    if not nombre.endswith(".txt"):
        nombre += ".txt"

    try:
        with open(nombre, "x", encoding="utf-8") as archivo:
            archivo.write(f"Archivo creado el {formato_fecha(Fecha)}\n")

        archivos[nombre[:-4]] = nombre
        print(f"Archivo {nombre} creado correctamente.")

    except FileExistsError:
        print("Error: Ya existe un archivo con ese nombre.")

    except PermissionError:
        print("Error: No tienes permisos para crear el archivo.")

    except OSError as error:
        print(f"Error al crear el archivo: {error}")

# PERSISTENCIA: ESCRIBIR O ANEXAR
def escribir_archivo(Fecha):
    # Anexa información al archivo elegido e incorpora la fecha.
    actualizar_archivos()
    print("\n---------- ARCHIVOS DISPONIBLES ----------")

    for nombre, archivo in archivos.items():
        print(f"{nombre} -> {archivo}")

    nombre = input("\nEscribe el nombre del archivo que deseas modificar: ").strip().lower()

    if nombre not in archivos:
        print("Error: Archivo no válido.")
        return

    texto = input("Ingresa la información que deseas guardar: ").strip()

    if not texto:
        print("Error: No puedes guardar información vacía.")
        return

    if DEBUG:
        pdb.set_trace()

    if anexar_registro(archivos[nombre], texto, Fecha):
        print("Información guardada correctamente.")

# 8. CONTROL DE EXCEPCIONES
# Los try-except impiden que errores de persistencia cierren el programa.
# Se manejan FileNotFoundError, FileExistsError, PermissionError y OSError.

# 9. DEBUGGING CON PDB
# DEBUG = True activa pdb.set_trace() para revisar Fecha, opcion, nombre y dentro.
# Las fallas localizadas y sus correcciones se documentan en el reporte final.

# INICIO DEL PROGRAMA
validar_archivos_base()
salir_sistema = False

while not salir_sistema:
    # Identificación, bienvenida y carga.
    nombre_usuario = solicitar_usuario()
    mostrar_bienvenida(nombre_usuario)
    pantalla_de_carga()

    # Fecha que se integrará a los registros.
    Fecha = capturar_fecha()
    print(f"Fecha de operación: {formato_fecha(Fecha)}")

    if DEBUG:
        pdb.set_trace()

    regresar_inicio = False

    while not regresar_inicio and not salir_sistema:
        mostrar_menu()
        opcion = controlar_inactividad()

        # Tras 10 minutos sin actividad pregunta si desea continuar.
        if opcion is None:
            continuar = preguntar_continuidad()

            if continuar:
                continue

            print("Regresando a la pantalla de inicio...")
            regresar_inicio = True
            continue

        if DEBUG:
            pdb.set_trace()

        if opcion == "1":
            registrar_usuario(Fecha)
        elif opcion == "2":
            registrar_entrada(Fecha)
        elif opcion == "3":
            registrar_salida(Fecha)
        elif opcion == "4":
            consultar_ocupacion(Fecha)
        elif opcion == "5":
            leer_archivo()
        elif opcion == "6":
            crear_archivo(Fecha)
        elif opcion == "7":
            escribir_archivo(Fecha)
        elif opcion == "8":
            print("\nHas seleccionado: Cerrar sistema")
            salir_sistema = True
        else:
            print("Opción inválida. Elige una opción del 1 al 8.")

print("Sistema cerrado correctamente.")