import customtkinter as ctk
from tkinter import ttk

# ---------------- CONFIG ----------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

BG = "#0a0a0a"
CARD = "#161616"
BORDER = "#4f0b0b"
TEXT = "#f0f0f0"
GRAY = "#8a8a8a"
GREEN = "#00d26a"

# ---------------- APP ----------------
def mostrar_ingresos(contenido):

    # Limpiar contenido anterior
    for widget in contenido.winfo_children():
        widget.destroy()

    ctk.CTkLabel(
        contenido,
        text="Ingresos",
        font=("Arial", 40, "bold"),
        text_color=TEXT
    ).pack(anchor="w", padx=40, pady=(25,0))

    ctk.CTkLabel(
        contenido,
        text="Gestión de ingresos y ventas",
        font=("Arial",20),
        text_color=GRAY
    ).pack(anchor="w", padx=40)

# ---------------- TITULO ----------------
ctk.CTkLabel(
    app,
    text="Ingresos",
    font=("Arial", 40, "bold"),
    text_color=TEXT
).pack(anchor="w", padx=40, pady=(25,0))

ctk.CTkLabel(
    app,
    text="Gestión de ingresos y ventas",
    font=("Arial",20),
    text_color=GRAY
).pack(anchor="w", padx=40)

# ---------------- TARJETAS ----------------
cards = ctk.CTkFrame(app, fg_color="transparent")
cards.pack(fill="x", padx=40, pady=30)

def crear_card(parent, titulo, valor, extra, color):
    frame = ctk.CTkFrame(
        parent,
        fg_color=CARD,
        corner_radius=20,
        border_color=BORDER,
        border_width=1,
        width=420,
        height=180
    )

    frame.pack(side="left", padx=18)
    frame.pack_propagate(False)

    ctk.CTkLabel(
        frame,
        text=titulo,
        font=("Arial",22),
        text_color=GRAY
    ).pack(anchor="w", padx=30, pady=(28,5))

    ctk.CTkLabel(
        frame,
        text=valor,
        font=("Arial",42,"bold"),
        text_color=TEXT
    ).pack(anchor="w", padx=30)

    ctk.CTkLabel(
        frame,
        text=extra,
        font=("Arial",18),
        text_color=color
    ).pack(anchor="w", padx=30)

crear_card(cards,"Total Ingresos","$129.750","+15.3% vs semana anterior",GREEN)
crear_card(cards,"Promedio por Ingreso","$18.536","Últimos 7 días",GRAY)
crear_card(cards,"Transacciones","7","Esta semana",GRAY)

# ---------------- FILTROS ----------------
filtros = ctk.CTkFrame(app, fg_color="transparent")
filtros.pack(fill="x", padx=40)

search_var = ctk.StringVar()

search = ctk.CTkEntry(
    filtros,
    textvariable=search_var,
    width=1000,
    height=50,
    placeholder_text="Buscar por concepto...",
    fg_color=CARD,
    border_color=BORDER,
    corner_radius=12
)
search.pack(side="left")

combo = ctk.CTkComboBox(
    filtros,
    values=["Todas","Venta","Servicio","Repuestos","Financiamiento"],
    width=250,
    height=50,
    fg_color=CARD,
    border_color=BORDER
)

combo.set("Todas")
combo.pack(side="right")

# ---------------- TABLA ----------------
tabla_frame = ctk.CTkFrame(
    app,
    fg_color=CARD,
    corner_radius=20,
    border_width=1,
    border_color=BORDER
)

tabla_frame.pack(
    fill="both",
    expand=True,
    padx=40,
    pady=30
)

style = ttk.Style()
style.theme_use("default")

style.configure(
    "Treeview",
    background=CARD,
    foreground="white",
    fieldbackground=CARD,
    rowheight=60,
    font=("Arial",16),
    borderwidth=0
)

style.configure(
    "Treeview.Heading",
    background=CARD,
    foreground="white",
    font=("Arial",18,"bold")
)

tree = ttk.Treeview(
    tabla_frame,
    columns=("fecha","concepto","categoria","monto"),
    show="headings"
)

tree.heading("fecha", text="Fecha")
tree.heading("concepto", text="Concepto")
tree.heading("categoria", text="Categoría")
tree.heading("monto", text="Monto")

tree.column("fecha", width=180)
tree.column("concepto", width=600)
tree.column("categoria", width=220)
tree.column("monto", width=200, anchor="e")

tree.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=20
)

# ---------------- DATOS ----------------
datos = [
("2026-04-20","Venta Toyota Corolla 2024","Venta","+28.500"),
("2026-04-19","Servicio de mantenimiento","Servicio","+450"),
("2026-04-18","Venta Honda CR-V 2024","Venta","+35.200"),
("2026-04-17","Venta de repuestos","Repuestos","+1200"),
("2026-04-16","Venta Ford Ranger 2023","Venta","+42.000"),
("2026-04-15","Financiamiento - Comisión","Financiamiento","+3500"),
("2026-04-14","Venta Chevrolet Onix 2024","Venta","+18.900"),
]

# ---------------- FUNCIONES ----------------
def cargar_tabla(lista):

    tree.delete(*tree.get_children())

    for fila in lista:
        tree.insert(
            "",
            "end",
            values=fila
        )

def filtrar(*args):

    texto = search_var.get().lower()
    categoria = combo.get()

    resultados = []

    for fila in datos:

        fecha, concepto, cat, monto = fila

        contenido = f"{fecha} {concepto} {cat} {monto}".lower()

        coincide_texto = texto in contenido
        coincide_categoria = (
            categoria == "Todas"
            or categoria == cat
        )

        if coincide_texto and coincide_categoria:
            resultados.append(fila)

    cargar_tabla(resultados)

# ---------------- EVENTOS ----------------
search_var.trace_add(
    "write",
    filtrar
)

combo.configure(
    command=lambda x: filtrar()
)

# ---------------- INICIO ----------------
cargar_tabla(datos)

app.mainloop()