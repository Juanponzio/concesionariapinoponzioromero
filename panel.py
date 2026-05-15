import customtkinter as ctk

def abrir_panel():

    ventana = ctk.CTkToplevel()

    ventana.geometry("1200x700")

    ventana.configure(fg_color="#1E1E1E")

    texto = ctk.CTkLabel(
        ventana,
        text="PANEL PRINCIPAL",
        font=("Arial", 40)
    )

    texto.pack(pady=100)