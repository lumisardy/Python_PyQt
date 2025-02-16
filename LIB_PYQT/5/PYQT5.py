import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QFormLayout, QPushButton, QLineEdit, QComboBox, QHBoxLayout, QMessageBox, QDateEdit)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt, QDate

class Mainwindow(QWidget):
    
    
    def __init__(self):
        super().__init__()
        self.inicializate()
        
    def inicializate(self):
        self.setGeometry(100,100,300,300)
        self.setWindowTitle("Formulario")
        self.crearformulario()
        self.show()
        
    def crearformulario(self):
        Titulo = QLabel("Solicitud del ingreso")
        Titulo.setFont(QFont("Arial",18))
        
        #esto es para colocarlo en el centro
        Titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.nombre_edit = QLineEdit()
        # esto es para decir que tiene que poner
        self.nombre_edit.setPlaceholderText("Nombre")
        self.apellido_edit = QLineEdit()
        self.apellido_edit.setPlaceholderText("Apellido")
        
        self.genero_select = QComboBox()
        self.genero_select.addItems(["Masculino","Femenino"])
        
        self.Fecha_Nacimiento = QDateEdit()
        self.Fecha_Nacimiento.setDisplayFormat("yyyy-mm-dd")
        self.Fecha_Nacimiento.setMaximumDate(QDate.currentDate())
        
        
        self.Fecha_Nacimiento.setCalendarPopup(True)
        self.Fecha_Nacimiento.setDate(QDate.currentDate())
        
        self.telefono = QLineEdit()
        self.telefono.setPlaceholderText("605-8768763")
        
        sumbit_button = QPushButton("Sumbit")
        sumbit_button.clicked.connect(self.mostrar_info)
        
        Primer_h_layaout = QHBoxLayout()
        Primer_h_layaout.addWidget(self.nombre_edit)
        Primer_h_layaout.addWidget(self.apellido_edit)
        
        Main_form = QFormLayout()
        Main_form.addRow(Titulo)
        Main_form.addRow("Nombre: ",Primer_h_layaout)
        Main_form.addRow("Genero: ",self.genero_select)
        Main_form.addRow("Fecha: ",self.Fecha_Nacimiento)
        Main_form.addRow("Telefono: ", self.telefono)
        Main_form.addRow(sumbit_button)
        
        self.setLayout(Main_form)
        
        
    def mostrar_info(self):
        QMessageBox.information(self,"Informacion",f"Nombre: {self.nombre_edit.text()}{self.apellido_edit.text()}\n \
                                    Genero : {self.genero_select.currentText()}\n \
                                    Fecha:  {self.Fecha_Nacimiento.text()}\n \
                                    Relefono: {self.telefono.text() }",QMessageBox.StandardButton.Ok,QMessageBox.StandardButton.Ok)
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Mainwindow()
    sys.exit(app.exec())
    