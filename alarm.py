#!/usr/bin/python

from PyQt4 import QtGui, QtCore
import gui
import sys
import os
import subprocess

class Score(QtGui.QMainWindow):
	def __init__(self):
		super(Score, self).__init__()
		self.ui = gui.Ui_MainWindow()
		self.ui.setupUi(self)
		self.setWindowTitle('Alarm Manager')
		self.ui.setAlarms.clicked.connect(self.set)
		self.centerOnScreen()
		self.show()

	def centerOnScreen (self):
		resolution = QtGui.QDesktopWidget().screenGeometry()
		self.move((resolution.width() / 2) - (self.frameSize().width() / 2), (resolution.height() / 2) - (self.frameSize().height() / 2))

	def set(self):
		self.hr1 = str(self.ui.hr1.toPlainText())
		self.hr2 = str(self.ui.hr2.toPlainText())
		self.hr3 = str(self.ui.hr3.toPlainText())
		self.hr4 = str(self.ui.hr4.toPlainText())
		self.min1 = str(self.ui.min1.toPlainText())
		self.min2 = str(self.ui.min2.toPlainText())
		self.min3 = str(self.ui.min3.toPlainText())
		self.min4 = str(self.ui.min4.toPlainText())
		self.message1 = str(self.ui.message1.toPlainText())
		self.message2 = str(self.ui.message2.toPlainText())
		self.message3 = str(self.ui.message3.toPlainText())
		self.message4 = str(self.ui.message4.toPlainText())


		if(self.hr1 != "" and self.min1 != ""):
			if len(self.hr1) == 1:
				self.hr1 = "0"+self.hr1

			if len(self.min1) == 1:
				self.min1 = "0"+self.min1
			os.system("/opt/alarm-manager/./script.sh" + " " + self.hr1 + " " + self.min1 + " " + self.message1.rstrip() + "&")

		if(self.hr2 != "" and self.min2 != ""):
			if len(self.hr2) == 1:
				self.hr2 = "0"+self.hr2

			if len(self.min2) == 1:
				self.min2 = "0"+self.min2
			os.system("/opt/alarm-manager/./script.sh" + " " + self.hr2 + " " + self.min2 + " " + self.message2.rstrip() + "&")

		if(self.hr3 != "" and self.min3 != ""):
			if len(self.hr3) == 1:
				self.hr3 = "0"+self.hr3

			if len(self.min3) == 1:
				self.min3 = "0"+self.min3
			os.system("/opt/alarm-manager/./script.sh" + " " + self.hr3 + " " + self.min3 + " " + self.message3.rstrip() + "&")

		if(self.hr4 != "" and self.min4 != ""):
			if len(self.hr4) == 1:
				self.hr4 = "0"+self.hr4

			if len(self.min4) == 1:
				self.min4 = "0"+self.min4
			os.system("/opt/alarm-manager/./script.sh" + " " + self.hr4 + " " + self.min4 + " " + self.message4.rstrip() + "&")

		self.close()


if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	o = Score()
	sys.exit(app.exec_())
