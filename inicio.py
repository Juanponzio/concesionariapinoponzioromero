import customtkinter as ctk
from PIL import Image
import panel

# Configuración
ctk.set_appearance_mode("dark")

# Ventana
app = ctk.CTk()

# En lugar de usar app.geometry con winfo_screenwidth...
# Usa esto para que se abra maximizada de una:
app.after(0, lambda: app.state("zoomed"))
# Fondo
app.configure(fg_color="#920202")

# Frame
frame = ctk.CTkFrame(
    app,
    width=475,
    height=450,
    corner_radius=20
      # color del frame
)

frame.place(relx=0.495, rely=0.5, anchor="center")


# IMPORTANTE
frame.pack_propagate(False)

# ================= LOGO =================
# LOGO
app.logo_img = ctk.CTkImage(
    light_image=Image.open("logox.png"),
    dark_image=Image.open("logox.png"),
    size=(220,150)
 
)


logo = ctk.CTkLabel(
    app,
image=app.logo_img,
    text=""
)

logo.place(relx=0.5, rely=0.1, anchor="center")

# ================= FUNCION LOGIN =================

def verificar_login():

    usuario_texto = usuario.get()
    contraseña_texto = contraseña.get()

    if usuario_texto == "jefe" and contraseña_texto == "123":

        app.withdraw() # Esto solo esconde la ventana, NO la cierra

        panel.abrir_panel()

# ================= TITULO =================

titulo = ctk.CTkLabel(
    frame,
    text="Inicio de Sesion",
    text_color="#FFFFFF",
    font=("Rockwell", 40, "bold", )
)

titulo.pack(pady=20)

# ================= INPUTS =================

usuario = ctk.CTkEntry(
    frame,
    placeholder_text="Ingresa tu nombre de Usuario",
    width=420,
    height=60,
     font=("poppins", 15, "bold")
)

usuario.pack(pady=(30,20))

contraseña = ctk.CTkEntry(
    frame,
    placeholder_text="Ingresa Tu Contraseña",
    show="*",
    width=420,
    height=60,

     font=("poppins", 15, "bold")

)

contraseña.pack(pady=(30,20))

# ================= BOTON =================

boton = ctk.CTkButton(
    frame,
    text="Iniciar Sesion",
    width=320,
    height=60,
    corner_radius=20,
    hover_color="#000000",
    fg_color="#920202",
    font=("poppins", 15, "bold"),
    command=verificar_login
)

boton.pack(pady=(30))





# Ejecutar
app.mainloop()