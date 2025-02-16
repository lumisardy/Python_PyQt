import sys
from PyQt6.QtWidgets import (QApplication,QMainWindow,QStatusBar,QFileDialog, QVBoxLayout,QTextEdit, QWidget, QFontDialog, QColorDialog,QToolBar)
from PyQt6.QtCore import QStandardPaths
from PyQt6.QtGui import QAction,QKeySequence,QTextCharFormat,QGuiApplication,QPixmap

class MainWindow(QMainWindow):
    def __init__(self) :
        super().__init__()
        self.status_Bar = QStatusBar()
        self.setStatusBar(self.status_Bar)
        self.inicializate()
        self.status_Bar.setStyleSheet("background-color: white")
        
    def inicializate(self):
        self.setGeometry(100,100,500,500)
        self.setWindowTitle("Ventana")
        self.Generar_Ventana()
        self.show()
    
    def Generar_Ventana(self):
        self.create_content()
        self.create_action()
        self.create_menu()
        self.create_tool_bar()
        
    
    def create_content(self):
        layout = QVBoxLayout()
        self.editor_text = QTextEdit()
        layout.addWidget(self.editor_text)
        layout.setContentsMargins(30,30,30,30)
        container1 = QWidget()
        container1.setLayout(layout)
        self.setCentralWidget(container1)
        
    
    
    def create_action(self):
        self.open_action = QAction("Abrir",self)
        self.open_action.setShortcut(QKeySequence("Ctrl+O"))
        self.open_action.setStatusTip("Abrir archivos")
        self.open_action.triggered.connect(self.open)
        
        self.save_action = QAction("Guardar",self)
        self.save_action.setShortcut(QKeySequence("Ctrl+S"))
        self.save_action.setStatusTip("Guardar archivos")
        self.save_action.triggered.connect(self.save)
        
        self.exportar_action = QAction("Exportar",self)
        self.exportar_action.setShortcut(QKeySequence("Ctrl+E"))
        self.exportar_action.setStatusTip("Exportar archivos")
        self.exportar_action.triggered.connect(self.exportar)
        
        self.deshacer_action = QAction("Deshacer",self)
        self.deshacer_action.setShortcut(QKeySequence("Ctrl+Z"))
        self.deshacer_action.setStatusTip("Deshacer cambios")
        self.deshacer_action.triggered.connect(self.editor_text.undo)
        
        self.color_action = QAction("Color",self)
        self.color_action.setShortcut(QKeySequence("Ctrl+H"))
        self.color_action.setStatusTip("Cambiar Color")
        self.color_action.triggered.connect(self.color)
        
        self.font_action = QAction("Fuente",self)
        self.font_action.setShortcut(QKeySequence("Ctrl+F"))
        self.font_action.setStatusTip("Cambio de fuente")
        self.font_action.triggered.connect(self.set_font)
        
        self.rehacer_action = QAction("Rehacer",self)
        self.rehacer_action.setShortcut(QKeySequence("Ctrl+Y"))
        self.rehacer_action.setStatusTip("Rehacer cambios")
        self.rehacer_action.triggered.connect(self.editor_text.redo)
        
        self.view_open_action = QAction("Abrir",self,checkable=True)
        self.view_open_action.setStatusTip("agregar boton en la barra de tareas para abrir archivos")
        self.view_open_action.triggered.connect(self.view_open)
        
        self.view_save_action = QAction("Guardar",self, checkable=True)
        self.view_save_action.setStatusTip("agregar boton en la barra de tareas para guardar archivos")
        self.view_save_action.triggered.connect(self.view_save)
        
        self.view_exportar_action = QAction("Exportar",self, checkable=True)
        self.view_exportar_action.setStatusTip("agregar boton en la barra de tareas para exportar archivos")
        self.view_exportar_action.triggered.connect(self.view_exportar)
        
        
    def create_tool_bar(self):
        self.toolbar = QToolBar("barra de herramientas")
        self.addToolBar(self.toolbar)
    
    def create_menu(self):
        menu_archivo = self.menuBar().addMenu("Archivo")
        menu_archivo.addAction(self.open_action)
        menu_archivo.addAction(self.save_action)
        menu_archivo.addAction(self.exportar_action)
        
        
        
        menu_editar = self.menuBar().addMenu("Editar")
        menu_editar.addAction(self.font_action)
        menu_editar.addAction(self.color_action)
        menu_editar.addAction(self.rehacer_action)
        menu_editar.addAction(self.deshacer_action)
        
        menu_ver = self.menuBar().addMenu("View")
        submenu_perso = menu_ver.addMenu("Personalizacion")
        submenu_perso.addAction(self.view_open_action)
        submenu_perso.addAction(self.view_save_action)
        submenu_perso.addAction(self.view_exportar_action)
        
    
    def color(self):
        
        color_text_cursor = self.editor_text.textCursor()
        
        color= QColorDialog.getColor(
            
            self.editor_text.textColor(),self
        )
        
        if color.isValid:
            if color_text_cursor.hasSelection():
                format = QTextCharFormat()
                format.setForeground(color)
                color_text_cursor.mergeCharFormat(format)
            else:
                self.editor_text.setTextColor(color)
        
        
    def set_font(self):
        select_text_cursor = self.editor_text.textCursor()
        
        font , ok = QFontDialog.getFont(
            
            self.editor_text.currentFont(),self
        )
        if ok:
            if select_text_cursor.hasSelection():
                format = self.editor_text.currentCharFormat()
                format.setFont(font)
                select_text_cursor.mergeCharFormat(format)
            else:
                self.editor_text.setCurrentFont(font )
        
    def open(self):
        options = (QFileDialog.Option.DontUseNativeDialog)
        initial_dir = QStandardPaths.writableLocation(
            
            QStandardPaths.StandardLocation.DocumentsLocation
            
            )
        file_type = "Text Files (*.txt);;Imagene (*.png);; All files (*)"
        self.file , _ =  QFileDialog.getOpenFileName(self,"Open file", initial_dir, file_type)
        
        with open(self.file, "r") as file:
            self.setWindowTitle(f"MainWindow - {self.file}")
            self.editor_text.setText(file.read())
        
    def save(self):
            
            initial_dir = QStandardPaths.writableLocation(
            
            QStandardPaths.StandardLocation.DocumentsLocation
            
            )
            
            file_name, _ = QFileDialog.getSaveFileName(self,"Guardar archivo",initial_dir,"archivo de texto (*.txt);; HTML (*.html)")
            
            if file_name.endswith(".txt"):
                text = self.editor_text.toPlainText()
                with open(file_name, "w") as f:
                    f.write(text)
            elif file_name.endswith(".html"):
                text_html = self.editor_text.toHtml()
                with open(file_name, "w") as f:
                    f.write(text_html)
            
        
    def exportar(self):
            initial_dir = QStandardPaths.writableLocation(
            
            QStandardPaths.StandardLocation.DocumentsLocation
            
            )
            screen = QGuiApplication.primaryScreen()
            pixmap = screen.grabWindow(self.editor_text.winId())
            
            file_name, _ = QFileDialog.getSaveFileName(self,"Exportar archivo",initial_dir,"PNG (*.png);; JPEG (*.Jpeg)")
            
            if file_name:
                pixmap.save(file_name)
        
        
    def view_open(self):
        if self.view_open_action.isChecked():
            self.toolbar.addAction(self.open_action)
        else:
            self.toolbar.removeAction(self.open_action)
    
    def view_save(self):
        if self.view_save_action.isChecked():
            self.toolbar.addAction(self.save_action)
        else:
            self.toolbar.removeAction(self.save_action)
    
    def view_exportar(self):
        if self.view_exportar_action.isChecked():
            self.toolbar.addAction(self.exportar_action)
        else:
            self.toolbar.removeAction(self.exportar_action)
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MainWindow()
    sys.exit(app.exec())
        
