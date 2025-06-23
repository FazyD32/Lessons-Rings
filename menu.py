from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QGridLayout, QPushButton, QTimeEdit, QTextEdit, QLineEdit, QHBoxLayout
from PyQt5.QtCore import Qt, QTimer, QPropertyAnimation, QPoint

class SlideMenu(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.init_ui()
        self.hide()

    def init_ui(self):
        # Настройка внешнего вида меню
        self.setGeometry(6, 6, self.parent.width(), 50)
        self.setStyleSheet('''background-color: rgba(40, 40, 40, 200);
                            color: #ffffff;
                            border: 1px solid #555555;
                            border-radius: 12px;
                            padding: 20px;''')

        self.lay = QHBoxLayout()
        # self.setLayout(self.lay)
        # self.lay.addWidget(self.btn)

        # Кнопка для демонстрации функционала
        self.btn = QPushButton("Следующая страница", self)
        self.btn.clicked.connect(self.parent.switch_page)
        self.btn.setStyleSheet('''
            background-color: #252932;
            color: #FED32C;
            padding: 10px;
            border: 3px solid #E6C02C;
            text-align: center;
            border-radius: 5px;
            font-size: 20px;
             ''')