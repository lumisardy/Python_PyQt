import sys
import os
import random
from PyQt6.QtWidgets import (QApplication, QMainWindow, QHBoxLayout, QStatusBar, 
                             QVBoxLayout, QWidget, QLabel, QPushButton, QDockWidget, 
                             QTabWidget, QListWidget, QFileDialog, QListWidgetItem, QSlider)

from PyQt6.QtGui import QPixmap, QKeySequence, QAction, QIcon, QFont
from PyQt6.QtCore import Qt, QStandardPaths, QUrl, QSize

from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput


# Nueva clase para la ventana secundaria
class NuevaVentana(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializarUI()

    def inicializarUI(self):
        self.setWindowTitle("Nueva Ventana")
        self.setGeometry(200, 200, 400, 300)
        layout = QVBoxLayout()

        label = QLabel("Esta es una nueva ventana", self)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)

        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.inicializarUI()
        self.statusbar = QStatusBar()
        self.setStatusBar(self.statusbar)
        self.current_music_folder = ""
        with open("Python/PYQT/8/estilos.css", "r") as file:
            style = file.read()
        self.setStyleSheet(style)
        self.player = None
        self.player_reproducto = False
        self.nueva_ventana = None  # Para almacenar la nueva ventana

    def inicializarUI(self):
        self.setGeometry(100, 100, 800, 500)
        self.setWindowTitle("Reproductor de Musica")

        # Llamar a la función para crear el fondo de la ventana
        self.create_background("PYQT/8/fondo.png")

        self.show()
        self.generar_window()
        self.create_dock()
        self.create_action()
        self.create_menu()

    def create_background(self, image_path):
        """Función para crear el fondo de la ventana principal con una imagen específica."""
        # Crear un QLabel para contener el fondo
        self.label_fondo = QLabel(self)

        # Cargar la imagen de fondo usando QPixmap
        self.pixmap_fondo = QPixmap(image_path)

        # Verificar si la imagen se cargó correctamente
        if self.pixmap_fondo.isNull():
            print(f"Error: no se pudo cargar la imagen {image_path}. Verifica la ruta.")
            return

        # Ajustar la imagen de fondo al tamaño de la ventana
        self.ajustar_fondo()

    def ajustar_fondo(self):
        """Ajustar la imagen de fondo al tamaño de la ventana."""
        # Redimensionar la imagen para ajustarse a la ventana
        pixmap_ajustado = self.pixmap_fondo.scaled(self.size(),
                                                   Qt.AspectRatioMode.IgnoreAspectRatio,
                                                   Qt.TransformationMode.SmoothTransformation)

        # Asignar el pixmap ajustado al QLabel
        self.label_fondo.setPixmap(pixmap_ajustado)
        self.label_fondo.setGeometry(0, 0, self.width(), self.height())

        # Enviar el QLabel al fondo para que otros widgets estén encima
        self.label_fondo.lower()

    def generar_window(self):
        tab_bar = QTabWidget(self)
        self.reproductor_container = QWidget()
        self.settings_container = QWidget()
        tab_bar.addTab(self.reproductor_container, "Reproductor")
        tab_bar.addTab(self.settings_container, "Settings")

        self.generate_reproductor_tab()
        self.generate_settings_tab()

        tab_h_layout = QHBoxLayout()
        tab_h_layout.addWidget(tab_bar)

        main_container = QWidget()
        main_container.setLayout(tab_h_layout)
        self.setCentralWidget(main_container)

    def generate_settings_tab(self):
        V_layout = QVBoxLayout()
        H_layout = QHBoxLayout()

        Ajustes = QLabel()
        Ajustes.setText("SETTINGS")
        Ajustes.setFont(QFont("Cooper Black", 20))
        Ajustes.setAlignment(Qt.AlignmentFlag.AlignCenter)
        Ajustes.setFixedHeight(20)

        Button_fondo1 = QPushButton()
        Button_fondo1.setObjectName("button_F1")
        Button_fondo1.setFixedSize(150, 100)
        Button_fondo1.clicked.connect(lambda: self.create_background("PYQT/6/espana.png"))

        Button_fondo2 = QPushButton()
        Button_fondo2.setObjectName("button_F2")
        Button_fondo2.setFixedSize(155, 100)
        Button_fondo2.clicked.connect(lambda: self.create_background("PYQT/8/fondo2.jpeg"))

        Button_fondo3 = QPushButton()
        Button_fondo3.setObjectName("button_F3")
        Button_fondo3.setFixedSize(160, 100)
        Button_fondo3.clicked.connect(lambda: self.create_background("PYQT/8/fondo3.jpg"))

        Button_fondo4 = QPushButton()
        Button_fondo4.setObjectName("button_F4")
        Button_fondo4.setText("Abrir nueva ventana")
        Button_fondo4.setFont(QFont("Cooper Black", 12))
        Button_fondo4.setFixedWidth(500)
        Button_fondo4.clicked.connect(self.abrir_nueva_ventana)  # Conectar a la nueva función

        H_layout.addWidget(Button_fondo1)
        H_layout.addWidget(Button_fondo2)
        H_layout.addWidget(Button_fondo3)

        V_layout.addWidget(Ajustes)
        V_layout.addLayout(H_layout)
        V_layout.addWidget(Button_fondo4)

        self.settings_container.setLayout(V_layout)

    def abrir_nueva_ventana(self):
        """Función para abrir una nueva ventana."""
        if self.nueva_ventana is None:
            self.nueva_ventana = NuevaVentana()
        self.nueva_ventana.show()

    def setvolume(self, value):
        try:
            self.audioOutput.setVolume(value / 100)
        except:
            pass

    def resizeEvent(self, event):
        self.ajustar_fondo()

    def generate_reproductor_tab(self):
        Main_v_buttons = QVBoxLayout()
        bottons_h_layaot = QHBoxLayout()

        song_image = QLabel()
        song_image.setFixedSize(512, 512)
        song_image.setObjectName("song_image")

        botton_repeat = QPushButton()
        botton_repeat.setObjectName("botton_repeat")
        botton_repeat.clicked.connect(self.repetir_cancion)
        botton_before = QPushButton()
        botton_before.setObjectName("botton_before")
        botton_before.clicked.connect(self.Cancion_anterior)
        self.botton_play = QPushButton()
        self.botton_play.setObjectName("botton_play")
        self.botton_play.clicked.connect(self.play_song)
        botton_next = QPushButton()
        botton_next.setObjectName("botton_next")
        botton_next.clicked.connect(self.cancion_posterior)
        botton_random = QPushButton()
        botton_random.setObjectName("botton_random")
        botton_random.clicked.connect(self.Cancion_aleatoria)

        Volumen = QLabel()
        Volumen.setText("Volumen")
        Volumen.setFont(QFont("Cooper Black", 12))
        Volumen.setAlignment(Qt.AlignmentFlag.AlignCenter)
        Volumen.setFixedHeight(20)

        self.Volume_slider = QSlider(Qt.Orientation.Horizontal)
        self.Volume_slider.setRange(0, 100)
        self.Volume_slider.setValue(50)

        self.Volume_slider.valueChanged.connect(self.setvolume)

        botton_random.setFixedSize(40, 40)
        botton_repeat.setFixedSize(40, 40)
        self.botton_play.setFixedSize(50, 50)
        botton_next.setFixedSize(40, 40)
        botton_before.setFixedSize(40, 40)

        bottons_h_layaot.addWidget(botton_repeat)
        bottons_h_layaot.addWidget(botton_before)
        bottons_h_layaot.addWidget(self.botton_play)
        bottons_h_layaot.addWidget(botton_next)
        bottons_h_layaot.addWidget(botton_random)

        buttons_container = QWidget()
        buttons_container.setLayout(bottons_h_layaot)

        Main_v_buttons.addWidget(song_image)
        Main_v_buttons.addWidget(Volumen)
        Main_v_buttons.addWidget(self.Volume_slider)
        Main_v_buttons.addWidget(buttons_container)

        self.reproductor_container.setLayout(Main_v_buttons)

    def create_menu(self):
        self.menuBar()
        menu_view = self.menuBar().addMenu("View")
        menu_view.addAction(self.lista_musica)

        menu_file = self.menuBar().addMenu("File")
        menu_file.addAction(self.open_folder_music_action)

    def list_music(self):
        if self.lista_musica.isChecked():
            self.dock.show()
        else:
            self.dock.hide()

    def create_dock(self):
        self.song_list = QListWidget()
        self.dock = QDockWidget()
        self.dock.setWindowTitle("Lista de canciones")
        self.dock.setAllowedAreas(
            Qt.DockWidgetArea.LeftDockWidgetArea |
            Qt.DockWidgetArea.RightDockWidgetArea
        )

        self.song_list.itemSelectionChanged.connect(self.handle_song_seleccion)
        self.dock.setWidget(self.song_list)
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.dock)

    def create_action(self):
        self.lista_musica = QAction("Listar musica", self, checkable=True)
        self.lista_musica.setShortcut(QKeySequence("Ctrl+l"))
        self.lista_musica.setStatusTip("Muestra la lista de canciones")
        self.lista_musica.triggered.connect(self.list_music)

        self.open_folder_music_action = QAction(QIcon.fromTheme("document-open-folder"), "Abrir carpeta de musica", self)
        self.open_folder_music_action.setShortcut(QKeySequence("Ctrl+O"))
        self.open_folder_music_action.setStatusTip("Abrir carpeta de musica")
        self.open_folder_music_action.triggered.connect(self.abrir_folder_musica)

    def abrir_folder_musica(self):
        folder_path = QFileDialog.getExistingDirectory(
            self, "Abrir carpeta de musica", QStandardPaths.writableLocation(QStandardPaths.StandardLocation.MusicLocation)
        )
        if folder_path:
            self.cargar_musica(folder_path)

    def cargar_musica(self, folder_path):
        self.song_list.clear()
        self.current_music_folder = folder_path
        extensions = (".mp3", ".wav", ".ogg", ".flac", ".m4a")
        for filename in os.listdir(folder_path):
            if filename.lower().endswith(extensions):
                list_item = QListWidgetItem(filename)
                self.song_list.addItem(list_item)

    def handle_song_seleccion(self):
        if not self.player_reproducto:
            self.play_song()
        else:
            self.player.stop()
            self.play_song()

    def play_song(self):
        self.botton_play.setObjectName("botton_pause")
        if not self.player_reproducto:
            self.player_reproducto = True
            self.iniciar_song()
        else:
            self.player_reproducto = False
            self.player.pause()

    def iniciar_song(self):
        current_song = self.song_list.currentItem().text()
        file_url = QUrl.fromLocalFile(os.path.join(self.current_music_folder, current_song))
        self.player = QMediaPlayer()
        self.player.setSource(file_url)

        self.audioOutput = QAudioOutput()
        self.audioOutput.setVolume(self.Volume_slider.value() / 100)

        self.player.setAudioOutput(self.audioOutput)
        self.player.play()

    def Cancion_aleatoria(self):
        song_count = self.song_list.count()
        if song_count > 0:
            random_song_index = random.randint(0, song_count - 1)
            self.song_list.setCurrentRow(random_song_index)

    def Cancion_anterior(self):
        current_row = self.song_list.currentRow()
        if current_row > 0:
            self.song_list.setCurrentRow(current_row - 1)

    def cancion_posterior(self):
        current_row = self.song_list.currentRow()
        if current_row < self.song_list.count() - 1:
            self.song_list.setCurrentRow(current_row + 1)

    def repetir_cancion(self):
        current_row = self.song_list.currentRow()
        self.song_list.setCurrentRow(current_row)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
