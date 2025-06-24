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
        self.setFixedHeight(100)

        # Кнопка для демонстрации функционала
        self.btn = QPushButton("Следующая страница", self)
        self.btn.clicked.connect(self.parent.switch_page)
        self.btn.setStyleSheet("""
        QPushButton {
            background-color: #46484B;
            color: #FED32C;
            border: 2px solid #A98C1D;
            border-radius: 8px;
            padding: 12px 24px;
            font-size: 16px;
            font-weight: bold;

        }
        QPushButton:hover {
            background-color: #9B9DA0;

        }
        QPushButton:pressed {
            background-color: #9B9DA0;
            border-top: 3px solid #3e8e41;
            border-left: 3px solid #3e8e41;
            border-right: 1px solid #3e8e41;
            border-bottom: 1px solid #3e8e41;
        }
        QPushButton:disabled {
            background-color: ##FED32C;
            border-color: ##FED32C;
            color: ##FED32C;
        }
        """)

        self.close_btn1 = QPushButton("Закрыть приложение", self)
        self.close_btn1.clicked.connect(self.parent.close)
        self.close_btn1.setStyleSheet("""
        QPushButton {
            background-color: #46484B;
            color: #FF5555;
            border: 2px solid #A91D1D;
            border-radius: 8px;
            padding: 12px 24px;
            font-size: 16px;
            font-weight: bold;
        }
        QPushButton:hover {
            background-color: #9B9DA0;
        }
        QPushButton:pressed {
            background-color: #9B9DA0;
            border-top: 3px solid #8e3e3e;
            border-left: 3px solid #8e3e3e;
            border-right: 1px solid #8e3e3e;
            border-bottom: 1px solid #8e3e3e;
        }
        """)

        # Добавление кнопок в layout (пример с горизонтальным расположением)
        layout = QHBoxLayout()
        layout.addWidget(self.btn)
        layout.addWidget(self.close_btn1)
        self.setLayout(layout)

