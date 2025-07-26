import json
from datetime import datetime
import tkinter as tk
from tkinter import messagebox, simpledialog

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

def dias_restantes(fecha_str):
    cumple = datetime.strptime(fecha_str, "%d/%m/%Y")
    hoy = datetime.now()
    proximo = datetime(hoy.year, cumple.month, cumple.day)
    if proximo < hoy:
        proximo = datetime(hoy.year + 1, cumple.month, cumple.day)
    return (proximo - hoy).days

# ---------- Funciones para la interfaz ----------
def ver_cumpleaños():
    if not cumpleaños:
        messagebox.showinfo("Cumpleaños", "No hay cumpleaños registrados.")
    else:
        lista = "\n".join(f"{n}: {f}" for n, f in sorted(cumpleaños.items()))
        messagebox.showinfo("Lista de cumpleaños", lista)

def agregar_cumpleaños():
    nombre = simpledialog.askstring("Agregar", "Nombre de la persona:").strip().title()
    if not nombre:
        messagebox.showwarning("Error", "El nombre no puede estar vacío.")
        return

    fecha = simpledialog.askstring("Agregar", "Fecha (DD/MM/AAAA):").strip()
    try:
        fecha_dt = datetime.strptime(fecha, "%d/%m/%Y")
        if fecha_dt > datetime.now():
            messagebox.showwarning("Error", "La fecha no puede ser futura.")
            return
    except ValueError:
        messagebox.showwarning("Error", "Formato inválido. Usa DD/MM/AAAA.")
        return

    if nombre in cumpleaños:
        if not messagebox.askyesno("Confirmar", f"{nombre} ya existe. ¿Deseas sobrescribirlo?"):
            return

    cumpleaños[nombre] = fecha
    guardar_cumpleaños(cumpleaños)
    messagebox.showinfo("Éxito", f"Cumpleaños de {nombre} guardado.")

def eliminar_cumpleaños():
    nombre = simpledialog.askstring("Eliminar", "Nombre a eliminar:").strip().title()
    if nombre in cumpleaños:
        del cumpleaños[nombre]
        guardar_cumpleaños(cumpleaños)
        messagebox.showinfo("Eliminado", f"Cumpleaños de {nombre} eliminado.")
    else:
        messagebox.showwarning("No encontrado", f"No se encontró {nombre}.")

def buscar_cumpleaños():
    nombre = simpledialog.askstring("Buscar", "Nombre a buscar:").strip().title()
    if nombre in cumpleaños:
        messagebox.showinfo("Resultado", f"{nombre} cumple el {cumpleaños[nombre]}")
    else:
        messagebox.showwarning("No encontrado", f"{nombre} no está registrado.")

def mostrar_dias_faltantes():
    if not cumpleaños:
        messagebox.showinfo("Cumpleaños", "No hay cumpleaños registrados.")
        return

    resultado = ""
    for nombre, fecha in cumpleaños.items():
        try:
            dias = dias_restantes(fecha)
            resultado += f"Faltan {dias} días para el cumpleaños de {nombre}\n"
        except ValueError:
            resultado += f"Fecha inválida para {nombre}: {fecha}\n"
    messagebox.showinfo("Días restantes", resultado.strip())

# ---------- Ventana principal ----------
cumpleaños = cargar_cumpleaños()

ventana = tk.Tk()
ventana.title("Gestor de Cumpleaños")
ventana.geometry("300x320")
ventana.resizable(False, False)

tk.Label(ventana, text="Menú de Cumpleaños", font=("Arial", 14)).pack(pady=10)

tk.Button(ventana, text="Ver cumpleaños", width=25, command=ver_cumpleaños).pack(pady=5)
tk.Button(ventana, text="Agregar cumpleaños", width=25, command=agregar_cumpleaños).pack(pady=5)
tk.Button(ventana, text="Eliminar cumpleaños", width=25, command=eliminar_cumpleaños).pack(pady=5)
tk.Button(ventana, text="Buscar cumpleaños", width=25, command=buscar_cumpleaños).pack(pady=5)
tk.Button(ventana, text="Ver días faltantes", width=25, command=mostrar_dias_faltantes).pack(pady=5)
tk.Button(ventana, text="Salir", width=25, command=ventana.quit).pack(pady=20)

ventana.mainloop()
