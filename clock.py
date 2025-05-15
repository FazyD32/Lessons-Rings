from PyQt5.QtWidgets import QWidget
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import QBrush, QPainter, QPen, QColor
from PyQt5.QtCore import QPoint, QTime, Qt, QTimer


class ClockWidget(QWidget): #Вместо маин виндов можно и просто виджет
 
    def __init__(self):
        super().__init__()
 
        # Инициализируем таймер, потом в скобках устанавливаем функцию, которая будет воспроизводится при timer,start() - раз в указанное в скобках количество милисекунд
        timer = QTimer(self)
        timer.timeout.connect(self.update) #Это встроенная функция, обновление всего в окне
        timer.start(1000)
 
        self.setWindowTitle('Clock')
 
        self.setGeometry(200, 200, 300, 300)
 
        # Установить цвет фона
        self.setStyleSheet("background : white;")
        self.setMouseTracking(True)
 
        # Создать секундную стрелку, тут через другой объект (точкаqt) устанавливаются координаты точки и в массиве он последовательно соединяет их в полигон

        

        self.mPointer2 = QtGui.QPolygon([QPoint(-2, 5), QPoint(-4, 0), QPoint(0, -76), QPoint(4, 0), QPoint(2, 5)])
        self.mPointer = QtGui.QPolygon([QPoint(-1, 4), QPoint(-3, 0), QPoint(0, -75), QPoint(3, 0), QPoint(1, 4)])

        self.hPointer2 = QtGui.QPolygon([QPoint(-2, 5), QPoint(-4, 0), QPoint(0, -61), QPoint(4, 0), QPoint(2, 5)])
        self.hPointer = QtGui.QPolygon([QPoint(-1, 4), QPoint(-3, 0), QPoint(0, -60), QPoint(3, 0), QPoint(1, 4)])

        self.sPointer = QtGui.QPolygon([QPoint(-1, 2), QPoint(-2, 0), QPoint(0, -100), QPoint(2, 0), QPoint(1, 2)])


 
        # Установить цвета, часовые и минуты, секунда красная
        self.bColor = Qt.yellow
        self.bbColor = QColor(255, 165, 0)
        self.sColor = Qt.red
 
    # Перезаписываем встроенный метод отрисовки
    def paintEvent(self, event):
 
        # Получаем минимальную высоту и ширину
        # Чтобы часы оставались в квадрате, а не растягивались
        rec = min(self.width(), self.height())
 
        # Получаем текущее время
        tik = QTime.currentTime()
 
        # Создаем объект кисти
        painter = QPainter(self)
 
        # кастомный метод отрисовки стрелок
        def drawPointer(color, rotation, pointer):
 
            # Установка настроек кисти в созданном выше объекте
            painter.setBrush(QBrush(color))
 
            # Сохранение настроек
            painter.save()
 
            # Поворот кисти,
            #  координаты считаются до поворота, то есть сначала мы  QtGui.QPolygon отрисовали свой многоугольник, а затем уже нарисованную фигуру тупо повернули
            painter.rotate(rotation)
 
            # Отрисовка полигона из точек
            painter.drawConvexPolygon(pointer)
 
            # Возобновить кисть, чтобы рисовать что-то новое, вообще это скорее сбросить цвет и угол
            painter.restore()
 
        # настроить режим кисть (сглаживание вроде)
        painter.setRenderHint(QPainter.Antialiasing)
 
        # тут от кисти будут отсчитываться координаты, в данном случае от центра главного виджета (класса)
        painter.translate(self.width() / 2, self.height() / 2)
 
        # масштабирование
        painter.scale(rec / 200, rec / 200)
 
        # Установить тип кисти, без кисти, если в переводе
        painter.setPen(QtCore.Qt.NoPen)
 
        # отрисовка стрелки 
        # Угол считается по логике: 6 * на условные 30 секунд = 180 градусов
        drawPointer(self.sColor, (6*tik.second()), self.sPointer) 

        drawPointer(self.bbColor, (30 * (tik.hour() + tik.minute() / 60)), self.hPointer2)
        drawPointer(self.bColor, (30 * (tik.hour() + tik.minute() / 60)), self.hPointer)

        drawPointer(self.bbColor, (6 * (tik.minute() + tik.second() / 60)), self.mPointer2)
        drawPointer(self.bColor, (6 * (tik.minute() + tik.second() / 60)), self.mPointer)

        

        #Ручка рисует контур, а кисть сплошняком
        painter.setBrush(QBrush(Qt.red))
        painter.setPen(QPen(QColor(255, 165, 0)))
        painter.drawEllipse(-4, -4, 9, 9)
 
        # Отрисовать задний фон, но не работает
        painter.setPen(QPen(self.sColor))

        # В цикле отрисовать черты для времени

        for i in range(0, 60):   
 
            # drawing background lines
            if (i%5) == 0:
                painter.drawLine(87, 0, 97, 0)
            painter.rotate(6)

        painter.setPen(QPen(QColor(255, 165, 0)))
        painter.setBrush(QBrush(Qt.red))
    
        painter.drawText(82-3, 4, str(3))
        painter.drawText(-3, 87-3, str(6))
        painter.drawText(-87+3, 4, str(9))
        painter.drawText(-6, -87+10, str(12))

        # Закончить рисование
        painter.end()