import sys
import operator
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QTextEdit, QPushButton, QGridLayout, QMessageBox


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
    def InicializarUI(self):
        self.setGeometry(100,100,600,400)
        self.setWindowTitle("Calculadora")
        self.generar_interfaz()
        self.show()
    
    def generar_interfaz(self):
        self.pantalla = QTextEdit()
        self.pantalla.setDisabled(True)
        boton1 = QPushButton("1")
        boton2 = QPushButton("2")
        boton3 = QPushButton("3")
        boton4 = QPushButton("4")
        boton5 = QPushButton("5")
        boton6 = QPushButton("6")
        boton7 = QPushButton("7")
        boton8 = QPushButton("8")
        boton9 = QPushButton("9")
        boton0 = QPushButton("0")
        boton00 = QPushButton("00")
        boton_punto = QPushButton(".")
        boton1.clicked.connect(self.ingresar_datos)
        boton2.clicked.connect(self.ingresar_datos)
        boton3.clicked.connect(self.ingresar_datos)
        boton4.clicked.connect(self.ingresar_datos)
        boton5.clicked.connect(self.ingresar_datos)
        boton6.clicked.connect(self.ingresar_datos)
        boton7.clicked.connect(self.ingresar_datos)
        boton8.clicked.connect(self.ingresar_datos)
        boton9.clicked.connect(self.ingresar_datos)
        boton0.clicked.connect(self.ingresar_datos)
        boton00.clicked.connect(self.ingresar_datos)
        boton_punto.clicked.connect(self.ingresar_datos)
        
        
        boton_suma = QPushButton("+")
        boton_resta = QPushButton("-")
        boton_multi = QPushButton("*")
        boton_divi = QPushButton("/")
        
        boton_suma.clicked.connect(self.ingresar_operador)
        boton_resta.clicked.connect(self.ingresar_operador)
        boton_multi.clicked.connect(self.ingresar_operador)
        boton_divi.clicked.connect(self.ingresar_operador)
        
        botonCE = QPushButton("CE")
        botonCE.clicked.connect(self.borrartodo)
        boton_borrar = QPushButton("<-")
        boton_borrar.clicked.connect(self.borrar)
        boton_resultado = QPushButton("=")
        boton_resultado.clicked.connect(self.calcular_operacion)
        
        self.main_grid = QGridLayout()
        
        
        #estos valores corresponde a 1: casiila y 2: casilla x 3: se extiende en fila 4: se extiende en columna
        self.main_grid.addWidget(self.pantalla,0,0,2,4)
        self.main_grid.addWidget(botonCE,2,0,1,2)
        self.main_grid.addWidget(boton_borrar,2,2)
        self.main_grid.addWidget(boton_suma,2,3)
        self.main_grid.addWidget(boton_resta,3,3)
        self.main_grid.addWidget(boton_multi,4,3)
        self.main_grid.addWidget(boton_divi,5,3)
        self.main_grid.addWidget(boton_resultado,6,3)
        self.main_grid.addWidget(boton1,5,0)
        self.main_grid.addWidget(boton2,5,1)
        self.main_grid.addWidget(boton3,5,2)
        self.main_grid.addWidget(boton4,4,0)
        self.main_grid.addWidget(boton5,4,1)
        self.main_grid.addWidget(boton6,4,2)
        self.main_grid.addWidget(boton7,3,0)
        self.main_grid.addWidget(boton8,3,1)
        self.main_grid.addWidget(boton9,3,2)
        self.main_grid.addWidget(boton0,6,0)
        self.main_grid.addWidget(boton00,6,1)
        self.main_grid.addWidget(boton_punto,6,2)
        
        
        self.setLayout(self.main_grid)
    
    def ingresar_datos(self):
        
        boton_text = self.sender().text()
        try:
            if self.after_equal:
                self.primer_valor = ""
                self.after_equal = False
                self.pantalla.setText(self.primer_valor)
                self.pointflag = "1"
            
            if self.pointflag == "1":
                self.primer_valor += boton_text
                self.pantalla.setText(self.primer_valor)   
            else:
                self.segundo_valor += boton_text
                self.pantalla.setText(self.pantalla.toPlainText() + boton_text)
        
        except ValueError:
            QMessageBox.information(self,"Numero","inserte algun numero",QMessageBox.StandardButton.Ok,QMessageBox.StandardButton.Ok)
            
                    
    def ingresar_operador(self):
        
        boton_text = self.sender().text()
        self.operador = boton_text
        self.pointflag = "2"
        
        if self.after_operator:
            self.calcular_operacion()
            self.pantalla.setText(self.primer_valor+""+self.operador+"")
            self.after_operator = False
        else:
            self.pantalla.setText(self.pantalla.toPlainText()+ ""+self.operador + "" )
        
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
            #con esto eliminas el ultimo elemento de la lista
            self.primer_valor = self.primer_valor[:-1]
            self.pantalla.setText(self.primer_valor)
        else:
            self.segundo_valor_valor = self.segundo_valor[:-1]
            self.pantalla.setText(self.segundo_valor)
            
    def calcular_operacion(self):
        try:
            if self.primer_valor == "":
                QMessageBox.information(self,"Primer Valor","Necesita insertar algun numero",QMessageBox.StandardButton.Ok,QMessageBox.StandardButton.Ok)
                self.borrartodo()
            else:
                resultado = str(operation[self.operador](float(self.primer_valor),float(self.segundo_valor)))
                self.pantalla.setText(resultado)
                self.primer_valor = resultado
                self.segundo_valor = ""
                self.after_equal = True
                self.after_operator = False
        except ValueError:
            QMessageBox.information(self,"Numero","Necesita insertar algun numero",QMessageBox.StandardButton.Ok,QMessageBox.StandardButton.Ok)
        
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    Ventana = MainWindow()
    sys.exit(app.exec())        

        
        