
#Librerias nuevas Qlabel: se utiliza para mostrar texto
# QlineEdit:  Permite al usuario ingresar y editar una única línea de texto.
# Qpushbutton:  puede ser clicado por el usuario para realizar una acción.
# QmessageBox: muestra mensajes de información, advertencia, error, preguntas o notas al usuario
# Qchekbox: representa una casilla de verificación, que el usuario puede marcar o desmarcar.
# Qfont: configurar la familia de fuentes, el tamaño, el estilo (negrita, cursiva, etc.)
# Qpixmap: diseñada para mostrar imágenes en widgets como QLabel.
import sys
import subprocess
try:
    from PyQt6.QtCore import Qt
    from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QLineEdit, QPushButton, QMessageBox, QCheckBox
    from PyQt6.QtGui import QFont
except ImportError:
    # Si PyQt6 no está instalado, instalarlo automáticamente
    print("PyQt6 no está instalado. Instalando ahora...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "PyQt6"])
    print("PyQt6 instalado con éxito. Reinicia el programa.")
    sys.exit()


from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QLineEdit, QPushButton, QMessageBox, QCheckBox
from PyQt6.QtGui import QFont, QPixmap
from PYQT2Registro import RegistrarUsuarioView
from PYQT2Main import MainWindow

class login(QWidget):
    def __init__(self) :
        super().__init__()
        self.inicializar_ui()
        
    def inicializar_ui(self):
        self.setGeometry(300,300,450,450)
        self.setWindowTitle("LOGIN")
        self.GenerarFormulario()
        self.show()
       
    def GenerarFormulario(self):
        
        self.is_logged = False
        user_label = QLabel(self)
        user_label.setText("Usuario: ")
        user_label.setFont(QFont("Arial",10))
        user_label.move(20,54)
        
        self.user_input = QLineEdit(self)
        self.user_input.resize(250,24)
        self.user_input.move(90,50)
        
        password_label = QLabel(self)
        password_label.setText("Password: ")
        password_label.setFont(QFont("Arial",10))
        password_label.move(20,86)
        
        self.password_input = QLineEdit(self)
        self.password_input.resize(250,24)
        self.password_input.move(90,82)
        # Esto es para que el apartado se vea con asteriscos
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        
        
        self.check_view_password = QCheckBox(self)  # Nombre corregido aquí
        self.check_view_password.setText("Ver contraseña")  # Nombre corregido aquí
        self.check_view_password.move(90,110)
        self.check_view_password.toggled.connect(self.mostrar_contrasena)
        
        
        login_button = QPushButton(self)
        login_button.setText("Login")
        login_button.resize(320,24)
        login_button.move(20,140)
        login_button.clicked.connect(self.login)
        
        
        register_button = QPushButton(self)
        register_button.setText("Registrarse")
        register_button.resize(320,24)
        register_button.move(20,170)
        register_button.clicked.connect(self.registrar_usuario)
        

    def mostrar_contrasena(self,clicked):
    
        if clicked:
            self.password_input.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
            
            
    def login(self):
        users = []
        user_path = "usuarios.txt"
        
        try:
            with open(user_path,"r") as f:
                for line in f:
                    users.append(line.strip("\n"))
            login_information = f"{self.user_input.text()},{self.password_input.text()}"
            
            if login_information in users:
                QMessageBox.information(self,"Inicio sesion,","Inicio de sesion exitosa", QMessageBox.StandardButton.Ok,QMessageBox.StandardButton.Ok)
                self.is_logged = True
                self.close()
                self.open_Main_Window()
                
            else:
                QMessageBox.warning(self,"Error","Credenciales incorrectas",QMessageBox.StandardButton.Close, QMessageBox.StandardButton.Close)
                
        except FileNotFoundError as e:
            QMessageBox.warning(self,"Error","Base de datos de usario no encontrada",QMessageBox.StandardButton.Close, QMessageBox.StandardButton.Close)
            
        except Exception as e:
            QMessageBox.warning(self,"Error","Error en el servidor",QMessageBox.StandardButton.Close, QMessageBox.StandardButton.Close)
            
            
            
        
    
    
    def registrar_usuario(self):
        self.new_user_form = RegistrarUsuarioView()
        self.new_user_form.show()
    
    def open_Main_Window(self):
        self.main_window = MainWindow()
        self.main_window.show()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    Login = login()
    sys.exit(app.exec())
