# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpinBox, QStatusBar, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(582, 559)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(20, 10, 551, 501))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayoutWidget_3 = QWidget(self.tab)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(20, 20, 511, 331))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_5 = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_5.setObjectName(u"pushButton_5")
        font = QFont()
        font.setPointSize(14)
        self.pushButton_5.setFont(font)

        self.gridLayout_2.addWidget(self.pushButton_5, 5, 0, 1, 1)

        self.pushButton_6 = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setFont(font)

        self.gridLayout_2.addWidget(self.pushButton_6, 1, 0, 1, 1)

        self.usa_time = QLineEdit(self.gridLayoutWidget_3)
        self.usa_time.setObjectName(u"usa_time")
        self.usa_time.setFont(font)

        self.gridLayout_2.addWidget(self.usa_time, 1, 1, 1, 1)

        self.germany_time = QLineEdit(self.gridLayoutWidget_3)
        self.germany_time.setObjectName(u"germany_time")
        self.germany_time.setFont(font)

        self.gridLayout_2.addWidget(self.germany_time, 5, 1, 1, 1)

        self.pushButton_4 = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setFont(font)

        self.gridLayout_2.addWidget(self.pushButton_4, 0, 0, 1, 1)

        self.iran_time = QLineEdit(self.gridLayoutWidget_3)
        self.iran_time.setObjectName(u"iran_time")
        self.iran_time.setFont(font)

        self.gridLayout_2.addWidget(self.iran_time, 0, 1, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout = QVBoxLayout(self.tab_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gl_alarms = QGridLayout()
        self.gl_alarms.setObjectName(u"gl_alarms")

        self.verticalLayout.addLayout(self.gl_alarms)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_2 = QPushButton(self.tab_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font)

        self.gridLayout.addWidget(self.pushButton_2, 1, 0, 1, 1)

        self.hour_box = QSpinBox(self.tab_2)
        self.hour_box.setObjectName(u"hour_box")
        self.hour_box.setFont(font)

        self.gridLayout.addWidget(self.hour_box, 1, 1, 1, 1)

        self.tb_alarm_title = QLineEdit(self.tab_2)
        self.tb_alarm_title.setObjectName(u"tb_alarm_title")
        self.tb_alarm_title.setFont(font)

        self.gridLayout.addWidget(self.tb_alarm_title, 0, 1, 1, 3)

        self.pushButton = QPushButton(self.tab_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font)

        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)

        self.min_box = QSpinBox(self.tab_2)
        self.min_box.setObjectName(u"min_box")
        self.min_box.setFont(font)

        self.gridLayout.addWidget(self.min_box, 2, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.tab_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font)

        self.gridLayout.addWidget(self.pushButton_3, 2, 0, 1, 1)

        self.btn_add_alarm = QPushButton(self.tab_2)
        self.btn_add_alarm.setObjectName(u"btn_add_alarm")
        self.btn_add_alarm.setFont(font)

        self.gridLayout.addWidget(self.btn_add_alarm, 3, 0, 1, 4)


        self.verticalLayout.addLayout(self.gridLayout)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.lbl_stopwatch = QLabel(self.tab_3)
        self.lbl_stopwatch.setObjectName(u"lbl_stopwatch")
        self.lbl_stopwatch.setGeometry(QRect(108, 40, 221, 71))
        font1 = QFont()
        font1.setFamilies([u"Rockwell"])
        font1.setPointSize(18)
        self.lbl_stopwatch.setFont(font1)
        self.lbl_stopwatch.setAlignment(Qt.AlignCenter)
        self.btn_start_stopwatch = QPushButton(self.tab_3)
        self.btn_start_stopwatch.setObjectName(u"btn_start_stopwatch")
        self.btn_start_stopwatch.setGeometry(QRect(30, 200, 101, 41))
        self.btn_stop_stopwatch = QPushButton(self.tab_3)
        self.btn_stop_stopwatch.setObjectName(u"btn_stop_stopwatch")
        self.btn_stop_stopwatch.setGeometry(QRect(150, 200, 101, 41))
        self.btn_rst_stopwatch = QPushButton(self.tab_3)
        self.btn_rst_stopwatch.setObjectName(u"btn_rst_stopwatch")
        self.btn_rst_stopwatch.setGeometry(QRect(270, 200, 101, 41))
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.btn_rst_timer = QPushButton(self.tab_4)
        self.btn_rst_timer.setObjectName(u"btn_rst_timer")
        self.btn_rst_timer.setGeometry(QRect(270, 210, 101, 41))
        self.btn_start_timer = QPushButton(self.tab_4)
        self.btn_start_timer.setObjectName(u"btn_start_timer")
        self.btn_start_timer.setGeometry(QRect(30, 210, 101, 41))
        self.btn_stop_timer = QPushButton(self.tab_4)
        self.btn_stop_timer.setObjectName(u"btn_stop_timer")
        self.btn_stop_timer.setGeometry(QRect(150, 210, 101, 41))
        self.lbl_timer = QLabel(self.tab_4)
        self.lbl_timer.setObjectName(u"lbl_timer")
        self.lbl_timer.setGeometry(QRect(90, 40, 221, 71))
        self.lbl_timer.setFont(font1)
        self.lbl_timer.setAlignment(Qt.AlignCenter)
        self.tabWidget.addTab(self.tab_4, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 582, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"GERMANY:", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"USA:", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"IRAN:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"World Clock", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Hour:", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Title:", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Minute:", None))
        self.btn_add_alarm.setText(QCoreApplication.translate("MainWindow", u"Add Alarm", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Alarm", None))
        self.lbl_stopwatch.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_start_stopwatch.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.btn_stop_stopwatch.setText(QCoreApplication.translate("MainWindow", u"STOP", None))
        self.btn_rst_stopwatch.setText(QCoreApplication.translate("MainWindow", u"RESET", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Stop Watch", None))
        self.btn_rst_timer.setText(QCoreApplication.translate("MainWindow", u"RESET", None))
        self.btn_start_timer.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.btn_stop_timer.setText(QCoreApplication.translate("MainWindow", u"STOP", None))
        self.lbl_timer.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Timer", None))
    # retranslateUi

