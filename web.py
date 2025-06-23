from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QToolBar, QLineEdit, QAction
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import QBrush, QPainter, QPen, QColor
from PyQt5.QtCore import QPoint, QTime, Qt, QTimer
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView


class ClockWidget(QWidget): #Вместо маин виндов можно и просто виджет
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Qt Web Browser")
        self.setGeometry(100, 100, 1024, 768)

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://sch5-gusev.gosuslugi.ru/roditelyam-i-uchenikam/novosti/"))
        
        self.browser.urlChanged.connect(self.update_url)

        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        self.setLayout(layout)
    
    def update_url(self, url):
        self.url_bar.setText(url.toString())
