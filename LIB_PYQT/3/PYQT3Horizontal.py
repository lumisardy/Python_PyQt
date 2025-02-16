import sys
from PyQt6.QtWidgets import QLabel, QPushButton, QLineEdit, QWidget, QDialog, QLineEdit, QMessageBox, QHBoxLayout, QApplication

class MainWindow(QWidget):
    def __init__(self) :
        super().__init__()
        self.inicializar_ui()
        
    def inicializar_ui(self):
        self.setMinimumWidth(600)
        self.setFixedHeight(80)
        self.setWindowTitle("Layout Horizontal")
        self.generar_formulario()
        self.show()
    
    def generar_formulario(self):
        correo_label = QLabel("Correo electronico: ")
        correo_input = QLineEdit()
        enviar_button = QPushButton("Enviar")
        layout = QHBoxLayout()
        layout.addWidget(correo_label)
        layout.addWidget(correo_input)
        layout.addWidget(enviar_button)
        self.setLayout(layout)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())