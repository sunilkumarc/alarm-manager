# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'alarmgui.ui'
#
# Created: Fri Aug 30 18:58:16 2013
#      by: PyQt4 UI code generator 4.10
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
        MainWindow.resize(480, 319)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.setAlarms = QtGui.QPushButton(self.centralwidget)
        self.setAlarms.setGeometry(QtCore.QRect(310, 270, 151, 41))
        self.setAlarms.setObjectName(_fromUtf8("setAlarms"))
        self.message4 = QtGui.QTextEdit(self.centralwidget)
        self.message4.setGeometry(QtCore.QRect(160, 220, 301, 41))
        self.message4.setObjectName(_fromUtf8("message4"))
        self.message3 = QtGui.QTextEdit(self.centralwidget)
        self.message3.setGeometry(QtCore.QRect(160, 170, 301, 41))
        self.message3.setObjectName(_fromUtf8("message3"))
        self.message2 = QtGui.QTextEdit(self.centralwidget)
        self.message2.setGeometry(QtCore.QRect(160, 120, 301, 41))
        self.message2.setObjectName(_fromUtf8("message2"))
        self.message1 = QtGui.QTextEdit(self.centralwidget)
        self.message1.setGeometry(QtCore.QRect(160, 70, 301, 41))
        self.message1.setObjectName(_fromUtf8("message1"))
        self.Hint = QtGui.QLabel(self.centralwidget)
        self.Hint.setGeometry(QtCore.QRect(60, 10, 51, 21))
        self.Hint.setObjectName(_fromUtf8("Hint"))
        self.Hint_2 = QtGui.QLabel(self.centralwidget)
        self.Hint_2.setGeometry(QtCore.QRect(200, 10, 221, 16))
        self.Hint_2.setObjectName(_fromUtf8("Hint_2"))
        self.hr1 = QtGui.QTextEdit(self.centralwidget)
        self.hr1.setGeometry(QtCore.QRect(10, 70, 51, 41))
        self.hr1.setObjectName(_fromUtf8("hr1"))
        self.min1 = QtGui.QTextEdit(self.centralwidget)
        self.min1.setGeometry(QtCore.QRect(80, 70, 51, 41))
        self.min1.setObjectName(_fromUtf8("min1"))
        self.hr2 = QtGui.QTextEdit(self.centralwidget)
        self.hr2.setGeometry(QtCore.QRect(10, 120, 51, 41))
        self.hr2.setObjectName(_fromUtf8("hr2"))
        self.min2 = QtGui.QTextEdit(self.centralwidget)
        self.min2.setGeometry(QtCore.QRect(80, 120, 51, 41))
        self.min2.setObjectName(_fromUtf8("min2"))
        self.hr3 = QtGui.QTextEdit(self.centralwidget)
        self.hr3.setGeometry(QtCore.QRect(10, 170, 51, 41))
        self.hr3.setObjectName(_fromUtf8("hr3"))
        self.min3 = QtGui.QTextEdit(self.centralwidget)
        self.min3.setGeometry(QtCore.QRect(80, 170, 51, 41))
        self.min3.setObjectName(_fromUtf8("min3"))
        self.hr4 = QtGui.QTextEdit(self.centralwidget)
        self.hr4.setGeometry(QtCore.QRect(10, 220, 51, 41))
        self.hr4.setObjectName(_fromUtf8("hr4"))
        self.min4 = QtGui.QTextEdit(self.centralwidget)
        self.min4.setGeometry(QtCore.QRect(80, 220, 51, 41))
        self.min4.setObjectName(_fromUtf8("min4"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 40, 51, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 40, 61, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.Hint_3 = QtGui.QLabel(self.centralwidget)
        self.Hint_3.setGeometry(QtCore.QRect(10, 280, 231, 21))
        self.Hint_3.setObjectName(_fromUtf8("Hint_3"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionSdsd = QtGui.QAction(MainWindow)
        self.actionSdsd.setObjectName(_fromUtf8("actionSdsd"))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.setAlarms.setText(_translate("MainWindow", "Set Alarms", None))
        self.Hint.setText(_translate("MainWindow", "Time", None))
        self.Hint_2.setText(_translate("MainWindow", "Enter the message to display", None))
        self.label.setText(_translate("MainWindow", "Hour", None))
        self.label_2.setText(_translate("MainWindow", "Minutes", None))
        self.Hint_3.setText(_translate("MainWindow", "Enter Hour value in 24 hr format", None))
        self.actionSdsd.setText(_translate("MainWindow", "sdsd\'", None))

