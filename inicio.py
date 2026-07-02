import customtkinter as ctk
from PIL import Image
import panel
import panelempleado
from tkinter import messagebox  # Importamos el módulo para mostrar alertas o mensajes
import sqlite3
    
# Configuración
ctk.set_appearance_mode("dark")



import sqlite3

def crear_base_de_datos():
    # 1. Conectar a la base de datos
    # Si el archivo 'concesionaria.db' no existe, Python lo creará automáticamente.
    conexion = sqlite3.connect('zalcas.db')
    
    # 2. Crear un cursor para ejecutar las sentencias SQL
    cursor = conexion.cursor()


# Ventana
app = ctk.CTk()

usuario1 = {
    "Ulises": "uli123",
    "jefe": "123",
}

usuario2 = {
    "Agustin": "agus123",
}

# En lugar de usar app.geometry con winfo_screenwidth...
# Usa esto para que se abra maximizada de una:
app.after(0, lambda: app.state("zoomed"))
# Fondo
app.configure(fg_color="#920202")

# Frame
frame = ctk.CTkFrame(
    app,
    width=425,
    height=380,
    corner_radius=20
      # color del frame
)

frame.place(relx=0.495, rely=0.52, anchor="center")


# IMPORTANTE
frame.pack_propagate(False)

# ================= LOGO =================
# LOGO
app.logo_img = ctk.CTkImage(
    light_image=Image.open("logox.png"),
    dark_image=Image.open("logox.png"),
    size=(200,130)
 
)


logo = ctk.CTkLabel(
    app,
image=app.logo_img,
    text=""
)

logo.place(relx=0.5, rely=0.1, anchor="center")

# ================= FUNCION LOGIN =================

def verificar_login():
# --- LÓGICA ----
#adentro de esta función deben realizar la validación

    # .get() extrae lo que se coloca en los campos de texto
    n1 = usuario.get()
    n2 = contrasena.get()

    # Validar contra los diccionarios (usuario: contraseña)
    if usuario1.get(n1) == n2:
        app.withdraw()
        panel.abrir_panel()
        return

    if usuario2.get(n1) == n2:
        app.withdraw()
        panelempleado.abrir_panel()
        return

    messagebox.showerror("Error", "Usuario o contraseña incorrectos")

# ================= TITULO =================

titulo = ctk.CTkLabel(
    frame,
    text="Inicio de Sesion",
    text_color="#FFFFFF",
    font=("poppins", 40, "bold")
)

titulo.pack(pady=20)

# ================= INPUTS =================

usuario = ctk.CTkEntry(
    frame,
    placeholder_text="Ingresa tu nombre de Usuario",
    width=370,
    height=50,
     font=("poppins", 15, "bold")
)

usuario.pack(pady=(20,20))

contraseña = ctk.CTkEntry(
    frame,
    placeholder_text="Ingresa Tu Contraseña",
    show="*",
    width=370,
    height=50,

     font=("poppins", 15, "bold")

)

contrasena = contraseña
contrasena.pack(pady=(20,20))

# ================= BOTON =================

boton = ctk.CTkButton(
    frame,
    text="Iniciar Sesion",
    width=320,
    height=60,
    corner_radius=10,
    hover_color="#000000",
    fg_color="#920202",
    font=("poppins", 15, "bold"),
    command=verificar_login
)

boton.pack(pady=30)





# Ejecutar
app.mainloop()