# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SettingsIP.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from form_empty import Ui_FormEmpty
from comboboxdelegateIP import ComboBoxDelegateIP
from lineEditDelegateIP import LineEditDelegateIP

import time

class Ui_SettingsIP(object):
	def __init__(self,SettingsIP, parent=None):
		object.__init__(parent)
	#def setupUi(self, SettingsIP):
		SettingsIP.setObjectName("SettingsIP")
		#SettingsIP.resize(463, 646)
		SettingsIP.setFixedSize(463,646) 
		SettingsIP.setLayoutDirection(QtCore.Qt.RightToLeft)
		self.centralwidget = QtWidgets.QWidget(SettingsIP)
		self.centralwidget.setObjectName("centralwidget")
		self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
		self.gridLayout.setObjectName("gridLayout")

		self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
		self.tableWidget.setGeometry(QtCore.QRect(0, 0, 421, 571))
		self.tableWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
		self.tableWidget.setRowCount(0)
		self.tableWidget.setColumnCount(2)
		self.tableWidget.setObjectName("tableWidget")
		self.tableWidget.horizontalHeader().setVisible(True)
		self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
		self.tableWidget.horizontalHeader().setHighlightSections(True)
		self.tableWidget.horizontalHeader().setMinimumSectionSize(57)
		self.tableWidget.verticalHeader().setVisible(True)
		#self.tableWidget.verticalHeader().setHighlightSections(True)
		self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)
		self.tableWidget.horizontalHeader().setStretchLastSection(True)
		self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)

		self.horizontalLayout = QtWidgets.QHBoxLayout()
		self.horizontalLayout.setObjectName("horizontalLayout")

		self.buttonSave = QtWidgets.QPushButton(self.centralwidget)
		self.buttonSave.setObjectName("buttonSave")
		self.horizontalLayout.addWidget(self.buttonSave)
		self.buttonCancel = QtWidgets.QPushButton(self.centralwidget)
		self.buttonCancel.setObjectName("buttonCancel")
		self.horizontalLayout.addWidget(self.buttonCancel)
		self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

		SettingsIP.setCentralWidget(self.centralwidget)
		self.statusbar = QtWidgets.QStatusBar(SettingsIP)
		self.statusbar.setObjectName("statusbar")
		SettingsIP.setStatusBar(self.statusbar)
		self.toolBar = QtWidgets.QToolBar(SettingsIP)
		self.toolBar.setEnabled(True)
		self.toolBar.setLayoutDirection(QtCore.Qt.LeftToRight)
		self.toolBar.setMovable(False)
		self.toolBar.setOrientation(QtCore.Qt.Horizontal)
		self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
		self.toolBar.setFloatable(True)
		self.toolBar.setObjectName("toolBar")
		SettingsIP.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

		self.menuBar = QtWidgets.QMenuBar(SettingsIP)
		self.menuBar.setGeometry(QtCore.QRect(0, 0, 427, 22))
		self.menuBar.setLayoutDirection(QtCore.Qt.LeftToRight)
		self.menuBar.setObjectName("menuBar")
		self.menuFile = QtWidgets.QMenu(self.menuBar)
		self.menuFile.setObjectName("menuFile")
	#	self.menuEdit = QtWidgets.QMenu(self.menuBar)
	#	self.menuEdit.setObjectName("menuEdit")
		SettingsIP.setMenuBar(self.menuBar)

		self.actionAddIP = QtWidgets.QAction(QtGui.QIcon('/opt/Ditsa/DitsaIP/image/ethernet.png'),'Add',SettingsIP)
		self.actionDelete = QtWidgets.QAction(QtGui.QIcon('/opt/Ditsa/DitsaIP/image/borrar.png'),'Delete',SettingsIP)
		
		#self.buttonSave.setIcon(QtGui.QIcon('/opt/Ditsa/DitsaIP/image/guardar.png'))
		#self.buttonSave.setIconSize(QtCore.QSize(5,5))
		
		self.actionExit = QtWidgets.QAction(SettingsIP)
		#self.actionExit.setObjectName("actionExit")
		self.toolBar.addAction(self.actionAddIP)
		self.toolBar.addAction(self.actionDelete)

		self.menuFile.addAction(self.actionExit)
	#	self.menuEdit.addAction(self.actionAddIP)
	#	self.menuEdit.addAction(self.actionDelete)
		self.menuBar.addAction(self.menuFile.menuAction())
	#	self.menuBar.addAction(self.menuEdit.menuAction())

		self.retranslateUi(SettingsIP)
		QtCore.QMetaObject.connectSlotsByName(SettingsIP)

		SettingsIP.showEvent = self.showEvent
		SettingsIP.closeEvent = self.closeEvent

		self.tableWidget.setHorizontalHeaderLabels(('IP','Assigned Names'))
		self.actionAddIP.triggered.connect(self.addRenglonIP)
		self.actionDelete.triggered.connect(self.deleteRenglon)

		self.tableWidget.cellClicked.connect(self.cellCh)

		self.SettingsIP = SettingsIP

	def retranslateUi(self, SettingsIP):
		_translate = QtCore.QCoreApplication.translate
		SettingsIP.setWindowTitle(_translate("SettingsIP", "Settings_IP"))
		SettingsIP.setWindowIcon(QtGui.QIcon('/opt/Ditsa/DitsaIP/configIp2.png'))

		self.buttonSave.setText(_translate("settingsIP", "Save"))
		self.buttonCancel.setText(_translate("settingsIP", "Cancel"))
		
		self.toolBar.setWindowTitle(_translate("SettingsIP", "toolBar"))
		self.menuFile.setTitle(_translate("SettingsIP", "File"))
		#self.menuEdit.setTitle(_translate("SettingsIP", "Edit"))
	#	self.actionAddIP.setText(_translate("SettingsIP", "Add IP"))
		self.actionExit.setText(_translate("SettingsIP", "Exit"))

		self.buttonSave.clicked.connect(self.bttnSave)
		self.buttonCancel.clicked.connect(self.bttnCancel)
		self.actionExit.triggered.connect(self.bttnExit)

		self.tableWidget.hide()
		self.buttonSave.hide()
		self.buttonCancel.hide()

		self.actionAddIP.setEnabled(False)
		self.actionDelete.setEnabled(False)

		self.wmin = False
		self.flag = False
		self.ip_column = list()
		self.ip_row = list()
		self.ip_final = list()
		self.name_Mod = list()
		self.myName = list()
		self.addr = list()

		self.n = 0

	def showEvent(self,event):
		if self.wmin != True:
			self.wmin = True
			print("showEvent")
			form = Ui_FormEmpty(self)
			self.gridLayout.addWidget(form)

	def closeEvent(self,event):
		print("closeEvent")

	def principalForm(self):
		self.actionAddIP.setEnabled(True)
		self.actionDelete.setEnabled(True)

		self.tableWidget.show()
		self.buttonSave.show()
		self.buttonCancel.show()

		settings = QtCore.QSettings('/home/ditsa/DitsaNet/Settings/archivo.ini', QtCore.QSettings.NativeFormat)
		if settings.value('/home/ditsa/DitsaNet/Settings/archivo.ini')!='':
			self.settingsList = settings.value("mylist")
			#self.settingsLabel = settings.value("mylabel")
			#self.settingsRowCol = settings.value("rowcol")

			if self.settingsList != None:
				self.name_Mod = self.settingsList[:] 
		
		for i in range(2,len(self.name_Mod),4):
			self.myName.append(self.name_Mod[i].replace('N=',''))
			self.addr.append(self.name_Mod[i+1].replace('A=',''))

	def addRenglonIP(self):
		self.n = 1 + self.n
		self.tableWidget.setRowCount(self.n)
		#Ui_DialogIP(self).exec_()
		self.tabItem()

	def deleteRenglon(self): #version sencilla puede ser mas complejo esta opcion
		if self.n != 0:
			self.n = self.n - 1

		self.tableWidget.setRowCount(self.n)

	def tabItem(self):	
		self.cbid2 = LineEditDelegateIP()
		self.nameColumnX = self.tableWidget.setItemDelegateForColumn(0,self.cbid2)
		
		self.cbid = ComboBoxDelegateIP(self.myName)
		self.nameColumnY = self.tableWidget.setItemDelegateForColumn(1,self.cbid)

	def cellCh(self):
		x = self.tableWidget.currentRow()
		y = self.tableWidget.currentColumn()

		if y == 0:
			item = QtWidgets.QTableWidgetItem(self.nameColumnX)  #falta esto , checar como hacerlo!!
			item.setTextAlignment(QtCore.Qt.AlignCenter)
			self.tableWidget.setItem(x,0,item)
		else:
			item = QtWidgets.QTableWidgetItem(self.nameColumnY)  #falta esto , checar como hacerlo!!
			item.setTextAlignment(QtCore.Qt.AlignCenter)
			self.tableWidget.setItem(x,1,item)
	
	def bttnExit(self):
		SettingsIP.close()

	def bttnCancel(self):
		print("cancel")
		time.sleep(1)
		SettingsIP.close()

	def bttnSave(self):
		self.ip_row.clear()
		self.ip_column.clear()
		self.flag = False

		try:
			for i in range(self.tableWidget.rowCount()):
				self.ip_column.append(self.tableWidget.item(i,1).text())
				self.ip_row.append(self.tableWidget.item(i,0).text())

			if len(self.ip_row)!=0: #ojo!!
				for i in range(len(self.ip_row)):
					x = self.ip_row.count(self.ip_row[i])
					if(x >= 2): #si esta repetido no guarda configuracion
						self.flag = True
						rep = QtWidgets.QMessageBox()
						rep.information(SettingsIP,'Error','Repeated IP.',QtWidgets.QMessageBox.Ok)
						break

			if len(self.ip_column)!=0: #ojo!!
				for i in range(len(self.ip_column)):
					x = self.ip_column.count(self.ip_column[i])
					if(x >= 2): #si esta repetido no guarda configuracion
						self.flag = True
						rep = QtWidgets.QMessageBox()
						rep.information(SettingsIP,'Error','Repeated Assigned Names.',QtWidgets.QMessageBox.Ok)
						break
		except:
			self.flag = True
			emptyList = QtWidgets.QMessageBox()
			emptyList.information(SettingsIP,'Error','Empty IP or Assigned Names.',QtWidgets.QMessageBox.Ok)
		
		if(self.flag!=True):
			self.ip_final.clear()
			for i in range(len(self.ip_column)):
				self.ip_final.append(self.ip_row[i])
				self.ip_final.append(self.ip_column[i])
				self.ip_final.append(self.addr[i])

			print("ip_final:",self.ip_final)
			settings = QtCore.QSettings('/home/ditsa/DitsaNet/Settings/archivo_ipconfig.ini', QtCore.QSettings.NativeFormat)
			settings.setValue("ip",self.ip_final)

			time.sleep(2) #opcional
			SettingsIP.close()


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	SettingsIP = QtWidgets.QMainWindow()
	ui = Ui_SettingsIP(SettingsIP)
	#ui.setupUi(SettingsIP)
	SettingsIP.show()
	sys.exit(app.exec_())
