import customtkinter as ctk
from PIL import Image


def abrir_panel():
    ventana = ctk.CTkToplevel()
    ventana.title("Panel Empleado - Concesionaria")
    ventana.geometry("1200x800")
    ventana.state("zoomed")
    ventana.configure(fg_color="#1E1E1E")

    # Contenedor principal
    content = ctk.CTkFrame(ventana, corner_radius=20, fg_color="#1E1E1E")
    content.pack(fill="both", expand=True, padx=20, pady=20)

    # Logo
    try:
        logo_img = ctk.CTkImage(
            light_image=Image.open("logox.png"),
            dark_image=Image.open("logox.png"),
            size=(180, 120)
        )
    except Exception:
        logo_img = None

    if logo_img:
        ctk.CTkLabel(content, image=logo_img, text="").pack(pady=(10, 15))

    ctk.CTkLabel(
        content,
        text="Panel de Empleado",
        font=("Akt", 32, "bold"),
        text_color="white"
    ).pack(pady=(10, 10))

    ctk.CTkLabel(
        content,
        text="Aquí puedes ver las funciones de empleado.",
        font=("Arial", 16),
        text_color="#AAAAAA"
    ).pack(pady=(0, 20))

    btn_frame = ctk.CTkFrame(content, fg_color="transparent")
    btn_frame.pack(pady=10)

    ctk.CTkButton(
        btn_frame,
        text="Ver tareas",
        width=180,
        height=45,
        fg_color="#920202",
        hover_color="#B00000",
        command=lambda: ctk.messagebox.showinfo("Tareas", "Funcionalidad de empleado todavía no implementada.")
    ).grid(row=0, column=0, padx=10)

    ctk.CTkButton(
        btn_frame,
        text="Cerrar Sesión",
        width=180,
        height=45,
        fg_color="#333333",
        hover_color="#555555",
        command=ventana.destroy
    ).grid(row=0, column=1, padx=10)

    ventana.protocol("WM_DELETE_WINDOW", ventana.destroy)
