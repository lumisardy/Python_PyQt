import sys
from PyQt6.QtWidgets import  QPushButton, QWidget, QVBoxLayout, QApplication, QMessageBox

class MainWindow(QWidget):
    def __init__(self) :
        super().__init__()
        self.inicializar_ui()
        
    def inicializar_ui(self):
        self.setMinimumHeight(200)
        self.setFixedWidth(200)
        self.setWindowTitle("Layout Vertical")
        self.generar_formulario()
        self.show()
    
    def generar_formulario(self):
        button1 = QPushButton("Boton1")
        button2 = QPushButton("Boton2")
        button3 = QPushButton("Boton3")
        button4 = QPushButton("Boton4")
        
        button1.clicked.connect(self.Nombre_boton)
        button2.clicked.connect(self.Nombre_boton)
        button3.clicked.connect(self.Nombre_boton)
        button4.clicked.connect(self.Nombre_boton)
        
        
        layout = QVBoxLayout()
        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)
        layout.addWidget(button4)
        
        self.setLayout(layout)
    
    def Nombre_boton(self):
        boton = self.sender()
        QMessageBox.information(self,"boton",f"se le dio click al boton: {boton.text()}",QMessageBox.StandardButton.Ok,QMessageBox.StandardButton.Ok)
        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
    