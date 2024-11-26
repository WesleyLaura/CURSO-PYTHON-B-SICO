import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
 
#vamos a crear una ventana principal
ventana=tk.Tk() 
#ahora vamos a darle algunas configuracione fundamentales
ventana.title(" WESLEY.COM")
ventana.geometry("300x300") # tamaño de la ventana

 # ahora vamos a insertar una imagene en la ventana
ruta_imagen= r"C:\Users\Usuario\Desktop\REPOSITORIOS DE OTRA CUENTA DE GITHUB\CURSO-PYTHON-B-SICO\tesla.jpg"
imagen1=Image.open(ruta_imagen)


# Ajustar la imagen al tamaño de la ventana
imagen_redimensionada = imagen1.resize((300, 300), Image.Resampling.LANCZOS)
imagen_fondo = ImageTk.PhotoImage(imagen_redimensionada)

# vamos a establecer la imagen como fondo
label_fondo = tk.Label(ventana, image=imagen_fondo)
label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

#usamos la etiqueta Label
# fg es para el color de la letra y bg el para el color del cuaadro de TEXTO
label=tk.Label(ventana,text="Hola, Wesley Laura", font=("Kristen ITC",16),fg="white",bg="black")
label.pack(pady=20)


# ahora vamos a agregar un widget, son botones, que te permite elegir opciones
def saludar():
    print("HOLAAA,AMIGUITOOO")
    
# ahora vamos a cambiar los estilos de los botones|
estilo=ttk.Style()
estilo.configure("TButton", font=("Impact",10), foreground="red")
    
boton=ttk.Button(ventana, text="Haz clic aquí", command=saludar, style="TButton")
boton.pack(pady=100) # es la posicion del boton sobre la ventana

#ahora vamos a inicial el bucle principal
ventana.mainloop()