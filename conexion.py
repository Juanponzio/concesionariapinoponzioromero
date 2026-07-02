import sqlite3

def crear_base_de_datos():
    # 1. Conectar a la base de datos
    # Si el archivo 'concesionaria.db' no existe, Python lo creará automáticamente.
    conexion = sqlite3.connect('zalcas.db')
    
    # 2. Crear un cursor para ejecutar las sentencias SQL
    cursor = conexion.cursor()

    def obtener_vehiculos_de_db():
        conexion = sqlite3.connect('zalcas.db')
        cursor = conexion.cursor()
        # Traemos exactamente las columnas que usa tu grilla/vista
        cursor.execute("SELECT marca, modelo, anio, precio, tipo, color, km, motor, transmision, combustible, patente, vin, descripcion FROM vehiculos")
        filas = cursor.fetchall()
        conexion.close()
        return filas    



    def obtener_empleados_de_db():
        conexion = sqlite3.connect('zalcas.db')
        cursor = conexion.cursor()
        cursor.execute("SELECT id, nombre, apellido, DNI, puesto, turno, telefono FROM empleados")
        filas = cursor.fetchall()
        conexion.close()
        return filas

def eliminar_auto_db(id_auto):
    """Borra un auto de la base de datos según su ID."""
    try:
        conexion = sqlite3.connect("zalcas.db")
        cursor = conexion.cursor()
        
        # Ejecutamos el DELETE
        cursor.execute("DELETE FROM autos WHERE id = ?", (id_auto,))
        
        conexion.commit()
        conexion.close()
        return True # Retorna True si todo salió bien
    except sqlite3.Error as e:
        print(f"Error en la base de datos: {e}")
        return False # Retorna False si hubo un error

    
    
    # 5. Guardar los cambios y cerrar la conexión
    conexion.commit()
    conexion.close()
    
print("éxito!")

# Ejecutar la función
if __name__ == '__main__':
    crear_base_de_datos()