import json
from datetime import datetime

ARCHIVO = "calendar.json"

def cargar_cumpleaños():
    try:
        with open(ARCHIVO, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def guardar_cumpleaños(cumpleaños):
    with open(ARCHIVO, "w") as file:
        json.dump(cumpleaños, file, indent=4)

def agregar_cumpleaños():
    nombre = input("Nombre de la persona: ").strip().title()
    fecha = input("Fecha de cumple (DD/MM/AAAA): ")
    try:
        datetime.strptime(fecha, "%d/%m/%Y")  # Validación de formato
        cumpleaños[nombre] = fecha
        guardar_cumpleaños(cumpleaños)
        print(f" Cumple de {nombre} guardado.\n")
    except ValueError:
        print(" Formato invalido. Usa DD/MM/AAAA.\n")

def ver_cumpleaños():
    if not cumpleaños:
        print(" No hay cumples registrados.\n")
    else:
        for nombre, fecha in cumpleaños.items():
            print(f" {nombre}: {fecha}")
        print()

def eliminar_cumpleaños():
    nombre = input("Nombre a eliminar: ").strip().title()
    if nombre in cumpleaños:
        del cumpleaños[nombre]
        guardar_cumpleaños(cumpleaños)
        print(f" Cumple de {nombre} eliminado.\n")
    else:
        print(" No se encontro ese nombre.\n")

def buscar_cumpleaños():
    nombre = input("Nombre a buscar: ").strip().title()
    if nombre in cumpleaños:
        print(f" {nombre} cumple el {cumpleaños[nombre]}\n")
    else:
        print(" No encontrado.\n")

def dias_restantes(fecha_str):
    cumple = datetime.strptime(fecha_str, "%d/%m/%Y")
    hoy = datetime.now()
    proximo = datetime(hoy.year, cumple.month, cumple.day)

    if proximo < hoy:
        proximo = datetime(hoy.year + 1, cumple.month, cumple.day)

    dias = (proximo - hoy).days
    return dias

def mostrar_dias_faltantes():
    if not cumpleaños:
        print(" No hay cumples registrados.\n")
        return

    for nombre, fecha in cumpleaños.items():
        dias = dias_restantes(fecha)
        print(f" Faltan {dias} dias para el cumple de {nombre}")
    print()

def menu():
    while True:
        print(" Menu de Calendario de Cumples")
        print("1. Ver cumples")
        print("2. Agregar cumples")
        print("3. Eliminar cumples")
        print("4. Buscar cumples")
        print("5. Ver cuantos dias faltan")
        print("6. Salir")
        opcion = input("Elige una opcion (1-6): ")

        if opcion == "1":
            ver_cumpleaños()
        elif opcion == "2":
            agregar_cumpleaños()
        elif opcion == "3":
            eliminar_cumpleaños()
        elif opcion == "4":
            buscar_cumpleaños()
        elif opcion == "5":
            mostrar_dias_faltantes()
        elif opcion == "6":
            print(" Saliendo...")
            break
        else:
            print(" Opción inválida.\n")

# Cargar cumpleaños al iniciar
cumpleaños = cargar_cumpleaños()
menu()
