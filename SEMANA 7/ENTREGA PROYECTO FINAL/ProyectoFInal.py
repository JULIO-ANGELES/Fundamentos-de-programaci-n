#Entrega Final del proyecto| Fundamentos de programación| Julio César Ángeles Mendoza|22/09/2026 (IDS)


# Entrega Final del Proyecto - Fundamentos de Programación
# Sistema de Control de Ocupación del Gimnasio Universitario

import time
import re
import pdb
import os
import sys
from datetime import datetime, date


# =========================================================
# COMPATIBILIDAD WINDOWS / LINUX / MAC
# =========================================================



# =========================================================
# RUTA DEL PROYECTO
# =========================================================

RUTA_PROYECTO = os.path.dirname(os.path.abspath(__file__))
os.chdir(RUTA_PROYECTO)
print("Carpeta usada por el programa:", os.getcwd())
print("Archivo usuarios:", os.path.abspath("usuarios.txt"))

# =========================================================
# CONFIGURACION GENERAL
# =========================================================

archivos = {
    "usuarios": "usuarios.txt",
    "entradas": "entradas.txt",
    "salidas": "salidas.txt",
    "ocupacion": "ocupacion.txt"
}

DEBUG = False

# 600 segundos = 10 minutos
TIEMPO_INACTIVIDAD = 600


# =========================================================
# FUNCIONES AUXILIARES
# =========================================================

def formato_fecha(Fecha):
    return f"{Fecha[0]:02d}/{Fecha[1]:02d}/{Fecha[2]}"


def validar_archivos_base():
    faltantes = []

    for archivo in archivos.values():
        if not os.path.exists(archivo):
            faltantes.append(archivo)

    if faltantes:
        print("\nAdvertencia: faltan los siguientes archivos:")

        for archivo in faltantes:
            print("-", archivo)

        print("Algunas funciones pueden no estar disponibles.")

    else:
        print("\nArchivos base verificados correctamente.")


def actualizar_archivos():
    try:
        for nombre in os.listdir("."):

            if nombre.lower().endswith(".txt"):
                archivos[nombre[:-4].lower()] = nombre

    except OSError as error:
        print(f"Error al consultar los archivos: {error}")


def leer_lineas(nombre_archivo):
    try:
        with open(
            nombre_archivo,
            "r",
            encoding="utf-8"
        ) as archivo:

            return archivo.readlines()

    except FileNotFoundError:
        print(f"Error: No se encontró {nombre_archivo}.")

    except PermissionError:
        print(
            f"Error: No tienes permisos para leer {nombre_archivo}."
        )

    except OSError as error:
        print(f"Error al leer el archivo: {error}")

    return None


def anexar_registro(nombre_archivo, texto, Fecha):
    try:

        if not os.path.exists(nombre_archivo):
            raise FileNotFoundError

        with open(
            nombre_archivo,
            "a",
            encoding="utf-8"
        ) as archivo:

            archivo.write(
                f"Fecha: {formato_fecha(Fecha)} | {texto}\n"
            )

        return True

    except FileNotFoundError:
        print(f"Error: No se encontró {nombre_archivo}.")

    except PermissionError:
        print(
            f"Error: No tienes permisos para modificar {nombre_archivo}."
        )

    except OSError as error:
        print(f"Error al guardar la información: {error}")

    return False


# =========================================================
# IDENTIFICACION DEL USUARIO
# =========================================================

def solicitar_usuario():
    while True:

        nombre = input(
            "\nIngresa tu nombre o nickname: "
        ).strip()

        if nombre:
            return nombre

        print(
            "Error: Debes ingresar un nombre o nickname."
        )


# =========================================================
# BIENVENIDA
# =========================================================

def mostrar_bienvenida(nombre):
    print("==========================================")
    print(" CONTROL DE OCUPACION DEL GIMNASIO")
    print("          UNIVERSITARIO")
    print("==========================================")

    print(
        f"\n¡Hola {nombre}! "
        "¡BIENVENIDO AL SISTEMA DE CONTROL"
    )

    print(
        "DE OCUPACIÓN DEL GIMNASIO UNIVERSITARIO!\n"
    )


# =========================================================
# PANTALLA DE CARGA
# =========================================================

def pantalla_de_carga():
    print(
        "Cargando sistema",
        end="",
        flush=True
    )

    for _ in range(5):

        time.sleep(1)

        print(
            ".",
            end="",
            flush=True
        )

    print("\nSistema cargado correctamente.")


# =========================================================
# MENU
# =========================================================

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

    for opcion, descripcion in menu:
        print(f"| {opcion} | {descripcion}")

    print("==========================================")


# =========================================================
# CONTROL DE INACTIVIDAD WINDOWS
# =========================================================

def inactividad_windows():

    import msvcrt

    print(
        "Selecciona una opción: ",
        end="",
        flush=True
    )

    opcion = ""
    ultima_actividad = time.time()

    while True:

        if time.time() - ultima_actividad >= TIEMPO_INACTIVIDAD:
            print("\nHan transcurrido 10 minutos sin actividad.")
            return None

        if msvcrt.kbhit():

            tecla = msvcrt.getwch()
            ultima_actividad = time.time()

            if tecla == "\r":
                print()
                return opcion.strip()

            if tecla == "\b":

                if opcion:
                    opcion = opcion[:-1]
                    print("\b \b", end="", flush=True)

                continue

            if tecla in ("\x00", "\xe0"):

                if msvcrt.kbhit():
                    msvcrt.getwch()

                continue

            opcion += tecla
            print(tecla, end="", flush=True)

        time.sleep(0.05)
    


# =========================================================
# CONTROL DE INACTIVIDAD LINUX / MAC
# =========================================================

def inactividad_unix():
    import select
    import termios
    import tty

    print(
        "Selecciona una opción: ",
        end="",
        flush=True
    )

    opcion = ""

    descriptor = sys.stdin.fileno()
    configuracion_original = termios.tcgetattr(descriptor)

    try:

        tty.setcbreak(descriptor)
        ultima_actividad = time.time()

        while True:

            restante = (
                TIEMPO_INACTIVIDAD
                - (time.time() - ultima_actividad)
            )

            if restante <= 0:
                print("\nHan transcurrido 10 minutos sin actividad.")
                return None

            disponibles, _, _ = select.select(
                [sys.stdin],
                [],
                [],
                min(1, restante)
            )

            if not disponibles:
                continue

            tecla = sys.stdin.read(1)
            ultima_actividad = time.time()

            if tecla in ("\n", "\r"):
                print()
                return opcion.strip()

            if tecla in ("\x7f", "\b"):

                if opcion:
                    opcion = opcion[:-1]
                    print("\b \b", end="", flush=True)

                continue

            if tecla == "\x1b":

                while select.select(
                    [sys.stdin],
                    [],
                    [],
                    0
                )[0]:

                    sys.stdin.read(1)

                continue

            opcion += tecla
            print(tecla, end="", flush=True)

    finally:

        termios.tcsetattr(
            descriptor,
            termios.TCSADRAIN,
            configuracion_original
        )
        


def controlar_inactividad():

    if os.name == "nt":
        return inactividad_windows()

    return inactividad_unix()


def preguntar_continuidad():

    while True:

        respuesta = input(
            "¿Deseas continuar en el menú? "
            "Escribe si o no: "
        ).strip().lower()

        if respuesta == "si":
            return True

        if respuesta == "no":
            return False

        print(
            "Respuesta no válida. "
            "Escribe solamente si o no."
        )


# =========================================================
# CAPTURA Y VALIDACION DE FECHA
# =========================================================

def capturar_fecha():

    while True:

        try:

            texto = input(
                "Ingresa la fecha de operación "
                "(dd/mm/aaaa): "
            ).strip()

            fecha = datetime.strptime(
                texto,
                "%d/%m/%Y"
            ).date()

            fecha_inicio = date(
                2026,
                1,
                1
            )

            fecha_actual = date.today()

            if fecha < fecha_inicio:

                print(
                    "Error: La fecha es anterior "
                    "al inicio de operaciones."
                )

                continue

            if fecha > fecha_actual:

                print(
                    "Error: No se permiten fechas futuras."
                )

                continue

            return (
                fecha.day,
                fecha.month,
                fecha.year
            )

        except ValueError:

            print(
                "Error: Ingresa una fecha válida "
                "en formato dd/mm/aaaa."
            )


# =========================================================
# VALIDACION DEL NOMBRE
# =========================================================

def nombre_valido(nombre):

    # Mínimo dos caracteres
    if len(nombre) < 2:
        return False

    # Solo letras, espacios, guiones y apóstrofes
    patron = r"[A-Za-zÁÉÍÓÚáéíóúÑñÜü' -]+"

    return re.fullmatch(
        patron,
        nombre
    ) is not None


# =========================================================
# COMPROBAR SI EL USUARIO ESTA REGISTRADO
# =========================================================

def usuario_registrado(nombre):

    lineas = leer_lineas(
        "usuarios.txt"
    )

    if lineas is None:
        return False

    for linea in lineas:

        if "Usuario: " in linea:

            usuario = linea.split(
                "Usuario: ",
                1
            )[1].strip()

            if usuario.lower() == nombre.lower():
                return True

    return False


# =========================================================
# COMPROBAR SI EL USUARIO ESTA DENTRO
# =========================================================

def usuario_dentro(nombre):

    entradas = leer_lineas(
        "entradas.txt"
    )

    salidas = leer_lineas(
        "salidas.txt"
    )

    if entradas is None or salidas is None:

        print(
            "Error: No fue posible leer "
            "entradas.txt o salidas.txt."
        )

        return None

    total_entradas = 0
    total_salidas = 0

    for linea in entradas:

        if "Entrada: " in linea:

            usuario = linea.split(
                "Entrada: ",
                1
            )[1].strip()

            if usuario.lower() == nombre.lower():
                total_entradas += 1

    for linea in salidas:

        if "Salida: " in linea:

            usuario = linea.split(
                "Salida: ",
                1
            )[1].strip()

            if usuario.lower() == nombre.lower():
                total_salidas += 1

    return total_entradas > total_salidas


# =========================================================
# REGISTRAR USUARIO
# =========================================================

def registrar_usuario(Fecha):

    print(
        "\n---------- REGISTRAR USUARIO ----------"
    )

    nombre = input(
        "Ingresa el nombre del usuario: "
    ).strip().title()

    if not nombre:

        print(
            "Error: El nombre no puede estar vacío."
        )

        return

    if not nombre_valido(nombre):

        print(
            "Error: El nombre solo puede contener letras, "
            "espacios, guiones o apóstrofes."
        )

        return

    if usuario_registrado(nombre):

        print(
            "Error: El usuario ya se encuentra registrado."
        )

        return

    if DEBUG:
        pdb.set_trace()

    if anexar_registro(
        "usuarios.txt",
        f"Usuario: {nombre}",
        Fecha
    ):

        print(
            f"Usuario {nombre} registrado correctamente."
        )

    else:

        print(
            "Error: No fue posible registrar al usuario."
        )


# =========================================================
# REGISTRAR ENTRADA
# =========================================================

def registrar_entrada(Fecha):

    print(
        "\n---------- REGISTRAR ENTRADA ----------"
    )

    nombre = input(
        "Ingresa el nombre del usuario: "
    ).strip().title()

    if not nombre:

        print(
            "Error: El nombre no puede estar vacío."
        )

        return

    if not nombre_valido(nombre):

        print(
            "Error: El nombre solo puede contener letras, "
            "espacios, guiones o apóstrofes."
        )

        return

    if not usuario_registrado(nombre):

        print(
            "Error: El usuario debe registrarse "
            "antes de ingresar."
        )

        return

    dentro = usuario_dentro(nombre)

    if DEBUG:
        pdb.set_trace()

    if dentro is None:

        print(
            "Error: No fue posible comprobar "
            "si el usuario está dentro."
        )

        return

    if dentro:

        print(
            "Error: El usuario ya tiene una entrada activa."
        )

        return

    if anexar_registro(
        "entradas.txt",
        f"Entrada: {nombre}",
        Fecha
    ):

        print(
            f"Entrada de {nombre} registrada correctamente."
        )

    else:

        print(
            "Error: No fue posible registrar la entrada."
        )


# =========================================================
# REGISTRAR SALIDA
# =========================================================

def registrar_salida(Fecha):

    print(
        "\n---------- REGISTRAR SALIDA ----------"
    )

    nombre = input(
        "Ingresa el nombre del usuario: "
    ).strip().title()

    if not nombre:

        print(
            "Error: El nombre no puede estar vacío."
        )

        return

    if not nombre_valido(nombre):

        print(
            "Error: El nombre solo puede contener letras, "
            "espacios, guiones o apóstrofes."
        )

        return

    if not usuario_registrado(nombre):

        print(
            "Error: El usuario no se encuentra registrado."
        )

        return

    dentro = usuario_dentro(nombre)

    if dentro is None:

        print(
            "Error: No fue posible comprobar "
            "si el usuario está dentro."
        )

        return

    if not dentro:

        print(
            "Error: El usuario no tiene una entrada activa."
        )

        return

    if anexar_registro(
        "salidas.txt",
        f"Salida: {nombre}",
        Fecha
    ):

        print(
            f"Salida de {nombre} registrada correctamente."
        )

    else:

        print(
            "Error: No fue posible registrar la salida."
        )


# =========================================================
# CONSULTAR OCUPACION
# =========================================================

def consultar_ocupacion(Fecha):

    print(
        "\n---------- CONSULTAR OCUPACION ----------"
    )

    fecha = formato_fecha(Fecha)

    entradas = leer_lineas(
        "entradas.txt"
    )

    salidas = leer_lineas(
        "salidas.txt"
    )

    if entradas is None or salidas is None:
        return

    total_entradas = sum(
        1
        for linea in entradas
        if fecha in linea
    )

    total_salidas = sum(
        1
        for linea in salidas
        if fecha in linea
    )

    ocupacion = max(
        0,
        total_entradas - total_salidas
    )

    print(
        f"Fecha: {fecha}"
    )

    print(
        f"Entradas: {total_entradas}"
    )

    print(
        f"Salidas: {total_salidas}"
    )

    print(
        f"Ocupación actual: {ocupacion} personas"
    )

    anexar_registro(
        "ocupacion.txt",
        f"Ocupación: {ocupacion} personas",
        Fecha
    )


# =========================================================
# LEER ARCHIVO
# =========================================================

def leer_archivo():

    actualizar_archivos()

    print(
        "\n---------- ARCHIVOS DISPONIBLES ----------"
    )

    for nombre, archivo in archivos.items():

        print(
            f"{nombre} -> {archivo}"
        )

    nombre = input(
        "\nEscribe el nombre del archivo "
        "que deseas abrir: "
    ).strip().lower()

    if nombre not in archivos:

        print(
            "Error: El archivo seleccionado no existe."
        )

        return

    try:

        with open(
            archivos[nombre],
            "r",
            encoding="utf-8"
        ) as archivo:

            contenido = archivo.read()

        print(
            "\n---------- CONTENIDO ----------"
        )

        if contenido:

            print(contenido)

        else:

            print(
                "El archivo está vacío."
            )

    except FileNotFoundError:

        print(
            "Error: El archivo no fue encontrado."
        )

    except PermissionError:

        print(
            "Error: No tienes permisos "
            "para abrir este archivo."
        )

    except OSError as error:

        print(
            f"Error al leer el archivo: {error}"
        )


# =========================================================
# CREAR ARCHIVO
# =========================================================

def crear_archivo(Fecha):

    print(
        "\n---------- CREAR ARCHIVO ----------"
    )

    nombre = input(
        "Ingresa el nombre del nuevo archivo: "
    ).strip().lower()

    if not nombre:

        print(
            "Error: El nombre no puede estar vacío."
        )

        return

    caracteres_invalidos = '\\/:*?"<>|'

    if any(
        caracter in nombre
        for caracter in caracteres_invalidos
    ):

        print(
            "Error: El nombre contiene "
            "caracteres no permitidos."
        )

        return

    if not nombre.endswith(".txt"):
        nombre += ".txt"

    try:

        with open(
            nombre,
            "x",
            encoding="utf-8"
        ) as archivo:

            archivo.write(
                f"Archivo creado el "
                f"{formato_fecha(Fecha)}\n"
            )

        archivos[
            nombre[:-4]
        ] = nombre

        print(
            f"Archivo {nombre} creado correctamente."
        )

    except FileExistsError:

        print(
            "Error: Ya existe un archivo "
            "con ese nombre."
        )

    except PermissionError:

        print(
            "Error: No tienes permisos "
            "para crear el archivo."
        )

    except OSError as error:

        print(
            f"Error al crear el archivo: {error}"
        )


# =========================================================
# ESCRIBIR O ANEXAR DATOS
# =========================================================

def escribir_archivo(Fecha):

    actualizar_archivos()

    print(
        "\n---------- ARCHIVOS DISPONIBLES ----------"
    )

    for nombre, archivo in archivos.items():

        print(
            f"{nombre} -> {archivo}"
        )

    nombre = input(
        "\nEscribe el nombre del archivo "
        "que deseas modificar: "
    ).strip().lower()

    if nombre not in archivos:

        print(
            "Error: Archivo no válido."
        )

        return

    texto = input(
        "Ingresa la información "
        "que deseas guardar: "
    ).strip()

    if not texto:

        print(
            "Error: No puedes guardar "
            "información vacía."
        )

        return

    if DEBUG:
        pdb.set_trace()

    if anexar_registro(
        archivos[nombre],
        texto,
        Fecha
    ):

        print(
            "Información guardada correctamente."
        )


# =========================================================
# PROGRAMA PRINCIPAL
# =========================================================

def main():

    validar_archivos_base()

    salir_sistema = False

    while not salir_sistema:

        nombre_usuario = solicitar_usuario()

        mostrar_bienvenida(
            nombre_usuario
        )

        pantalla_de_carga()

        Fecha = capturar_fecha()

        print(
            f"Fecha de operación: "
            f"{formato_fecha(Fecha)}"
        )

        if DEBUG:
            pdb.set_trace()

        regresar_inicio = False

        while (
            not regresar_inicio
            and not salir_sistema
        ):

            mostrar_menu()

            opcion = controlar_inactividad()

            # Inactividad
            if opcion is None:

                continuar = preguntar_continuidad()

                if continuar:
                    continue

                print(
                    "Regresando a la pantalla de inicio..."
                )

                regresar_inicio = True

                continue

            if DEBUG:
                pdb.set_trace()

            # Opciones del menú
            if opcion == "1":

                registrar_usuario(
                    Fecha
                )

            elif opcion == "2":

                registrar_entrada(
                    Fecha
                )

            elif opcion == "3":

                registrar_salida(
                    Fecha
                )

            elif opcion == "4":

                consultar_ocupacion(
                    Fecha
                )

            elif opcion == "5":

                leer_archivo()

            elif opcion == "6":

                crear_archivo(
                    Fecha
                )

            elif opcion == "7":

                escribir_archivo(
                    Fecha
                )

            elif opcion == "8":

                print(
                    "\nHas seleccionado: Cerrar sistema"
                )

                salir_sistema = True

            else:

                print(
                    "Opción inválida. "
                    "Elige una opción del 1 al 8."
                )

    print(
        "Sistema cerrado correctamente."
    )


# =========================================================
# INICIO DEL PROGRAMA
# =========================================================

if __name__ == "__main__":
    main()