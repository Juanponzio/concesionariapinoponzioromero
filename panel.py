import customtkinter as ctk
from PIL import Image
from tkinter import messagebox, ttk

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
    pag_estadisticas = ctk.CTkFrame(main_content, fg_color="#1E1E1E")
    ctk.CTkLabel(pag_estadisticas, text="Panel de estadisticas", font=("Akt", 30, "bold")).pack(pady=20)

    pag_ingresos = ctk.CTkFrame(main_content, fg_color="#1E1E1E")
    ctk.CTkLabel(pag_ingresos, text="Gestion de Ingresos", font=("Akt", 30, "bold")).pack(pady=20)

    pag_gastos = ctk.CTkFrame(main_content, fg_color="#1E1E1E")
    ctk.CTkLabel(pag_gastos, text="Gestión de Gastos", font=("Akt", 30, "bold")).pack(pady=20)

    pag_stock = ctk.CTkFrame(main_content, fg_color="#1E1E1E")
    ctk.CTkLabel(pag_stock, text="Gestión de Stock", font=("Akt", 30, "bold")).pack(pady=20)

    pag_clientes = ctk.CTkFrame(main_content, fg_color="#1E1E1E")
    ctk.CTkLabel(pag_clientes, text="Gestión de Clientes", font=("Akt", 30, "bold")).pack(pady=20)

    pag_reportes = ctk.CTkFrame(main_content, fg_color="#1E1E1E")
    ctk.CTkLabel(pag_reportes, text="Reportes", font=("Akt", 30, "bold")).pack(pady=20)

    pag_nuevo_empleado = ctk.CTkFrame(main_content, fg_color="#1E1E1E")
    ctk.CTkLabel(pag_nuevo_empleado, text="Nuevo Empleado", font=("Akt", 30, "bold")).pack(pady=20)

    pag_configuracion = ctk.CTkFrame(main_content, fg_color="#1E1E1E")
    ctk.CTkLabel(pag_configuracion, text="Configuración", font=("Akt", 30, "bold")).pack(pady=20)

   
   
   
   
   

   
   
   
    # ================= NUEVO VEHÍCULO =================
    def agregar_auto():
        marca = entry_marca.get()
        modelo = entry_modelo.get()
        kilometraje = entry_km.get()
        transmision = combo_transmision.get()
        direccion = combo_direccion.get()
        segmento = combo_segmento.get()
        cilindrada = entry_cilindrada.get()

        if not all([marca, modelo, kilometraje, transmision, direccion, segmento, cilindrada]):
            messagebox.showerror("Error", "Completa todos los campos")
            return

        tabla.insert("", "end", values=(marca, modelo, kilometraje, transmision, direccion, segmento, cilindrada))
        limpiar_campos()
        messagebox.showinfo("Éxito", "Auto agregado al stock")

    def limpiar_campos():
        entry_marca.delete(0, "end")
        entry_modelo.delete(0, "end")
        entry_km.delete(0, "end")
        entry_cilindrada.delete(0, "end")
        combo_transmision.set("")
        combo_direccion.set("")
        combo_segmento.set("")

    def eliminar_auto():
        seleccionado = tabla.selection()
        if not seleccionado:
            messagebox.showwarning("Atención", "Selecciona un auto")
            return
        tabla.delete(seleccionado)
        messagebox.showinfo("Eliminado", "Auto eliminado")

    pag_nuevo_vehiculo = ctk.CTkFrame(main_content, fg_color="transparent")
    ctk.CTkLabel(pag_nuevo_vehiculo, text="REGISTRO DE STOCK", font=("Akt", 32, "bold"), text_color="#ffffff").pack(pady=20)

    frame_form = ctk.CTkFrame(pag_nuevo_vehiculo, fg_color="#111111", corner_radius=15)
    frame_form.pack(padx=20, pady=10, fill="x")

    for i in range(4):
        frame_form.grid_columnconfigure(i, weight=1)

    # Fila 0: Marca y Modelo
    ctk.CTkLabel(frame_form, text="Marca", font=("Akt", 14, "bold")).grid(row=0, column=0, padx=10, pady=10)
    entry_marca = ctk.CTkEntry(frame_form, width=200, fg_color="#1a1a1a", border_width=0)
    entry_marca.grid(row=0, column=1)

    ctk.CTkLabel(frame_form, text="Modelo", font=("Akt", 14, "bold")).grid(row=0, column=2, padx=10, pady=10)
    entry_modelo = ctk.CTkEntry(frame_form, width=200, fg_color="#1a1a1a", border_width=0)
    entry_modelo.grid(row=0, column=3)

    # Fila 1: KM y Transmisión
    ctk.CTkLabel(frame_form, text="Kilometraje", font=("Akt", 14, "bold")).grid(row=1, column=0, padx=10, pady=10)
    entry_km = ctk.CTkEntry(frame_form, width=200, fg_color="#1a1a1a", border_width=0)
    entry_km.grid(row=1, column=1)

    ctk.CTkLabel(frame_form, text="Transmisión", font=("Akt", 14, "bold")).grid(row=1, column=2, padx=10, pady=10)
    combo_transmision = ctk.CTkComboBox(frame_form, values=["Manual", "Automática"], width=200, fg_color="#1a1a1a", button_color="#990000", border_width=0)
    combo_transmision.grid(row=1, column=3)

    # Fila 2: Dirección y Segmento
    ctk.CTkLabel(frame_form, text="Dirección", font=("Akt", 14, "bold")).grid(row=2, column=0, padx=10, pady=10)
    combo_direccion = ctk.CTkComboBox(frame_form, values=["Hidráulica", "Eléctrica", "Mecánica"], width=200, fg_color="#1a1a1a", button_color="#990000", border_width=0)
    combo_direccion.grid(row=2, column=1)

    ctk.CTkLabel(frame_form, text="Segmento", font=("Akt", 14, "bold")).grid(row=2, column=2, padx=10, pady=10)
    combo_segmento = ctk.CTkComboBox(frame_form, values=["Sedán", "SUV", "Pickup", "Hatchback", "Deportivo"], width=200, fg_color="#1a1a1a", button_color="#990000", border_width=0)
    combo_segmento.grid(row=2, column=3)

    # Fila 3: Cilindrada
    ctk.CTkLabel(frame_form, text="Cilindrada", font=("Akt", 14, "bold")).grid(row=3, column=0, padx=10, pady=10)
    entry_cilindrada = ctk.CTkEntry(frame_form, width=200, fg_color="#1a1a1a", border_width=0)
    entry_cilindrada.grid(row=3, column=1)

    # Botones
    frame_botones = ctk.CTkFrame(pag_nuevo_vehiculo, fg_color="transparent")
    frame_botones.pack(pady=15)

    btn_agregar = ctk.CTkButton(frame_botones, text="Agregar Auto", command=agregar_auto, fg_color="#b30000", hover_color="#ff1a1a", font=("Akt", 15, "bold"))
    btn_agregar.grid(row=0, column=0, padx=15)

    btn_eliminar = ctk.CTkButton(frame_botones, text="Eliminar Auto", command=eliminar_auto, fg_color="#660000", hover_color="#cc0000", font=("Akt", 15, "bold"))
    btn_eliminar.grid(row=0, column=1, padx=15)

    # Tabla
    style = ttk.Style()
    style.theme_use("default")
    style.configure("Treeview", background="#0b0b0b", foreground="white", fieldbackground="#0b0b0b", rowheight=40, borderwidth=0)
    style.configure("Treeview.Heading", background="#990000", foreground="white", relief="flat")
    style.map("Treeview", background=[("selected", "#cc0000")])

    columnas = ("Marca", "Modelo", "KM", "Transmisión", "Dirección", "Segmento", "Cilindrada")
    tabla = ttk.Treeview(pag_nuevo_vehiculo, columns=columnas, show="headings", height=10)
    for col in columnas:
        tabla.heading(col, text=col)
        tabla.column(col, width=100, anchor="center")
    tabla.pack(fill="both", expand=True, padx=20, pady=10)

  
  
  
  
  
  
  
  
  
    # ================= EMPLEADOS =================
    empleados_data = [
        ("Carlos Zalcas", "Gerente General", "Administración", "carlos@zalcas.com", "2020-01-15", "$120.000"),
        ("Ana Martínez", "Vendedor Senior", "Ventas", "ana@zalcas.com", "2021-03-10", "$65.000"),
        ("Roberto Silva", "Mecánico", "Servicio Técnico", "roberto@zalcas.com", "2021-06-20", "$55.000"),
    ]

    def cargar_empleados():
        for item in tabla_empleados.get_children():
            tabla_empleados.delete(item)
        for empleado in empleados_data:
            tabla_empleados.insert("", "end", values=empleado)

    def buscar_empleado(event=None):
        filtro = buscador_empleados.get().lower()
        for item in tabla_empleados.get_children():
            tabla_empleados.delete(item)
        for empleado in empleados_data:
            if filtro in empleado[0].lower() or filtro in empleado[1].lower():
                tabla_empleados.insert("", "end", values=empleado)

    def eliminar_empleado():
        seleccionado = tabla_empleados.selection()
        if not seleccionado:
            messagebox.showwarning("Atención", "Selecciona un empleado")
            return
        tabla_empleados.delete(seleccionado)
        messagebox.showinfo("Éxito", "Empleado eliminado")

    pag_empleados = ctk.CTkFrame(main_content, fg_color="#1E1E1E")

    titulo_emp = ctk.CTkLabel(pag_empleados, text="Empleados", font=("Akt", 34, "bold"), text_color="white")
    titulo_emp.pack(anchor="w", padx=20, pady=(20, 5))

    subtitulo_emp = ctk.CTkLabel(pag_empleados, text="Gestión de personal y recursos humanos", font=("Akt", 16), text_color="#AAAAAA")
    subtitulo_emp.pack(anchor="w", padx=20)

    # Tarjetas
    cards_frame = ctk.CTkFrame(pag_empleados, fg_color="transparent")
    cards_frame.pack(fill="x", padx=20, pady=20)
    cards_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)

    def crear_card(parent, titulo, valor, extra=""):
        card = ctk.CTkFrame(parent, fg_color="#161616", border_width=1, border_color="#5A0000", corner_radius=15, height=130)
        label_titulo = ctk.CTkLabel(card, text=titulo, font=("Akt", 18), text_color="#BFBFBF")
        label_titulo.pack(anchor="w", padx=20, pady=(20, 5))
        label_valor = ctk.CTkLabel(card, text=valor, font=("Akt", 36, "bold"), text_color="white")
        label_valor.pack(anchor="w", padx=20)
        if extra:
            extra_label = ctk.CTkLabel(card, text=extra, font=("Akt", 14), text_color="#00CC66")
            extra_label.pack(anchor="w", padx=20)
        return card

    card1 = crear_card(cards_frame, "Total Empleados", "6", "+2 este mes")
    card1.grid(row=0, column=0, padx=10, sticky="ew")

    card2 = crear_card(cards_frame, "Departamentos", "5")
    card2.grid(row=0, column=1, padx=10, sticky="ew")

    card3 = crear_card(cards_frame, "Nómina Mensual", "$400k")
    card3.grid(row=0, column=2, padx=10, sticky="ew")

    card4 = crear_card(cards_frame, "Salario Promedio", "$67k")
    card4.grid(row=0, column=3, padx=10, sticky="ew")

    # Tabla contenedor
    tabla_container = ctk.CTkFrame(pag_empleados, fg_color="#161616", corner_radius=20, border_width=1, border_color="#2D2D2D")
    tabla_container.pack(fill="both", expand=True, padx=20, pady=10)

    top_frame = ctk.CTkFrame(tabla_container, fg_color="transparent")
    top_frame.pack(fill="x", padx=20, pady=20)

    buscador_empleados = ctk.CTkEntry(top_frame, placeholder_text="Buscar por nombre o puesto...", height=45, fg_color="#101010", border_color="#5A0000", text_color="white")
    buscador_empleados.pack(side="left", fill="x", expand=True, padx=(0, 20))
    buscador_empleados.bind("<KeyRelease>", buscar_empleado)

    filtro_combo = ctk.CTkComboBox(top_frame, values=["Todos", "Ventas", "Administración", "Servicio Técnico"], width=180, height=45, fg_color="#101010", button_color="#5A0000", border_color="#5A0000")
    filtro_combo.set("Todos")
    filtro_combo.pack(side="right")

    # Tabla de empleados
    style.configure("empleados.Treeview", background="#161616", foreground="white", fieldbackground="#161616", rowheight=45, borderwidth=0, font=("Akt", 12))
    style.configure("empleados.Treeview.Heading", background="#1F1F1F", foreground="white", relief="flat", font=("Akt", 13, "bold"))
    style.map("empleados.Treeview", background=[("selected", "#920202")])

    columnas_empleados = ("Nombre", "Puesto", "Departamento", "Contacto", "Fecha Ingreso", "Salario")
    tabla_empleados = ttk.Treeview(tabla_container, columns=columnas_empleados, show="headings", style="empleados.Treeview", height=15)

    for col in columnas_empleados:
        tabla_empleados.heading(col, text=col)
        tabla_empleados.column(col, anchor="center", width=180)

    tabla_empleados.pack(fill="both", expand=True, padx=20, pady=(0, 20))
    cargar_empleados()

    # ================= DICCIONARIO DE PÁGINAS =================
    diccionario_paginas = {
        "Estadisticas": pag_estadisticas,
        "Ingresos": pag_ingresos,
        "Nuevo Vehiculo": pag_nuevo_vehiculo,
        "Empleados": pag_empleados,
        "Gastos": pag_gastos,
        "Stock": pag_stock,
        "clientes": pag_clientes,
        "Reportes": pag_reportes,
        "Nuevo Empleado": pag_nuevo_empleado,
        "Configuracion": pag_configuracion
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

























    # ================= BOTONES DEL MENÚ =================
    btn_estadisticas = ctk.CTkButton(sidebar_frame, text="Estadisticas", height=50, width=100, font=("Akt", 18, "bold"), fg_color="transparent", hover_color="#920202", anchor="w", command=lambda: mostrar_contenido("Estadisticas", btn_estadisticas))
    btn_estadisticas.grid(row=2, column=0, padx=20, pady=3, sticky="ew")

    btn_ingresos = ctk.CTkButton(sidebar_frame, text="Ingresos", height=50, width=100, font=("Akt", 18, "bold"), fg_color="transparent", hover_color="#920202", anchor="w", command=lambda: mostrar_contenido("Ingresos", btn_ingresos))
    btn_ingresos.grid(row=3, column=0, padx=20, pady=3, sticky="ew")

    btn_gastos = ctk.CTkButton(sidebar_frame, text="Gastos", height=50, width=100, font=("Akt", 18, "bold"), fg_color="transparent", hover_color="#920202", anchor="w", command=lambda: mostrar_contenido("Gastos", btn_gastos))
    btn_gastos.grid(row=4, column=0, padx=20, pady=3, sticky="ew")

    btn_stock = ctk.CTkButton(sidebar_frame, text="Stock", height=50, width=100, font=("Akt", 18, "bold"), fg_color="transparent", hover_color="#920202", anchor="w", command=lambda: mostrar_contenido("Stock", btn_stock))
    btn_stock.grid(row=5, column=0, padx=20, pady=3, sticky="ew")

    btn_clientes = ctk.CTkButton(sidebar_frame, text="Clientes", height=50, width=100, font=("Akt", 18, "bold"), fg_color="transparent", hover_color="#920202", anchor="w", command=lambda: mostrar_contenido("clientes", btn_clientes))
    btn_clientes.grid(row=6, column=0, padx=20, pady=3, sticky="ew")

    btn_reportes = ctk.CTkButton(sidebar_frame, text="Reportes", height=50, width=100, font=("Akt", 18, "bold"), fg_color="transparent", hover_color="#920202", anchor="w", command=lambda: mostrar_contenido("Reportes", btn_reportes))
    btn_reportes.grid(row=7, column=0, padx=20, pady=3, sticky="ew")

    btn_empleados = ctk.CTkButton(sidebar_frame, text="Empleados", height=50, width=100, font=("Akt", 18, "bold"), fg_color="transparent", hover_color="#920202", anchor="w", command=lambda: mostrar_contenido("Empleados", btn_empleados))
    btn_empleados.grid(row=8, column=0, padx=20, pady=3, sticky="ew")

    linea2 = ctk.CTkFrame(sidebar_frame, height=1.5, fg_color="#4E0000")
    linea2.grid(row=9, column=0, padx=20, pady=3, sticky="ew")

    btn_nvehiculo = ctk.CTkButton(sidebar_frame, text="Nuevo Vehiculo", height=50, width=100, font=("Akt", 18, "bold"), fg_color="transparent", hover_color="#920202", anchor="w", command=lambda: mostrar_contenido("Nuevo Vehiculo", btn_nvehiculo))
    btn_nvehiculo.grid(row=10, column=0, padx=20, pady=3, sticky="ew")

    btn_nempleado = ctk.CTkButton(sidebar_frame, text="Nuevo Empleado", height=50, width=100, font=("Akt", 18, "bold"), fg_color="transparent", hover_color="#920202", anchor="w", command=lambda: mostrar_contenido("Nuevo Empleado", btn_nempleado))
    btn_nempleado.grid(row=11, column=0, padx=20, pady=3, sticky="ew")

    linea3 = ctk.CTkFrame(sidebar_frame, height=1.5, fg_color="#4E0000")
    linea3.grid(row=12, column=0, padx=20, pady=3, sticky="ew")

    btn_config = ctk.CTkButton(sidebar_frame, text="Configuracion", height=50, width=100, font=("Akt", 18, "bold"), fg_color="transparent", hover_color="#920202", anchor="w", command=lambda: mostrar_contenido("Configuracion", btn_config))
    btn_config.grid(row=13, column=0, padx=20, pady=3, sticky="ew")

    btn_salir = ctk.CTkButton(sidebar_frame, text="Cerrar Sesión", height=60, width=250, font=("Akt", 18, "bold"), fg_color="#920202", hover_color="#000000", command=ventana.destroy)
    btn_salir.grid(row=15, column=0, padx=20, pady=20)

    ventana.focus()
    ventana.protocol("WM_DELETE_WINDOW", lambda: exit())

if __name__ == "__main__":
    pass