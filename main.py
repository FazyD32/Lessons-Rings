from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication, QHBoxLayout
from clock import ClockWidget
from mywidgets import RightWidget
import pygame


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def play_audio(self):
        pygame.init()
        file = "C:\\Users\\bapcyk\\Downloads\\00101.mp3"
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        
    def init_ui(self):
        self.play_audio()
        self.setWindowTitle("Lessons & Rings")
        self.setGeometry(100, 100, 800, 600)
        clock = ClockWidget()
        central_layout =  QHBoxLayout()
        main_widget = QWidget()
        self.time_widget = RightWidget()
        self.time_widget.setFixedWidth(self.width()//3) 

        central_layout.addWidget(clock)
        central_layout.addWidget(self.time_widget)
        
        main_widget.setLayout(central_layout)
        self.setCentralWidget(main_widget)

    
        


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()