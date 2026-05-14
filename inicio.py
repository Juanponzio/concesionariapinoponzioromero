import customtkinter as ctk
from PIL import Image

# Configuración
ctk.set_appearance_mode("dark")

# Ventana
app = ctk.CTk()
app.geometry("1920x1080")

# Fondo
app.configure(fg_color="#810000")

# Frame
frame = ctk.CTkFrame(app, width=300, height=300, corner_radius=20)
#asfd
frame.place(relx=0.5, rely=0.5, anchor="center")

# IMPORTANTE
frame.pack_propagate(False)

# ================= LOGO =================
# LOGO
logo_img = ctk.CTkImage(
    light_image=Image.open("logo.png"),
    dark_image=Image.open("logo.png"),
    size=(200,150)
)

logo = ctk.CTkLabel(
    app,
    image=logo_img,
    text=""
)

logo.place(relx=0.5, rely=0.10, anchor="center")

# ================= TITULO =================

titulo = ctk.CTkLabel(
    frame,
    text="Inicio de Sesion",
    font=("Arial", 30, "bold")
)

titulo.pack(pady=10)

# ================= INPUTS =================

usuario = ctk.CTkEntry(
    frame,
    placeholder_text="Usuario",
    width=240,
    height=50,
     font=("poppins", 15, "bold")
)

usuario.pack(pady=(20,10))

contraseña = ctk.CTkEntry(
    frame,
    placeholder_text="Contraseña",
    show="*",
    width=240,
    height=50,
     font=("poppins", 15, "bold")

)

contraseña.pack(pady=(20,10))

# ================= BOTON =================

boton = ctk.CTkButton(
    frame,
    text="Iniciar Sesión",
     font=("poppins", 15, "bold")

)

boton.pack(pady=20)

# Ejecutar
app.mainloop()