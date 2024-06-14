import tkinter as tk
from tkinter import PhotoImage

# Función para actualizar el contador de una marca específica
def contar_envase(marca):
    if marca == "Coca-Cola":
        global contador_coca_cola
        contador_coca_cola += 1
        label_coca_cola.config(text=f"Coca-Cola: {contador_coca_cola}")
    elif marca == "Pepsi":
        global contador_pepsi
        contador_pepsi += 1
        label_pepsi.config(text=f"Pepsi: {contador_pepsi}")
    elif marca == "Sprite":
        global contador_sprite
        contador_sprite += 1
        label_sprite.config(text=f"Sprite: {contador_sprite}")

# Configuración inicial de los contadores
contador_coca_cola = 0
contador_pepsi = 0
contador_sprite = 0

# Creación de la ventana principal
ventana = tk.Tk()
ventana.title("Contador de Envases de Gaseosas")

# Ajustar el tamaño de las letras
font_size = 20  # Tamaño de la fuente

# Etiquetas para mostrar los contadores
label_coca_cola = tk.Label(ventana, text=f"Coca-Cola: {contador_coca_cola}", font=("Helvetica", font_size))
label_coca_cola.pack()

label_pepsi = tk.Label(ventana, text=f"Pepsi: {contador_pepsi}", font=("Helvetica", font_size))
label_pepsi.pack()

label_sprite = tk.Label(ventana, text=f"Sprite: {contador_sprite}", font=("Helvetica", font_size))
label_sprite.pack()

# Cargar imágenes
imagen_coca_cola = PhotoImage(file="COCA.png")
imagen_pepsi = PhotoImage(file="pepsi.png")
imagen_sprite = PhotoImage(file="SPRITE.png")

# Mostrar imágenes en etiquetas
label_imagen_coca_cola = tk.Label(ventana, image=imagen_coca_cola)
label_imagen_coca_cola.pack()

label_imagen_pepsi = tk.Label(ventana, image=imagen_pepsi)
label_imagen_pepsi.pack()

label_imagen_sprite = tk.Label(ventana, image=imagen_sprite)
label_imagen_sprite.pack()

# Botones para contar cada tipo de envase
btn_coca_cola = tk.Button(ventana, text="Contar Coca-Cola", command=lambda: contar_envase("Coca-Cola"), font=("Helvetica", font_size))
btn_coca_cola.pack()

btn_pepsi = tk.Button(ventana, text="Contar Pepsi", command=lambda: contar_envase("Pepsi"), font=("Helvetica", font_size))
btn_pepsi.pack()

btn_sprite = tk.Button(ventana, text="Contar Sprite", command=lambda: contar_envase("Sprite"), font=("Helvetica", font_size))
btn_sprite.pack()

# Función para cerrar la ventana
def cerrar_ventana():
    ventana.destroy()

# Botón para cerrar la aplicación
btn_salir = tk.Button(ventana, text="Salir", command=cerrar_ventana, font=("Helvetica", font_size))
btn_salir.pack()

# Ejecutar la ventana principal
ventana.mainloop()
