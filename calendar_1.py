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

def agregar_cumpleaños(cumpleaños):
    nombre = input("Nombre de la persona: ").strip().title()
    if not nombre:
        print(" El nombre no puede estar vacío.\n")
        return cumpleaños

    fecha = input("Fecha de cumpleaños (DD/MM/AAAA): ").strip()
    try:
        fecha_dt = datetime.strptime(fecha, "%d/%m/%Y")
        if fecha_dt > datetime.now():
            print(" La fecha no puede ser futura.\n")
            return cumpleaños
    except ValueError:
        print(" Formato inválido. Usa DD/MM/AAAA.\n")
        return cumpleaños

    if nombre in cumpleaños:
        confirm = input(f"{nombre} ya existe. ¿Deseas sobrescribirlo? (s/n): ").lower()
        if confirm != "s":
            return cumpleaños

    cumpleaños[nombre] = fecha
    guardar_cumpleaños(cumpleaños)
    print(f" Cumpleaños de {nombre} guardado.\n")
    return cumpleaños

def ver_cumpleaños(cumpleaños):
    if not cumpleaños:
        print(" No hay cumpleaños registrados.\n")
    else:
        print("\n Lista de cumpleaños:")
        for nombre in sorted(cumpleaños):
            print(f" {nombre}: {cumpleaños[nombre]}")
        print()

def eliminar_cumpleaños(cumpleaños):
    nombre = input("Nombre a eliminar: ").strip().title()
    if nombre in cumpleaños:
        del cumpleaños[nombre]
        guardar_cumpleaños(cumpleaños)
        print(f" Cumpleaños de {nombre} eliminado.\n")
    else:
        print(" No se encontró ese nombre.\n")
    return cumpleaños

def buscar_cumpleaños(cumpleaños):
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

def mostrar_dias_faltantes(cumpleaños):
    if not cumpleaños:
        print(" No hay cumpleaños registrados.\n")
        return

    print("\n Días restantes para cada cumpleaños:")
    for nombre, fecha in cumpleaños.items():
        try:
            dias = dias_restantes(fecha)
            print(f" Faltan {dias} días para el cumpleaños de {nombre}")
        except ValueError:
            print(f" Fecha inválida para {nombre}: {fecha}")
    print()

def main():
    cumpleaños = cargar_cumpleaños()

    while True:
        print("------------ Menú de Cumpleaños ------------")
        print("1. Ver cumpleaños")
        print("2. Agregar cumpleaños")
        print("3. Eliminar cumpleaños")
        print("4. Buscar cumpleaños")
        print("5. Ver cuántos días faltan")
        print("6. Salir")
        opcion = input("Elige una opción (1-6): ").strip()

        if opcion == "1":
            ver_cumpleaños(cumpleaños)
        elif opcion == "2":
            cumpleaños = agregar_cumpleaños(cumpleaños)
        elif opcion == "3":
            cumpleaños = eliminar_cumpleaños(cumpleaños)
        elif opcion == "4":
            buscar_cumpleaños(cumpleaños)
        elif opcion == "5":
            mostrar_dias_faltantes(cumpleaños)
        elif opcion == "6":
            print(" ¡Hasta luego!\n")
            break
        else:
            print(" Opción inválida. Intenta de nuevo.\n")

if __name__ == "__main__":
    main()
