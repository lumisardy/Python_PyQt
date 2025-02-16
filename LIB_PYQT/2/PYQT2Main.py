from PyQt6.QtWidgets import QLabel, QWidget, QMessageBox
from PyQt6.QtGui import QPixmap


class MainWindow(QWidget):
    def __init__(self) :
        super().__init__()
        self.inicializarUI()
    
    def inicializarUI(self):
        
        self.setGeometry(200,100,1200,700)
        self.setWindowTitle("Ventana Principal")
        self.generar_contenido()
    
    
    def generar_contenido(self):
        image_path = "Mari.png"
        
        try:
            with open(image_path):
                image_label = QLabel(self)
                image_label.setPixmap(QPixmap(image_path ))
                
        except FileNotFoundError as e:
            QMessageBox.warning(self,"Error","Imagen no encontrada",QMessageBox.StandardButton.Close, QMessageBox.StandardButton.Close)
            
        except Exception as e:
            QMessageBox.warning(self,"Error","Error en el main view",QMessageBox.StandardButton.Close, QMessageBox.StandardButton.Close)
        
    