
from PyQt6.QtWidgets import QLabel, QPushButton, QLineEdit, QWidget, QDialog, QLineEdit, QMessageBox
from PyQt6.QtGui import QFont


class RegistrarUsuarioView(QDialog):
    def __init__(self):
        super().__init__()
        #con esto no podras interactuar con la otra pestaña hasta que se cierre esta
        self.setModal(True)
        self.Generar_Formulario()
        
    def Generar_Formulario(self):
        self.setGeometry(100,100,350,350)
        self.setWindowTitle("Registro")
        
        
        user_label = QLabel(self)
        user_label.setText("Usuario: ")
        user_label.setFont(QFont("Arial",10))
        user_label.move(20,44)
        
        self.user_input = QLineEdit(self)
        self.user_input.resize(250,24)
        self.user_input.move(90,40)
        
        password_label1 = QLabel(self)
        password_label1.setText("Password: ")
        password_label1.setFont(QFont("Arial",10))
        password_label1.move(20,74)
        
        self.user_password1 = QLineEdit(self)
        self.user_password1.resize(250,24)
        self.user_password1.move(90,70)
        self.user_password1.setEchoMode(QLineEdit.EchoMode.Password)
        
        
        self.user_password2 = QLineEdit(self)
        self.user_password2.resize(250,24)
        self.user_password2.move(90,100)
        self.user_password2.setEchoMode(QLineEdit.EchoMode.Password)
        
        
        password_label2 = QLabel(self)
        password_label2.setText("Password: ")
        password_label2.setFont(QFont("Arial",10))
        password_label2.move(20,104)
        
        create_Button = QPushButton(self)
        create_Button.setText("Crear")
        create_Button.resize(150,32)
        create_Button.move(20,170)
        create_Button.clicked.connect(self.cancelar_registro)
        
        
        cancel_Button = QPushButton(self)
        cancel_Button.setText("Cancelar")
        cancel_Button.resize(150,32)
        cancel_Button.move(170,170)
        cancel_Button.clicked.connect(self.crear_usuario)
       
        
    def crear_usuario(self):
        self.close()
        
    def cancelar_registro(self):
        user_path = "usuarios.txt"
        usuario = self.user_input.text()
        password1 = self.user_password1.text()
        password2 = self.user_password2.text()
        
        if password1 == "" or password2 == "" or usuario == "":
            QMessageBox.warning(self,"Error","Introduzca bien los datos",QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)
        elif password1 != password2:
            QMessageBox.warning(self,"Error","Las contraseñas no son iguales",QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)
        else:
            try:
                with open(user_path,"a+") as f:
                    f.write(f"{usuario},{password1}\n")
                    
                QMessageBox.information(self, "Creacion Exitosa","Usuario creado correctamente",QMessageBox.StandardButton.Ok,QMessageBox.StandardButton.Ok)
                self.close()
                
            except FileNotFoundError as e:
                
                QMessageBox.warning(self,"Error","La base de datos de usuario no existe: {e}",QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)
                
            
        