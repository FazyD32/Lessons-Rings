from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication, QHBoxLayout, QStackedWidget
from PyQt5.QtCore import Qt, QTimer
from clock import ClockWidget
from mywidgets import RightWidget, SlideMenu, SettingWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.menu = SlideMenu(self)
        self.setMouseTracking(True)

        
    def init_ui(self):
        self.setWindowTitle("Lessons & Rings")
        self.setGeometry(100, 100, 800, 600)
        clock = ClockWidget()
        central_layout =  QHBoxLayout()
        self.base_clock_widget = QWidget()
        self.time_widget = RightWidget()
        self.time_widget.setFixedWidth(self.width()//3) 

        central_layout.addWidget(clock)
        central_layout.addWidget(self.time_widget)
        
        self.base_clock_widget.setLayout(central_layout)
        self.base_clock_widget.setMouseTracking(True)

        self.settings = SettingWidget()

        self.pages = QStackedWidget()
        self.pages.setMouseTracking(True)
        self.pages.addWidget(self.base_clock_widget)
        self.pages.addWidget(self.settings)
        self.setCentralWidget(self.pages)  

    def switch_page(self):
        # Переключение на следующую страницу
        new_index = (self.pages.currentIndex() + 1) % self.pages.count()
        self.pages.setCurrentIndex(new_index)   

    def mouseMoveEvent(self, event):
        pos = event.windowPos().toPoint()
        y = pos.y()
        if y < 40:
            self.menu.show()
        else:
            self.menu.hide()

            
            


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()