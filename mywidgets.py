from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QGridLayout, QPushButton
from PyQt5.QtCore import Qt, QTimer, QPropertyAnimation, QPoint
import datetime

class SlideMenu(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.init_ui()
        self.hide()

    def init_ui(self):
        # Настройка внешнего вида меню
        self.setGeometry(0, 0, self.parent.width(), 50)
        self.setStyleSheet("background: #3498db; border-bottom: 2px solid #2980b9;")

        # Кнопка для демонстрации функционала
        btn = QPushButton("Следующая страница", self)
        btn.clicked.connect(self.parent.switch_page)
        btn.setStyleSheet('''
            background-color: #f7fafa;
            color: #FED32C;
            padding: 10px;
            border: 3px solid #E6C02C;
            text-align: center;
            border-radius: 5px;
            font-size: 20px;
             ''')


class RightWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        layout = QVBoxLayout()

        self.lbl_time = QLabel("Время")
        self.lbl_time.setAlignment(Qt.AlignHCenter)
        self.lbl_time.setStyleSheet('''
            background-color: #252932;
            color: #FED32C;
            padding: 10px;
            border: 3px solid #E6C02C;
            text-align: center;
            border-radius: 5px;
            font-size: 20px;
             ''')
        self.lbl_time.setFixedHeight(48)

        self.lbl_time2 = QLabel("Дата")
        self.lbl_time2.setAlignment(Qt.AlignHCenter)
        self.lbl_time2.setStyleSheet('''
            background-color: #252932;
            color: #FED32C;
            padding: 10px;
            border: 3px solid #E6C02C;
            text-align: center;
            border-radius: 5px;
            font-size: 20px;
             ''')
        self.lbl_time2.setFixedHeight(48)

        grid1 =QGridLayout() 
        card1 = QWidget()
        card1.setStyleSheet('''QWidget{
            background-color: #252932;
            color: #FED32C;
            padding: 10px;
            border: 3px solid #E6C02C;
            text-align: center;
            border-radius: 5px;
            font-size: 20px;
             }''')
        card1.setLayout(grid1)
        card1.setFixedHeight(132)
 

        lbl_now = QLabel("Сейчас")
        lbl_now.setAlignment(Qt.AlignHCenter)
        
        lbl_lessn = QLabel("Перемена")
        lbl_lessn.setAlignment(Qt.AlignHCenter)
        
        grid1.addWidget(lbl_now, 0, 0)
        grid1.addWidget(lbl_lessn, 1, 0)

        grid2 = QGridLayout()
        card2 = QWidget()
        card2.setStyleSheet('''
            background-color: #252932;
            color: #FED32C;
            padding: 10px;
            border: 3px solid #E6C02C;
            text-align: center;
            font-size: 20px;
             ''')
        card2.setLayout(grid2)

        lessns = [QLabel(f'Урок {i}: ') for i in range(1, 8)]

        for i in range(7):
            grid2.addWidget(lessns[i], i, 0)
            grid2.addWidget(QLabel(f'00:00:0{i}'), i, 1)


        layout.addWidget(self.lbl_time)
        layout.addWidget(self.lbl_time2)
        layout.addWidget(card1)
        layout.addWidget(card2)

        self.setLayout(layout)

        timer = QTimer(self)
        timer.timeout.connect(self.update_time)
        timer.start(1000)

    def update_time(self):
        tm = str(datetime.datetime.now().time())
        tm = tm[0:8]
        tm2 = str(datetime.datetime.now().date())
        self.lbl_time.setText(f'{tm}')
        self.lbl_time2.setText(f'{tm2}')

class SettingWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.setMouseTracking(True)
        
    def init_ui(self):
        self.layout = QVBoxLayout()
        self.lbl = QLabel(f"Страница настройки", alignment=Qt.AlignCenter)
        self.lbl.setStyleSheet('''
            background-color: #f7fafa;
            color: blue;
            padding: 10px;
            border: none;
            text-align: center;
            border-radius: 5px;
            font-size: 20px;
             ''')
        self.lbl.setMouseTracking(True)
        self.layout.addWidget(self.lbl)
        self.setLayout(self.layout)

       

    