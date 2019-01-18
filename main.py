# -*- coding:utf-8 -*-
import datetime
import sys
from PyQt5 import QtSql
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip
from PyQt5.uic.properties import QtCore
from window import Ui_STATE
from PyQt5.QtSql import QSqlDatabase
from PyQt5.QtCore import pyqtSignal, Qt, QDateTime


class window(QWidget, Ui_STATE):
	'''集成页面布局'''
	# JwsubSignal = pyqtSignal()
	def __init__(self, parent=None):
		super(QWidget,self).__init__(parent)
		
		self.setupUi(self)
		self.initUI()
	def initUI(self):
		'''连接槽函数'''
		self.Jwsub.clicked.connect(self.subWJInfo)
		self.Jwquery.clicked.connect(self.getJwInfo)
		# self.Jwchange.clicked.connect(self.Jwchanged)
		self.Rwgetid.clicked.connect(self.getRwid)
		self.Rwquery.clicked.connect(self.subRwInfo)
		self.getTimeBtn.clicked.connect(self.getCurrentTime)
		self.Rwchange.clicked.connect(self.getInInfo)
		self.Cwgetid.clicked.connect(self.getWid_Ck)
		self.getCwtime.clicked.connect(self.gettime)
		self.Cwquery.clicked.connect(self.subCwInfo)
		self.Cwchange.clicked.connect(self.getCwInfo)
		self.Kc.clicked.connect(self.getKcInfo)
		# self.Kc.clicked.connect(self.getId)
	def getKcInfo(self):
		model = QtSql.QSqlTableModel()
		self.initKcInfo(model)
		view = self.reservetable
		view.setModel(model)
	def initKcInfo(self,model):
		model.setTable('fr')
		model.select()
		model.setHeaderData(0, Qt.Horizontal, '物资编号')
		model.setHeaderData(1, Qt.Horizontal, '物资名称')
		model.setHeaderData(2, Qt.Horizontal, '规格型号')
		model.setHeaderData(3, Qt.Horizontal, '类别')
		model.setHeaderData(4, Qt.Horizontal, '计量单位')
		model.setHeaderData(5, Qt.Horizontal, '数量')
		model.setHeaderData(6, Qt.Horizontal, '金额')
		model.setHeaderData(0, Qt.Horizontal, '仓库')
	def initCwInfo(self,model):
		model.setTable('putout')
		model.select()
		model.setHeaderData(0, Qt.Horizontal, '信息编号')
		model.setHeaderData(8, Qt.Horizontal, '商品编号')
		model.setHeaderData(2, Qt.Horizontal, '商品单价')
		model.setHeaderData(1, Qt.Horizontal, '商品数量')
		model.setHeaderData(3, Qt.Horizontal, '商品金额')
		model.setHeaderData(4, Qt.Horizontal, '入库时间')
		model.setHeaderData(5, Qt.Horizontal, '经办人')
		model.setHeaderData(6, Qt.Horizontal, '保管人')
		model.setHeaderData(9, Qt.Horizontal, '仓库')
		model.setHeaderData(7, Qt.Horizontal, '备注')
	def getCwInfo(self):
		'''将入库表中的信息展示在TableView中'''
		model = QtSql.QSqlTableModel()
		self.initCwInfo(model)
		view = self.Cwtable
		view.setModel(model)
	def getWid_Ck(self):
		view = self.Cwidtable
		model = QtSql.QSqlTableModel()
		self.initRwidModel(model)
		# view = self.Rwidtable
		view.setModel(model)
	def gettime(self):
		i = QDateTime.currentDateTime()
		self.Cwtime.setText(i.toString(Qt.ISODate).replace('T',' '))
	def getCurrentTime(self):
		'''获取当前的日期时间'''
		i = QDateTime.currentDateTime() # PyQt5中的类QDateTime用来获取时间，输出形式为（日期）T（时间）
		print(i.toString(Qt.ISODate))
		self.Rwtime.setText(i.toString(Qt.ISODate).replace('T',' ')) # 将时间转为ISO时间格式，并去除T，为了和数据库的字段类型匹配
	def subCwInfo(self):
		self.query = QtSql.QSqlQuery()
		insert_sql = 'insert into putout(outNum,outprice,outSum,outTime,outGetPer,outviaPer,outRemark,outMaterials,outStore) values(?,?,?,?,?,?,?,?,?)'
		self.query.prepare(insert_sql)
		# self.query.addBindValue(int(self.e))
		# self.e = self.e + 1
		self.query.addBindValue(int(self.Cwnum.text()))
		self.query.addBindValue(int(self.Cwuprice.text()))
		self.query.addBindValue(int(self.Cwprice.text()))
		self.query.addBindValue(self.Cwtime.text())
		self.query.addBindValue(self.Cwgetperson.text())
		self.query.addBindValue(self.Cwviaperson.text())
		self.query.addBindValue(self.Cwtxt.text())
		self.query.addBindValue(int(self.Cwid.text()))
		self.query.addBindValue(int(self.outstore.currentText()))
		if not self.query.exec_(): # 执行SQL语句
			self.query.lastError().text()
			print(self.query.lastError().text())
		else:
			print('create a table')
	def subRwInfo(self):
		'''提交入库信息的槽函数'''
		self.query = QtSql.QSqlQuery() # 实例化PyQt5中的数据库操作对象QSqlQuery()
		insert_sql1 = 'insert into putin(inNum,inSum,inprice,intime,inViaPerson,inSavePerson,inRemark,inMaterials,inStore) values(?,?,?,?,?,?,?,?,?)'
		self.query.prepare(insert_sql1) # 和addBindvalue组合使用，向数据库中插入数据
		# self.query.addBindValue(int(self.d+8))
		# self.d= self.d+8
		self.query.addBindValue(int(self.Rwnum.text()))
		self.query.addBindValue(int(self.Rwuprice.text()))
		self.query.addBindValue(int(self.Rwprice.text()))
		self.query.addBindValue(self.Rwtime.text())
		self.query.addBindValue(self.Rwviaperson.text())
		self.query.addBindValue(self.Rwsaveperson.text())
		self.query.addBindValue(self.Rwtxt.text())
		self.query.addBindValue(int(self.Rwid.text()))
		print(self.instore.currentText())
		self.query.addBindValue(int(self.instore.currentText()))
		print(insert_sql1)
		if not self.query.exec_(): # 执行SQL语句
			self.query.lastError().text()
			print(self.query.lastError().text())
			self.initLabel()
			self.intip.setText("添加失败！")
		else:
			print('create a table')
			self.initLabel()
			self.intip.setText("添加成功！")
	def getInInfo(self):
		'''将入库表中的信息展示在TableView中'''
		model = QtSql.QSqlTableModel()
		self.initInModel(model)
		view = self.Rwtable
		view.setModel(model)
	def initInModel(self, model):
		'''用数据库模型的数据表，将数据库中物资的入库信息表显示出来'''
		# 设置数据库模型的数据表
		model.setTable('putin')
		model.select()
		model.setHeaderData(0, Qt.Horizontal, '信息编号')
		model.setHeaderData(1, Qt.Horizontal, '商品编号')
		model.setHeaderData(2, Qt.Horizontal, '商品单价')
		model.setHeaderData(8, Qt.Horizontal, '商品数量')
		model.setHeaderData(3, Qt.Horizontal, '商品金额')
		model.setHeaderData(4, Qt.Horizontal, '入库时间')
		model.setHeaderData(5, Qt.Horizontal, '经办人')
		model.setHeaderData(6, Qt.Horizontal, '保管人')
		model.setHeaderData(9, Qt.Horizontal, '仓库')
		model.setHeaderData(7, Qt.Horizontal, '备注')
	def getRwid(self):
		model = QtSql.QSqlTableModel()
		self.initRwidModel(model)
		view = self.Rwidtable
		view.setModel(model)
	def initRwidModel(self, model):
		model.setTable('materialsinfo')
		# 允许字段更改
		# model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
		# 查询所有数据
		model.select()
		model.removeColumn(1)
		model.removeColumn(2)
		model.removeColumn(1)
		model.removeColumn(2)
		model.removeColumn(1)
		model.removeColumn(2)
		# 设置表格头
		model.setHeaderData(0, Qt.Horizontal, '商品编号')
	def getJwInfo(self):
		model = QtSql.QSqlTableModel()
		self.initModel(model)
		view = self.Jwtable
		self.initLabel()
		self.tip.setText("查询成功！")
		view.setModel(model)
	def initModel(self, model):
		# self.table_widget.setModel(self.model)
		# 设置数据模型的数据表
		model.setTable('materialsinfo')
		# 允许字段更改
		# model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
		# 查询所有数据
		model.select()
		# 设置表格头
		model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
		model.setHeaderData(0, Qt.Horizontal, '商品编号')
		model.setHeaderData(1, Qt.Horizontal, '商品名称')
		model.setHeaderData(2, Qt.Horizontal, '规格型号')
		model.setHeaderData(3, Qt.Horizontal, '类别')
		model.setHeaderData(4, Qt.Horizontal, '计量单位')
		# self.JwsubSignal.emit()
		# return model
	# def Jwchanged(self):
	# 	view = self.Jwtable
	# 	view.setModel(model)
	# def modelChanged(self,model):
	# 	# self.getJwInfo(model)
	# 	self.initModel(model)
	# 	model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
	# 	# self.status.showMessage("dsds")
	def initLabel(self):
		'''为label设置字体颜色'''
		pe = QPalette()
		pe.setColor(QPalette.WindowText, Qt.red)  # 设置字体颜色
		self.label.setAutoFillBackground(True)  # 设置背景充满，为设置背景颜色的必要条件
		pe.setColor(QPalette.Window, Qt.blue)  # 设置背景颜色
		# pe.setColor(QPalette.Background,Qt.blue)<span style="font-family: Arial, Helvetica, sans-serif;">#设置背景颜色，和上面一行的效果一样
		self.tip.setPalette(pe)
		self.intip.setPalette(pe)
	def subWJInfo(self):
		'''将商品信息写进数据库'''
		# 实例化数据库查询操作
		self.q = QtSql.QSqlQuery()
		# 定义SQl语句
		insert_sql = 'insert into materialsinfo values (?,?,?,?,?)'
		# 将商品字段绑定到数据库对应字段
		self.q.prepare(insert_sql)
		self.q.addBindValue(int(self.Jwid.text()))
		self.q.addBindValue(self.Jwname.text())
		self.q.addBindValue(self.Jwsample.text())
		self.q.addBindValue(self.Jwtype.text())
		self.q.addBindValue(self.Jwunit.text())
		# 提交插入数据库
		# print(insert_sql)
		if not self.q.exec_():
			self.q.lastError()
			print(self.q.lastError().text())
			self.initLabel()
			self.tip.setText("添加失败！")
		else:
			print('create a table')
			self.initLabel()
			self.tip.setText("添加成功！")
if __name__ == '__main__':
	# db = dataBase()
	# db.show()
	# 连接数据库
	db = QSqlDatabase.addDatabase("QMYSQL")
	# 连接本地服务器
	db.setHostName("127.0.0.1")
	# 连接数据库端口
	db.setPort(3306)
	# 数据库名称
	db.setDatabaseName("materialsadmin")
	# 数据库用户名
	db.setUserName("root")
	# 数据库密码
	db.setPassword("mysql")
	# 打开数据库
	db.open()
	# model = QtSql.QSqlTableModel()
	# 实例化一个可编辑数据模型
	model = QtSql.QSqlTableModel()
	app = QApplication(sys.argv)
	win = window()
	win.setWindowTitle("物资管理系统")
	win.initModel(model)
	print(win.size())
	# 固定客户端大小为580x452
	win.setFixedHeight(571)
	win.setFixedWidth(1171)
	# win.modelChanged(model)
	win.show()
	sys.exit(app.exec_())
	