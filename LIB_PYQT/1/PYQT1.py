

#QApplication: Es la clase principal que gestiona la aplicación. Se requiere para inicializar la aplicación.
#QMainWindow: Es la ventana principal de la aplicación. Se puede personalizar y configurar.
#QWidget: Es un widget genérico de Qt que puede ser utilizado como un contenedor básico.
#QVBoxLayout: Es un layout vertical que organiza los widgets en una columna.
#QLabel: Es un widget de texto simple que puede mostrar etiquetas y texto.


import sys
from PyQt6.QtWidgets import QApplication, QWidget 

class VentanaVacia(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializarUI()
        
    def inicializarUI(self):
        
        #orden de geometria x,y,ancho,largo
        self.setGeometry(1200,200,700,700)
        self.setWindowTitle("Calculadora")
        self.show()

#if __name__ == "__main__" Esta línea verifica si el script se está ejecutando directamente o se importa desde otro script.

if __name__ == "__main__":
    
    # con esta linea podemos ver todal las interacciones q se hacen en la ventana
    app = QApplication(sys.argv)
    ventana = VentanaVacia()
    
    #esto es para que cuando le demos a cerrar programa se cierre por completo y no se queden archivos en segundo plano abiertos
    sys.exit(app.exec())
        

