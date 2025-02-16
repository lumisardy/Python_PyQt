import sys
import operator
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QTextEdit, QPushButton, QGridLayout, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy, QMessageBox, QCheckBox
from PyQt6.QtGui import QFont

operation = {
    "+" : operator.add,
    "-" : operator.sub,
    "*" : operator.mul,
    "/" : operator.truediv
}

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.InicializarUI()
        self.primer_valor = ""
        self.segundo_valor = ""
        self.operador = ""
        self.pointflag = "1"
        self.after_equal = False
        self.after_operator = False
        with open("Python/David/calculadoradavid1/estilos_calcu.css","r") as file:
            style = file.read()
        self.setStyleSheet(style)
        
    def InicializarUI(self):
        self.setGeometry(100, 100, 600, 400)
        self.setWindowTitle("Calculadora")
        self.generar_interfaz()
        self.show()
    
    def generar_interfaz(self):
        # Crear layout principal
        layout_principal = QHBoxLayout()  # Usamos un VBox para organizar la calculadora y los otros botones verticalmente

        # Crear la pantalla
        self.pantalla = QTextEdit()
        self.pantalla.setFont(QFont("Arial",40))
        self.pantalla.setDisabled(True)
        
        # Crear botones numéricos y de operaciones
        boton1 = QPushButton("1")
        boton1.setMinimumSize(80,30)
        boton2 = QPushButton("2")
        boton2.setMinimumSize(80,30)
        boton3 = QPushButton("3")
        boton3.setMinimumSize(80,30)
        boton4 = QPushButton("4")
        boton4.setMinimumSize(80,30)
        boton5 = QPushButton("5")
        boton5.setMinimumSize(80,30)
        boton6 = QPushButton("6")
        boton6.setMinimumSize(80,30)
        boton7 = QPushButton("7")
        boton7.setMinimumSize(80,30)
        boton8 = QPushButton("8")
        boton8.setMinimumSize(80,30)
        boton9 = QPushButton("9")
        boton9.setMinimumSize(80,30)
        boton0 = QPushButton("0")
        boton0.setMinimumSize(80,30)
        boton00 = QPushButton("00")
        boton00.setMinimumSize(80,30)
        boton_punto = QPushButton(".")
        boton_punto.setMinimumSize(80,30)
        
        # Conectar los botones numéricos a la función ingresar_datos
        botones_numeros = [boton1, boton2, boton3, boton4, boton5, boton6, boton7, boton8, boton9, boton0, boton00, boton_punto]
        for boton in botones_numeros:
            boton.clicked.connect(self.ingresar_datos)
        
        # Crear botones de operaciones
        boton_suma = QPushButton("+")
        boton_suma.setMinimumSize(80,30)
        boton_resta = QPushButton("-")
        boton_resta.setMinimumSize(80,30)
        boton_multi = QPushButton("*")
        boton_multi.setMinimumSize(80,30)
        boton_divi = QPushButton("/")
        boton_divi.setMinimumSize(80,30)
        
        # Conectar los botones de operadores a la función ingresar_operador
        boton_suma.clicked.connect(self.ingresar_operador)
        boton_resta.clicked.connect(self.ingresar_operador)
        boton_multi.clicked.connect(self.ingresar_operador)
        boton_divi.clicked.connect(self.ingresar_operador)
        
        # Botones especiales
        botonCE = QPushButton("CE")
        botonCE.setMinimumSize(80,30)
        botonCE.clicked.connect(self.borrartodo)
        boton_borrar = QPushButton("<-")
        boton_borrar.setMinimumSize(80,30)
        boton_borrar.clicked.connect(self.borrar)
        boton_resultado = QPushButton("=")
        boton_resultado.setMinimumSize(80,30)
        boton_resultado.clicked.connect(self.calcular_operacion)
        
        # Crear el layout de la calculadora
        grid_calculadora = QGridLayout()
        grid_calculadora.addWidget(self.pantalla, 0, 0, 2, 4)
        grid_calculadora.addWidget(botonCE, 2, 0, 1, 2)
        grid_calculadora.addWidget(boton_borrar, 2, 2)
        grid_calculadora.addWidget(boton_suma, 2, 3)
        grid_calculadora.addWidget(boton_resta, 3, 3)
        grid_calculadora.addWidget(boton_multi, 4, 3)
        grid_calculadora.addWidget(boton_divi, 5, 3)
        grid_calculadora.addWidget(boton_resultado, 6, 3)
        grid_calculadora.addWidget(boton1, 5, 0)
        grid_calculadora.addWidget(boton2, 5, 1)
        grid_calculadora.addWidget(boton3, 5, 2)
        grid_calculadora.addWidget(boton4, 4, 0)
        grid_calculadora.addWidget(boton5, 4, 1)
        grid_calculadora.addWidget(boton6, 4, 2)
        grid_calculadora.addWidget(boton7, 3, 0)
        grid_calculadora.addWidget(boton8, 3, 1)
        grid_calculadora.addWidget(boton9, 3, 2)
        grid_calculadora.addWidget(boton0, 6, 0)
        grid_calculadora.addWidget(boton00, 6, 1)
        grid_calculadora.addWidget(boton_punto, 6, 2)
        
        # Añadir el layout de la calculadora al layout principal
        layout_principal.addLayout(grid_calculadora)

        # Añadir un espaciador vertical para separar la calculadora de los botones adicionales
        layout_principal.addItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        # Crear layout horizontal para los botones adicionales (Baile, Competi, Clases)
        botones_layout = QVBoxLayout()
        
        b_Danza1 = QPushButton("Danza 1 dia (30$)")
        b_Danza1.setFixedHeight(60)
        b_Danza1.setMinimumWidth(180)
        
        b_Danza2 = QPushButton("Danza 2 dias (45$)")
        b_Danza2.setFixedHeight(60)
        b_Danza2.setMinimumWidth(180)
        
        b_pilates = QPushButton("Pilates (45$)")
        b_pilates.setFixedHeight(60)
        b_pilates.setMinimumWidth(180)
        
        b_sportdance = QPushButton("Sportdance (35$)")
        b_sportdance.setFixedHeight(60)
        b_sportdance.setMinimumWidth(180)
        
        b_Competi = QPushButton("Competición")
        b_Competi.setFixedHeight(60)
        b_Competi.setMinimumWidth(180)
        
        # Checkbox para el descuento
        self.checkbox_descuento = QCheckBox("Aplicar Descuento (10%)")
        self.checkbox_descuento.setFixedHeight(60)
        self.checkbox_descuento.setMinimumWidth(180)

        b_Danza1.clicked.connect(self.Danza1)
        b_pilates.clicked.connect(self.Danza2_Pilates)
        b_Danza2.clicked.connect(self.Danza2_Pilates)
        b_sportdance.clicked.connect(self.sportdance)
        b_Competi.clicked.connect(self.Competi)

        # Añadir los botones adicionales al layout horizontal
        botones_layout.addItem(QSpacerItem(20,40,QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))
        botones_layout.addWidget(b_Danza1)
        botones_layout.addWidget(b_Danza2)
        botones_layout.addWidget(b_pilates)
        botones_layout.addWidget(b_sportdance)
        botones_layout.addWidget(b_Competi)
        botones_layout.addWidget(self.checkbox_descuento)  # Añadimos el checkbox para el descuento
        
        botones_layout.addItem(QSpacerItem(20,40,QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        # Añadir el layout de los botones adicionales al layout principal
        layout_principal.addLayout(botones_layout)
        
        # Establecer el layout principal en la ventana
        self.setLayout(layout_principal)
    
    # Función para aplicar el descuento
    def aplicar_descuento(self, precio):
        if self.checkbox_descuento.isChecked():
            precio *= 0.9  # Aplica un descuento del 10%
        return precio
    
    # Función para los botones adicionales
    def Danza1(self):
        precio = self.aplicar_descuento(30)  # Aplicar el descuento si el checkbox está seleccionado
        self.pantalla.setText(f"El precio es {precio} euros.")
    
    def Danza2_Pilates(self):
        precio = self.aplicar_descuento(45)
        self.pantalla.setText(f"El precio es {precio} euros.")
        
    def sportdance(self):
        precio = self.aplicar_descuento(35)
        self.pantalla.setText(f"El precio es {precio} euros.")
    
    def Competi(self):
        precio = self.aplicar_descuento(60)
        self.pantalla.setText(f"El precio es {precio} euros.")
    
    # Funciones de la calculadora
    def ingresar_datos(self):
        sender = self.sender()
        if self.after_equal:
            self.pantalla.clear()
            self.after_equal = False
        self.pantalla.insertPlainText(sender.text())
    
    def ingresar_operador(self):
        sender = self.sender()
        self.primer_valor = self.pantalla.toPlainText()
        self.operador = sender.text()
        self.pantalla.clear()
    
    def calcular_operacion(self):
        try:
            self.segundo_valor = self.pantalla.toPlainText()
            resultado = operation[self.operador](float(self.primer_valor), float(self.segundo_valor))
            self.pantalla.setText(str(resultado))
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))
    
    def borrartodo(self):
        self.pantalla.clear()
    
    def borrar(self):
        self.pantalla.textCursor().deletePreviousChar()
        
        
    def calcular_operacion(self):
        try:
            if self.primer_valor == "":
                QMessageBox.information(self, "Primer Valor", "Necesita insertar algún número", QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Ok)
                self.borrartodo()
            else:
                resultado = str(operation[self.operador](float(self.primer_valor), float(self.segundo_valor)))
                self.pantalla.setText(resultado)
                self.primer_valor = resultado
                self.segundo_valor = ""
                self.after_equal = True
                self.after_operator = False
        except ValueError:
            QMessageBox.information(self, "Número", "Necesita insertar algún número", QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Ok)   
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MainWindow()
    sys.exit(app.exec())