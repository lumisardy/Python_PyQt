
import sys
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout,QWidget,QApplication,QLineEdit,QLabel,QPushButton 

class MainWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        self.inicializarUI()
        
    def inicializarUI(self):
        self.setGeometry(100,100,400,150)
        self.setWindowTitle("Ventana")
        self.generar_formulario()
        self.show()
    
    def generar_formulario(self):
        
        mensaje_princip = QLabel("Intorduzca sus datos")
        nombre_label = QLabel("Nombres:")
        nombre_label.setFixedWidth(60)
        self.nombres_input = QLineEdit()
        apellidos_label = QLabel("Apellidos:")
        apellidos_label.setFixedWidth(60)
        self.apellidos_input = QLineEdit()
        Edad_label = QLabel("Edad:")
        Edad_label.setFixedWidth(60)
        self.Edad_input = QLineEdit()
        correo_label = QLabel("Correo:")
        correo_label.setFixedWidth(60)
        self.Correo_input = QLineEdit()
        direcion_label = QLabel("Direccion:")
        direcion_label.setFixedWidth(60)
        self.direccion_input = QLineEdit()
        telefono_label = QLabel("telefono:")
        telefono_label.setFixedWidth(60)
        self.telefono_input = QLineEdit()
        enviar_boton = QPushButton("Enviar")
        
        Vertical_layout = QVBoxLayout()
        Horizontal_layout1 = QHBoxLayout()
        Horizontal_layout2 = QHBoxLayout()
        Horizontal_layout3 = QHBoxLayout()
       
        
        Horizontal_layout1.addWidget(nombre_label)
        Horizontal_layout1.addWidget(self.nombres_input)
        Horizontal_layout1.addWidget(correo_label)
        Horizontal_layout1.addWidget(self.Correo_input)
        
        Horizontal_layout2.addWidget(apellidos_label)
        Horizontal_layout2.addWidget(self.apellidos_input)
        Horizontal_layout2.addWidget(direcion_label)
        Horizontal_layout2.addWidget(self.direccion_input)
        
        
        Horizontal_layout3.addWidget(Edad_label)
        Horizontal_layout3.addWidget(self.Edad_input)
        Horizontal_layout3.addWidget(telefono_label)
        Horizontal_layout3.addWidget(self.telefono_input)
        
        
        Vertical_layout.addWidget(mensaje_princip)
        
        Vertical_layout.addLayout(Horizontal_layout1)
        Vertical_layout.addLayout(Horizontal_layout2)
        Vertical_layout.addLayout(Horizontal_layout3)
        Vertical_layout.addWidget(enviar_boton)
        
        self.setLayout(Vertical_layout)
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    Ventana = MainWindow()
    sys.exit(app.exec())
        