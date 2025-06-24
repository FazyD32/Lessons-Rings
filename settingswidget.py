from PyQt5 import QtCore, QtGui, QtWidgets
from pygame import mixer

class Ui_SettingWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setMouseTracking(True)
        self.set_settings()

       

    def setupUi(self, SettingWidget):
        lblStyle = '''
            color: #FED32C;
             '''
        style = '''QWidget{
            color: #FED32C;
            padding: 10px;
            border: 3px solid #E6C02C;
            border-radius: 5px;}
             '''
        
        SettingWidget.setObjectName("SettingWidget")
        SettingWidget.resize(1280, 720)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(SettingWidget)
        self.verticalLayout_10.setObjectName("verticalLayout_10")

        self.setStyleSheet(lblStyle)
        self.setMouseTracking(True)

        #Надпись Настройки
        self.SettingLabel = QtWidgets.QLabel(SettingWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SettingLabel.sizePolicy().hasHeightForWidth())
        self.SettingLabel.setSizePolicy(sizePolicy)
        self.SettingLabel.setMinimumSize(QtCore.QSize(0, 120))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.SettingLabel.setFont(font)
        self.SettingLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.SettingLabel.setObjectName("SettingLabel")

        self.SettingLabel.setStyleSheet(lblStyle)
        self.SettingLabel.setMouseTracking(True)

        self.verticalLayout_10.addWidget(self.SettingLabel)
        
        #Основной компановщик
        self.TopLayout = QtWidgets.QHBoxLayout()
        self.TopLayout.setObjectName("TopLayout")

        #Виджет настроек браузера
        self.WebWidgetSetting = QtWidgets.QWidget(SettingWidget)
        self.WebWidgetSetting.setObjectName("WebWidgetSetting")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.WebWidgetSetting)
        self.verticalLayout.setObjectName("verticalLayout")

        self.WebWidgetSetting.setStyleSheet('''QWidget#WebWidgetSetting{
  
            padding: 10px;
            border: 3px solid #E6C02C;
            border-radius: 5px;}
             ''')
        self.WebWidgetSetting.setMouseTracking(True)

        #Надпись Веб Браузер
        self.label_2 = QtWidgets.QLabel(self.WebWidgetSetting)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        self.label_2.setStyleSheet(lblStyle)
        self.label_2.setMouseTracking(True)

        self.verticalLayout.addWidget(self.label_2)

        #Использовать браузер?
        self.BrowserBool = QtWidgets.QCheckBox(self.WebWidgetSetting)
        self.BrowserBool.setLayoutDirection(QtCore.Qt.RightToLeft)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.BrowserBool.setFont(font)
        self.BrowserBool.setObjectName("BrowserBool")

        self.verticalLayout.addWidget(self.BrowserBool)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.BrowserBool.setStyleSheet(lblStyle)
        self.BrowserBool.setMouseTracking(True)

        #Надпись адреса url
        self.urlLabel = QtWidgets.QLabel(self.WebWidgetSetting)
        self.urlLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.urlLabel.setObjectName("urlLabel")

        self.horizontalLayout.addWidget(self.urlLabel)

        self.urlLabel.setStyleSheet(lblStyle)
        self.urlLabel.setMouseTracking(True)

        #Поле ввода url
        self.urlEdit = QtWidgets.QLineEdit(self.WebWidgetSetting)
        self.urlEdit.setObjectName("urlEdit")

        self.horizontalLayout.addWidget(self.urlEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.urlEdit.setStyleSheet(style)
        self.urlEdit.setMouseTracking(True)

        #Текущий url
        self.CurrentURLLabel = QtWidgets.QLabel(self.WebWidgetSetting)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.CurrentURLLabel.setFont(font)
        self.CurrentURLLabel.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.CurrentURLLabel.setObjectName("CurrentURLLabel")

        self.CurrentURLLabel.setStyleSheet(lblStyle)
        self.CurrentURLLabel.setMouseTracking(True)

        self.verticalLayout.addWidget(self.CurrentURLLabel)
        self.TopLayout.addWidget(self.WebWidgetSetting)

        #Разделитель
        spacerItem = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)

        self.TopLayout.addItem(spacerItem)

        #Виджет настроек аудио и  разрешения
        self.AudioResWidget = QtWidgets.QWidget(SettingWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AudioResWidget.sizePolicy().hasHeightForWidth())
        self.AudioResWidget.setSizePolicy(sizePolicy)
        self.AudioResWidget.setObjectName("AudioResWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.AudioResWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.AudioResWidget.setStyleSheet('''QWidget#AudioResWidget{
            padding: 10px;
            border: 3px solid #E6C02C;
            border-radius: 5px;}
             ''')
        self.AudioResWidget.setMouseTracking(True)

        #Надпись Аудио
        self.AudioLabel = QtWidgets.QLabel(self.AudioResWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.AudioLabel.setFont(font)
        self.AudioLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.AudioLabel.setObjectName("AudioLabel")

        self.AudioLabel.setStyleSheet(lblStyle)
        self.AudioLabel.setMouseTracking(True)

        self.verticalLayout_2.addWidget(self.AudioLabel)

        #Кнопка Воспроизвести
        self.PlayButton = QtWidgets.QPushButton(self.AudioResWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.PlayButton.setFont(font)
        self.PlayButton.setObjectName("PlayButton")

        self.PlayButton.setStyleSheet(style)
        self.PlayButton.setMouseTracking(True)

        self.verticalLayout_2.addWidget(self.PlayButton)

        self.PlayButton.setStyleSheet("""
        QPushButton {
            background-color: #4CAF50;
            color: white;
            border: 2px solid #3e8e41;
            border-radius: 8px;
            padding: 12px 24px;
            font-size: 16px;
            font-weight: bold;

        }
        QPushButton:hover {
            background-color: #45a049;

        }
        QPushButton:pressed {
            background-color: #3d8b40;
            border-top: 3px solid #3e8e41;
            border-left: 3px solid #3e8e41;
            border-right: 1px solid #3e8e41;
            border-bottom: 1px solid #3e8e41;
        }
        QPushButton:disabled {
            background-color: #cccccc;
            border-color: #aaaaaa;
            color: #888888;
        }
        """)

        self.PlayButton.clicked.connect(self.play_audio)

        #Надпись разрешение
        self.ResolutionLabel = QtWidgets.QLabel(self.AudioResWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.ResolutionLabel.setFont(font)
        self.ResolutionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ResolutionLabel.setObjectName("ResolutionLabel")

        self.ResolutionLabel.setStyleSheet(lblStyle)
        self.ResolutionLabel.setMouseTracking(True)

        self.verticalLayout_2.addWidget(self.ResolutionLabel)

        #Список доступных разрешений (выпадающий)
        self.ResolutionListBox = QtWidgets.QComboBox(self.AudioResWidget)
        self.ResolutionListBox.setObjectName("ResolutionListBox")

        self.ResolutionListBox.addItem("")
        self.ResolutionListBox.addItem("")
        self.ResolutionListBox.addItem("")
        self.ResolutionListBox.addItem("")

        self.ResolutionListBox.setStyleSheet(style)
        self.ResolutionListBox.setMouseTracking(True)

        self.verticalLayout_2.addWidget(self.ResolutionListBox)
        self.TopLayout.addWidget(self.AudioResWidget)
        self.verticalLayout_10.addLayout(self.TopLayout)

        #Таблица расписания
        self.LessTab = QtWidgets.QTabWidget(SettingWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LessTab.sizePolicy().hasHeightForWidth())
        self.LessTab.setSizePolicy(sizePolicy)
        self.LessTab.setObjectName("LessTab")

        self.LessTab.setStyleSheet(style)
        self.LessTab.setMouseTracking(True)

        #Вкладка Понедельник
        self.Mon = QtWidgets.QWidget()
        self.Mon.setObjectName("Mon")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.Mon)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        #надпись Понедельник
        self.MonLbl = QtWidgets.QLabel(self.Mon)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MonLbl.sizePolicy().hasHeightForWidth())
        self.MonLbl.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.MonLbl.setFont(font)
        self.MonLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.MonLbl.setObjectName("MonLbl")
        self.verticalLayout_3.addWidget(self.MonLbl)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")

        #Урок 1 П
        self.mLes1 = QtWidgets.QLabel(self.Mon)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mLes1.setFont(font)
        self.mLes1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.mLes1.setObjectName("mLes1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.mLes1)

        self.mEdit1 = QtWidgets.QTimeEdit(self.Mon)
        self.mEdit1.setObjectName("mEdit1")

        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.mEdit1)

        #Урок 2 П
        self.mLes2 = QtWidgets.QLabel(self.Mon)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mLes2.setFont(font)
        self.mLes2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.mLes2.setObjectName("mLes2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.mLes2)

        self.mEdit2 = QtWidgets.QTimeEdit(self.Mon)
        self.mEdit2.setObjectName("mEdit2")

        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.mEdit2)

        #Урок 3 П
        self.mLes3 = QtWidgets.QLabel(self.Mon)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mLes3.setFont(font)
        self.mLes3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.mLes3.setObjectName("mLes3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.mLes3)

        self.mEdit3 = QtWidgets.QTimeEdit(self.Mon)
        self.mEdit3.setObjectName("mEdit3")

        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.mEdit3)

        #Урок 4 П
        self.mLes4 = QtWidgets.QLabel(self.Mon)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mLes4.setFont(font)
        self.mLes4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.mLes4.setObjectName("mLes4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.mLes4)

        self.mEdit4 = QtWidgets.QTimeEdit(self.Mon)
        self.mEdit4.setObjectName("mEdit4")

        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.mEdit4)

        #Урок 5 П
        self.mLes5 = QtWidgets.QLabel(self.Mon)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mLes5.setFont(font)
        self.mLes5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.mLes5.setObjectName("mLes5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.mLes5)

        self.mEdit5 = QtWidgets.QTimeEdit(self.Mon)
        self.mEdit5.setObjectName("mEdit5")

        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.mEdit5)

        #Урок 6 П
        self.mLes6 = QtWidgets.QLabel(self.Mon)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mLes6.setFont(font)
        self.mLes6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.mLes6.setObjectName("mLes6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.mLes6)

        self.mEdit6 = QtWidgets.QTimeEdit(self.Mon)
        self.mEdit6.setObjectName("mEdit6")

        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.mEdit6)

        #Урок 7 П
        self.mLes7 = QtWidgets.QLabel(self.Mon)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mLes7.setFont(font)
        self.mLes7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.mLes7.setObjectName("mLes7")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.mLes7)

        self.mEdit7 = QtWidgets.QTimeEdit(self.Mon)
        self.mEdit7.setObjectName("mEdit7")

        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.mEdit7)
        self.verticalLayout_3.addLayout(self.formLayout)
        self.LessTab.addTab(self.Mon, "")

        #Вкладка Вторник
        self.Tyo = QtWidgets.QWidget()
        self.Tyo.setObjectName("Tyo")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.Tyo)
        self.verticalLayout_5.setObjectName("verticalLayout_5")

        #Надпись Dnjhybr
        self.TyoLbl = QtWidgets.QLabel(self.Tyo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TyoLbl.sizePolicy().hasHeightForWidth())
        self.TyoLbl.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.TyoLbl.setFont(font)
        self.TyoLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.TyoLbl.setObjectName("TyoLbl")
        self.verticalLayout_5.addWidget(self.TyoLbl)
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setObjectName("formLayout_4")

        #урок 1 В
        self.tLes1 = QtWidgets.QLabel(self.Tyo)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tLes1.setFont(font)
        self.tLes1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tLes1.setObjectName("tLes1")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.tLes1)

        self.tEdit1 = QtWidgets.QTimeEdit(self.Tyo)
        self.tEdit1.setObjectName("tEdit1")

        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.tEdit1)

        #урок 2 В
        self.tLes2 = QtWidgets.QLabel(self.Tyo)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tLes2.setFont(font)
        self.tLes2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tLes2.setObjectName("tLes2")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.tLes2)

        self.tEdit2 = QtWidgets.QTimeEdit(self.Tyo)
        self.tEdit2.setObjectName("tEdit2")

        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.tEdit2)

        #урок 3 В
        self.tLes3 = QtWidgets.QLabel(self.Tyo)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tLes3.setFont(font)
        self.tLes3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tLes3.setObjectName("tLes3")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.tLes3)

        self.tEdit3 = QtWidgets.QTimeEdit(self.Tyo)
        self.tEdit3.setObjectName("tEdit3")

        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.tEdit3)

        #Урок 4 В
        self.tLes4 = QtWidgets.QLabel(self.Tyo)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tLes4.setFont(font)
        self.tLes4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tLes4.setObjectName("tLes4")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.tLes4)

        self.tEdit4 = QtWidgets.QTimeEdit(self.Tyo)
        self.tEdit4.setObjectName("tEdit4")

        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.tEdit4)

        #Урок 5 В
        self.tLes5 = QtWidgets.QLabel(self.Tyo)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tLes5.setFont(font)
        self.tLes5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tLes5.setObjectName("tLes5")
        self.formLayout_4.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.tLes5)

        self.tEdit5 = QtWidgets.QTimeEdit(self.Tyo)
        self.tEdit5.setObjectName("tEdit5")

        self.formLayout_4.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.tEdit5)

        #Урок 6 В
        self.tLes6 = QtWidgets.QLabel(self.Tyo)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tLes6.setFont(font)
        self.tLes6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tLes6.setObjectName("tLes6")
        self.formLayout_4.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.tLes6)

        self.tEdit6 = QtWidgets.QTimeEdit(self.Tyo)
        self.tEdit6.setObjectName("tEdit6")

        self.formLayout_4.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.tEdit6)

        #Урок 7 В
        self.tLes7 = QtWidgets.QLabel(self.Tyo)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tLes7.setFont(font)
        self.tLes7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tLes7.setObjectName("tLes7")
        self.formLayout_4.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.tLes7)

        self.tEdit7 = QtWidgets.QTimeEdit(self.Tyo)
        self.tEdit7.setObjectName("tEdit7")

        self.formLayout_4.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.tEdit7)

        self.verticalLayout_5.addLayout(self.formLayout_4)
        self.LessTab.addTab(self.Tyo, "")

        #Вкладка Среда
        self.Wen = QtWidgets.QWidget()
        self.Wen.setObjectName("Wen")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.Wen)
        self.verticalLayout_6.setObjectName("verticalLayout_6")

        #Надпись Среда
        self.WenLbl = QtWidgets.QLabel(self.Wen)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.WenLbl.setFont(font)
        self.WenLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.WenLbl.setObjectName("WenLbl")
        self.verticalLayout_6.addWidget(self.WenLbl)
        self.formLayout_5 = QtWidgets.QFormLayout()
        self.formLayout_5.setObjectName("formLayout_5")
        self.wLes1 = QtWidgets.QLabel(self.Wen)
        font = QtGui.QFont()
        font.setPointSize(12)

        #Урок 1 С
        self.wLes1.setFont(font)
        self.wLes1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.wLes1.setObjectName("wLes1")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.wLes1)

        self.wEdit1 = QtWidgets.QTimeEdit(self.Wen)
        self.wEdit1.setObjectName("wEdit1")

        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.wEdit1)

        #Урок 2 С
        self.wLes2 = QtWidgets.QLabel(self.Wen)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.wLes2.setFont(font)
        self.wLes2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.wLes2.setObjectName("wLes2")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.wLes2)

        self.wEdit2 = QtWidgets.QTimeEdit(self.Wen)
        self.wEdit2.setObjectName("wEdit2")

        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.wEdit2)

        #Урок 3 С
        self.wLes3 = QtWidgets.QLabel(self.Wen)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.wLes3.setFont(font)
        self.wLes3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.wLes3.setObjectName("wLes3")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.wLes3)

        self.wEdit3 = QtWidgets.QTimeEdit(self.Wen)
        self.wEdit3.setObjectName("wEdit3")

        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.wEdit3)

        #Урок 4 С
        self.wLes4 = QtWidgets.QLabel(self.Wen)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.wLes4.setFont(font)
        self.wLes4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.wLes4.setObjectName("wLes4")
        self.formLayout_5.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.wLes4)

        self.wEdit4 = QtWidgets.QTimeEdit(self.Wen)
        self.wEdit4.setObjectName("wEdit4")

        self.formLayout_5.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.wEdit4)

        #Урок 5 С
        self.wLes5 = QtWidgets.QLabel(self.Wen)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.wLes5.setFont(font)
        self.wLes5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.wLes5.setObjectName("wLes5")
        self.formLayout_5.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.wLes5)

        self.wEdit5 = QtWidgets.QTimeEdit(self.Wen)
        self.wEdit5.setObjectName("wEdit5")

        self.formLayout_5.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.wEdit5)

        #Урок 6 С
        self.wLes6 = QtWidgets.QLabel(self.Wen)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.wLes6.setFont(font)
        self.wLes6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.wLes6.setObjectName("wLes6")
        self.formLayout_5.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.wLes6)

        self.wEdit6 = QtWidgets.QTimeEdit(self.Wen)
        self.wEdit6.setObjectName("wEdit6")

        self.formLayout_5.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.wEdit6)

        #Урок 7 С
        self.wLes7 = QtWidgets.QLabel(self.Wen)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.wLes7.setFont(font)
        self.wLes7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.wLes7.setObjectName("wLes7")
        self.formLayout_5.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.wLes7)

        self.wEdit7 = QtWidgets.QTimeEdit(self.Wen)
        self.wEdit7.setObjectName("wEdit7")

        self.formLayout_5.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.wEdit7)
        self.verticalLayout_6.addLayout(self.formLayout_5)
        self.LessTab.addTab(self.Wen, "")

        #Вкладка Четверг
        self.Thi = QtWidgets.QWidget()
        self.Thi.setObjectName("Thi")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.Thi)
        self.verticalLayout_7.setObjectName("verticalLayout_7")

        #Надпись Четверг
        self.ThiLbl = QtWidgets.QLabel(self.Thi)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.ThiLbl.setFont(font)
        self.ThiLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.ThiLbl.setObjectName("ThiLbl")
        self.verticalLayout_7.addWidget(self.ThiLbl)
        self.formLayout_6 = QtWidgets.QFormLayout()
        self.formLayout_6.setObjectName("formLayout_6")

        #Урок 1 Ч
        self.thLes1 = QtWidgets.QLabel(self.Thi)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.thLes1.setFont(font)
        self.thLes1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.thLes1.setObjectName("thLes1")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.thLes1)

        self.thEdit1 = QtWidgets.QTimeEdit(self.Thi)
        self.thEdit1.setObjectName("thEdit1")

        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.thEdit1)

        #Урок 2 Ч
        self.thLes2 = QtWidgets.QLabel(self.Thi)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.thLes2.setFont(font)
        self.thLes2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.thLes2.setObjectName("thLes2")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.thLes2)

        self.thEdit2 = QtWidgets.QTimeEdit(self.Thi)
        self.thEdit2.setObjectName("thEdit2")

        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.thEdit2)

        #Урок 3 Ч
        self.thLes3 = QtWidgets.QLabel(self.Thi)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.thLes3.setFont(font)
        self.thLes3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.thLes3.setObjectName("thLes3")
        self.formLayout_6.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.thLes3)
        self.thEdit3 = QtWidgets.QTimeEdit(self.Thi)
        self.thEdit3.setObjectName("thEdit3")
        self.formLayout_6.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.thEdit3)
        self.thLes4 = QtWidgets.QLabel(self.Thi)
        font = QtGui.QFont()
        font.setPointSize(12)

        #Урок 4 Ч
        self.thLes4.setFont(font)
        self.thLes4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.thLes4.setObjectName("thLes4")
        self.formLayout_6.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.thLes4)

        self.thEdit4 = QtWidgets.QTimeEdit(self.Thi)
        self.thEdit4.setObjectName("thEdit4")

        self.formLayout_6.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.thEdit4)

        #Урок 5 Ч
        self.thLes5 = QtWidgets.QLabel(self.Thi)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.thLes5.setFont(font)
        self.thLes5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.thLes5.setObjectName("thLes5")
        self.formLayout_6.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.thLes5)

        self.thEdit5 = QtWidgets.QTimeEdit(self.Thi)
        self.thEdit5.setObjectName("thEdit5")

        self.formLayout_6.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.thEdit5)

        #Урок 6 Ч
        self.thLes6 = QtWidgets.QLabel(self.Thi)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.thLes6.setFont(font)
        self.thLes6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.thLes6.setObjectName("thLes6")
        self.formLayout_6.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.thLes6)

        self.thEdit6 = QtWidgets.QTimeEdit(self.Thi)
        self.thEdit6.setObjectName("thEdit6")

        self.formLayout_6.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.thEdit6)

        #Урок 7 Ч
        self.thLes7 = QtWidgets.QLabel(self.Thi)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.thLes7.setFont(font)
        self.thLes7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.thLes7.setObjectName("thLes7")
        self.formLayout_6.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.thLes7)

        self.thEdit7 = QtWidgets.QTimeEdit(self.Thi)
        self.thEdit7.setObjectName("thEdit7")

        self.formLayout_6.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.thEdit7)
        self.verticalLayout_7.addLayout(self.formLayout_6)
        self.LessTab.addTab(self.Thi, "")

        #Вкладка Пятница
        self.Fri = QtWidgets.QWidget()
        self.Fri.setObjectName("Fri")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.Fri)
        self.verticalLayout_8.setObjectName("verticalLayout_8")

        #Надпись пятница
        self.FriLbl = QtWidgets.QLabel(self.Fri)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.FriLbl.setFont(font)
        self.FriLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.FriLbl.setObjectName("FriLbl")
        self.verticalLayout_8.addWidget(self.FriLbl)
        self.formLayout_7 = QtWidgets.QFormLayout()
        self.formLayout_7.setObjectName("formLayout_7")
        self.fLes1 = QtWidgets.QLabel(self.Fri)
        font = QtGui.QFont()
        font.setPointSize(12)

        #Урок 1 Пя
        self.fLes1.setFont(font)
        self.fLes1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.fLes1.setObjectName("fLes1")
        self.formLayout_7.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.fLes1)

        self.fEdit1 = QtWidgets.QTimeEdit(self.Fri)
        self.fEdit1.setObjectName("fEdit1")

        self.formLayout_7.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.fEdit1)

        #Урок 2 Пя
        self.fLes2 = QtWidgets.QLabel(self.Fri)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.fLes2.setFont(font)
        self.fLes2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.fLes2.setObjectName("fLes2")
        self.formLayout_7.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.fLes2)

        self.fEdit2 = QtWidgets.QTimeEdit(self.Fri)
        self.fEdit2.setObjectName("fEdit2")

        self.formLayout_7.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.fEdit2)

        #Урок 3 Пя
        self.fLes3 = QtWidgets.QLabel(self.Fri)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.fLes3.setFont(font)
        self.fLes3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.fLes3.setObjectName("fLes3")
        self.formLayout_7.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.fLes3)

        self.fEdit3 = QtWidgets.QTimeEdit(self.Fri)
        self.fEdit3.setObjectName("fEdit3")

        self.formLayout_7.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.fEdit3)

        #Урок 4 Пя
        self.fLes4 = QtWidgets.QLabel(self.Fri)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.fLes4.setFont(font)
        self.fLes4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.fLes4.setObjectName("fLes4")
        self.formLayout_7.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.fLes4)

        self.fEdit4 = QtWidgets.QTimeEdit(self.Fri)
        self.fEdit4.setObjectName("fEdit4")

        self.formLayout_7.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.fEdit4)

        #Урок 5 Пя
        self.fLes5 = QtWidgets.QLabel(self.Fri)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.fLes5.setFont(font)
        self.fLes5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.fLes5.setObjectName("fLes5")
        self.formLayout_7.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.fLes5)

        self.fEdit5 = QtWidgets.QTimeEdit(self.Fri)
        self.fEdit5.setObjectName("fEdit5")

        self.formLayout_7.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.fEdit5)

        #Урок 6 Пя
        self.fLes6 = QtWidgets.QLabel(self.Fri)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.fLes6.setFont(font)
        self.fLes6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.fLes6.setObjectName("fLes6")
        self.formLayout_7.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.fLes6)

        self.fEdit6 = QtWidgets.QTimeEdit(self.Fri)
        self.fEdit6.setObjectName("fEdit6")

        self.formLayout_7.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.fEdit6)

        #Урок 7 Пя
        self.fLes7 = QtWidgets.QLabel(self.Fri)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.fLes7.setFont(font)
        self.fLes7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.fLes7.setObjectName("fLes7")
        self.formLayout_7.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.fLes7)

        self.fEdit7 = QtWidgets.QTimeEdit(self.Fri)
        self.fEdit7.setObjectName("fEdit7")

        self.formLayout_7.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.fEdit7)
        self.verticalLayout_8.addLayout(self.formLayout_7)
        self.LessTab.addTab(self.Fri, "")

        #Вкладка Суббота
        self.Sut = QtWidgets.QWidget()
        self.Sut.setObjectName("Sut")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.Sut)
        self.verticalLayout_9.setObjectName("verticalLayout_9")

        #Надпись Суббота
        self.SutLbl = QtWidgets.QLabel(self.Sut)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.SutLbl.setFont(font)
        self.SutLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.SutLbl.setObjectName("SutLbl")
        self.verticalLayout_9.addWidget(self.SutLbl)
        self.formLayout_8 = QtWidgets.QFormLayout()
        self.formLayout_8.setObjectName("formLayout_8")

        #Урок 1 Су
        self.sLes1 = QtWidgets.QLabel(self.Sut)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sLes1.setFont(font)
        self.sLes1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sLes1.setObjectName("sLes1")
        self.formLayout_8.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.sLes1)

        self.sEdit1 = QtWidgets.QTimeEdit(self.Sut)
        self.sEdit1.setObjectName("sEdit1")

        self.formLayout_8.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.sEdit1)

        #Урок 2 Су
        self.sLes2 = QtWidgets.QLabel(self.Sut)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sLes2.setFont(font)
        self.sLes2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sLes2.setObjectName("sLes2")
        self.formLayout_8.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.sLes2)

        self.sEdit2 = QtWidgets.QTimeEdit(self.Sut)
        self.sEdit2.setObjectName("sEdit2")

        self.formLayout_8.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.sEdit2)

        #Урок 3 Су
        self.sLes3 = QtWidgets.QLabel(self.Sut)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sLes3.setFont(font)
        self.sLes3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sLes3.setObjectName("sLes3")
        self.formLayout_8.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.sLes3)

        self.sEdit3 = QtWidgets.QTimeEdit(self.Sut)
        self.sEdit3.setObjectName("sEdit3")

        self.formLayout_8.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.sEdit3)

        #Урок 4 Су
        self.sLes4 = QtWidgets.QLabel(self.Sut)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sLes4.setFont(font)
        self.sLes4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sLes4.setObjectName("sLes4")
        self.formLayout_8.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.sLes4)

        self.sEdit4 = QtWidgets.QTimeEdit(self.Sut)
        self.sEdit4.setObjectName("sEdit4")

        self.formLayout_8.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.sEdit4)

        #Урок 5 Су
        self.sLes5 = QtWidgets.QLabel(self.Sut)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sLes5.setFont(font)
        self.sLes5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sLes5.setObjectName("sLes5")
        self.formLayout_8.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.sLes5)

        self.sEdit5 = QtWidgets.QTimeEdit(self.Sut)
        self.sEdit5.setObjectName("sEdit5")

        self.formLayout_8.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.sEdit5)

        #Урок 6 Су
        self.sLes6 = QtWidgets.QLabel(self.Sut)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sLes6.setFont(font)
        self.sLes6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sLes6.setObjectName("sLes6")
        self.formLayout_8.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.sLes6)

        self.sEdit6 = QtWidgets.QTimeEdit(self.Sut)
        self.sEdit6.setObjectName("sEdit6")

        self.formLayout_8.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.sEdit6)

        #Урок 7 Су
        self.sLes7 = QtWidgets.QLabel(self.Sut)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sLes7.setFont(font)
        self.sLes7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sLes7.setObjectName("sLes7")
        self.formLayout_8.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.sLes7)

        self.sEdit7 = QtWidgets.QTimeEdit(self.Sut)
        self.sEdit7.setObjectName("sEdit7")

        self.formLayout_8.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.sEdit7)
        self.verticalLayout_9.addLayout(self.formLayout_8)
        self.LessTab.addTab(self.Sut, "")
        self.verticalLayout_10.addWidget(self.LessTab)

        #Виджжет для кнопки
        self.WidgetBtn = QtWidgets.QWidget(SettingWidget)
        self.WidgetBtn.setObjectName("WidgetBtn")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.WidgetBtn)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.WidgetBtn.setStyleSheet(lblStyle)
        self.WidgetBtn.setMouseTracking(True)

        #Спейсер
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)

        #Кнопка сохранения
        self.SaveBtn = QtWidgets.QPushButton(self.WidgetBtn)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SaveBtn.sizePolicy().hasHeightForWidth())
        self.SaveBtn.setSizePolicy(sizePolicy)
        self.SaveBtn.setMinimumSize(QtCore.QSize(800, 0))
        self.SaveBtn.setBaseSize(QtCore.QSize(800, 0))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.SaveBtn.setFont(font)
        self.SaveBtn.setObjectName("SaveBtn")
        self.horizontalLayout_3.addWidget(self.SaveBtn)

        self.SaveBtn.setStyleSheet("""
        QPushButton {
            background-color: #4CAF50;
            color: white;
            border: 2px solid #3e8e41;
            border-radius: 8px;
            padding: 12px 24px;
            font-size: 16px;
            font-weight: bold;

        }
        QPushButton:hover {
            background-color: #45a049;

        }
        QPushButton:pressed {
            background-color: #3d8b40;
            border-top: 3px solid #3e8e41;
            border-left: 3px solid #3e8e41;
            border-right: 1px solid #3e8e41;
            border-bottom: 1px solid #3e8e41;
        }
        QPushButton:disabled {
            background-color: #cccccc;
            border-color: #aaaaaa;
            color: #888888;
        }
        """)
        self.SaveBtn.clicked.connect(self.save_data)

        #Спейсер
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout_11.addLayout(self.horizontalLayout_3)
        self.verticalLayout_10.addWidget(self.WidgetBtn)

        self.retranslateUi(SettingWidget)
        self.LessTab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(SettingWidget)

    def retranslateUi(self, SettingWidget):
        _translate = QtCore.QCoreApplication.translate
        SettingWidget.setWindowTitle(_translate("SettingWidget", "Form"))
        self.SettingLabel.setText(_translate("SettingWidget", "Настройки"))
        self.label_2.setText(_translate("SettingWidget", "Web Браузер"))
        self.BrowserBool.setText(_translate("SettingWidget", "Использовать браузер?"))
        self.urlLabel.setText(_translate("SettingWidget", "URL Адресс"))
        self.CurrentURLLabel.setText(_translate("SettingWidget", "TextLabel"))
        self.AudioLabel.setText(_translate("SettingWidget", "Аудио"))
        self.PlayButton.setText(_translate("SettingWidget", "Воспроизвести"))
        self.ResolutionLabel.setText(_translate("SettingWidget", "Разрешение"))
        self.ResolutionListBox.setItemText(0, _translate("SettingWidget", "1280×720"))
        self.ResolutionListBox.setItemText(1, _translate("SettingWidget", "1920×1080"))
        self.ResolutionListBox.setItemText(2, _translate("SettingWidget", "2560×1440"))
        self.ResolutionListBox.setItemText(3, _translate("SettingWidget", "3840×2160"))
        self.MonLbl.setText(_translate("SettingWidget", "Понедельник"))
        self.mLes1.setText(_translate("SettingWidget", "Урок 1:"))
        self.mLes2.setText(_translate("SettingWidget", "Урок 2:"))
        self.mLes3.setText(_translate("SettingWidget", "Урок 3:"))
        self.mLes4.setText(_translate("SettingWidget", "Урок 4:"))
        self.mLes5.setText(_translate("SettingWidget", "Урок 5:"))
        self.mLes6.setText(_translate("SettingWidget", "Урок 6:"))
        self.mLes7.setText(_translate("SettingWidget", "Урок 7:"))
        self.LessTab.setTabText(self.LessTab.indexOf(self.Mon), _translate("SettingWidget", "Понедельник"))
        self.TyoLbl.setText(_translate("SettingWidget", "Вторник"))
        self.tLes1.setText(_translate("SettingWidget", "Урок 1:"))
        self.tLes2.setText(_translate("SettingWidget", "Урок 2:"))
        self.tLes3.setText(_translate("SettingWidget", "Урок 3:"))
        self.tLes4.setText(_translate("SettingWidget", "Урок 4:"))
        self.tLes5.setText(_translate("SettingWidget", "Урок 5:"))
        self.tLes6.setText(_translate("SettingWidget", "Урок 6:"))
        self.tLes7.setText(_translate("SettingWidget", "Урок 7:"))
        self.LessTab.setTabText(self.LessTab.indexOf(self.Tyo), _translate("SettingWidget", "Вторник"))
        self.WenLbl.setText(_translate("SettingWidget", "Среда"))
        self.wLes1.setText(_translate("SettingWidget", "Урок 1:"))
        self.wLes2.setText(_translate("SettingWidget", "Урок 2:"))
        self.wLes3.setText(_translate("SettingWidget", "Урок 3:"))
        self.wLes4.setText(_translate("SettingWidget", "Урок 4:"))
        self.wLes5.setText(_translate("SettingWidget", "Урок 5:"))
        self.wLes6.setText(_translate("SettingWidget", "Урок 6:"))
        self.wLes7.setText(_translate("SettingWidget", "Урок 7:"))
        self.LessTab.setTabText(self.LessTab.indexOf(self.Wen), _translate("SettingWidget", "Среда"))
        self.ThiLbl.setText(_translate("SettingWidget", "Четверг"))
        self.thLes1.setText(_translate("SettingWidget", "Урок 1:"))
        self.thLes2.setText(_translate("SettingWidget", "Урок 2:"))
        self.thLes3.setText(_translate("SettingWidget", "Урок 3:"))
        self.thLes4.setText(_translate("SettingWidget", "Урок 4:"))
        self.thLes5.setText(_translate("SettingWidget", "Урок 5:"))
        self.thLes6.setText(_translate("SettingWidget", "Урок 6:"))
        self.thLes7.setText(_translate("SettingWidget", "Урок 7:"))
        self.LessTab.setTabText(self.LessTab.indexOf(self.Thi), _translate("SettingWidget", "Четверг"))
        self.FriLbl.setText(_translate("SettingWidget", "Пятница"))
        self.fLes1.setText(_translate("SettingWidget", "Урок 1:"))
        self.fLes2.setText(_translate("SettingWidget", "Урок 2:"))
        self.fLes3.setText(_translate("SettingWidget", "Урок 3:"))
        self.fLes4.setText(_translate("SettingWidget", "Урок 4:"))
        self.fLes5.setText(_translate("SettingWidget", "Урок 5:"))
        self.fLes6.setText(_translate("SettingWidget", "Урок 6:"))
        self.fLes7.setText(_translate("SettingWidget", "Урок 7:"))
        self.LessTab.setTabText(self.LessTab.indexOf(self.Fri), _translate("SettingWidget", "Пятница"))
        self.SutLbl.setText(_translate("SettingWidget", "Суббота"))
        self.sLes1.setText(_translate("SettingWidget", "Урок 1:"))
        self.sLes2.setText(_translate("SettingWidget", "Урок 2:"))
        self.sLes3.setText(_translate("SettingWidget", "Урок 3:"))
        self.sLes4.setText(_translate("SettingWidget", "Урок 4:"))
        self.sLes5.setText(_translate("SettingWidget", "Урок 5:"))
        self.sLes6.setText(_translate("SettingWidget", "Урок 6:"))
        self.sLes7.setText(_translate("SettingWidget", "Урок 7:"))
        self.LessTab.setTabText(self.LessTab.indexOf(self.Sut), _translate("SettingWidget", "Суббота"))
        self.SaveBtn.setText(_translate("SettingWidget", "Сохранить"))

    def save_data(self):
        with open("monday.txt", "w", encoding="UTF-8") as file:
            mass = []
            mass.append(self.mEdit1.text())
            mass.append(self.mEdit2.text())
            mass.append(self.mEdit3.text())
            mass.append(self.mEdit4.text())
            mass.append(self.mEdit5.text())
            mass.append(self.mEdit6.text())
            mass.append(self.mEdit7.text())
            for i in mass:
                file.write(i+'|')

        with open("tuesday.txt", "w", encoding="UTF-8") as file:
            mass = []
            mass.append(self.tEdit1.text())
            mass.append(self.tEdit2.text())
            mass.append(self.tEdit3.text())
            mass.append(self.tEdit4.text())
            mass.append(self.tEdit5.text())
            mass.append(self.tEdit6.text())
            mass.append(self.tEdit7.text())
            for i in mass:
                file.write(i+'|')

        with open("wenthday.txt", "w", encoding="UTF-8") as file:
            mass = []
            mass.append(self.wEdit1.text())
            mass.append(self.wEdit2.text())
            mass.append(self.wEdit3.text())
            mass.append(self.wEdit4.text())
            mass.append(self.wEdit5.text())
            mass.append(self.wEdit6.text())
            mass.append(self.wEdit7.text())
            for i in mass:
                file.write(i+'|')

        with open("thutterday.txt", "w", encoding="UTF-8") as file:
            mass = []
            mass.append(self.thEdit1.text())
            mass.append(self.thEdit2.text())
            mass.append(self.thEdit3.text())
            mass.append(self.thEdit4.text())
            mass.append(self.thEdit5.text())
            mass.append(self.thEdit6.text())
            mass.append(self.thEdit7.text())
            for i in mass:
                file.write(i+'|')

        with open("friday.txt", "w", encoding="UTF-8") as file:
            mass = []
            mass.append(self.fEdit1.text())
            mass.append(self.fEdit2.text())
            mass.append(self.fEdit3.text())
            mass.append(self.fEdit4.text())
            mass.append(self.fEdit5.text())
            mass.append(self.fEdit6.text())
            mass.append(self.fEdit7.text())
            for i in mass:
                file.write(i+'|')

        with open("sutturday.txt", "w", encoding="UTF-8") as file:
            mass = []
            mass.append(self.sEdit1.text())
            mass.append(self.sEdit2.text())
            mass.append(self.sEdit3.text())
            mass.append(self.sEdit4.text())
            mass.append(self.sEdit5.text())
            mass.append(self.sEdit6.text())
            mass.append(self.sEdit7.text())
            for i in mass:
                file.write(i+'|')

        with open("websetting.txt", "w", encoding="UTF-8") as file:
            d = self.BrowserBool.isChecked()
            c = self.urlEdit.text()
            file.write(str(d)+'|')
            file.write(c+'|')

    def set_settings(self):
            with open("monday.txt", "r", encoding="UTF-8") as file:
                try:
                    d = file.read().split('|')
                    d = d[:-1]
                    s = []
                    for i in d:
                        if len(i) < 5:
                            s.append('0'+i)
                        else:
                            s.append(i)
                    time = QtCore.QTime.fromString(s[0])
                    self.mEdit1.setTime(time)
                    time = QtCore.QTime.fromString(s[1])
                    self.mEdit2.setTime(time)
                    time = QtCore.QTime.fromString(s[2])
                    self.mEdit3.setTime(time)
                    time = QtCore.QTime.fromString(s[3])
                    self.mEdit4.setTime(time)
                    time = QtCore.QTime.fromString(s[4])
                    self.mEdit5.setTime(time)
                    time = QtCore.QTime.fromString(s[5])
                    self.mEdit6.setTime(time)
                    time = QtCore.QTime.fromString(s[6])
                    self.mEdit7.setTime(time)
                except Exception:
                    pass

            with open("wenthday.txt", "r", encoding="UTF-8") as file:
                try:
                    d = file.read().split('|')
                    d = d[:-1]
                    s = []
                    for i in d:
                        if len(i) < 5:
                            s.append('0'+i)
                        else:
                            s.append(i)
                    time = QtCore.QTime.fromString(s[0])
                    self.wEdit1.setTime(time)
                    time = QtCore.QTime.fromString(s[1])
                    self.wEdit2.setTime(time)
                    time = QtCore.QTime.fromString(s[2])
                    self.wEdit3.setTime(time)
                    time = QtCore.QTime.fromString(s[3])
                    self.wEdit4.setTime(time)
                    time = QtCore.QTime.fromString(s[4])
                    self.wEdit5.setTime(time)
                    time = QtCore.QTime.fromString(s[5])
                    self.wEdit6.setTime(time)
                    time = QtCore.QTime.fromString(s[6])
                    self.wEdit7.setTime(time)
                except Exception:
                    pass

            with open("tuesday.txt", "r", encoding="UTF-8") as file:
                try:
                    d = file.read().split('|')
                    d = d[:-1]
                    s = []
                    for i in d:
                        if len(i) < 5:
                            s.append('0'+i)
                        else:
                            s.append(i)
                    time = QtCore.QTime.fromString(s[0])
                    self.thEdit1.setTime(time)
                    time = QtCore.QTime.fromString(s[1])
                    self.tEdit2.setTime(time)
                    time = QtCore.QTime.fromString(s[2])
                    self.tEdit3.setTime(time)
                    time = QtCore.QTime.fromString(s[3])
                    self.tEdit4.setTime(time)
                    time = QtCore.QTime.fromString(s[4])
                    self.tEdit5.setTime(time)
                    time = QtCore.QTime.fromString(s[5])
                    self.tEdit6.setTime(time)
                    time = QtCore.QTime.fromString(s[6])
                    self.tEdit7.setTime(time)
                except Exception:
                    pass

            with open("thutterday.txt", "r", encoding="UTF-8") as file:
                try:
                    d = file.read().split('|')
                    d = d[:-1]
                    s = []
                    for i in d:
                        if len(i) < 5:
                            s.append('0'+i)
                        else:
                            s.append(i)
                    time = QtCore.QTime.fromString(s[0])
                    self.thEdit1.setTime(time)
                    time = QtCore.QTime.fromString(s[1])
                    self.thEdit2.setTime(time)
                    time = QtCore.QTime.fromString(s[2])
                    self.thEdit3.setTime(time)
                    time = QtCore.QTime.fromString(s[3])
                    self.thEdit4.setTime(time)
                    time = QtCore.QTime.fromString(s[4])
                    self.thEdit5.setTime(time)
                    time = QtCore.QTime.fromString(s[5])
                    self.thEdit6.setTime(time)
                    time = QtCore.QTime.fromString(s[6])
                    self.thEdit7.setTime(time)
                except Exception:
                    pass

            with open("friday.txt", "r", encoding="UTF-8") as file:
                try:
                    d = file.read().split('|')
                    d = d[:-1]
                    s = []
                    for i in d:
                        if len(i) < 5:
                            s.append('0'+i)
                        else:
                            s.append(i)
                    time = QtCore.QTime.fromString(s[0])
                    self.fEdit1.setTime(time)
                    time = QtCore.QTime.fromString(s[1])
                    self.fEdit2.setTime(time)
                    time = QtCore.QTime.fromString(s[2])
                    self.fEdit3.setTime(time)
                    time = QtCore.QTime.fromString(s[3])
                    self.fEdit4.setTime(time)
                    time = QtCore.QTime.fromString(s[4])
                    self.fEdit5.setTime(time)
                    time = QtCore.QTime.fromString(s[5])
                    self.fEdit6.setTime(time)
                    time = QtCore.QTime.fromString(s[6])
                    self.fEdit7.setTime(time)
                except Exception:
                    pass

            with open("sutturday.txt", "r", encoding="UTF-8") as file:
                try:
                    d = file.read().split('|')
                    d = d[:-1]
                    s = []
                    for i in d:
                        if len(i) < 5:
                            s.append('0'+i)
                        else:
                            s.append(i)
                    time = QtCore.QTime.fromString(s[0])
                    self.sEdit1.setTime(time)
                    time = QtCore.QTime.fromString(s[1])
                    self.sEdit2.setTime(time)
                    time = QtCore.QTime.fromString(s[2])
                    self.sEdit3.setTime(time)
                    time = QtCore.QTime.fromString(s[3])
                    self.sEdit4.setTime(time)
                    time = QtCore.QTime.fromString(s[4])
                    self.sEdit5.setTime(time)
                    time = QtCore.QTime.fromString(s[5])
                    self.sEdit6.setTime(time)
                    time = QtCore.QTime.fromString(s[6])
                    self.sEdit7.setTime(time)
                except Exception:
                    pass    

            with open("websetting.txt", "r", encoding="UTF-8") as file:
                try:
                    data = file.read().split('|')
                    data = data[:-1]
                    if data[0] == 'True':
                        self.BrowserBool.setChecked(True)
                    self.CurrentURLLabel.setText(data[1])
                    self.urlEdit.setText(data[1])
                except Exception:
                    pass

    def play_audio(self):
        mixer.init()
        mixer.music.load("ring.mp3")
        mixer.music.play()

