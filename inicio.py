import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QMessageBox
)

# Función que se ejecuta al presionar el botón
def verificar_login():
    usuario = input_usuario.text()
    clave = input_clave.text()

    # Usuario y contraseña de prueba
    if usuario == "admin" and clave == "1234":
        QMessageBox.information(None, "Login correcto", "Bienvenido 😄")
    else:
        QMessageBox.warning(None, "Error", "Usuario o contraseña incorrectos")


# Crear aplicación
app = QApplication(sys.argv)

# Crear ventana
ventana = QWidget()
ventana.setWindowTitle("Login básico")
ventana.setGeometry(500, 200, 350, 200)

# Texto usuario
label_usuario = QLabel("Usuario:", ventana)
label_usuario.move(50, 40)

# Input usuario
input_usuario = QLineEdit(ventana)
input_usuario.move(120, 35)
input_usuario.resize(180, 30)

# Texto contraseña
label_clave = QLabel("Contraseña:", ventana)
label_clave.move(50, 90)

# Input contraseña
input_clave = QLineEdit(ventana)
input_clave.move(120, 85)
input_clave.resize(180, 30)
input_clave.setEchoMode(QLineEdit.Password)  # Oculta la contraseña

# Botón login
boton_login = QPushButton("Ingresar", ventana)
boton_login.move(120, 135)
boton_login.resize(100, 30)

# Conectar botón con función
boton_login.clicked.connect(verificar_login)

# Mostrar ventana
ventana.show()

# Ejecutar app
sys.exit(app.exec_())

ventana.show()   # mostrar ventana

sys.exit(app.exec_())   # ejecutar programa