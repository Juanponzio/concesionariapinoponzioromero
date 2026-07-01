import customtkinter as ctk
from PIL import Image
from tkinter import messagebox, ttk
# --- ESTO VA JUSTO ACÁ ABAJO, EN ESTE ORDEN EXACTO ---
import numpy as np
import matplotlib
matplotlib.use("TkAgg")  # <-- Obliga a matplotlib a usar el motor de Tkinter
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

    
def abrir_panel():
    ventana = ctk.CTkToplevel()
    ventana.title("Sistema de Gestión - Concesionaria")
    ventana.geometry("1920x1080")
    ventana.configure(fg_color="#1E1E1E")
    ventana.state("zoomed")

    # Configurar el peso de las columnas
    ventana.grid_columnconfigure(1, weight=1)
    ventana.grid_rowconfigure(0, weight=1)

    # ================= BARRA LATERAL (SIDEBAR) =================
    sidebar_frame = ctk.CTkFrame(ventana, width=200, corner_radius=0, fg_color="#2B2B2B")
    sidebar_frame.grid(row=0, column=0, sticky="nsew")
    sidebar_frame.grid_rowconfigure(14, weight=1)

    # Borde lateral
    border_line = ctk.CTkFrame(ventana, width=2, corner_radius=0, fg_color="#4E0000")
    border_line.grid(row=0, column=0, sticky="nse")

    # Logo
    logo_image = ctk.CTkImage(
        light_image=Image.open("logox.png"),
        dark_image=Image.open("logox.png"),
        size=(200, 150)
    )
    logo_label = ctk.CTkLabel(sidebar_frame, image=logo_image, text="")
    logo_label.grid(row=0, column=0, padx=20, pady=20)

    # Línea divisoria
    linea = ctk.CTkFrame(sidebar_frame, height=1.5, fg_color="#4E0000")
    linea.grid(row=1, column=0, padx=20, pady=3, sticky="ew")

    # ================= ÁREA PRINCIPAL =================
    main_content = ctk.CTkFrame(ventana, corner_radius=15, fg_color="#1E1E1E")
    main_content.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

    titulo_bienvenida = ctk.CTkLabel(main_content, text="Bienvenido Ulises", font=("Akt", 35, "bold"))
    titulo_bienvenida.pack(pady=40)
    titulo_bienvenida.place(relx=0.4, rely=0.02)

    # Crear las páginas
    
    

    pag_stock = ctk.CTkFrame(main_content, fg_color="#1E1E1E")
    ctk.CTkLabel(pag_stock, text="Gestión de Stock", font=("Akt", 30, "bold")).pack(pady=20)










# =========================================================================
    # ============================= ESTADÍSTICAS ==============================
    # =========================================================================

    # Definimos pag_estadisticas como un scrollable frame
    pag_estadisticas = ctk.CTkScrollableFrame(main_content, fg_color="#0B0B0B")

    # Títulos superiores de la sección
    ctk.CTkLabel(pag_estadisticas, text="Estadísticas", font=("Akt", 34, "bold"), text_color="white").pack(anchor="w", padx=25, pady=(25, 5))
    ctk.CTkLabel(pag_estadisticas, text="Análisis de rendimiento, balances y control de stock", font=("Akt", 16), text_color="#AAAAAA").pack(anchor="w", padx=25, pady=(0, 25))

    # --- FUNCIÓN REUTILIZABLE PARA CREAR TARJETAS EN ESTADÍSTICAS ---
    def crear_tarjeta_dashboard(parent, titulo, valor, ssubtitulo, color_subtitulo, icono_texto, color_icono, side="left", row_index=None, col_index=None, grid_mode=False):
        card = ctk.CTkFrame(parent, fg_color="#171717", border_color="#4E0000", border_width=1, corner_radius=12, height=130)
        
        if grid_mode:
            card.grid(row=row_index, column=col_index, padx=8, pady=8, sticky="nsew")
        else:
            card.pack(side=side, fill="x", expand=True, padx=8)
            
        card.pack_propagate(False)

        info_frame = ctk.CTkFrame(card, fg_color="transparent")
        info_frame.pack(side="left", fill="both", expand=True, padx=(20, 10), pady=15)

        ctk.CTkLabel(info_frame, text=titulo, font=("Akt", 14), text_color="#AAAAAA").pack(anchor="w")
        ctk.CTkLabel(info_frame, text=valor, font=("Akt", 26, "bold"), text_color="white").pack(anchor="w", pady=(2, 2))
        ctk.CTkLabel(info_frame, text=ssubtitulo, font=("Akt", 12), text_color=color_subtitulo).pack(anchor="w")

        ctk.CTkLabel(card, text=icono_texto, font=("Akt", 22), text_color=color_icono).pack(side="right", padx=25, pady=25, anchor="n")

    # --- 1. FILA SUPERIOR: CUATRO TARJETAS DE MÉTRICAS MÁSTER ---
    fila_superior_metrics = ctk.CTkFrame(pag_estadisticas, fg_color="transparent")
    fila_superior_metrics.pack(fill="x", padx=25, pady=(0, 20))

    crear_tarjeta_dashboard(fila_superior_metrics, "Ingresos del Mes", "$580.000", "+12.5% vs mes anterior", "#00D46A", "$", "#E02020")
    crear_tarjeta_dashboard(fila_superior_metrics, "Gastos del Mes", "$205.000", "+3.2% vs mes anterior", "#E02020", "📉", "#E02020")
    crear_tarjeta_dashboard(fila_superior_metrics, "Vehículos en Stock", "65", "5 vendidos esta semana", "#00D46A", "🚗", "#E02020")
    crear_tarjeta_dashboard(fila_superior_metrics, "Clientes Activos", "342", "+28 este mes", "#00D46A", "👥", "#E02020")

    # --- 2. SECCIÓN CENTRAL: CONTENEDOR GRID DIVIDIDO PARA LOS DOS GRÁFICOS ---
    section_graficos = ctk.CTkFrame(pag_estadisticas, fg_color="transparent")
    section_graficos.pack(fill="x", padx=25, pady=(0, 20))
    section_graficos.grid_columnconfigure(0, weight=6, uniform="grupo_graficos")
    section_graficos.grid_columnconfigure(1, weight=4, uniform="grupo_graficos")

    # --- GRÁFICO IZQUIERDO: INGRESOS VS GASTOS (BARRAS DOBLES COMPUESTAS) ---
    bar_card = ctk.CTkFrame(section_graficos, fg_color="#171717", border_color="#4E0000", border_width=1, corner_radius=12)
    bar_card.grid(row=0, column=0, padx=(0, 10), sticky="nsew")

    ctk.CTkLabel(bar_card, text="Historial de Ingresos vs Gastos", font=("Akt", 18, "bold"), text_color="white").pack(anchor="w", padx=25, pady=(15, 5))
    ctk.CTkLabel(bar_card, text="Comparativa semestral del balance comercial", font=("Akt", 12), text_color="#AAAAAA").pack(anchor="w", padx=25, pady=(0, 10))

    # Creamos la figura y forzamos explícitamente que no tenga márgenes blancos externos
    fig1, ax1 = plt.subplots(figsize=(6, 3.8), facecolor="#171717")
    ax1.set_facecolor("#171717")

    meses_grafico = ["Ene", "Feb", "Mar", "Abr", "May", "Jun"]
    ingresos_vals = [450000, 520000, 480000, 600000, 620000, 590000]
    gastos_vals = [180000, 190000, 175000, 210000, 195000, 205000]

    x_indices = np.arange(len(meses_grafico))
    width_bar = 0.35

    ax1.bar(x_indices - width_bar/2, ingresos_vals, width_bar, label="Ingresos", color="#E02020")
    ax1.bar(x_indices + width_bar/2, gastos_vals, width_bar, label="Gastos", color="#4A1E1E")

    ax1.legend(facecolor="#171717", edgecolor="#4E0000", labelcolor="white", loc="upper left")
    ax1.set_xticks(x_indices)
    ax1.set_xticklabels(meses_grafico)
    ax1.spines["bottom"].set_color("#4E0000")
    ax1.spines["left"].set_color("#4E0000")
    ax1.spines["top"].set_visible(False)
    ax1.spines["right"].set_visible(False)
    ax1.tick_params(colors="#AAAAAA", labelsize=10)
    ax1.grid(True, linestyle="--", alpha=0.08, color="white")
    ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: f"${int(x/1000)}k"))

    # ESTO SOLUCIONA EL RECORTE: Ajusta los elementos automáticamente dentro de la tarjeta
    fig1.tight_layout()

    canvas1 = FigureCanvasTkAgg(fig1, master=bar_card)
    canvas1.draw()
    canvas1.get_tk_widget().pack(fill="both", expand=True, padx=20, pady=(0, 15))
    plt.close(fig1)

    # --- GRÁFICO DERECHO: DISTRIBUCIÓN DE STOCK (TORTA) ---
    pie_card = ctk.CTkFrame(section_graficos, fg_color="#171717", border_color="#4E0000", border_width=1, corner_radius=12)
    pie_card.grid(row=0, column=1, padx=(10, 0), sticky="nsew")

    ctk.CTkLabel(pie_card, text="Distribución de Stock", font=("Akt", 18, "bold"), text_color="white").pack(anchor="w", padx=25, pady=(15, 5))
    ctk.CTkLabel(pie_card, text="Modelos disponibles en concesionaria", font=("Akt", 12), text_color="#AAAAAA").pack(anchor="w", padx=25, pady=(0, 10))

    fig2, ax2 = plt.subplots(figsize=(4, 3.8), facecolor="#171717")
    ax2.set_facecolor("#171717")

    categorias_stock = ["Sedán", "SUV", "Deportivo", "Camioneta"]
    cantidades_stock = [24, 18, 8, 15]
    colores_pie = ["#E02020", "#B01515", "#7A0F0F", "#4A0808"]

    wedges, texts, autotexts = ax2.pie(
        cantidades_stock, 
        labels=categorias_stock, 
        colors=colores_pie, 
        autopct='%1.0f%%', 
        startangle=90, 
        textprops=dict(color="#AAAAAA", fontsize=10),
        wedgeprops=dict(edgecolor="#171717", linewidth=2)
    )

    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_weight('bold')

    # También ajustamos de manera compacta el gráfico de torta
    fig2.tight_layout()

    canvas2 = FigureCanvasTkAgg(fig2, master=pie_card)
    canvas2.draw()
    canvas2.get_tk_widget().pack(fill="both", expand=True, padx=20, pady=(0, 15))
    plt.close(fig2)

    # --- 3. FILA INFERIOR: TRES TARJETAS DE RESUMEN FINAL ---
    fila_inferior_metrics = ctk.CTkFrame(pag_estadisticas, fg_color="transparent")
    fila_inferior_metrics.pack(fill="x", padx=25, pady=(0, 25))
    
    for i in range(3):
        fila_inferior_metrics.grid_columnconfigure(i, weight=1)

    crear_tarjeta_dashboard(fila_inferior_metrics, "Empleados registrados", "24", "Personal bajo nómina", "#AAAAAA", "👥", "#E02020", row_index=0, col_index=0, grid_mode=True)
    crear_tarjeta_dashboard(fila_inferior_metrics, "Ventas concretadas", "18", "Vehículos entregados este mes", "#AAAAAA", "🛒", "#E02020", row_index=0, col_index=1, grid_mode=True)
    crear_tarjeta_dashboard(fila_inferior_metrics, "Ganancia Neta", "$375.000", "Rentabilidad limpia del período", "#00D46A", "💰", "#E02020", row_index=0, col_index=2, grid_mode=True)









# =========================================================================
    # =============================== INGRESOS ================================
    # =========================================================================
    
    # Datos simulados (en el futuro vendrán de tu Base de Datos)
    ingresos_data = [
        ("2026-04-20", "Venta Toyota Corolla 2024", "Venta", "+$28.500"),
        ("2026-04-19", "Servicio de Mantenimiento", "Servicio", "+$450"),
        ("2026-04-18", "Venta Honda CR-V 2024", "Venta", "+$35.200"),
        ("2026-04-17", "Venta de Repuestos", "Repuestos", "+$1.200"),
        ("2026-04-16", "Venta Ford Ranger 2023", "Venta", "+$42.000"),
        ("2026-04-15", "Financiamiento - Comisión", "Financiamiento", "+$3.500"),
        ("2026-04-14", "Venta Chevrolet Onix 2024", "Venta", "+$18.900"),
    ]

    # Redefinimos pag_ingresos como un frame con scrollbar para asegurar responsividad
    pag_ingresos = ctk.CTkScrollableFrame(main_content, fg_color="#0B0B0B")

    # Títulos principales de la sección
    ctk.CTkLabel(
        pag_ingresos,
        text="Ingresos",
        font=("Akt", 34, "bold"),
        text_color="white"
    ).pack(anchor="w", padx=25, pady=(25, 5))

    ctk.CTkLabel(
        pag_ingresos,
        text="Gestión de ingresos y ventas",
        font=("Akt", 16),
        text_color="#AAAAAA"
    ).pack(anchor="w", padx=25, pady=(0, 25))

    # --- CONTENEDOR DE TARJETAS (Métricas Superiores) ---
    ingresos_resumen = ctk.CTkFrame(pag_ingresos, fg_color="transparent")
    ingresos_resumen.pack(fill="x", padx=25, pady=(0, 25))

    def crear_tarjeta_ingreso(parent, titulo, valor, ssubtitulo, color_valor, icono_texto, color_icono):
        card = ctk.CTkFrame(
            parent,
            fg_color="#171717",
            border_color="#4E0000",
            border_width=1,
            corner_radius=12,
            height=140
        )
        card.pack(side="left", fill="x", expand=True, padx=8)
        card.pack_propagate(False)

        # Contenedor interno para alinear textos a la izquierda e icono a la derecha
        info_frame = ctk.CTkFrame(card, fg_color="transparent")
        info_frame.pack(side="left", fill="both", expand=True, padx=(20, 10), pady=15)

        ctk.CTkLabel(info_frame, text=titulo, font=("Akt", 14), text_color="#AAAAAA").pack(anchor="w")
        ctk.CTkLabel(info_frame, text=valor, font=("Akt", 28, "bold"), text_color="white").pack(anchor="w", pady=(5, 2))
        ctk.CTkLabel(info_frame, text=ssubtitulo, font=("Akt", 12), text_color=color_valor).pack(anchor="w")

        # Icono simulado en texto plano respetando el color del diseño original
        ctk.CTkLabel(card, text=icono_texto, font=("Akt", 24), text_color=color_icono).pack(side="right", padx=25, pady=25, anchor="n")

    # Generamos las 3 tarjetas de indicadores superiores
    crear_tarjeta_ingreso(ingresos_resumen, "Total Ingresos", "$129.750", "+15.3% vs semana anterior", "#00D46A", "$", "#E02020")
    crear_tarjeta_ingreso(ingresos_resumen, "Promedio por Ingreso", "$18.536", "Últimos 7 días", "#AAAAAA", "📈", "#E02020")
    crear_tarjeta_ingreso(ingresos_resumen, "Transacciones", "7", "Esta semana", "#AAAAAA", "🏷️", "#E02020")

    # --- CONTENEDOR PRINCIPAL DE LA TABLA ---
    tabla_cards_frame = ctk.CTkFrame(
        pag_ingresos,
        fg_color="#171717",
        border_color="#4E0000",
        border_width=1,
        corner_radius=12
    )
    tabla_cards_frame.pack(fill="both", expand=True, padx=25, pady=(0, 25))

    # Buscador integrado dentro del frame de la tabla
    buscador_ingresos = ctk.CTkEntry(
        tabla_cards_frame,
        placeholder_text="Buscar por concepto...",
        height=42,
        fg_color="#141414",
        border_color="#4E0000",
        border_width=1,
        corner_radius=10
    )
    buscador_ingresos.pack(fill="x", padx=25, pady=(25, 15))

    # Contenedor exclusivo para Treeview
    tabla_ingresos_container = ctk.CTkFrame(tabla_cards_frame, fg_color="transparent")
    tabla_ingresos_container.pack(fill="both", expand=True, padx=25, pady=(0, 25))

    # Configuración de estilos para el Treeview (Se adapta a la paleta oscura de la app)
    style_ingresos = ttk.Style()
    style_ingresos.configure(
        "ingresos.Treeview",
        background="#141414",
        foreground="white",
        fieldbackground="#141414",
        rowheight=45,
        font=("Akt", 13)
    )
    style_ingresos.configure(
        "ingresos.Treeview.Heading",
        background="#171717",
        foreground="#AAAAAA",
        relief="flat",
        font=("Akt", 14, "bold")
    )
    style_ingresos.map("ingresos.Treeview", background=[("selected", "#4E0000")])

    columnas_ingresos = ("Fecha", "Concepto", "Categoría", "Monto")
    tabla_ingresos = ttk.Treeview(
        tabla_ingresos_container,
        columns=columnas_ingresos,
        show="headings",
        style="ingresos.Treeview",
        height=10
    )

    for col in columnas_ingresos:
        tabla_ingresos.heading(col, text=col)
        # Alineación izquierda para Concepto, centro para el resto como en tu captura
        if col == "Concepto":
            tabla_ingresos.column(col, anchor="w", width=350)
        else:
            tabla_ingresos.column(col, anchor="center", width=150)

    tabla_ingresos.pack(fill="both", expand=True)

    # Función encargada de renderizar y aplicar filtros sobre la tabla
    def actualizar_tabla_ingresos(event=None):
        for item in tabla_ingresos.get_children():
            tabla_ingresos.delete(item)
            
        filtro = buscador_ingresos.get().lower()
        
        for ingreso in ingresos_data:
            fecha, concepto, categoria, monto = ingreso
            if filtro in concepto.lower() or filtro in categoria.lower():
                tabla_ingresos.insert("", "end", values=(fecha, concepto, categoria, monto))

    # Evento de teclado para búsquedas interactivas en tiempo real
    buscador_ingresos.bind("<KeyRelease>", actualizar_tabla_ingresos)
    
    # Carga inicial de datos
    ventana.after(100, actualizar_tabla_ingresos)



























# =========================================================================
    # =============================== GASTOS ================================
    # =========================================================================
    
    # Datos simulados (en el futuro vendrán de tu Base de Datos)
    gastos_data = [
        ("2026-04-22", "Salario del personales", "Salarios", "-$85.500"),
        ("2026-04-16", "Compra de repuestos", "Inventario", "-$12.000"),
        ("2026-04-10", "Servicios publicos", "Servicios", "-$3.200"),
        ("2026-04-7", "Mantenimiento de instalaciones", "Mantenimiento", "-6.000"),
        ("2026-04-6", "Venta Ford Ranger 2023", "Venta", "+$42.000"),
        ("2026-04-3", "Marketing y Publicidad", "Marketing", "+$8.500"),
        ]

    # Redefinimos pag_ingresos como un frame con scrollbar para asegurar responsividad
    pag_gastos = ctk.CTkScrollableFrame(main_content, fg_color="#0B0B0B")

    # Títulos principales de la sección
    ctk.CTkLabel(
        pag_gastos,
        text="Gastos",
        font=("Akt", 34, "bold"),
        text_color="white"
    ).pack(anchor="w", padx=25, pady=(25, 5))

    ctk.CTkLabel(
        pag_gastos,
        text="Control de egresos y costos operativos",
        font=("Akt", 16),
        text_color="#AAAAAA"
    ).pack(anchor="w", padx=25, pady=(0, 25))

    # --- CONTENEDOR DE TARJETAS (Métricas Superiores) ---
    gastos_resumen = ctk.CTkFrame(pag_gastos, fg_color="transparent")
    gastos_resumen.pack(fill="x", padx=25, pady=(0, 25))

    def crear_tarjeta_gasto(parent, titulo, valor, ssubtitulo, color_valor, icono_texto, color_icono):
        card = ctk.CTkFrame(
            parent,
            fg_color="#171717",
            border_color="#4E0000",
            border_width=1,
            corner_radius=12,
            height=140
        )
        card.pack(side="left", fill="x", expand=True, padx=8)
        card.pack_propagate(False)

        # Contenedor interno para alinear textos a la izquierda e icono a la derecha
        info_frame = ctk.CTkFrame(card, fg_color="transparent")
        info_frame.pack(side="left", fill="both", expand=True, padx=(20, 10), pady=15)

        ctk.CTkLabel(info_frame, text=titulo, font=("Akt", 14), text_color="#AAAAAA").pack(anchor="w")
        ctk.CTkLabel(info_frame, text=valor, font=("Akt", 28, "bold"), text_color="white").pack(anchor="w", pady=(5, 2))
        ctk.CTkLabel(info_frame, text=ssubtitulo, font=("Akt", 12), text_color=color_valor).pack(anchor="w")

        # Icono simulado en texto plano respetando el color del diseño original
        ctk.CTkLabel(card, text=icono_texto, font=("Akt", 24), text_color=color_icono).pack(side="right", padx=25, pady=25, anchor="n")

    # Generamos las 3 tarjetas de indicadores superiores
    crear_tarjeta_gasto(gastos_resumen, "Total Gastos", "$309.750", "+8% vs semana anterior", "#E02020", "$", "#E02020")
    crear_tarjeta_gasto(gastos_resumen, "Promedio por Gasto", "$43.536", "Últimos 7 días", "#AAAAAA", "📈", "#E02020")
    crear_tarjeta_gasto(gastos_resumen, "Transacciones", "7", "Esta semana", "#AAAAAA", "🏷️", "#E02020")

    # --- CONTENEDOR PRINCIPAL DE LA TABLA ---
    tabla_cards_frame = ctk.CTkFrame(
        pag_gastos,
        fg_color="#171717",
        border_color="#4E0000",
        border_width=1,
        corner_radius=12
    )
    tabla_cards_frame.pack(fill="both", expand=True, padx=25, pady=(0, 25))

    # Buscador integrado dentro del frame de la tabla
    buscador_gastos = ctk.CTkEntry(
        tabla_cards_frame,
        placeholder_text="Buscar por concepto...",
        height=42,
        fg_color="#141414",
        border_color="#4E0000",
        border_width=1,
        corner_radius=10
    )
    buscador_gastos.pack(fill="x", padx=25, pady=(25, 15))

    # Contenedor exclusivo para Treeview
    tabla_gastos_container = ctk.CTkFrame(tabla_cards_frame, fg_color="transparent")
    tabla_gastos_container.pack(fill="both", expand=True, padx=25, pady=(0, 25))

    # Configuración de estilos para el Treeview (Se adapta a la paleta oscura de la app)
    style_gastos = ttk.Style()
    style_gastos.configure(
        "gastos.Treeview",
        background="#141414",
        foreground="white",
        fieldbackground="#141414",
        rowheight=45,
        font=("Akt", 13)
    )
    style_gastos.configure(
        "gastos.Treeview.Heading",
        background="#171717",
        foreground="#AAAAAA",
        relief="flat",
        font=("Akt", 14, "bold")
    )
    style_gastos.map("gastos.Treeview", background=[("selected", "#4E0000")])

    columnas_gastos = ("Fecha", "Concepto", "Categoría", "Monto")
    tabla_gastos = ttk.Treeview(
        tabla_gastos_container,
        columns=columnas_gastos,
        show="headings",
        style="gastos.Treeview",
        height=10
    )

    for col in columnas_gastos:
        tabla_gastos.heading(col, text=col)
        # Alineación izquierda para Concepto, centro para el resto como en tu captura
        if col == "Concepto":
            tabla_gastos.column(col, anchor="w", width=350)
        else:
            tabla_gastos.column(col, anchor="center", width=150)

    tabla_gastos.pack(fill="both", expand=True)

    # Función encargada de renderizar y aplicar filtros sobre la tabla
    def actualizar_tabla_gastos(event=None):
        for item in tabla_gastos.get_children():
            tabla_gastos.delete(item)
            
        filtro = buscador_gastos.get().lower()
        
        for gasto in gastos_data:
            fecha, concepto, categoria, monto = gasto
            if filtro in concepto.lower() or filtro in categoria.lower():
                tabla_gastos.insert("", "end", values=(fecha, concepto, categoria, monto))

    # Evento de teclado para búsquedas interactivas en tiempo real
    buscador_gastos.bind("<KeyRelease>", actualizar_tabla_gastos)
    
    # Carga inicial de datos
    ventana.after(100, actualizar_tabla_gastos)


























    pag_clientes = ctk.CTkFrame(main_content, fg_color="#1E1E1E")
    ctk.CTkLabel(pag_clientes, text="Gestión de Clientes", font=("Akt", 30, "bold")).pack(pady=20)

    # ================= CLIENTES =================
    clientes_data = [
        ("Juan Pérez", "2", "juan.perez@email.com", "+54 11 2345-6789", "Buenos Aires", "2026-04-20"),
        ("María González", "1", "maria.gonzalez@email.com", "+54 11 3456-7890", "Córdoba", "2026-04-18"),
        ("Carlos Rodríguez", "3", "carlos.rodriguez@email.com", "+54 11 4567-8901", "Mendoza", "2026-04-15"),
        ("Ana Martínez", "1", "ana.martinez@email.com", "+54 11 5678-9012", "Rosario", "2026-04-10"),
    ]

    pag_clientes = ctk.CTkScrollableFrame(main_content, fg_color="#0B0B0B")

    ctk.CTkLabel(
        pag_clientes,
        text="Clientes",
        font=("Akt", 34, "bold"),
        text_color="white"
    ).pack(anchor="w", padx=25, pady=(25, 5))

    ctk.CTkLabel(
        pag_clientes,
        text="Gestión de clientes y su historial de compras",
        font=("Akt", 16),
        text_color="#AAAAAA"
    ).pack(anchor="w", padx=25, pady=(0, 25))

    pag_reportes = ctk.CTkFrame(main_content, fg_color="#1E1E1E")
    ctk.CTkLabel(pag_reportes, text="Reportes", font=("Akt", 30, "bold")).pack(pady=20)
    clientes_resumen = ctk.CTkFrame(pag_clientes, fg_color="transparent")
    clientes_resumen.pack(fill="x", padx=25, pady=(0, 25))

    clientes_cards_frame = ctk.CTkFrame(
        pag_clientes,
        fg_color="#171717",
        border_color="#4E0000",
        border_width=1,
        corner_radius=12
    )
    clientes_cards_frame.pack(fill="both", expand=True, padx=25, pady=(0, 25))

    buscador_clientes = ctk.CTkEntry(
        clientes_cards_frame,
        placeholder_text="Buscar por nombre, email o ciudad...",
        height=42,
        fg_color="#141414",
        border_color="#4E0000",
        border_width=1,
        corner_radius=10
    )
    buscador_clientes.pack(fill="x", padx=25, pady=(25, 15))

    clientes_grid = ctk.CTkFrame(clientes_cards_frame, fg_color="transparent")
    clientes_grid.pack(fill="both", expand=True, padx=25, pady=(0, 25))

    def crear_resumen_clientes(titulo, valor, color):
        card = ctk.CTkFrame(
            clientes_resumen,
            fg_color="#171717",
            border_color="#4E0000",
            border_width=1,
            corner_radius=10,
            height=105
        )
        card.pack(side="left", fill="x", expand=True, padx=8)
        card.pack_propagate(False)

        ctk.CTkLabel(card, text=titulo, font=("Akt", 14), text_color="#AAAAAA").pack(anchor="w", padx=20, pady=(18, 4))
        ctk.CTkLabel(card, text=str(valor), font=("Akt", 28), text_color=color).pack(anchor="w", padx=20)

    def actualizar_clientes(event=None):
        for widget in clientes_resumen.winfo_children():
            widget.destroy()

        for widget in clientes_grid.winfo_children():
            widget.destroy()

        filtro = buscador_clientes.get().lower()

        clientes_filtrados = []
        for cliente in clientes_data:
            nombre, compras, email, telefono, ciudad, ultima_compra = cliente
            if (filtro in nombre.lower() or 
                filtro in email.lower() or 
                filtro in ciudad.lower() or
                filtro in telefono.lower()):
                clientes_filtrados.append(cliente)

        # Calcular estadísticas
        total_compras = sum(int(cliente[1]) for cliente in clientes_data)
        promedio_compras = total_compras / len(clientes_data) if clientes_data else 0

        crear_resumen_clientes("Total Clientes", len(clientes_data), "white")
        crear_resumen_clientes("Clientes Activos", len(clientes_data), "#00D46A")
        crear_resumen_clientes("Total Compras", total_compras, "#E02020")
        crear_resumen_clientes("Promedio Compras", f"{promedio_compras:.1f}", "#FFB000")

        # Grid de clientes
        for i in range(2):
            clientes_grid.grid_columnconfigure(i, weight=1)

        for index, cliente in enumerate(clientes_filtrados):
            nombre, compras, email, telefono, ciudad, ultima_compra = cliente

            card = ctk.CTkFrame(
                clientes_grid,
                fg_color="#242424",
                border_color="#4E0000",
                border_width=1,
                corner_radius=10,
                height=280
            )
            card.grid(row=index // 2, column=index % 2, padx=12, pady=12, sticky="nsew")
            card.grid_propagate(False)

            # Header con nombre y botones
            header = ctk.CTkFrame(card, fg_color="transparent")
            header.pack(fill="x", padx=16, pady=(15, 5))

            ctk.CTkLabel(
                header,
                text=nombre,
                font=("Akt", 18, "bold"),
                text_color="white"
            ).pack(side="left")

            # Número de compras en rojo
            compras_frame = ctk.CTkFrame(header, fg_color="transparent")
            compras_frame.pack(side="right")

            ctk.CTkLabel(
                compras_frame,
                text=compras,
                font=("Akt", 12, "bold"),
                text_color="#E02020"
            ).pack(side="right", padx=(5, 0))

            ctk.CTkLabel(
                compras_frame,
                text="compras",
                font=("Akt", 10),
                text_color="#E02020"
            ).pack(side="right")

            # Email
            email_frame = ctk.CTkFrame(card, fg_color="transparent")
            email_frame.pack(fill="x", padx=16, pady=(10, 5))

            ctk.CTkLabel(
                email_frame,
                text="📧",
                font=("Akt", 14)
            ).pack(side="left", padx=(0, 8))

            ctk.CTkLabel(
                email_frame,
                text=email,
                font=("Akt", 12),
                text_color="#AAAAAA"
            ).pack(side="left", anchor="w")

            # Teléfono
            tel_frame = ctk.CTkFrame(card, fg_color="transparent")
            tel_frame.pack(fill="x", padx=16, pady=5)

            ctk.CTkLabel(
                tel_frame,
                text="📱",
                font=("Akt", 14)
            ).pack(side="left", padx=(0, 8))

            ctk.CTkLabel(
                tel_frame,
                text=telefono,
                font=("Akt", 12),
                text_color="#AAAAAA"
            ).pack(side="left", anchor="w")

            # Ubicación
            ubi_frame = ctk.CTkFrame(card, fg_color="transparent")
            ubi_frame.pack(fill="x", padx=16, pady=5)

            ctk.CTkLabel(
                ubi_frame,
                text="📍",
                font=("Akt", 14)
            ).pack(side="left", padx=(0, 8))

            ctk.CTkLabel(
                ubi_frame,
                text=ciudad,
                font=("Akt", 12),
                text_color="#AAAAAA"
            ).pack(side="left", anchor="w")

            # Última compra
            ultima_compra_frame = ctk.CTkFrame(card, fg_color="transparent")
            ultima_compra_frame.pack(fill="x", padx=16, pady=(10, 15))

            ctk.CTkLabel(
                ultima_compra_frame,
                text="Última compra:",
                font=("Akt", 12),
                text_color="#AAAAAA"
            ).pack(anchor="w")

            ctk.CTkLabel(
                ultima_compra_frame,
                text=ultima_compra,
                font=("Akt", 12),
                text_color="white"
            ).pack(anchor="w")

            # Botones
            botones = ctk.CTkFrame(card, fg_color="transparent")
            botones.pack(fill="x", padx=16, pady=(0, 16))

            ctk.CTkButton(
                botones,
                text="Ver Detalles",
                height=36,
                fg_color="#E02020",
                hover_color="#B00000",
                font=("Akt", 12, "bold")
            ).pack(side="left", fill="x", expand=True, padx=(0, 8))

            ctk.CTkButton(
                botones,
                text="Eliminar",
                width=80,
                height=36,
                fg_color="#4A1E1E",
                hover_color="#7A2525",
                font=("Akt", 11, "bold"),
                command=lambda c=cliente: eliminar_cliente(c)
            ).pack(side="right")

    def eliminar_cliente(cliente):
        if messagebox.askyesno("Eliminar cliente", "¿Querés eliminar este cliente?"):
            clientes_data.remove(cliente)
            actualizar_clientes()

    buscador_clientes.bind("<KeyRelease>", actualizar_clientes)
    ventana.after(100, actualizar_clientes)

    pag_configuracion = ctk.CTkFrame(main_content, fg_color="#1E1E1E")
    ctk.CTkLabel(pag_configuracion, text="Configuración", font=("Akt", 30, "bold")).pack(pady=20)





















    # ================= pagina de vehiculos =================

    # ================= STOCK =================

    pag_stock = ctk.CTkScrollableFrame(main_content, fg_color="#0B0B0B")

    ctk.CTkLabel(
    pag_stock,
    text="Stock de Vehículos",
    font=("Akt", 34, "bold"),
    text_color="white"
    ).pack(anchor="w", padx=25, pady=(25, 5))

    ctk.CTkLabel(
    pag_stock,
    text="Inventario completo de vehículos",
    font=("Akt", 16),
    text_color="#AAAAAA"
    ).pack(anchor="w", padx=25, pady=(0, 25))

    stock_resumen = ctk.CTkFrame(pag_stock, fg_color="transparent")
    stock_resumen.pack(fill="x", padx=25, pady=(0, 25))

    stock_cards_frame = ctk.CTkFrame(
    pag_stock,
    fg_color="#171717",
    border_color="#4E0000",
    border_width=1,
    corner_radius=12
    )
    stock_cards_frame.pack(fill="both", expand=True, padx=25, pady=(0, 25))

    buscador_stock = ctk.CTkEntry(
    stock_cards_frame,
    placeholder_text="Buscar por marca o modelo...",
    height=42,
    fg_color="#141414",
    border_color="#4E0000",
    border_width=1,
    corner_radius=10
    )
    buscador_stock.pack(fill="x", padx=25, pady=(25, 15))

    vehiculos_grid = ctk.CTkFrame(stock_cards_frame, fg_color="transparent")
    vehiculos_grid.pack(fill="both", expand=True, padx=25, pady=(0, 25))

    def crear_resumen_stock(titulo, valor, color):
        card = ctk.CTkFrame(
            stock_resumen,
            fg_color="#171717",
            border_color="#4E0000",
            border_width=1,
            corner_radius=10,
            height=105
        )
        card.pack(side="left", fill="x", expand=True, padx=8)
        card.pack_propagate(False)

        ctk.CTkLabel(card, text=titulo, font=("Akt", 14), text_color="#AAAAAA").pack(anchor="w", padx=20, pady=(18, 4))
        ctk.CTkLabel(card, text=str(valor), font=("Akt", 28), text_color=color).pack(anchor="w", padx=20)

    def actualizar_stock(event=None):
        for widget in stock_resumen.winfo_children():
            widget.destroy()

        for widget in vehiculos_grid.winfo_children():
            widget.destroy()

        filtro = buscador_stock.get().lower()

        vehiculos_filtrados = []
        for vehiculo in vehiculos_data:
            marca = vehiculo[0]
            modelo = vehiculo[1]
            if filtro in marca.lower() or filtro in modelo.lower():
                vehiculos_filtrados.append(vehiculo)

        crear_resumen_stock("Total Vehículos", len(vehiculos_data), "white")
        crear_resumen_stock("Disponibles", len(vehiculos_data), "#00D46A")
        crear_resumen_stock("Reservados", 0, "#FFB000")
        crear_resumen_stock("Vendidos", 0, "#FF4D5E")

        for i in range(3):
            vehiculos_grid.grid_columnconfigure(i, weight=1)

        for index, vehiculo in enumerate(vehiculos_filtrados):
            marca, modelo, anio, precio, tipo, color, km, motor, transmision, combustible, dominio, vin, descripcion = vehiculo

            card = ctk.CTkFrame(
                vehiculos_grid,
                fg_color="#242424",
                border_color="#4E0000",
                border_width=1,
                corner_radius=10
            )
            card.grid(row=index // 3, column=index % 3, padx=12, pady=12, sticky="nsew")

            header = ctk.CTkFrame(card, fg_color="transparent")
            header.pack(fill="x", padx=16, pady=(15, 5))

            ctk.CTkLabel(
                header,
                text=f"{marca} {modelo}",
                font=("Akt", 18, "bold"),
                text_color="white"
            ).pack(side="left")

            ctk.CTkLabel(
                header,
                text="Disponible",
                font=("Akt", 12),
                text_color="#00D46A",
                fg_color="#133B24",
                corner_radius=6,
                padx=10,
                pady=4
            ).pack(side="right")

            ctk.CTkLabel(card, text=f"Año {anio}", font=("Akt", 14), text_color="#AAAAAA").pack(anchor="w", padx=16)

            datos = [
                ("Tipo:", tipo),
                ("Color:", color),
                ("Kilometraje:", f"{km} km"),
                ("Precio:", f"${precio}")
            ]

            for etiqueta, valor in datos:
                fila = ctk.CTkFrame(card, fg_color="transparent")
                fila.pack(fill="x", padx=16, pady=3)

                ctk.CTkLabel(fila, text=etiqueta, font=("Akt", 14), text_color="#AAAAAA").pack(side="left")
                ctk.CTkLabel(
                    fila,
                    text=valor,
                    font=("Akt", 14),
                    text_color="#E02020" if etiqueta == "Precio:" else "white"
                ).pack(side="right")

            botones = ctk.CTkFrame(card, fg_color="transparent")
            botones.pack(fill="x", padx=16, pady=(12, 16))

            ctk.CTkButton(
                botones,
                text="Ver",
                height=36,
                fg_color="#E02020",
                hover_color="#B00000",
                font=("Akt", 14, "bold")
            ).pack(side="left", fill="x", expand=True, padx=(0, 8))

            ctk.CTkButton(
                botones,
                text="Eliminar",
                width=90,
                height=36,
                fg_color="#4A1E1E",
                hover_color="#7A2525",
                font=("Akt", 13, "bold"),
                command=lambda v=vehiculo: eliminar_vehiculo_stock(v)
            ).pack(side="right")

    def eliminar_vehiculo_stock(vehiculo):
        if messagebox.askyesno("Eliminar vehículo", "¿Querés eliminar este vehículo del stock?"):
            vehiculos_data.remove(vehiculo)
            actualizar_stock()

    buscador_stock.bind("<KeyRelease>", actualizar_stock)
    ventana.after(100, actualizar_stock)



















    # ================= NUEVO VEHICULO =================
    vehiculos_data = []
    vehiculos_data = [
    (
        "Toyota", "Corolla", "2024", "28500",
        "Sedan", "Blanco", "0", "2.0L",
        "Automatica", "Nafta",
        "AB123CD", "JTDBR32E530123456",
        "Unidad nueva, lista para entrega inmediata."
    ),
    (
        "Honda", "CR-V", "2024", "35200",
        "SUV", "Negro", "0", "1.5L Turbo",
        "Automatica", "Nafta",
        "AC456EF", "2HKRW2H85RH654321",
        "SUV familiar con excelente equipamiento."
    ),
    (
        "Ford", "Ranger", "2023", "42000",
        "Pickup", "Gris", "15000", "3.2L Diesel",
        "Automatica", "Diesel",
        "AD789GH", "8AFAR23L4PJ987654",
        "Camioneta usada en muy buen estado."
    )
    ]
    

    pag_nuevo_vehiculo = ctk.CTkScrollableFrame(main_content, fg_color="#1E1E1E")

    ctk.CTkLabel(
        pag_nuevo_vehiculo,
        text="Registrar Nuevo Vehiculo",
        font=("Akt", 32, "bold"),
        text_color="white"
    ).pack(anchor="w", padx=20, pady=(20, 5))

    ctk.CTkLabel(
        pag_nuevo_vehiculo,
        text="Agregar vehiculo al inventario",
        font=("Akt", 16),
        text_color="#AAAAAA"
    ).pack(anchor="w", padx=20)

    frame_form_vehiculo = ctk.CTkFrame(
        pag_nuevo_vehiculo,
        fg_color="#252525",
        border_color="#660000",
        border_width=1,
        corner_radius=15
    )
    frame_form_vehiculo.pack(fill="both", expand=True, padx=20, pady=30)

    for i in range(2):
        frame_form_vehiculo.grid_columnconfigure(i, weight=1)

    ctk.CTkLabel(
        frame_form_vehiculo,
        text="Informacion del Vehiculo",
        font=("Akt", 22, "bold"),
        text_color="white"
    ).grid(row=0, column=0, columnspan=2, sticky="w", padx=25, pady=(25, 5))

    ctk.CTkLabel(
        frame_form_vehiculo,
        text="Complete todos los campos requeridos",
        font=("Akt", 14),
        text_color="#AAAAAA"
    ).grid(row=1, column=0, columnspan=2, sticky="w", padx=25, pady=(0, 15))

    ctk.CTkFrame(frame_form_vehiculo, height=1, fg_color="#4E0000").grid(
        row=2, column=0, columnspan=2, padx=25, pady=(0, 20), sticky="ew"
    )

    def label_vehiculo(texto, fila, columna):
        ctk.CTkLabel(
            frame_form_vehiculo,
            text=texto,
            font=("Akt", 14, "bold"),
            text_color="white"
        ).grid(row=fila, column=columna, padx=25, pady=(0, 6), sticky="w")

    def entry_vehiculo(fila, columna, placeholder=""):
        entry = ctk.CTkEntry(
            frame_form_vehiculo,
            height=42,
            fg_color="#1E1E1E",
            border_color="#660000",
            border_width=1,
            corner_radius=10,
            placeholder_text=placeholder
        )
        entry.grid(row=fila, column=columna, padx=25, pady=(0, 20), sticky="ew")
        return entry

    def combo_vehiculo(fila, columna, opciones):
        combo = ctk.CTkComboBox(
            frame_form_vehiculo,
            values=opciones,
            height=42,
            fg_color="#1E1E1E",
            border_color="#660000",
            border_width=1,
            button_color="#1E1E1E",
            button_hover_color="#920202",
            dropdown_fg_color="#252525",
            dropdown_hover_color="#920202"
        )
        combo.grid(row=fila, column=columna, padx=25, pady=(0, 20), sticky="ew")
        combo.set(opciones[0])
        return combo

    label_vehiculo("Marca *", 3, 0)
    label_vehiculo("Modelo *", 3, 1)
    entry_marca = entry_vehiculo(4, 0, "Toyota, Ford, Chevrolet...")
    entry_modelo = entry_vehiculo(4, 1, "Corolla, Ranger, Onix...")

    label_vehiculo("Año *", 5, 0)
    label_vehiculo("Precio (USD) *", 5, 1)
    entry_anio = entry_vehiculo(6, 0, "2026")
    entry_precio = entry_vehiculo(6, 1, "25000")

    label_vehiculo("Tipo *", 7, 0)
    label_vehiculo("Color *", 7, 1)
    combo_tipo = combo_vehiculo(8, 0, ["Sedan", "SUV", "Pickup", "Hatchback", "Deportivo"])
    entry_color = entry_vehiculo(8, 1, "Blanco, Negro, Rojo...")

    label_vehiculo("Kilometraje *", 9, 0)
    label_vehiculo("Motor", 9, 1)
    entry_km = entry_vehiculo(10, 0, "0")
    entry_motor = entry_vehiculo(10, 1, "2.0L Turbo")

    label_vehiculo("Transmision *", 11, 0)
    label_vehiculo("Combustible *", 11, 1)
    combo_transmision = combo_vehiculo(12, 0, ["Automatica", "Manual"])
    combo_combustible = combo_vehiculo(12, 1, ["Nafta", "Diesel", "Hibrido", "Electrico", "GNC"])

    label_vehiculo("Dominio / Patente *", 13, 0)
    label_vehiculo("VIN (Numero de Chasis)", 13, 1)
    entry_dominio = entry_vehiculo(14, 0, "AB123CD")
    entry_vin = entry_vehiculo(14, 1, "1HGBH41JXMN109186")

    label_vehiculo("Descripcion", 15, 0)
    entry_descripcion = ctk.CTkTextbox(
        frame_form_vehiculo,
        height=100,
        fg_color="#1E1E1E",
        border_color="#660000",
        border_width=1,
        corner_radius=10
    )
    entry_descripcion.grid(row=16, column=0, columnspan=2, padx=25, pady=(0, 25), sticky="ew")

    def limpiar_campos_vehiculo():
        for entry in [entry_marca, entry_modelo, entry_anio, entry_precio, entry_color, entry_km, entry_motor, entry_dominio, entry_vin]:
            entry.delete(0, "end")
        entry_descripcion.delete("1.0", "end")
        combo_tipo.set("Sedan")
        combo_transmision.set("Automatica")
        combo_combustible.set("Nafta")

    def registrar_vehiculo():
        datos = (
            entry_marca.get(), entry_modelo.get(), entry_anio.get(), entry_precio.get(),
            combo_tipo.get(), entry_color.get(), entry_km.get(), entry_motor.get(),
            combo_transmision.get(), combo_combustible.get(),
            entry_dominio.get().upper(), entry_vin.get(),
            entry_descripcion.get("1.0", "end").strip()
        )
        requeridos = [datos[0], datos[1], datos[2], datos[3], datos[4], datos[5], datos[6], datos[8], datos[9], datos[10]]

        if not all(requeridos):
            messagebox.showerror("Error", "Completa todos los campos requeridos")
            return

        vehiculos_data.append(datos)
        actualizar_stock()
        limpiar_campos_vehiculo()
        messagebox.showinfo("Vehiculo Registrado", "El vehiculo fue registrado correctamente")
        mostrar_contenido("Stock", btn_stock)

    frame_btn_vehiculo = ctk.CTkFrame(frame_form_vehiculo, fg_color="transparent")
    frame_btn_vehiculo.grid(row=17, column=0, columnspan=2, padx=25, pady=(5, 30), sticky="ew")
    frame_btn_vehiculo.grid_columnconfigure(0, weight=1)

    ctk.CTkButton(
        frame_btn_vehiculo,
        text="Registrar Vehiculo",
        height=50,
        fg_color="#E02020",
        hover_color="#B00000",
        font=("Akt", 16, "bold"),
        command=registrar_vehiculo
    ).grid(row=0, column=0, padx=(0, 15), sticky="ew")

    ctk.CTkButton(
        frame_btn_vehiculo,
        text="Cancelar",
        width=160,
        height=50,
        fg_color="#333333",
        hover_color="#555555",
        font=("Akt", 16, "bold"),
        command=limpiar_campos_vehiculo
    ).grid(row=0, column=1, sticky="e")












    # ================= EMPLEADOS =================
    empleados_data = [
        ("Carlos", "Zalcas", "12345678", "1978-04-12", "Casado", "+54 11 1234-5678", "carlos@zalcas.com", "Buenos Aires", "Av. Siempre Viva 123", "Gerente General", "Administración", "2020-01-15", "$120.000", "Tiempo Completo", "carlos@zalcas.com", "+54 11 8765-4321"),
        ("Ana", "Martínez", "23456789", "1990-09-01", "Soltera", "+54 11 2345-6789", "ana@zalcas.com", "La Plata", "Calle Falsa 456", "Vendedor Senior", "Ventas", "2021-03-10", "$65.000", "Medio Tiempo", "ana@zalcas.com", "+54 11 9876-5432"),
        ("Roberto", "Silva", "34567890", "1985-12-22", "Casado", "+54 11 3456-7890", "roberto@zalcas.com", "Quilmes", "Ruta 2 km 34", "Mecánico", "Servicio Técnico", "2021-06-20", "$55.000", "Turno Mañana", "roberto@zalcas.com", "+54 11 7654-3210"),
    ]

    empleado_editando = None

    def cargar_empleados():
        for item in tabla_empleados.get_children():
            tabla_empleados.delete(item)
        for idx, empleado in enumerate(empleados_data):
            nombre_completo = f"{empleado[0]} {empleado[1]}"
            tabla_empleados.insert("", "end", iid=str(idx), values=(nombre_completo, empleado[9], empleado[10], empleado[14], empleado[11], empleado[12], "Editar | Eliminar"))

    def buscar_empleado(event=None):
        filtro = buscador_empleados.get().lower()
        for item in tabla_empleados.get_children():
            tabla_empleados.delete(item)
        for idx, empleado in enumerate(empleados_data):
            nombre_completo = f"{empleado[0]} {empleado[1]}"
            if filtro in nombre_completo.lower() or filtro in empleado[9].lower() or filtro in empleado[10].lower():
                tabla_empleados.insert("", "end", iid=str(idx), values=(nombre_completo, empleado[9], empleado[10], empleado[14], empleado[11], empleado[12], "Editar | Eliminar"))

    def eliminar_empleado():
        seleccionado = tabla_empleados.selection()
        if not seleccionado:
            messagebox.showwarning("Atención", "Selecciona un empleado")
            return
        item_id = seleccionado[0]
        if item_id.isdigit():
            idx = int(item_id)
        else:
            idx = None
        if idx is not None and 0 <= idx < len(empleados_data):
            empleados_data.pop(idx)
        cargar_empleados()
        messagebox.showinfo("Éxito", "Empleado eliminado")

    def abrir_formulario_empleado(index):
        nonlocal empleado_editando

        datos = empleados_data[index]
        entry_nombre_emp.delete(0, "end")
        entry_nombre_emp.insert(0, datos[0])
        entry_apellido_emp.delete(0, "end")
        entry_apellido_emp.insert(0, datos[1])
        entry_dni_emp.delete(0, "end")
        entry_dni_emp.insert(0, datos[2])
        entry_nacimiento_emp.delete(0, "end")
        entry_nacimiento_emp.insert(0, datos[3])
        combo_estado_civil.set(datos[4])
        entry_telefono_emp.delete(0, "end")
        entry_telefono_emp.insert(0, datos[5])
        entry_email_emp.delete(0, "end")
        entry_email_emp.insert(0, datos[6])
        entry_ciudad_emp.delete(0, "end")
        entry_ciudad_emp.insert(0, datos[7])
        entry_direccion_emp.delete(0, "end")
        entry_direccion_emp.insert(0, datos[8])
        entry_puesto_emp.delete(0, "end")
        entry_puesto_emp.insert(0, datos[9])
        combo_departamento.set(datos[10])
        entry_fecha_ingreso.delete(0, "end")
        entry_fecha_ingreso.insert(0, datos[11])
        entry_salario.delete(0, "end")
        entry_salario.insert(0, datos[12].lstrip("$"))
        combo_horario.set(datos[13])
        entry_contacto.delete(0, "end")
        entry_contacto.insert(0, datos[14])
        entry_tel_emergencia.delete(0, "end")
        entry_tel_emergencia.insert(0, datos[15])

        btn_registrar.configure(text="Guardar Cambios")
        titulo_emp_nuevo.configure(text="Editar Empleado")
        subtitulo_emp_nuevo.configure(text="Modifica los datos del empleado")
        empleado_editando = index
        mostrar_contenido("Nuevo Empleado", btn_nempleado)

    def editar_empleado():
        seleccionado = tabla_empleados.selection()
        if not seleccionado:
            messagebox.showwarning("Atención", "Selecciona un empleado")
            return
        item_id = seleccionado[0]
        if item_id.isdigit():
            abrir_formulario_empleado(int(item_id))
        else:
            abrir_formulario_empleado(list(tabla_empleados.get_children()).index(item_id))

    pag_empleados = ctk.CTkFrame(main_content, fg_color="#1E1E1E")

    titulo_emp = ctk.CTkLabel(pag_empleados, text="Empleados", font=("Akt", 34, "bold"), text_color="white")
    titulo_emp.pack(anchor="w", padx=20, pady=(20, 5))

    subtitulo_emp = ctk.CTkLabel(pag_empleados, text="Gestión de personal y recursos humanos", font=("Akt", 16), text_color="#AAAAAA")
    subtitulo_emp.pack(anchor="w", padx=20)

    # Buscador de empleados
    buscador_empleados = ctk.CTkEntry(pag_empleados, placeholder_text="Buscar empleado...", width=400)
    buscador_empleados.pack(anchor="w", padx=20, pady=(10,5))
    # El binding se resuelve cuando la función exista al ejecutarse el evento
    buscador_empleados.bind("<KeyRelease>", lambda e: buscar_empleado())
    # (Se suprimieron campos duplicados/incorrectos del formulario antiguo)

    # (botones de acción del formulario de vehículo movidos/centralizados más abajo)

    # Tabla
    style = ttk.Style()
    style.theme_use("default")
    style.configure("Treeview", background="#0b0b0b", foreground="white", fieldbackground="#0b0b0b", rowheight=40, borderwidth=0)
    style.configure("Treeview.Heading", background="#990000", foreground="white", relief="flat")
    style.map("Treeview", background=[("selected", "#cc0000")])

    columnas_empleados = (
        "Nombre",
        "Puesto",
        "Departamento",
        "Contacto",
        "Fecha Ingreso",
        "Salario",
        "Acciones"
    )
    # Contenedor para la tabla de empleados (antes no estaba definido)
    tabla_container = ctk.CTkFrame(pag_empleados, fg_color="transparent")
    tabla_container.pack(fill="both", expand=True, padx=20, pady=10)

    # Estilo específico para la tabla de empleados (aumentar tamaño de encabezados y filas)
    style.configure("empleados.Treeview", background="#0b0b0b", foreground="white", fieldbackground="#0b0b0b", rowheight=50, borderwidth=0, font=("Akt", 14))
    style.configure("empleados.Treeview.Heading", background="#990000", foreground="white", relief="flat", font=("Akt", 18, "bold"))

    tabla_empleados = ttk.Treeview(tabla_container, columns=columnas_empleados, show="headings", style="empleados.Treeview", height=15)

    for col in columnas_empleados:
        tabla_empleados.heading(col, text=col)
        tabla_empleados.column(col, anchor="center", width=180)

    tabla_empleados.pack(fill="both", expand=True, padx=20, pady=(0, 20))

    # ---------- Acciones por fila: abrir editor/confirmar eliminación ----------
    def editar_empleado_item(item_id):
        if item_id.isdigit():
            abrir_formulario_empleado(int(item_id))
        else:
            abrir_formulario_empleado(list(tabla_empleados.get_children()).index(item_id))

    def eliminar_empleado_item(item_id):
        idx = int(item_id) if item_id.isdigit() else None
        tabla_empleados.delete(item_id)
        if idx is not None and 0 <= idx < len(empleados_data):
            empleados_data.pop(idx)
        messagebox.showinfo("Éxito", "Empleado eliminado")

    def confirmar_eliminar_item(item_id):
        popup = ctk.CTkToplevel()
        popup.title("Confirmar eliminación")
        popup.geometry("360x140")
        popup.configure(fg_color="#1E1E1E")

        ctk.CTkLabel(popup, text="¿Confirmar eliminación del empleado?", font=("Akt", 16)).pack(pady=(20,10))

        frame_btns = ctk.CTkFrame(popup, fg_color="transparent")
        frame_btns.pack(pady=5)

        ctk.CTkButton(frame_btns, text="Confirmar", fg_color="#920202", command=lambda: (eliminar_empleado_item(item_id), popup.destroy())).grid(row=0, column=0, padx=10)
        ctk.CTkButton(frame_btns, text="Cancelar", fg_color="#555555", command=popup.destroy).grid(row=0, column=1, padx=10)

    def on_tabla_click(event):
        # Detectar columna y fila
        region = tabla_empleados.identify_region(event.x, event.y)
        if region != "cell":
            return
        col = tabla_empleados.identify_column(event.x)
        row = tabla_empleados.identify_row(event.y)
        if not row:
            return

        col_index = int(col.replace('#', '')) - 1
        if col_index >= 0 and col_index < len(columnas_empleados) and columnas_empleados[col_index] == "Acciones":
            # Ejecutar acción directa según el área del clic en el texto "Editar | Eliminar"
            bbox = tabla_empleados.bbox(row, col)
            if bbox:
                cell_x = event.x - bbox[0]
                if cell_x < bbox[2] * 0.5:
                    editar_empleado_item(row)
                else:
                    confirmar_eliminar_item(row)
            else:
                # En caso de no obtener bbox, usar edición por defecto
                editar_empleado_item(row)

    tabla_empleados.bind("<Button-1>", on_tabla_click)

    frame_botones_emp = ctk.CTkFrame(tabla_container, fg_color="transparent")
    frame_botones_emp.pack(pady=15)

    btn_editar_emp = ctk.CTkButton(
        frame_botones_emp,
        text="Editar Empleado",
        width=180,
        height=45,
        fg_color="#8B0000",
        hover_color="#B00000",
        font=("Akt", 15, "bold"),
        command=editar_empleado
    )
    btn_editar_emp.grid(row=0, column=0, padx=10)

    btn_eliminar_emp = ctk.CTkButton(
        frame_botones_emp,
        text="Eliminar Empleado",
        width=180,
        height=45,
        fg_color="#400000",
        hover_color="#920202",
        font=("Akt", 15, "bold"),
        command=eliminar_empleado
    )
    btn_eliminar_emp.grid(row=0, column=1, padx=10)

    cargar_empleados()

    # ================= NUEVO EMPLEADO =================

    pag_nuevo_empleado = ctk.CTkScrollableFrame(
        main_content,
        fg_color="#1E1E1E"
    )

    titulo_emp_nuevo = ctk.CTkLabel(
        pag_nuevo_empleado,
        text="Registrar Nuevo Empleado",
        font=("Akt", 32, "bold"),
        text_color="white"
    )
    titulo_emp_nuevo.pack(anchor="w", padx=20, pady=(20,5))

    subtitulo_emp_nuevo = ctk.CTkLabel(
        pag_nuevo_empleado,
        text="Agregar empleado al sistema",
        font=("Akt", 16),
        text_color="#AAAAAA"
    )
    subtitulo_emp_nuevo.pack(anchor="w", padx=20)

    # CONTENEDOR
    frame_form_emp = ctk.CTkFrame(
        pag_nuevo_empleado,
        fg_color="#252525",
        border_color="#660000",
        border_width=1,
        corner_radius=15
    )

    frame_form_emp.pack(fill="both", expand=True, padx=20, pady=20)

    for i in range(2):
        frame_form_emp.grid_columnconfigure(i, weight=1)

    # ---------------- INFORMACIÓN PERSONAL ----------------

    titulo_personal = ctk.CTkLabel(
        frame_form_emp,
        text="Información Personal",
        font=("Akt", 22, "bold"),
        text_color="#ff3333"
    )
    titulo_personal.grid(row=0, column=0, columnspan=2, sticky="w", padx=20, pady=(20,10))

    entry_nombre_emp = ctk.CTkEntry(frame_form_emp, placeholder_text="Nombre")
    entry_nombre_emp.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

    entry_apellido_emp = ctk.CTkEntry(frame_form_emp, placeholder_text="Apellido")
    entry_apellido_emp.grid(row=1, column=1, padx=20, pady=10, sticky="ew")

    entry_dni_emp = ctk.CTkEntry(frame_form_emp, placeholder_text="DNI")
    entry_dni_emp.grid(row=2, column=0, padx=20, pady=10, sticky="ew")

    entry_nacimiento_emp = ctk.CTkEntry(frame_form_emp, placeholder_text="dd/mm/aaaa")
    entry_nacimiento_emp.grid(row=2, column=1, padx=20, pady=10, sticky="ew")

    combo_estado_civil = ctk.CTkComboBox(
        frame_form_emp,
        values=["Soltero", "Casado", "Divorciado", "Viudo"]
    )
    combo_estado_civil.grid(row=3, column=0, padx=20, pady=10, sticky="ew")

    entry_telefono_emp = ctk.CTkEntry(frame_form_emp, placeholder_text="+54 11 1234-5678")
    entry_telefono_emp.grid(row=3, column=1, padx=20, pady=10, sticky="ew")

    entry_email_emp = ctk.CTkEntry(frame_form_emp, placeholder_text="empleado@zalcas.com")
    entry_email_emp.grid(row=4, column=0, padx=20, pady=10, sticky="ew")

    entry_ciudad_emp = ctk.CTkEntry(frame_form_emp, placeholder_text="Ciudad")
    entry_ciudad_emp.grid(row=4, column=1, padx=20, pady=10, sticky="ew")

    entry_direccion_emp = ctk.CTkEntry(frame_form_emp, placeholder_text="Dirección")
    entry_direccion_emp.grid(row=5, column=0, columnspan=2, padx=20, pady=10, sticky="ew")

    # ---------------- INFORMACIÓN LABORAL ----------------

    titulo_laboral = ctk.CTkLabel(
        frame_form_emp,
        text="Información Laboral",
        font=("Akt", 22, "bold"),
        text_color="#ff3333"
    )
    titulo_laboral.grid(row=6, column=0, columnspan=2, sticky="w", padx=20, pady=(20,10))

    entry_puesto_emp = ctk.CTkEntry(frame_form_emp, placeholder_text="Puesto")
    entry_puesto_emp.grid(row=7, column=0, padx=20, pady=10, sticky="ew")

    combo_departamento = ctk.CTkComboBox(
        frame_form_emp,
        values=[
            "Ventas",
            "Administración",
            "Mecánica",
            "RRHH",
            "Finanzas"
        ]
    )
    combo_departamento.grid(row=7, column=1, padx=20, pady=10, sticky="ew")

    entry_fecha_ingreso = ctk.CTkEntry(frame_form_emp, placeholder_text="dd/mm/aaaa")
    entry_fecha_ingreso.grid(row=8, column=0, padx=20, pady=10, sticky="ew")

    entry_salario = ctk.CTkEntry(frame_form_emp, placeholder_text="Salario")
    entry_salario.grid(row=8, column=1, padx=20, pady=10, sticky="ew")

    combo_horario = ctk.CTkComboBox(
        frame_form_emp,
        values=[
            "Tiempo Completo",
            "Medio Tiempo",
            "Turno Mañana",
            "Turno Tarde"
        ]
    )
    combo_horario.grid(row=9, column=0, padx=20, pady=10, sticky="ew")

    # ---------------- CONTACTO EMERGENCIA ----------------

    titulo_emergencia = ctk.CTkLabel(
        frame_form_emp,
        text="Contacto de Emergencia",
        font=("Akt", 22, "bold"),
        text_color="#ff3333"
    )
    titulo_emergencia.grid(row=10, column=0, columnspan=2, sticky="w", padx=20, pady=(20,10))

    entry_contacto = ctk.CTkEntry(
        frame_form_emp,
        placeholder_text="Nombre del contacto"
    )
    entry_contacto.grid(row=11, column=0, padx=20, pady=10, sticky="ew")

    entry_tel_emergencia = ctk.CTkEntry(
        frame_form_emp,
        placeholder_text="Teléfono de emergencia"
    )
    entry_tel_emergencia.grid(row=11, column=1, padx=20, pady=10, sticky="ew")

    # ---------------- FUNCIONES ----------------

    def limpiar_formulario_empleado():
        nonlocal empleado_editando
        entry_nombre_emp.delete(0, "end")
        entry_apellido_emp.delete(0, "end")
        entry_dni_emp.delete(0, "end")
        entry_nacimiento_emp.delete(0, "end")
        combo_estado_civil.set("")
        entry_telefono_emp.delete(0, "end")
        entry_email_emp.delete(0, "end")
        entry_ciudad_emp.delete(0, "end")
        entry_direccion_emp.delete(0, "end")
        entry_puesto_emp.delete(0, "end")
        combo_departamento.set("")
        entry_fecha_ingreso.delete(0, "end")
        entry_salario.delete(0, "end")
        combo_horario.set("")
        entry_contacto.delete(0, "end")
        entry_tel_emergencia.delete(0, "end")
        btn_registrar.configure(text="Registrar Empleado")
        titulo_emp_nuevo.configure(text="Registrar Nuevo Empleado")
        subtitulo_emp_nuevo.configure(text="Agregar empleado al sistema")
        empleado_editando = None

    def registrar_empleado():
        nonlocal empleado_editando
        nuevo = (
            entry_nombre_emp.get(),
            entry_apellido_emp.get(),
            entry_dni_emp.get(),
            entry_nacimiento_emp.get(),
            combo_estado_civil.get(),
            entry_telefono_emp.get(),
            entry_email_emp.get(),
            entry_ciudad_emp.get(),
            entry_direccion_emp.get(),
            entry_puesto_emp.get(),
            combo_departamento.get(),
            entry_fecha_ingreso.get(),
            f"${entry_salario.get()}",
            combo_horario.get(),
            entry_contacto.get(),
            entry_tel_emergencia.get()
        )

        if empleado_editando is None:
            empleados_data.append(nuevo)
            messagebox.showinfo("Empleado Registrado", "El empleado fue registrado correctamente")
        else:
            empleados_data[empleado_editando] = nuevo
            messagebox.showinfo("Empleado Actualizado", "Los datos del empleado fueron actualizados")

        cargar_empleados()
        limpiar_formulario_empleado()







# =========================================================================
    # ============================ CONFIGURACIÓN ==============================
    # =========================================================================

    # Redefinimos pag_config como un scrollable frame para asegurar compatibilidad
    pag_config = ctk.CTkScrollableFrame(main_content, fg_color="#0B0B0B")

    # Títulos superiores de la sección
    ctk.CTkLabel(pag_config, text="Configuración", font=("Akt", 34, "bold"), text_color="white").pack(anchor="w", padx=25, pady=(25, 5))
    ctk.CTkLabel(pag_config, text="Administración integral del sistema y parámetros del establecimiento", font=("Akt", 16), text_color="#AAAAAA").pack(anchor="w", padx=25, pady=(0, 20))

    # --- BARRA DE NAVEGACIÓN INTERNA (SUBMENÚ DE BOTONES) ---
    nav_config_frame = ctk.CTkFrame(pag_config, fg_color="transparent")
    nav_config_frame.pack(fill="x", padx=25, pady=(0, 20))

    # --- CONTENEDOR PRINCIPAL PARA LAS PÁGINAS ---
    # Aquí es donde se van a montar las tarjetas ocupando todo el ancho posible
    container_paginas = ctk.CTkFrame(pag_config, fg_color="transparent")
    container_paginas.pack(fill="both", expand=True, padx=25, pady=(0, 25))

    # Declaramos los contenedores de las sub-páginas (pero no los empaquetamos todavía)
    sub_pag_horarios = ctk.CTkFrame(container_paginas, fg_color="#171717", border_color="#4E0000", border_width=1, corner_radius=12)
    sub_pag_db = ctk.CTkFrame(container_paginas, fg_color="#171717", border_color="#4E0000", border_width=1, corner_radius=12)

    # --- FUNCIÓN NAVEGADORA DE PESTAÑAS INTERNAS ---
    def cambiar_pestana_config(pestana_destino, boton_activo):
        # 1. Ocultamos las dos sub-páginas para limpiar la pantalla
        sub_pag_horarios.pack_forget()
        sub_pag_db.pack_forget()
        
        # 2. Reseteamos el diseño visual de ambos botones a su estado normal (transparente)
        btn_nav_horarios.configure(fg_color="transparent", text_color="#AAAAAA", border_width=0)
        btn_nav_db.configure(fg_color="transparent", text_color="#AAAAAA", border_width=0)
        
        # 3. Mostramos la página seleccionada expandiéndose en toda la pantalla disponible
        pestana_destino.pack(fill="both", expand=True)
        
        # 4. Destacamos visualmente el botón que acabamos de tocar con color rojo vivo
        boton_activo.configure(fg_color="#E02020", text_color="white", border_width=0)

    # Creamos los botones de navegación interna
    btn_nav_horarios = ctk.CTkButton(nav_config_frame, text="Horarios de Atención", font=("Akt", 15, "bold"), height=35, width=180, corner_radius=8, command=lambda: cambiar_pestana_config(sub_pag_horarios, btn_nav_horarios))
    btn_nav_horarios.pack(side="left", padx=(0, 10))

    btn_nav_db = ctk.CTkButton(nav_config_frame, text="Base de Datos", font=("Akt", 15, "bold"), height=35, width=180, corner_radius=8, command=lambda: cambiar_pestana_config(sub_pag_db, btn_nav_db))
    btn_nav_db.pack(side="left", padx=10)

# =========================================================================
    # PESTAÑA 1: HORARIOS DE ATENCIÓN
    # =========================================================================
    ctk.CTkLabel(sub_pag_horarios, text="Horarios de Atención", font=("Akt", 22, "bold"), text_color="white").pack(anchor="w", padx=30, pady=(25, 5))
    ctk.CTkLabel(sub_pag_horarios, text="Establecer las jornadas laborales del establecimiento", font=("Akt", 13), text_color="#AAAAAA").pack(anchor="w", padx=30, pady=(0, 20))

    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    
    # Lista para guardar todas las cajas de texto y poder bloquearlas juntas
    lista_entries_horarios = []

    for dia in dias_semana:
        dia_row = ctk.CTkFrame(sub_pag_horarios, fg_color="transparent")
        dia_row.pack(fill="x", padx=30, pady=6)

        ctk.CTkLabel(dia_row, text=dia, font=("Akt", 15, "bold"), text_color="white", width=120, anchor="w").pack(side="left")

        entry_apertura = ctk.CTkEntry(dia_row, placeholder_text="09:00", width=90, height=34, fg_color="#0B0B0B", border_color="#4E0000", text_color="white", justify="center")
        entry_apertura.pack(side="left", padx=15)

        ctk.CTkLabel(dia_row, text="a", font=("Akt", 14), text_color="#AAAAAA").pack(side="left")

        entry_cierre = ctk.CTkEntry(dia_row, placeholder_text="19:00", width=90, height=34, fg_color="#0B0B0B", border_color="#4E0000", text_color="white", justify="center")
        entry_cierre.pack(side="left", padx=15)

        if dia == "Domingo":
            entry_apertura.configure(placeholder_text="Cerrado")
            entry_cierre.configure(placeholder_text="Cerrado")
        elif dia == "Sábado":
            entry_cierre.configure(placeholder_text="13:00")

        # Guardamos las entradas en la lista
        lista_entries_horarios.extend([entry_apertura, entry_cierre])

    # Función interna que se ejecuta al clickear el botón
    def bloquear_cronograma():
        for entry in lista_entries_horarios:
            entry.configure(state="disabled", text_color="#666666") # Los bloquea y pone el texto gris sutil
        btn_guardar_horarios.configure(text="🔒 Cronograma Guardado", fg_color="#2B2B2B", state="disabled")
        messagebox.showinfo("Configuración", "El cronograma laboral fue guardado y bloqueado con éxito.")

    # Botón configurado para llamar a la función de bloqueo
    btn_guardar_horarios = ctk.CTkButton(sub_pag_horarios, text="Guardar Cronograma Laboral", font=("Akt", 14, "bold"), fg_color="#E02020", hover_color="#920202", text_color="white", height=40, width=250, command=bloquear_cronograma)
    btn_guardar_horarios.pack(anchor="w", padx=30, pady=(30, 25))


    # =========================================================================
    # PESTAÑA 2: CONFIGURACIÓN DE BASE DE DATOS (OCUPA TODA LA PANTALLA)
    # =========================================================================
    db_header = ctk.CTkFrame(sub_pag_db, fg_color="transparent")
    db_header.pack(fill="x", padx=30, pady=(25, 15))
    ctk.CTkLabel(db_header, text="Conexión de Base de Datos", font=("Akt", 22, "bold"), text_color="white").pack(side="left")
    
    # Indicador de estado circular verde
    status_frame = ctk.CTkFrame(db_header, fg_color="transparent")
    status_frame.pack(side="right")
    ctk.CTkLabel(status_frame, text="🟢 Servidor Activo", font=("Akt", 14, "bold"), text_color="#00D46A").pack(side="right")

    # Función auxiliar para campos de texto del formulario (ahora más anchos)
    def crear_campo_db_ancho(label_text, placeholder, show_char=None):
        frame = ctk.CTkFrame(sub_pag_db, fg_color="transparent")
        frame.pack(fill="x", padx=30, pady=8)
        ctk.CTkLabel(frame, text=label_text, font=("Akt", 15), text_color="#AAAAAA", width=150, anchor="w").pack(side="left")
        entry = ctk.CTkEntry(frame, placeholder_text=placeholder, show=show_char, height=36, fg_color="#0B0B0B", border_color="#4E0000", text_color="white")
        entry.pack(side="left", fill="x", expand=True)
        return entry

    # Inputs del formulario técnico expandidos horizontalmente
    input_host = crear_campo_db_ancho("Servidor (Host):", "localhost")
    input_port = crear_campo_db_ancho("Puerto de enlace:", "3306")
    input_dbname = crear_campo_db_ancho("Nombre Base de Datos:", "concesionaria_db")
    input_user = crear_campo_db_ancho("Usuario Administrador:", "root")
    input_pass = crear_campo_db_ancho("Contraseña de Acceso:", "••••••••", show_char="*")

    # Botonera operativa inferior alineada a la izquierda de forma ordenada
    db_buttons = ctk.CTkFrame(sub_pag_db, fg_color="transparent")
    db_buttons.pack(fill="x", padx=30, pady=(30, 25))

    btn_probar_db = ctk.CTkButton(db_buttons, text="Probar Conexión", font=("Akt", 14, "bold"), fg_color="transparent", border_color="#4E0000", border_width=1, text_color="white", hover_color="#262626", height=40, width=160)
    btn_probar_db.pack(side="left", padx=(0, 10))

    btn_inicializar_db = ctk.CTkButton(db_buttons, text="Inicializar Tablas", font=("Akt", 14, "bold"), fg_color="transparent", border_color="#4E0000", border_width=1, text_color="#AAAAAA", hover_color="#262626", height=40, width=160)
    btn_inicializar_db.pack(side="left", padx=10)

    btn_guardar_db = ctk.CTkButton(db_buttons, text="Guardar Parámetros", font=("Akt", 14, "bold"), fg_color="#E02020", hover_color="#920202", text_color="white", height=40, width=180)
    btn_guardar_db.pack(side="left", padx=10)



# --- FILA DE BOTONES DE ACCIONES AVANZADAS (RESPALDAR Y RESTAURAR) ---
    db_advanced_buttons = ctk.CTkFrame(sub_pag_db, fg_color="transparent")
    db_advanced_buttons.pack(fill="x", padx=30, pady=(10, 0))

    btn_respaldar_db = ctk.CTkButton(db_advanced_buttons, text="📥 Respaldar Base de Datos", font=("Akt", 14, "bold"), fg_color="transparent", border_color="#4E0000", border_width=1, text_color="white", hover_color="#262626", height=40)
    btn_respaldar_db.pack(side="left", fill="x", expand=True, padx=(0, 10))

    btn_restaurar_db = ctk.CTkButton(db_advanced_buttons, text="📤 Restaurar Base de Datos", font=("Akt", 14, "bold"), fg_color="transparent", border_color="#4E0000", border_width=1, text_color="white", hover_color="#262626", height=40)
    btn_restaurar_db.pack(side="left", fill="x", expand=True, padx=(10, 0))

    # --- FILA DE SEGURIDAD / ACCIÓN CRÍTICA (ZONA DE PELIGRO) ---
    danger_zone_frame = ctk.CTkFrame(sub_pag_db, fg_color="transparent")
    danger_zone_frame.pack(fill="x", padx=30, pady=(20, 0))

    btn_zona_peligro = ctk.CTkButton(danger_zone_frame, text="⚠️ Zona de Peligro (Formatear / Borrar Datos)", font=("Akt", 14, "bold"), fg_color="#360000", border_color="#800000", border_width=1, text_color="#FF9999", hover_color="#570000", height=42)
    btn_zona_peligro.pack(fill="x", expand=True)


    # --- INICIALIZACIÓN POR DEFECTO ---
    # Forzamos que al abrir configuración por primera vez, muestre Horarios en pantalla completa
    cambiar_pestana_config(sub_pag_horarios, btn_nav_horarios)


























    # ---------------- BOTONES ----------------

    frame_btn_emp = ctk.CTkFrame(
        frame_form_emp,
        fg_color="transparent"
    )
    frame_btn_emp.grid(
        row=12,
        column=0,
        columnspan=2,
        pady=30
    )

    btn_registrar = ctk.CTkButton(
        frame_btn_emp,
        text="Registrar Empleado",
        width=300,
        height=50,
        fg_color="#E02020",
        hover_color="#B00000",
        command=registrar_empleado
    )
    btn_registrar.grid(row=0, column=0, padx=10)

    btn_cancelar = ctk.CTkButton(
        frame_btn_emp,
        text="Cancelar",
        width=180,
        height=50,
        fg_color="#333333",
        hover_color="#555555",
        command=limpiar_formulario_empleado
    )
    btn_cancelar.grid(row=0, column=1, padx=10)

    diccionario_paginas = {
        "Estadisticas": pag_estadisticas,
        "Ingresos": pag_ingresos,
        "Nuevo Vehiculo": pag_nuevo_vehiculo,
        "Empleados": pag_empleados,
        "Gastos": pag_gastos,
        "Stock": pag_stock,
        "clientes": pag_clientes,
        "Nuevo Empleado": pag_nuevo_empleado,
        "Configuracion": pag_config
    }

    boton_activo = None

    def mostrar_contenido(nombre, boton):
        nonlocal boton_activo

        if boton_activo:
            boton_activo.configure(fg_color="transparent")

        boton.configure(fg_color="#920202")
        boton_activo = boton

        titulo_bienvenida.place_forget()

        for pag in diccionario_paginas.values():
            pag.pack_forget()

        if nombre in diccionario_paginas:
            diccionario_paginas[nombre].pack(fill="both", expand=True)
        else:
            print(f"Error: La sección '{nombre}' no está definida")

    btn_estadisticas = ctk.CTkButton(sidebar_frame, text="Estadisticas", height=30, width=100, font=("Akt", 18, "bold"), fg_color="transparent", hover_color="#920202", anchor="w", command=lambda: mostrar_contenido("Estadisticas", btn_estadisticas))
    btn_estadisticas.grid(row=2, column=0, padx=20, pady=3, sticky="ew")

    btn_ingresos = ctk.CTkButton(sidebar_frame, text="Ingresos", height=30, width=100, font=("Akt", 18, "bold"), fg_color="transparent", hover_color="#920202", anchor="w", command=lambda: mostrar_contenido("Ingresos", btn_ingresos))
    btn_ingresos.grid(row=3, column=0, padx=20, pady=3, sticky="ew")

    btn_gastos = ctk.CTkButton(sidebar_frame, text="Gastos", height=30, width=100, font=("Akt", 18, "bold"), fg_color="transparent", hover_color="#920202", anchor="w", command=lambda: mostrar_contenido("Gastos", btn_gastos))
    btn_gastos.grid(row=4, column=0, padx=20, pady=3, sticky="ew")

    btn_stock = ctk.CTkButton(sidebar_frame, text="Stock", height=30, width=100, font=("Akt", 18, "bold"), fg_color="transparent", hover_color="#920202", anchor="w", command=lambda: mostrar_contenido("Stock", btn_stock))
    btn_stock.grid(row=5, column=0, padx=20, pady=3, sticky="ew")

    btn_clientes = ctk.CTkButton(sidebar_frame, text="Clientes", height=30, width=100, font=("Akt", 18, "bold"), fg_color="transparent", hover_color="#920202", anchor="w", command=lambda: mostrar_contenido("clientes", btn_clientes))
    btn_clientes.grid(row=6, column=0, padx=20, pady=3, sticky="ew")

   
    btn_empleados = ctk.CTkButton(sidebar_frame, text="Empleados", height=30, width=100, font=("Akt", 18, "bold"), fg_color="transparent", hover_color="#920202", anchor="w", command=lambda: mostrar_contenido("Empleados", btn_empleados))
    btn_empleados.grid(row=8, column=0, padx=20, pady=3, sticky="ew")

    linea2 = ctk.CTkFrame(sidebar_frame, height=1.5, fg_color="#4E0000")
    linea2.grid(row=9, column=0, padx=20, pady=3, sticky="ew")

    btn_nvehiculo = ctk.CTkButton(sidebar_frame, text="Nuevo Vehiculo", height=30, width=100, font=("Akt", 18, "bold"), fg_color="transparent", hover_color="#920202", anchor="w", command=lambda: mostrar_contenido("Nuevo Vehiculo", btn_nvehiculo))
    btn_nvehiculo.grid(row=10, column=0, padx=20, pady=3, sticky="ew")

    btn_nempleado = ctk.CTkButton(sidebar_frame, text="Nuevo Empleado", height=30, width=100, font=("Akt", 18, "bold"), fg_color="transparent", hover_color="#920202", anchor="w", command=lambda: mostrar_contenido("Nuevo Empleado", btn_nempleado))
    btn_nempleado.grid(row=11, column=0, padx=20, pady=3, sticky="ew")

    linea3 = ctk.CTkFrame(sidebar_frame, height=1.5, fg_color="#4E0000")
    linea3.grid(row=12, column=0, padx=20, pady=3, sticky="ew")

    btn_config = ctk.CTkButton(sidebar_frame, text="Configuracion", height=30, width=100, font=("Akt", 18, "bold"), fg_color="transparent", hover_color="#920202", anchor="w", command=lambda: mostrar_contenido("Configuracion", btn_config))
    btn_config.grid(row=13, column=0, padx=20, pady=3, sticky="ew")

    btn_salir = ctk.CTkButton(sidebar_frame, text="Cerrar Sesión", height=40, width=250, font=("Akt", 18, "bold"), fg_color="#920202", hover_color="#000000", command=ventana.destroy)
    btn_salir.grid(row=15, column=0, padx=20, pady=20)

    ventana.focus()
    ventana.protocol("WM_DELETE_WINDOW", lambda: exit())

if __name__ == "__main__":
    pass
    