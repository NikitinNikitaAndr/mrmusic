# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created: Mon May 23 17:59:20 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(758, 436)
        MainWindow.setStyleSheet(_fromUtf8("QPushButton\n"
"{\n"
"background-color:#4b4b4b;\n"
"border:1px solid white;\n"
"border-radius:10px;\n"
"color:#ffffff;\n"
"font-family:arial;\n"
"font-size:15px;\n"
"font-weight:bold;\n"
"text-decoration:none;\n"
"padding-right:10px;\n"
"outline: 0;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color: #00c6d7;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color: #095c63;\n"
"}\n"
"QMainWindow\n"
"{\n"
"background-color: #4b4b4b;\n"
"}\n"
"QLabel\n"
"{\n"
"color: white\n"
"}\n"
"QLabel#label_RInstrument\n"
"{\n"
"color: #00c6d7\n"
"}\n"
"QLabel#label_RColor\n"
"{\n"
"color: #00c6d7\n"
"}\n"
"QLabel#label_RTonality\n"
"{\n"
"color: #00c6d7\n"
"}\n"
"QLabel#label_RTempo\n"
"{\n"
"color: #00c6d7\n"
"}\n"
"QLabel#label_RDuration\n"
"{\n"
"color: #00c6d7\n"
"}\n"
"QLabel#label_RScheme\n"
"{\n"
"color: #00c6d7\n"
"}\n"
"QMenu {\n"
"    background-color: lightgray; /* sets background of the menu */\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QMenu::item {\n"
"    /* sets background of menu item. set this to something non-transparent\n"
"        if you want menu color and menu item color to be different */\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QMenu::item:selected { /* when user selects item using mouse or keyboard */\n"
"    background-color: #00c6d7;\n"
"}\n"
"QMenuBar {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                      stop:0 lightgray, stop:1 darkgray);\n"
"}\n"
"\n"
"QMenuBar::item {\n"
"    spacing: 3px; /* spacing between menu bar items */\n"
"    padding: 1px 4px;\n"
"    background: transparent;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QMenuBar::item:selected { /* when selected using mouse or keyboard */\n"
"    background: #a8a8a8;\n"
"}\n"
"\n"
"QMenuBar::item:pressed {\n"
"    background: #888888;\n"
"}\n"
"\n"
"QGraphicsView\n"
"{\n"
"background-color: lightgray; \n"
"border:3px solid white;\n"
"border-radius:10px;\n"
"}"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pushButton_Generate = QtGui.QPushButton(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(75, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(75, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(75, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(75, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(75, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(75, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(75, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(75, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(75, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.pushButton_Generate.setPalette(palette)
        self.pushButton_Generate.setStyleSheet(_fromUtf8(""))
        self.pushButton_Generate.setFlat(False)
        self.pushButton_Generate.setObjectName(_fromUtf8("pushButton_Generate"))
        self.verticalLayout.addWidget(self.pushButton_Generate)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_Play = QtGui.QPushButton(self.centralwidget)
        self.pushButton_Play.setObjectName(_fromUtf8("pushButton_Play"))
        self.horizontalLayout.addWidget(self.pushButton_Play)
        self.pushButton_Pause = QtGui.QPushButton(self.centralwidget)
        self.pushButton_Pause.setObjectName(_fromUtf8("pushButton_Pause"))
        self.horizontalLayout.addWidget(self.pushButton_Pause)
        self.pushButton_Stop = QtGui.QPushButton(self.centralwidget)
        self.pushButton_Stop.setObjectName(_fromUtf8("pushButton_Stop"))
        self.horizontalLayout.addWidget(self.pushButton_Stop)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        self.verticalLayout_Information = QtGui.QVBoxLayout()
        self.verticalLayout_Information.setObjectName(_fromUtf8("verticalLayout_Information"))
        self.label_LInstrument = QtGui.QLabel(self.centralwidget)
        self.label_LInstrument.setObjectName(_fromUtf8("label_LInstrument"))
        self.verticalLayout_Information.addWidget(self.label_LInstrument)
        self.label_RInstrument = QtGui.QLabel(self.centralwidget)
        self.label_RInstrument.setObjectName(_fromUtf8("label_RInstrument"))
        self.verticalLayout_Information.addWidget(self.label_RInstrument)
        self.line_Instrument = QtGui.QFrame(self.centralwidget)
        self.line_Instrument.setFrameShape(QtGui.QFrame.HLine)
        self.line_Instrument.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_Instrument.setObjectName(_fromUtf8("line_Instrument"))
        self.verticalLayout_Information.addWidget(self.line_Instrument)
        self.label_LScheme = QtGui.QLabel(self.centralwidget)
        self.label_LScheme.setObjectName(_fromUtf8("label_LScheme"))
        self.verticalLayout_Information.addWidget(self.label_LScheme)
        self.label_RScheme = QtGui.QLabel(self.centralwidget)
        self.label_RScheme.setText(_fromUtf8(""))
        self.label_RScheme.setObjectName(_fromUtf8("label_RScheme"))
        self.verticalLayout_Information.addWidget(self.label_RScheme)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_Information.addWidget(self.line)
        self.label_LColor = QtGui.QLabel(self.centralwidget)
        self.label_LColor.setObjectName(_fromUtf8("label_LColor"))
        self.verticalLayout_Information.addWidget(self.label_LColor)
        self.label_RColor = QtGui.QLabel(self.centralwidget)
        self.label_RColor.setText(_fromUtf8(""))
        self.label_RColor.setObjectName(_fromUtf8("label_RColor"))
        self.verticalLayout_Information.addWidget(self.label_RColor)
        self.line_Color = QtGui.QFrame(self.centralwidget)
        self.line_Color.setFrameShape(QtGui.QFrame.HLine)
        self.line_Color.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_Color.setObjectName(_fromUtf8("line_Color"))
        self.verticalLayout_Information.addWidget(self.line_Color)
        self.label_LTonality = QtGui.QLabel(self.centralwidget)
        self.label_LTonality.setObjectName(_fromUtf8("label_LTonality"))
        self.verticalLayout_Information.addWidget(self.label_LTonality)
        self.label_RTonality = QtGui.QLabel(self.centralwidget)
        self.label_RTonality.setText(_fromUtf8(""))
        self.label_RTonality.setObjectName(_fromUtf8("label_RTonality"))
        self.verticalLayout_Information.addWidget(self.label_RTonality)
        self.line_Tonality = QtGui.QFrame(self.centralwidget)
        self.line_Tonality.setFrameShape(QtGui.QFrame.HLine)
        self.line_Tonality.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_Tonality.setObjectName(_fromUtf8("line_Tonality"))
        self.verticalLayout_Information.addWidget(self.line_Tonality)
        self.label_LTempo = QtGui.QLabel(self.centralwidget)
        self.label_LTempo.setObjectName(_fromUtf8("label_LTempo"))
        self.verticalLayout_Information.addWidget(self.label_LTempo)
        self.label_RTempo = QtGui.QLabel(self.centralwidget)
        self.label_RTempo.setText(_fromUtf8(""))
        self.label_RTempo.setObjectName(_fromUtf8("label_RTempo"))
        self.verticalLayout_Information.addWidget(self.label_RTempo)
        self.line_Tempo = QtGui.QFrame(self.centralwidget)
        self.line_Tempo.setFrameShape(QtGui.QFrame.HLine)
        self.line_Tempo.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_Tempo.setObjectName(_fromUtf8("line_Tempo"))
        self.verticalLayout_Information.addWidget(self.line_Tempo)
        self.label_LDuration = QtGui.QLabel(self.centralwidget)
        self.label_LDuration.setObjectName(_fromUtf8("label_LDuration"))
        self.verticalLayout_Information.addWidget(self.label_LDuration)
        self.label_RDuration = QtGui.QLabel(self.centralwidget)
        self.label_RDuration.setText(_fromUtf8(""))
        self.label_RDuration.setObjectName(_fromUtf8("label_RDuration"))
        self.verticalLayout_Information.addWidget(self.label_RDuration)
        self.line_Duration = QtGui.QFrame(self.centralwidget)
        self.line_Duration.setFrameShape(QtGui.QFrame.HLine)
        self.line_Duration.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_Duration.setObjectName(_fromUtf8("line_Duration"))
        self.verticalLayout_Information.addWidget(self.line_Duration)
        self.gridLayout.addLayout(self.verticalLayout_Information, 0, 1, 1, 1)
        self.graphicsView_LoadedImage = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView_LoadedImage.setObjectName(_fromUtf8("graphicsView_LoadedImage"))
        self.gridLayout.addWidget(self.graphicsView_LoadedImage, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 758, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName(_fromUtf8("menu_File"))
        self.menu_Scheme = QtGui.QMenu(self.menubar)
        self.menu_Scheme.setObjectName(_fromUtf8("menu_Scheme"))
        self.menu_Instruments = QtGui.QMenu(self.menubar)
        self.menu_Instruments.setObjectName(_fromUtf8("menu_Instruments"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.action_loadImage = QtGui.QAction(MainWindow)
        self.action_loadImage.setObjectName(_fromUtf8("action_loadImage"))
        self.action_SaveSong = QtGui.QAction(MainWindow)
        self.action_SaveSong.setObjectName(_fromUtf8("action_SaveSong"))
        self.action_SelectScheme = QtGui.QAction(MainWindow)
        self.action_SelectScheme.setObjectName(_fromUtf8("action_SelectScheme"))
        self.action_Piano = QtGui.QAction(MainWindow)
        self.action_Piano.setObjectName(_fromUtf8("action_Piano"))
        self.action_Guitar = QtGui.QAction(MainWindow)
        self.action_Guitar.setObjectName(_fromUtf8("action_Guitar"))
        self.menu_File.addAction(self.action_loadImage)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_SaveSong)
        self.menu_Scheme.addAction(self.action_SelectScheme)
        self.menu_Instruments.addAction(self.action_Piano)
        self.menu_Instruments.addAction(self.action_Guitar)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Scheme.menuAction())
        self.menubar.addAction(self.menu_Instruments.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Mr. Music", None))
        self.pushButton_Generate.setText(_translate("MainWindow", "Сгенерировать", None))
        self.pushButton_Play.setText(_translate("MainWindow", "Воспроизвести", None))
        self.pushButton_Pause.setText(_translate("MainWindow", "Приостановить", None))
        self.pushButton_Stop.setText(_translate("MainWindow", "Остановить", None))
        self.label_LInstrument.setText(_translate("MainWindow", "Текущий инструмент:", None))
        self.label_RInstrument.setText(_translate("MainWindow", "Фортепьяно", None))
        self.label_LScheme.setText(_translate("MainWindow", "Текущая схема:", None))
        self.label_LColor.setText(_translate("MainWindow", "Преимущественный цвет: ", None))
        self.label_LTonality.setText(_translate("MainWindow", "Тональность:", None))
        self.label_LTempo.setText(_translate("MainWindow", "Темп:", None))
        self.label_LDuration.setText(_translate("MainWindow", "Длительность:", None))
        self.menu_File.setTitle(_translate("MainWindow", "Файл", None))
        self.menu_Scheme.setTitle(_translate("MainWindow", "Схема", None))
        self.menu_Instruments.setTitle(_translate("MainWindow", "Инструменты", None))
        self.action_loadImage.setText(_translate("MainWindow", "Загрузить изображение", None))
        self.action_SaveSong.setText(_translate("MainWindow", "Сохранить композицию", None))
        self.action_SelectScheme.setText(_translate("MainWindow", "Выбрать схему соотнесения цветов и нот", None))
        self.action_Piano.setText(_translate("MainWindow", "Фортепьяно", None))
        self.action_Guitar.setText(_translate("MainWindow", "Гитара", None))

