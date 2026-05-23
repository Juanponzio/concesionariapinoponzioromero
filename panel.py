import customtkinter as ctk
from PIL import Image
from tkinter import messagebox, ttk

def abrir_panel():
    ventana = ctk.CTkToplevel()
    ventana.title("Sistema de Gestión - Concesionaria")
    ventana.geometry("1920x1080")
    ventana.configure(fg_color="#1E1E1E")
    ventana.state("zoomed")

    # Configurar el peso de las columnas para que el contenido se expanda
    ventana.grid_columnconfigure(1, weight=1)
    ventana.grid_rowconfigure(0, weight=1)


    # ================= BARRA LATERAL (SIDEBAR) =================
    sidebar_frame = ctk.CTkFrame(ventana, width=200, corner_radius=0, fg_color="#2B2B2B")

    
    sidebar_frame.grid(row=0, column=0, sticky="nsew")
    sidebar_frame.grid_rowconfigure(14   , weight=1) # Espacio flexible al final
# Creamos un frame de ancho 2 y el color que quieras (rojo o gris oscuro)
    border_line = ctk.CTkFrame(ventana, width=2, corner_radius=0, fg_color="#4E0000")
    border_line.grid(row=0, column=0, sticky="nse") # "nse" lo pega al Norte, Sur y ESTE (derecha)


    # Título o Logo en la barra lateral
   # --- CARGAR LOGO PARA EL PANEL ---
    # Nota: Asegúrate de que "logox.png" esté en la misma carpeta
    logo_image = ctk.CTkImage(
        light_image=Image.open("logox.png"),
        dark_image=Image.open("logox.png"),
        size=(200, 150) # Ajustá el tamaño a lo que necesites
    )

    # Mostrar el Logo en un Label
    logo_label = ctk.CTkLabel(
        sidebar_frame, 
        image=logo_image, 
        text=""
    )
    logo_label.grid(row=0, column=0, padx=20, pady=20)
# Línea divisoria roja (ajustá el color a tu gusto)
    linea = ctk.CTkFrame(
    sidebar_frame, 
    height=1.5,          # Grosor de la línea
    fg_color="#4E0000" # Color rojo de tu concesionaria
)

# La ubicamos en el grid
# Si 'Reportes' está en la fila 6, la línea va en la 7, y 'Nuevo Vehículo' en la 8
    linea.grid(row=1, column=0, padx=20, pady=3, sticky="ew")



# 1. Contenedor principal donde va a ocurrir la "magia"
    # (Ya lo tenés como main_content, pero asegúrate de que esté así)
    main_content = ctk.CTkFrame(ventana, corner_radius=15, fg_color="#1E1E1E")
    main_content.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

    titulo_bienvenida = ctk.CTkLabel(main_content, text="Bienvenido Ulises", font=("Akt",35,"bold"),)
    titulo_bienvenida.pack(pady=40)
    titulo_bienvenida.place(relx=0.4, rely=0.02)












    # 2. Creamos los frames de cada sección (como "páginas" invisibles)
    # Les ponemos colores distintos solo para probar que cambian
    secciones = {}
    
    pag_estadisticas = ctk.CTkFrame(main_content, fg_color="#1E1E1E")
    ctk.CTkLabel(pag_estadisticas, text="Panel de estadisticas", font=("Akt", 30, "bold")).pack(pady=20)
    
    
    pag_ingresos = ctk.CTkFrame(main_content, fg_color="#1E1E1E")
    ctk.CTkLabel(pag_ingresos, text="Gestion de Ingresos", font=("Akt", 30, "bold")).pack(pady=20)
    
  

    #================================Nuevo Vehiculo================================================================

# ---------------- FUNCIONES NUEVO VEHICULO ----------------

    def agregar_auto():
        # Usamos .get() de las variables que definiremos abajo
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

        # Insertar en la tabla visual
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

# ---------------- FUNCIONES NUEVO VEHICULO HASTA ACA ----------------





    pag_nuevo_vehiculo = ctk.CTkFrame(main_content, fg_color="transparent") # Usamos scrollable por si la pantalla es chica
    # Título
    ctk.CTkLabel(pag_nuevo_vehiculo, text="REGISTRO DE STOCK", font=("Akt", 32, "bold"), text_color="#ffffff").pack(pady=20)

    # Frame Formulario
    frame_form = ctk.CTkFrame(pag_nuevo_vehiculo, fg_color="#111111", corner_radius=15)
    frame_form.pack(padx=20, pady=10, fill="x")

    for i in range(4): frame_form.grid_columnconfigure(i, weight=1)

    # --- CAMPOS (Usamos variables globales para que las funciones las lean) ---
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

    # Frame Botones
    frame_botones = ctk.CTkFrame(pag_nuevo_vehiculo, fg_color="transparent")
    frame_botones.pack(pady=15)

    btn_agregar = ctk.CTkButton(frame_botones, text="Agregar Auto", command=agregar_auto, fg_color="#b30000", hover_color="#ff1a1a", font=("Akt", 15, "bold"))
    btn_agregar.grid(row=0, column=0, padx=15)

    btn_eliminar = ctk.CTkButton(frame_botones, text="Eliminar Auto", command=eliminar_auto, fg_color="#660000", hover_color="#cc0000", font=("Akt", 15, "bold"))
    btn_eliminar.grid(row=0, column=1, padx=15)

    # --- TABLA (TREEVIEW) ---
    # Aplicar el estilo que ya tenías definido
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



#================================Nuevo Vehiculo HASTA ACA=================================================================================================




    # Diccionario para encontrarlos fácil
    diccionario_paginas = {
        "Estadisticas": pag_estadisticas,
        "Ingresos": pag_ingresos,
        "Nuevo Vehiculo":pag_nuevo_vehiculo
    }




#====================funciones para mostrar y cambiar contenido===============================================
    boton_activo = None

    def mostrar_contenido(nombre, boton):
        nonlocal boton_activo
        
        # --- LÓGICA DE BOTONES ---
        if boton_activo:
            boton_activo.configure(fg_color="transparent")
        
        boton.configure(fg_color="#920202")
        boton_activo = boton

        # --- LÓGICA DE PANTALLAS ---
        # 1. Ocultamos el saludo inicial
        titulo_bienvenida.place_forget()

        # 2. Ocultamos todas las "páginas"
        for pag in diccionario_paginas.values():
            pag.pack_forget()

        # 3. Mostramos la que elegimos
        if nombre in diccionario_paginas:
            diccionario_paginas[nombre].pack(fill="both", expand=True)
        else:
            print(f"Error: La sección '{nombre}' no está definida en el diccionario.")



#====================funciones para mostrar y cambiar contenido HASTA ACA===============================================



    #========================================Botones del Menú===========================================================================



    btn_estadisticas = ctk.CTkButton(sidebar_frame, text="Estadisticas",height=50,width=100, font=("Akt",18,"bold"), fg_color="transparent", hover_color="#920202",anchor="w", 
                               command=lambda: (mostrar_contenido("Estadisticas", btn_estadisticas)) ) 
    btn_estadisticas.grid(row=2, column=0, padx=20, pady=3, sticky="ew")

    btn_ingresos = ctk.CTkButton(sidebar_frame, text="Ingresos",height=50,width=100,  font=("Akt",18,"bold"),fg_color="transparent", hover_color="#920202",anchor="w",
                               command=lambda:mostrar_contenido("Ingresos",btn_ingresos))
    btn_ingresos.grid(row=3, column=0, padx=20, pady=3, sticky="ew")

    btn_gastos = ctk.CTkButton(sidebar_frame, text="Gastos", height=50,width=100, font=("Akt",18,"bold"),fg_color="transparent",hover_color="#920202", anchor="w",
                              command=lambda:mostrar_contenido("Gastos",btn_gastos))
    btn_gastos.grid(row=4, column=0, padx=20, pady=3, sticky="ew")
    
    btn_stock = ctk.CTkButton(sidebar_frame, text="Stock", height=50,width=100, font=("Akt",18,"bold"),fg_color="transparent",hover_color="#920202", anchor="w",
                               command=lambda:mostrar_contenido("Stock",btn_stock))
    btn_stock.grid(row=5, column=0, padx=20, pady=3, sticky="ew")

    btn_clientes = ctk.CTkButton(sidebar_frame, text="Clientes", height=50,width=100, font=("Akt",18,"bold"),fg_color="transparent",hover_color="#920202", anchor="w",
                               command=lambda:mostrar_contenido("clientes",btn_clientes))
    btn_clientes.grid(row=6, column=0, padx=20, pady=3, sticky="ew")

    btn_reportes = ctk.CTkButton(sidebar_frame, text="Reportes", height=50,width=100, font=("Akt",18,"bold"),fg_color="transparent",hover_color="#920202", anchor="w",
                               command=lambda:mostrar_contenido("Reportes",btn_reportes))
    btn_reportes.grid(row=7, column=0, padx=20, pady=3, sticky="ew")  


    btn_empleados = ctk.CTkButton(sidebar_frame, text="Empleados", height=50,width=100, font=("Akt",18,"bold"),fg_color="transparent",hover_color="#920202", anchor="w",
                              command=lambda:mostrar_contenido("Empleados",btn_empleados))
    btn_empleados.grid(row=8, column=0, padx=20, pady=3, sticky="ew")  

#linea divisoria

# Línea divisoria roja (ajustá el color a tu gusto)
    linea = ctk.CTkFrame(
    sidebar_frame, 
    height=1.5,          # Grosor de la línea
    fg_color="#4E0000" # Color rojo de tu concesionaria
)

# La ubicamos en el grid
# Si 'Reportes' está en la fila 6, la línea va en la 7, y 'Nuevo Vehículo' en la 8
    linea.grid(row=9, column=0, padx=20, pady=3, sticky="ew")



    btn_nvehiculo = ctk.CTkButton(sidebar_frame, text="Nuevo Vehiculo", height=50,width=100, font=("Akt",18,"bold"),fg_color="transparent",hover_color="#920202", anchor="w",
                               command=lambda:mostrar_contenido("Nuevo Vehiculo",btn_nvehiculo))
    btn_nvehiculo.grid(row=10, column=0, padx=20, pady=3, sticky="ew")  


    btn_nempleado = ctk.CTkButton(sidebar_frame, text="Nuevo Empleado", height=50,width=100, font=("Akt",18,"bold"),fg_color="transparent",hover_color="#920202", anchor="w",
                                command=lambda:mostrar_contenido("Nuevo Empleado",btn_nempleado))
    btn_nempleado.grid(row=11, column=0, padx=20, pady=3, sticky="ew")  


# Línea divisoria roja (ajustá el color a tu gusto)
    linea2 = ctk.CTkFrame(
    sidebar_frame, 
    height=1.5,          # Grosor de la línea
    fg_color="#4E0000" # Color rojo de tu concesionaria
)

# La ubicamos en el grid
# Si 'Reportes' está en la fila 6, la línea va en la 7, y 'Nuevo Vehículo' en la 8
    linea2.grid(row=12, column=0, padx=20, pady=3, sticky="ew")

    btn_config = ctk.CTkButton(sidebar_frame, text="Configuracion", height=50,width=100, font=("Akt",18,"bold"),fg_color="transparent",hover_color="#920202", anchor="w",
                                command=lambda:mostrar_contenido("Configuracion",btn_config))
    btn_config.grid(row=13, column=0, padx=20, pady=3, sticky="ew")  




    # Botón Salir (al fondo)
    btn_salir = ctk.CTkButton(sidebar_frame, text="Cerrar Sesión", height=60,width=250, font=("Akt",18,"bold"),fg_color="#920202", hover_color="#000000",
                              command=ventana.destroy)
    btn_salir.grid(row=15, column=0, padx=20, pady=20)
    



    #========================================Botones del Menú HASTA ACA===========================================================================









    # ================= ÁREA DE CONTENIDO (MAIN CONTENT) =================

    titulo_bienvenida = ctk.CTkLabel(main_content, text="Bienvenido Ulises", font=("Akt",35,"bold"),)
    titulo_bienvenida.pack(pady=40)
    titulo_bienvenida.place(relx=0.4, rely=0.02)

    
 




    # Aquí puedes seguir agregando más widgets dentro de 'main_content'
    ventana.focus() # Hace que la ventana nueva tome el foco
    ventana.protocol("WM_DELETE_WINDOW", lambda: exit())