import customtkinter as ctk
from PIL import Image

def abrir_panel():
    ventana = ctk.CTkToplevel()
    ventana.title("Panel Empleado - Concesionaria")
    ventana.geometry("1200x800")
    ventana.state("zoomed")
    ventana.configure(fg_color="#1E1E1E")

    # Logo (opcional)
    try:
        logo_img = ctk.CTkImage(
            light_image=Image.open("logox.png"),
            dark_image=Image.open("logox.png"),
            size=(200, 150)
        )
    except Exception:
        logo_img = None

    if logo_img:
        ctk.CTkLabel(ventana, image=logo_img, text="").pack(pady=20)

    ctk.CTkLabel(
        ventana,
        text="Panel de Empleado",
        font=("Akt", 32, "bold"),
        text_color="#FFFFFF"
    ).pack(pady=10)

    ctk.CTkLabel(
        ventana,
        text="Aquí puedes ver las funciones de empleado.",
        font=("Arial", 16),
        text_color="#AAAAAA"
    ).pack(pady=10)

    ctk.CTkButton(
        ventana,
        text="Cerrar",
        command=ventana.destroy,
        fg_color="#920202"
    ).pack(pady=20)
