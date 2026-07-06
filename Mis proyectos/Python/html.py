import tkinter as tk
from tkinter import filedialog
import webbrowser
import os

# --- Funciones ---

def nuevo_archivo():
    texto.delete("1.0", tk.END)

def abrir_archivo():
    archivo = filedialog.askopenfilename(
        filetypes=[("Archivos HTML", "*.html"), ("Todos los archivos", "*.*")]
    )
    if archivo:
        with open(archivo, "r", encoding="utf-8") as f:
            texto.delete("1.0", tk.END)
            texto.insert(tk.END, f.read())

def guardar_archivo():
    archivo = filedialog.asksaveasfilename(
        defaultextension=".html",
        filetypes=[("Archivos HTML", "*.html")]
    )
    if archivo:
        with open(archivo, "w", encoding="utf-8") as f:
            f.write(texto.get("1.0", tk.END))

def previsualizar():
    archivo = "preview.html"
    with open(archivo, "w", encoding="utf-8") as f:
        f.write(texto.get("1.0", tk.END))
    webbrowser.open("file://" + os.path.abspath(archivo))


# --- Interfaz ---
ventana = tk.Tk()
ventana.title("Editor HTML en Python")
ventana.geometry("800x600")

texto = tk.Text(ventana, wrap="word", font=("Consolas", 12))
texto.pack(expand=True, fill="both")

# --- Menú ---
menu = tk.Menu(ventana)
ventana.config(menu=menu)

archivo_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Archivo", menu=archivo_menu)

archivo_menu.add_command(label="Nuevo", command=nuevo_archivo)
archivo_menu.add_command(label="Abrir", command=abrir_archivo)
archivo_menu.add_command(label="Guardar", command=guardar_archivo)
archivo_menu.add_separator()
archivo_menu.add_command(label="Salir", command=ventana.quit)

menu.add_command(label="Previsualizar", command=previsualizar)

ventana.mainloop()