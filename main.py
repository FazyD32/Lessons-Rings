from clock import ClockWidget
from menu import SlideMenu
from settingswidget import Ui_SettingWidget
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setMouseTracking(True)

    def setupUi(self, MainWindow):
        self.menu = SlideMenu(self)
        self.settings = Ui_SettingWidget()

        #Главный виджет
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1241, 732)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMouseTracking(True)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")

        self.centralwidget.setStyleSheet('''background : #20232A;''')

        # MainWindow.setStyleSheet("""QMainWindow#MainWindow{
        #     background-image: url(background);
        #     background-position: center;
        #     background-repeat: no-repeat;
        #     background-attachment: fixed;
        #     background-size: cover;}
        # """)

        #Виджет для часов
        self.ClockForWidget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ClockForWidget.sizePolicy().hasHeightForWidth())
        self.ClockForWidget.setSizePolicy(sizePolicy)
        self.ClockForWidget.setMouseTracking(True)
        self.ClockForWidget.setObjectName("ClockForWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.ClockForWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.LayForClock = QtWidgets.QVBoxLayout()
        self.LayForClock.setObjectName("LayForClock")

        self.verticalLayout_2.addLayout(self.LayForClock)
        self.horizontalLayout_8.addWidget(self.ClockForWidget)

        #Виджет самих часов
        self.clock = ClockWidget()
        self.LayForClock.addWidget(self.clock)

        #Правый виджет
        self.LessnsWidget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LessnsWidget.sizePolicy().hasHeightForWidth())
        self.LessnsWidget.setSizePolicy(sizePolicy)
        self.LessnsWidget.setMouseTracking(True)
        self.LessnsWidget.setObjectName("LessnsWidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.LessnsWidget)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        #Виджет для даты и времени
        self.DateWidget = QtWidgets.QWidget(self.LessnsWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DateWidget.sizePolicy().hasHeightForWidth())
        self.DateWidget.setSizePolicy(sizePolicy)
        self.DateWidget.setMinimumSize(QtCore.QSize(800, 0))
        self.DateWidget.setMouseTracking(True)
        self.DateWidget.setObjectName("DateWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.DateWidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        self.DateWidget.setStyleSheet('''QWidget#DateWidget{
            color: #FED32C;
            padding: 10px;
            border: 3px solid #E6C02C;
            border-radius: 5px;}
             ''')

        #Надпись дня недели
        self.weekDayLbl = QtWidgets.QLabel(self.DateWidget)
        self.weekDayLbl.setMouseTracking(True)
        self.weekDayLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.weekDayLbl.setObjectName("weekDayLbl")

        self.verticalLayout_4.addWidget(self.weekDayLbl)

        self.weekDayLbl.setStyleSheet('''
            color: #FED32C;
            text-align: center;
            font-size: 42px;
            font-style: bold;
             ''')

        #Надпись даты
        self.DateLbl = QtWidgets.QLabel(self.DateWidget)
        self.DateLbl.setMouseTracking(True)
        self.DateLbl.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.DateLbl.setObjectName("DateLbl")

        self.verticalLayout_4.addWidget(self.DateLbl)

        self.DateLbl.setStyleSheet('''
            color: #FED32C;
            text-align: center;
            font-size: 32px;
             ''')

        #Надпись времени
        self.TimeLbl = QtWidgets.QLabel(self.DateWidget)
        self.TimeLbl.setMouseTracking(True)
        self.TimeLbl.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.TimeLbl.setObjectName("TimeLbl")

        self.verticalLayout_4.addWidget(self.TimeLbl)
        self.verticalLayout.addWidget(self.DateWidget)

        self.TimeLbl.setStyleSheet('''
            color: #FED32C;
            text-align: center;
            font-size: 32px;
             ''')

        #Виджет для текущего статуса
        self.CurrentLessonWidget = QtWidgets.QWidget(self.LessnsWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CurrentLessonWidget.sizePolicy().hasHeightForWidth())
        self.CurrentLessonWidget.setSizePolicy(sizePolicy)
        self.CurrentLessonWidget.setMinimumSize(QtCore.QSize(800, 0))
        self.CurrentLessonWidget.setMouseTracking(True)
        self.CurrentLessonWidget.setObjectName("CurrentLessonWidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.CurrentLessonWidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")

        self.CurrentLessonWidget.setStyleSheet('''QWidget#CurrentLessonWidget{
            color: #FED32C;
            padding: 10px;
            border: 3px solid #E6C02C;
            border-radius: 5px;}
             ''')

        #Надпись Сейчас
        self.LblNow = QtWidgets.QLabel(self.CurrentLessonWidget)
        self.LblNow.setMouseTracking(True)
        self.LblNow.setAlignment(QtCore.Qt.AlignCenter)
        self.LblNow.setObjectName("LblNow")

        self.verticalLayout_5.addWidget(self.LblNow)

        self.LblNow.setStyleSheet('''
            color: #FED32C;
            text-align: center;
            font-size: 42px;
            font-style: bold;
             ''')

        #Надпись урока или перемены
        self.LblPeremena = QtWidgets.QLabel(self.CurrentLessonWidget)
        self.LblPeremena.setMouseTracking(True)
        self.LblPeremena.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.LblPeremena.setObjectName("LblPeremena")

        self.verticalLayout_5.addWidget(self.LblPeremena)

        self.LblPeremena.setStyleSheet('''
            color: #FED32C;
            text-align: center;
            font-size: 32px;
             ''')

        #Надпись до урока осталось
        self.LblTimeTo = QtWidgets.QLabel(self.CurrentLessonWidget)
        self.LblTimeTo.setMouseTracking(True)
        self.LblTimeTo.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.LblTimeTo.setObjectName("LblTimeTo")

        self.verticalLayout_5.addWidget(self.LblTimeTo)
        self.verticalLayout.addWidget(self.CurrentLessonWidget)

        self.LblTimeTo.setStyleSheet('''
            color: #FED32C;
            text-align: center;
            font-size: 32px;
             ''')
        
        #Виджет для расписания
        self.WidgetLessns = QtWidgets.QWidget(self.LessnsWidget)    
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(80)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.WidgetLessns.sizePolicy().hasHeightForWidth())
        self.WidgetLessns.setSizePolicy(sizePolicy)
        self.WidgetLessns.setMinimumSize(QtCore.QSize(800, 0))
        self.WidgetLessns.setMouseTracking(True)
        self.WidgetLessns.setObjectName("WidgetLessns")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.WidgetLessns)
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")

        self.WidgetLessns.setStyleSheet('''QWidget#WidgetLessns{
            background-color: #252932;
            color: #FED32C;
            padding: 10px;
            border: 3px solid #E6C02C;
            border-radius: 5px;}
             ''')

        #Урок 1
        self.Les1 = QtWidgets.QLabel(self.WidgetLessns)
        self.Les1.setMouseTracking(True)
        self.Les1.setAlignment(QtCore.Qt.AlignCenter)
        self.Les1.setObjectName("Les1")

        self.horizontalLayout_6.addWidget(self.Les1)

        self.Les1.setStyleSheet('''
            color: #FED32C;
            text-align: center;
            font-size: 24px;
            font-style: bold;
             ''')

        #Время 1
        self.Time1 = QtWidgets.QLabel(self.WidgetLessns)
        self.Time1.setMouseTracking(True)
        self.Time1.setAlignment(QtCore.Qt.AlignCenter)
        self.Time1.setObjectName("Time1")

        self.horizontalLayout_6.addWidget(self.Time1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")

        self.Time1.setStyleSheet('''
            color: #FED32C;
            text-align: center;
            font-size: 24px;
             ''')

        #Урок 2
        self.Les2 = QtWidgets.QLabel(self.WidgetLessns)
        self.Les2.setMouseTracking(True)
        self.Les2.setAlignment(QtCore.Qt.AlignCenter)
        self.Les2.setObjectName("Les2")

        self.horizontalLayout_5.addWidget(self.Les2)

        self.Les2.setStyleSheet('''
            color: #FED32C;
            text-align: center;
            font-size: 24px;
            font-style: bold;
             ''')

        #Время 2
        self.Time2 = QtWidgets.QLabel(self.WidgetLessns)
        self.Time2.setMouseTracking(True)
        self.Time2.setAlignment(QtCore.Qt.AlignCenter)
        self.Time2.setObjectName("Time2")

        self.horizontalLayout_5.addWidget(self.Time2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        self.Time2.setStyleSheet('''
            color: #FED32C;
            text-align: center;
            font-size: 24px;
             ''')

        #Урок 3
        self.Les3 = QtWidgets.QLabel(self.WidgetLessns)
        self.Les3.setMouseTracking(True)
        self.Les3.setAlignment(QtCore.Qt.AlignCenter)
        self.Les3.setObjectName("Les3")

        self.horizontalLayout_4.addWidget(self.Les3)

        self.Les3.setStyleSheet('''
            color: #FED32C;
            text-align: center;
            font-size: 24px;
            font-style: bold;
             ''')

        #Время 3
        self.Time3 = QtWidgets.QLabel(self.WidgetLessns)
        self.Time3.setMouseTracking(True)
        self.Time3.setAlignment(QtCore.Qt.AlignCenter)
        self.Time3.setObjectName("Time3")

        self.horizontalLayout_4.addWidget(self.Time3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.Time3.setStyleSheet('''
            color: #FED32C;
            text-align: center;
            font-size: 24px;
             ''')

        #Урок 4
        self.Les4 = QtWidgets.QLabel(self.WidgetLessns)
        self.Les4.setMouseTracking(True)
        self.Les4.setAlignment(QtCore.Qt.AlignCenter)
        self.Les4.setObjectName("Les4")

        self.horizontalLayout_3.addWidget(self.Les4)

        self.Les4.setStyleSheet('''
            color: #FED32C;
            text-align: center;
            font-size: 24px;
            font-style: bold;
             ''')

        #Время 4
        self.Time4 = QtWidgets.QLabel(self.WidgetLessns)
        self.Time4.setMouseTracking(True)
        self.Time4.setAlignment(QtCore.Qt.AlignCenter)
        self.Time4.setObjectName("Time4")

        self.horizontalLayout_3.addWidget(self.Time4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")

        self.Time4.setStyleSheet('''
            color: #FED32C;
            text-align: center;
            font-size: 24px;
             ''')

        #урок 5
        self.Les5 = QtWidgets.QLabel(self.WidgetLessns)
        self.Les5.setMouseTracking(True)
        self.Les5.setAlignment(QtCore.Qt.AlignCenter)
        self.Les5.setObjectName("Les5")

        self.horizontalLayout_7.addWidget(self.Les5)

        self.Les5.setStyleSheet('''
            color: #FED32C;
            text-align: center;
            font-size: 24px;
            font-style: bold;
             ''')

        #Время 5
        self.Time5 = QtWidgets.QLabel(self.WidgetLessns)
        self.Time5.setMouseTracking(True)
        self.Time5.setAlignment(QtCore.Qt.AlignCenter)
        self.Time5.setObjectName("Time5")

        self.horizontalLayout_7.addWidget(self.Time5)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.Time5.setStyleSheet('''
            color: #FED32C;
            text-align: center;
            font-size: 24px;
             ''')

        #Урок 6
        self.Les6 = QtWidgets.QLabel(self.WidgetLessns)
        self.Les6.setMouseTracking(True)
        self.Les6.setAlignment(QtCore.Qt.AlignCenter)
        self.Les6.setObjectName("Les6")

        self.horizontalLayout_2.addWidget(self.Les6)

        self.Les6.setStyleSheet('''
            color: #FED32C;
            text-align: center;
            font-size: 24px;
            font-style: bold;
             ''')

        #Время 6
        self.Time6 = QtWidgets.QLabel(self.WidgetLessns)
        self.Time6.setMouseTracking(True)
        self.Time6.setAlignment(QtCore.Qt.AlignCenter)
        self.Time6.setObjectName("Time6")

        self.horizontalLayout_2.addWidget(self.Time6)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.Time6.setStyleSheet('''
            color: #FED32C;
            text-align: center;
            font-size: 24px;
             ''')

        #Урок 7
        self.Les7 = QtWidgets.QLabel(self.WidgetLessns)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Les7.sizePolicy().hasHeightForWidth())
        self.Les7.setSizePolicy(sizePolicy)
        self.Les7.setMouseTracking(True)
        self.Les7.setAlignment(QtCore.Qt.AlignCenter)
        self.Les7.setObjectName("Les7")

        self.horizontalLayout.addWidget(self.Les7)

        self.Les7.setStyleSheet('''
            color: #FED32C;
            text-align: center;
            font-size: 24px;
            font-style: bold;
             ''')

        #Время 7
        self.Time7 = QtWidgets.QLabel(self.WidgetLessns)
        self.Time7.setMouseTracking(True)
        self.Time7.setAlignment(QtCore.Qt.AlignCenter)
        self.Time7.setObjectName("Time7")

        self.horizontalLayout.addWidget(self.Time7)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout.addWidget(self.WidgetLessns)
        self.verticalLayout_6.addLayout(self.verticalLayout)
        self.horizontalLayout_8.addWidget(self.LessnsWidget)

        self.Time7.setStyleSheet('''
            color: #FED32C;
            text-align: center;
            font-size: 24px;
             ''')

        #Многостраничное приложение     
        self.pages = QtWidgets.QStackedWidget()
        self.pages.setMouseTracking(True)
        self.pages.addWidget(self.centralwidget)
        self.pages.addWidget(self.settings)

        MainWindow.setCentralWidget(self.pages)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.weekDayLbl.setText(_translate("MainWindow", "День недели"))
        self.DateLbl.setText(_translate("MainWindow", "Дата"))
        self.TimeLbl.setText(_translate("MainWindow", "Время"))
        self.LblNow.setText(_translate("MainWindow", "Сейчас"))
        self.LblPeremena.setText(_translate("MainWindow", "Перемена/УрокХ"))
        self.LblTimeTo.setText(_translate("MainWindow", "До урока/перемены осталось ..."))
        self.Les1.setText(_translate("MainWindow", "Урок 1"))
        self.Time1.setText(_translate("MainWindow", "Время 1"))
        self.Les2.setText(_translate("MainWindow", "Урок 2"))
        self.Time2.setText(_translate("MainWindow", "Время 2"))
        self.Les3.setText(_translate("MainWindow", "Урок 3"))
        self.Time3.setText(_translate("MainWindow", "Время 3"))
        self.Les4.setText(_translate("MainWindow", "Урок 4"))
        self.Time4.setText(_translate("MainWindow", "Время 4"))
        self.Les5.setText(_translate("MainWindow", "Урок 5"))
        self.Time5.setText(_translate("MainWindow", "Время 5"))
        self.Les6.setText(_translate("MainWindow", "Урок 6"))
        self.Time6.setText(_translate("MainWindow", "Время 6"))
        self.Les7.setText(_translate("MainWindow", "Урок 7"))
        self.Time7.setText(_translate("MainWindow", "Время 7"))

    def switch_page(self):
        # Переключение на следующую страницу
        new_index = (self.pages.currentIndex() + 1) % self.pages.count()
        self.pages.setCurrentIndex(new_index)   

    def mouseMoveEvent(self, event):
        print('11')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
