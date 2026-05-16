import customtkinter as ctk
from PIL import Image

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
        size=(150, 100) # Ajustá el tamaño a lo que necesites
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


    # Botones del Menú
    btn_estadisticas = ctk.CTkButton(sidebar_frame, text="Estadisticas",height=50,width=100, fg_color="transparent", hover_color="#920202",anchor="w", 
                               command=lambda: print("Click en Inicio"))
    btn_estadisticas.grid(row=2, column=0, padx=20, pady=3, sticky="ew")

    btn_ingresos = ctk.CTkButton(sidebar_frame, text="Ingresos",height=50,width=100, fg_color="transparent", hover_color="#920202",anchor="w",
                              command=lambda: print("Click en Ingresos"))
    btn_ingresos.grid(row=3, column=0, padx=20, pady=3, sticky="ew")

    btn_gastos = ctk.CTkButton(sidebar_frame, text="Gastos", height=50,width=100,fg_color="transparent",hover_color="#920202", anchor="w",
                               command=lambda: print("Click en Gastos"))
    btn_gastos.grid(row=4, column=0, padx=20, pady=3, sticky="ew")
    
    btn_stock = ctk.CTkButton(sidebar_frame, text="Stock", height=50,width=100,fg_color="transparent",hover_color="#920202", anchor="w",
                               command=lambda: print("Click en Stock"))
    btn_stock.grid(row=5, column=0, padx=20, pady=3, sticky="ew")

    btn_clientes = ctk.CTkButton(sidebar_frame, text="Clientes", height=50,width=100,fg_color="transparent",hover_color="#920202", anchor="w",
                               command=lambda: print("Click en Clientes"))
    btn_clientes.grid(row=6, column=0, padx=20, pady=3, sticky="ew")

    btn_reportes = ctk.CTkButton(sidebar_frame, text="Reportes", height=50,width=100,fg_color="transparent",hover_color="#920202", anchor="w",
                               command=lambda: print("Click en Reportes"))
    btn_reportes.grid(row=7, column=0, padx=20, pady=3, sticky="ew")  


    btn_empleados = ctk.CTkButton(sidebar_frame, text="Empleados", height=50,width=100,fg_color="transparent",hover_color="#920202", anchor="w",
                               command=lambda: print("Click en Empleados"))
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



    btn_nvehiculo = ctk.CTkButton(sidebar_frame, text="Nuevo Vehiculo", height=50,width=100,fg_color="transparent",hover_color="#920202", anchor="w",
                               command=lambda: print("Click en Nuevo Vehiculo"))
    btn_nvehiculo.grid(row=10, column=0, padx=20, pady=3, sticky="ew")  


    btn_nempleado = ctk.CTkButton(sidebar_frame, text="Nuevo Empleado", height=50,width=100,fg_color="transparent",hover_color="#920202", anchor="w",
                               command=lambda: print("Click en Nuevo Empleado"))
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

    btn_config = ctk.CTkButton(sidebar_frame, text="Configuracion", height=50,width=100,fg_color="transparent",hover_color="#920202", anchor="w",
                               command=lambda: print("Click en Configuracion"))
    btn_config.grid(row=13, column=0, padx=20, pady=3, sticky="ew")  




    # Botón Salir (al fondo)
    btn_salir = ctk.CTkButton(sidebar_frame, text="Cerrar Sesión", height=60,width=250, fg_color="#920202", hover_color="#000000",
                              command=ventana.destroy)
    btn_salir.grid(row=15, column=0, padx=20, pady=2+0)
    












    # ================= ÁREA DE CONTENIDO (MAIN CONTENT) =================
    main_content = ctk.CTkFrame(ventana, corner_radius=15, fg_color="#1E1E1E")
    main_content.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

    titulo_bienvenida = ctk.CTkLabel(main_content, text="Estadisticas Generales", font=("Segoe UI", 30))
    titulo_bienvenida.pack(pady=40)
    titulo_bienvenida.place(relx=0.02, rely=0.02)

    # Aquí puedes seguir agregando más widgets dentro de 'main_content'
    ventana.focus() # Hace que la ventana nueva tome el foco

    ventana.protocol("WM_DELETE_WINDOW", lambda: exit())