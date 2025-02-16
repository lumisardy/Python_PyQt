
import subprocess
import sys

try:
    # Intenta importar PyQt6
    import PyQt6
    print("La librería PyQt6 ya está instalada.")
except ImportError:
    # Si no está instalada, procede con la instalación
    print("La librería PyQt6 no está instalada. Procediendo a instalarla...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "PyQt6"])
    print("PyQt6 se ha instalado correctamente.")




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
        
        b_Danza1 = QPushButton()
        b_Danza1.setObjectName("Danza1")
        b_Danza1.setText("Danza 1 dia (30$)")
        b_Danza1.setFixedHeight(60)
        b_Danza1.setMinimumWidth(180)
        
        b_Danza2 = QPushButton()
        b_Danza2.setObjectName("Danza2")
        b_Danza2.setText("Danza 2 dias (45$)")
        b_Danza2.setFixedHeight(60)
        b_Danza2.setMinimumWidth(180)
        
        b_pilates = QPushButton()
        b_pilates.setObjectName("Pilates")
        b_pilates.setText("Pilates (45$)")
        b_pilates.setFixedHeight(60)
        b_pilates.setMinimumWidth(180)
        
        b_sportdance = QPushButton()
        b_sportdance.setObjectName("Sportdance")
        b_sportdance.setText("Sportdance (35$)")
        b_sportdance.setFixedHeight(60)
        b_sportdance.setMinimumWidth(180)
        
        b_Competi = QPushButton()
        b_Competi.setObjectName("Competi")
        b_Competi.setText("Competición")
        b_Competi.setFixedHeight(60)
        b_Competi.setMinimumWidth(180)
        
        self.b_Descuento = QCheckBox()
        self.b_Descuento.setObjectName("Descuento")
        self.b_Descuento.setText("Descuento (10%)")
        self.b_Descuento.setFixedHeight(60)
        self.b_Descuento.setMinimumWidth(180)

        b_Danza1.clicked.connect(self.Danza1)
        b_pilates.clicked.connect(self.Danza2_Pilates)
        b_Danza2.clicked.connect(self.Danza2_Pilates)
        b_sportdance.clicked.connect(self.sportdance)
        b_Competi.clicked.connect(self.Competi)
        self.b_Descuento.toggled.connect(self.Descuento)

        # Añadir los botones adicionales al layout horizontal
        botones_layout.addItem(QSpacerItem(20,40,QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))
        botones_layout.addWidget(b_Danza1)
        botones_layout.addWidget(b_Danza2)
        botones_layout.addWidget(b_pilates)
        botones_layout.addWidget(b_sportdance)
        botones_layout.addWidget(b_Competi)
        botones_layout.addWidget(self.b_Descuento)
        
        
        botones_layout.addItem(QSpacerItem(20,40,QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        # Añadir el layout de los botones adicionales al layout principal
        layout_principal.addLayout(botones_layout)
        
        # Establecer el layout principal en la ventana
        self.setLayout(layout_principal)
    
    def ingresar_datos(self):
        boton_text = self.sender().text()
        try:
            
            if self.b_Descuento.isChecked():
                QMessageBox.information(self, "Descuento", "No introducir valores con la casilla de descuento marcada", QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Ok)
            else:
                try:
                    if self.after_equal:
                        self.primer_valor = ""
                        self.after_equal = False
                        self.pantalla.setText(self.primer_valor)
                        self.pointflag = "1"
            
                    if self.pointflag == "1":
                        try:
                            self.primer_valor += boton_text
                            self.pantalla.setText(self.primer_valor)   
                        except: pass
                    else:
                        try:
                            self.segundo_valor += boton_text
                            self.pantalla.setText(self.pantalla.toPlainText() + boton_text)
                        except: pass
                except: pass
        
        except ValueError:
            QMessageBox.information(self, "Número", "Inserte algún número", QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Ok)
    
    def Danza1(self):
        try:
            if self.b_Descuento.isChecked():
                QMessageBox.information(self, "Descuento", "No introducir valores con la casilla de descuento marcada", QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Ok)
            else:
                if self.pantalla.toPlainText() == "":
                    self.primer_valor = 30
                    self.pantalla.setText(str(self.primer_valor))
                else:
                
                    self.pantalla.setText(str(float(self.pantalla.toPlainText()) + 30))
                    self.primer_valor = float(self.pantalla.toPlainText())
                
                

        except: pass
            
    
    def Danza2_Pilates(self):
        try:
            if self.b_Descuento.isChecked():
                QMessageBox.information(self, "Descuento", "No introducir valores con la casilla de descuento marcada", QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Ok)
            else:
                if self.pantalla.toPlainText() == "":
                    self.primer_valor = 45
                    self.pantalla.setText(str(self.primer_valor))
                else:
                
                    self.pantalla.setText(str(float(self.pantalla.toPlainText()) + 45))
                    self.primer_valor = float(self.pantalla.toPlainText())
                
                

        except: pass
        
    def sportdance(self):
        try:
            if self.b_Descuento.isChecked():
                QMessageBox.information(self, "Descuento", "No introducir valores con la casilla de descuento marcada", QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Ok)
            else:
                if self.pantalla.toPlainText() == "":
                    self.primer_valor = 35
                    self.pantalla.setText(str(self.primer_valor))
                else:
                
                    self.pantalla.setText(str(float(self.pantalla.toPlainText()) + 35))
                    self.primer_valor = float(self.pantalla.toPlainText())
                
                

        except: pass
    
    def Competi(self):
        pass
    
    def Descuento(self):
        try:
    # Obtener el valor actual de la pantalla
            valor_actual = float(self.pantalla.toPlainText())

    # Si el checkbox está marcado
            if self.b_Descuento.isChecked():
        # Si es la primera vez que aplicamos el descuento, guardamos el valor original
                if not hasattr(self, 'valor_original'):
                    self.valor_original = valor_actual
        
        # Aplicar el descuento del 10%
                valor_con_descuento = self.valor_original * 0.9
                self.pantalla.setText(str(valor_con_descuento))
                self.primer_valor = valor_con_descuento

    # Si el checkbox está desmarcado
            else:
        # Restaurar el valor original guardado
                if hasattr(self, 'valor_original'):
                    self.pantalla.setText(str(self.valor_original))
                    self.primer_valor = self.valor_original

        # Limpiar el valor guardado para futuras operaciones
                del self.valor_original
        
        except: pass
           
                    
    def ingresar_operador(self):
        boton_text = self.sender().text()
        self.operador = boton_text
        self.pointflag = "2"
        
        if self.after_operator:
            self.calcular_operacion()
            self.pantalla.setText(self.primer_valor + "" + self.operador + "")
            self.after_operator = False
        else:
            self.pantalla.setText(self.pantalla.toPlainText() + "" + self.operador + "")
        
        self.after_operator = True
        self.after_equal = False
        
    def borrartodo(self):
        self.primer_valor = ""
        self.segundo_valor = ""
        self.operador = ""
        self.pointflag = "1"
        self.after_equal = False
        self.after_operator = False
        self.pantalla.setText("")
        
    def borrar(self):
        if self.after_equal:
            self.borrartodo()
        
        if self.pointflag == "1":
            try:
                self.primer_valor = self.primer_valor[:-1]
                self.pantalla.setText(self.primer_valor)
            except: pass
        else:
            try:
                
                self.segundo_valor = self.segundo_valor[:-1]
                self.pantalla.setText(self.segundo_valor)
            except: pass
            
    def calcular_operacion(self):
        try:
            if self.primer_valor == "":
                QMessageBox.information(self, "Primer Valor", "Necesita insertar algún número", QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Ok)
                self.borrartodo()
            else:
                try:
                    resultado = str(operation[self.operador](float(self.primer_valor), float(self.segundo_valor)))
                    self.pantalla.setText(resultado)
                    self.primer_valor = resultado
                    self.segundo_valor = ""
                    self.after_equal = True
                    self.after_operator = False
                except:pass
        except ValueError:
            QMessageBox.information(self, "Número", "Necesita insertar algún número", QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Ok)   
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MainWindow()
    sys.exit(app.exec())
