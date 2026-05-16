import os
import shutil
import tkinter as tk

def limpiar_temporales():
    temp = os.getenv('TEMP')
    shutil.rmtree(temp, ignore_errors=True)
    os.makedirs(temp, exist_ok=True)

def cerrar_procesos():
    procesos = ["chrome.exe", "discord.exe"]
    for p in procesos:
        os.system(f"taskkill /f /im {p}")

def optimizar():
    estado_label.config(text="Optimizando...", fg="#00ffcc")
    ventana.update()

    limpiar_temporales()
    cerrar_procesos()

    estado_label.config(text="✔ Listo para jugar 🚀", fg="#00ff00")

# Ventana principal
ventana = tk.Tk()
ventana.title("Game Booster")
ventana.geometry("400x300")
ventana.config(bg="#0f172a")  # fondo oscuro

# Título
titulo = tk.Label(
    ventana,
    text="GAME BOOSTER",
    font=("Arial", 18, "bold"),
    fg="#00ffcc",
    bg="#0f172a"
)
titulo.pack(pady=20)

# Botón estilo gamer
boton = tk.Button(
    ventana,
    text="OPTIMIZAR",
    command=optimizar,
    font=("Arial", 14, "bold"),
    bg="#00ffcc",
    fg="#000000",
    activebackground="#00ffaa",
    width=15,
    height=2,
    bd=0
)
boton.pack(pady=20)

# Estado
estado_label = tk.Label(
    ventana,
    text="Esperando...",
    font=("Arial", 12),
    fg="#94a3b8",
    bg="#0f172a"
)
estado_label.pack(pady=20)

ventana.mainloop()