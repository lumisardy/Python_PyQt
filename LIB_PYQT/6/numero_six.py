import sys

from PyQt6.QtWidgets import (QWidget,QLabel,QTextEdit,QMessageBox,QApplication,QPushButton,QFormLayout,QVBoxLayout,QHBoxLayout,QComboBox,QDateEdit,QLineEdit,QStackedLayout)
from PyQt6.QtGui import QFont,QPixmap
from PyQt6.QtCore import Qt,QDate

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializate()
    
    
    def inicializate(self):
        self.setFixedSize(500,580)
        self.setWindowTitle("Ventana")
        self.show()
        self.Crear_formulario()
        
    def Crear_formulario(self):
        
        boton1 = QPushButton("Ventana 1")
        boton2 = QPushButton("Ventana 2")
        boton3 = QPushButton("Ventana 3")
        boton1.clicked.connect(self.change_window)
        boton2.clicked.connect(self.change_window)
        boton3.clicked.connect(self.change_window)
        
        buttons_group = QHBoxLayout()
        buttons_group.addWidget(boton1)
        buttons_group.addWidget(boton2)
        buttons_group.addWidget(boton3)
        
        #Pagina 1
        tittle = QLabel("España")
        tittle.setFont(QFont("Arial", 18))
        tittle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        image_map = QLabel()
        pixmap = QPixmap("PYQT/6/espana")
        image_map.setPixmap(pixmap)
        #obtener tamaño de la ventana
        window_size = self.size()
        image_map.setMaximumSize(window_size)
        image_map.setScaledContents(True)
        
        page1 = QVBoxLayout()
        
        page1.addWidget(tittle)
        page1.addWidget(image_map)
        
        
        container1 = QWidget()
        container1.setLayout(page1)
        
        #page 2 
        
        
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
        
        container2 = QWidget()
        container2.setLayout(Main_form)
        
        #pagina 3 
        
        tittle3 = QLabel("Observaciones")
        tittle3.setFont(QFont("Arial",18))
        tittle3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.observation = QTextEdit()
        form3 = QFormLayout()
        form3.addRow(tittle3)
        form3.addRow("Observations", self.observation)
        
        container3 = QWidget()
        container3.setLayout(form3)
        
        self.stacked_layaout = QStackedLayout()
        self.stacked_layaout.addWidget(container1)
        self.stacked_layaout.addWidget(container2)
        self.stacked_layaout.addWidget(container3)
        
        main_layaout = QVBoxLayout()
        main_layaout.addLayout(buttons_group)
        main_layaout.addLayout(self.stacked_layaout)
        self.setLayout(main_layaout)
        
    
    def mostrar_info(self):
        QMessageBox.information(self,"Informacion",f"Nombre: {self.nombre_edit.text()}{self.apellido_edit.text()}\n \
                                    Genero : {self.genero_select.currentText()}\n \
                                    Fecha:  {self.Fecha_Nacimiento.text()}\n \
                                    Telefono: {self.telefono.text() }",QMessageBox.StandardButton.Ok,QMessageBox.StandardButton.Ok)
    
    def change_window(self):
        button = self.sender()
        if button.text().lower() == "ventana 1":
            self.stacked_layaout.setCurrentIndex(0)
        elif button.text().lower() == "ventana 2":
            self.stacked_layaout.setCurrentIndex(1)
        elif button.text().lower() == "ventana 3":
            self.stacked_layaout.setCurrentIndex(2)
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MainWindow()
    sys.exit(app.exec())