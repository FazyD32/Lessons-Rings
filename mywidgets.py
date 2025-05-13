from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QGridLayout
from PyQt5.QtCore import Qt, QTimer
import datetime


class RightWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        layout = QVBoxLayout()

        self.lbl_time = QLabel("Время")
        self.lbl_time.setAlignment(Qt.AlignHCenter)
        self.lbl_time.setStyleSheet('''
            background-color: #f7fafa;
            color: blue;
            padding: 10px;
            border: none;
            text-align: center;
            border-radius: 5px;
            font-size: 20px;
             ''')
        self.lbl_time.setFixedHeight(48)

        self.lbl_time2 = QLabel("Дата")
        self.lbl_time2.setAlignment(Qt.AlignHCenter)
        self.lbl_time2.setStyleSheet('''
            background-color: #f7fafa;
            color: blue;
            padding: 10px;
            border: none;
            text-align: center;
            border-radius: 5px;
            font-size: 20px;
             ''')
        self.lbl_time2.setFixedHeight(48)

        grid1 =QGridLayout() 
        card1 = QWidget()
        card1.setStyleSheet('''
            background-color: #f7fafa;
            color: blue;
            padding: 10px;
            border: none;
            text-align: center;
            border-radius: 5px;
            font-size: 20px;
             ''')
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
            background-color: #f7fafa;
            color: blue;
            padding: 10px;
            border: none;
            text-align: center;
            border-radius: 5px;
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