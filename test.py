# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!
import sys
import pyodbc
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(1031, 687)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
		self.gridLayout.setObjectName("gridLayout")
		self.frame = QtWidgets.QFrame(self.centralwidget)
		self.frame.setMinimumSize(QtCore.QSize(0, 80))
		self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame.setObjectName("frame")
		self.label = QtWidgets.QLabel(self.frame)
		self.label.setGeometry(QtCore.QRect(40, 10, 54, 12))
		self.label.setObjectName("label")
		self.label_2 = QtWidgets.QLabel(self.frame)
		self.label_2.setGeometry(QtCore.QRect(150, 10, 54, 12))
		self.label_2.setObjectName("label_2")
		self.label_3 = QtWidgets.QLabel(self.frame)
		self.label_3.setGeometry(QtCore.QRect(270, 10, 54, 12))
		self.label_3.setObjectName("label_3")
		self.label_4 = QtWidgets.QLabel(self.frame)
		self.label_4.setGeometry(QtCore.QRect(390, 10, 54, 12))
		self.label_4.setObjectName("label_4")
		self.label_5 = QtWidgets.QLabel(self.frame)
		self.label_5.setGeometry(QtCore.QRect(510, 10, 200, 12))
		self.label_5.setObjectName("label_5")
		self.lineEdit = QtWidgets.QLineEdit(self.frame)
		self.lineEdit.setGeometry(QtCore.QRect(10, 40, 113, 20))
		self.lineEdit.setObjectName("lineEdit")
		self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
		self.lineEdit_2.setGeometry(QtCore.QRect(130, 40, 113, 20))
		self.lineEdit_2.setObjectName("lineEdit_2")
		self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
		self.lineEdit_3.setGeometry(QtCore.QRect(250, 40, 113, 20))
		self.lineEdit_3.setObjectName("lineEdit_3")
		self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
		self.lineEdit_4.setGeometry(QtCore.QRect(370, 40, 113, 20))
		self.lineEdit_4.setObjectName("lineEdit_4")
		self.pushButton = QtWidgets.QPushButton(self.frame)
		self.pushButton.setGeometry(QtCore.QRect(500, 40, 75, 23))
		self.pushButton.setObjectName("pushButton")
		self.comboBox = QtWidgets.QComboBox(self.frame)
		self.comboBox.setGeometry(QtCore.QRect(590, 40, 91, 22))
		self.comboBox.setObjectName("comboBox")
		self.pushButton_2 = QtWidgets.QPushButton(self.frame)
		self.pushButton_2.setGeometry(QtCore.QRect(700, 40, 75, 23))
		self.pushButton_2.setObjectName("pushButton_2")
		self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
		self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
		self.tableWidget.setObjectName("tableWidget")
		self.tableWidget.setColumnCount(0)
		self.tableWidget.setRowCount(0)
		self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 1)
		self.frame_2 = QtWidgets.QFrame(self.centralwidget)
		self.frame_2.setMinimumSize(QtCore.QSize(80, 0))
		self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame_2.setObjectName("frame_2")
		self.pushButton_3 = QtWidgets.QPushButton(self.frame_2)
		self.pushButton_3.setGeometry(QtCore.QRect(0, 90, 75, 23))
		self.pushButton_3.setObjectName("pushButton_3")
		self.gridLayout.addWidget(self.frame_2, 0, 1, 2, 1)
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 1031, 23))
		self.menubar.setObjectName("menubar")
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)

		self.retranslateUi(MainWindow)
		self.pushButton.clicked.connect(self.nnn)
		self.pushButton_2.clicked.connect(self.nni)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.label.setText(_translate("MainWindow", "SERVER"))
		self.label_2.setText(_translate("MainWindow", "DATABASE"))
		self.label_3.setText(_translate("MainWindow", "UID"))
		self.label_4.setText(_translate("MainWindow", "PWD"))
		self.label_5.setText(_translate("MainWindow", ""))
		self.lineEdit.setText(_translate("MainWindow", "192.168.1.210,1433"))
		self.lineEdit_2.setText(_translate("MainWindow", ""))
		self.lineEdit_3.setText(_translate("MainWindow", "sa"))
		self.lineEdit_4.setText(_translate("MainWindow", ""))
		self.pushButton.setText(_translate("MainWindow", "连接"))
		self.pushButton_2.setText(_translate("MainWindow", "表字段"))
		self.pushButton_3.setText(_translate("MainWindow", "PushButton"))

	def nnn(self):
		le = self.lineEdit.text()
		le2 = self.lineEdit_2.text()
		le3 = self.lineEdit_3.text()
		le4 = self.lineEdit_4.text()

		sql = "SELECT * FROM SysObjects Where XType='U'"  # 查询表名
		try:
			conn = pyodbc.connect(
				r"DRIVER={SQL Server};SERVER=" + le + ";DATABASE=" + le2 + ";UID=" + le3 + ";PWD=" + le4)
		except:
			_translate = QtCore.QCoreApplication.translate
			self.label_5.setText(_translate("MainWindow", "连接出错"))
		else:
			print(conn)
			cursor = conn.cursor()
			data = cursor.execute(sql)
			i = 0
			for row in data:
				print(row[0])
				self.comboBox.addItem(row[0])
			conn.close()
			_translate = QtCore.QCoreApplication.translate
			self.label_5.setText(_translate("MainWindow", "连接成功      选择数据表"))

	def nn(self):
		le = self.comboBox.currentText()
		print(le)

	def nni(self):
		le = self.lineEdit.text()
		le2 = self.lineEdit_2.text()
		le3 = self.lineEdit_3.text()
		le4 = self.lineEdit_4.text()
		cb = self.comboBox.currentText()
		sql = "SELECT name FROM syscolumns Where id=(select max(id) from sysobjects where xtype='u' and name='" + cb + "')"  # 查询指定表列名
		conn = pyodbc.connect(r"DRIVER={SQL Server};SERVER=" + le + ";DATABASE=" + le2 + ";UID=" + le3 + ";PWD=" + le4)
		cursor = conn.cursor()
		data = cursor.execute(sql)
		i = 0
		for row in data:
			print(row[0])

			self.tableWidget.setColumnCount(i + 1)

			item = QtWidgets.QTableWidgetItem()
			self.tableWidget.setHorizontalHeaderItem(i, item)
			_translate = QtCore.QCoreApplication.translate
			item.setText(_translate("MainWindow", row[0]))
			i = i + 1
		conn.close()


if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)

	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()

	sys.exit(app.exec_())
