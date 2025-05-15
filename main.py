from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication, QHBoxLayout, QStackedWidget
# from PyQt5.QtCore import Qt, QTimer
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

        self.time_widget = RightWidget()
        self.time_widget.setFixedWidth(self.width()//2) 
        self.time_widget.sizeHint()

        self.clock = ClockWidget()
        self.base_clock_widget = QWidget()
        self.settings = SettingWidget()

        self.central_layout =  QHBoxLayout()
        self.central_layout.addWidget(self.clock)
        self.central_layout.addWidget(self.time_widget)
        
        self.base_clock_widget.setLayout(self.central_layout)
        self.base_clock_widget.setStyleSheet("background : #20232A;")
        self.base_clock_widget.setMouseTracking(True)      

        self.pages = QStackedWidget()
        self.pages.addWidget(self.base_clock_widget)
        self.pages.addWidget(self.settings)
        self.pages.setMouseTracking(True)

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