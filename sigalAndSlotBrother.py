import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from sigalAndSlot import Ui_Form
from PyQt5.QtCore import pyqtSignal,Qt

class mainWindow(QMainWindow, Ui_Form):
	helpSignal = pyqtSignal(str)
	printSignal = pyqtSignal(list)

	previewSignal = pyqtSignal([int,str],[str])

	def __init__(self, parent=None):
		super(mainWindow, self).__init__(parent)
		self.setupUi(self)
		self.initUi()

	def initUi(self):
		self.helpSignal.connect(self.showHelpMessage)
		self.printSignal.connect(self.printPaper)
		self.previewSignal[str].connect(self.previewPaper)
		self.previewSignal[int,str].connect(self.previewPaperWithArgs)
		self.printButton.clicked.connect(self.emitPrintSignal)
		self.previewButton.clicked.connect(self.emitPreviewSignal)


	def emitPreviewSignal(self):
		if self.previewStatus.isChecked() == True:
			self.previewSignal[int,str].emit(1080, "Full Screen")
		elif self.previewSignal.isChecked() == False:
			self.previewSignal[str].emit("Preview")

	def emitPritSinal(self):
		pList = []
		pList.append(self.numberSpinBox.value())
		pList.append(self.styleCombo.currentText())
		self.previewSignal.emit(pList)

	def printPaper(self):
		self.resultLabel.setText("打印："+"份数："+str(list[0]) + "纸张："+str(list[1]))

	def previewPaperWithArgs(self):
		self.resultLabel.setText(str(style)+text)
