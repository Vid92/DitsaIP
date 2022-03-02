# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogip.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import os
import subprocess
import time

class Ui_DialogIP(QtWidgets.QDialog):
	#def setupUi(self, DialogIP):
	def __init__(self,parent=None):
		super(Ui_DialogIP, self).__init__()
		self.parent = parent

		self.setObjectName("DialogIP")
		#self.resize(490, 368) 
		self.setFixedSize(519,476) 
		self.buttonBox = QtWidgets.QDialogButtonBox(self)
		self.buttonBox.setGeometry(QtCore.QRect(335, 440, 166, 25))
		self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Abort|QtWidgets.QDialogButtonBox.Save)
		self.buttonBox.setObjectName("buttonBox_2")
		self.tableWidget = QtWidgets.QTableWidget(self)
		self.tableWidget.setGeometry(QtCore.QRect(10, 70, 491, 361))
		self.tableWidget.setColumnCount(2)
		self.tableWidget.setObjectName("tableWidget")
		self.tableWidget.setRowCount(0)
		self.tableWidget.horizontalHeader().setDefaultSectionSize(220)#cuidar tamaño renglones y columnas
		self.tableWidget.horizontalHeader().setMinimumSectionSize(160)
		self.widget = QtWidgets.QWidget(self)
		self.widget.setGeometry(QtCore.QRect(10, 20, 491, 29))
		self.widget.setObjectName("widget")
		self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
		self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
		self.horizontalLayout_2.setObjectName("horizontalLayout_2")
		self.horizontalLayout = QtWidgets.QHBoxLayout()
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.label = QtWidgets.QLabel(self.widget)
		self.label.setObjectName("label")
		self.horizontalLayout.addWidget(self.label)
		self.lineIP_1 = QtWidgets.QLineEdit(self.widget)
		self.lineIP_1.setObjectName("lineIP_1")
		self.lineIP_1.setInputMask("000.000.000.000")
		
		self.horizontalLayout.addWidget(self.lineIP_1)
		self.label_2 = QtWidgets.QLabel(self.widget)
		self.label_2.setObjectName("label_2")
		self.horizontalLayout.addWidget(self.label_2)
		self.lineIP_2 = QtWidgets.QLineEdit(self.widget)
		self.lineIP_2.setObjectName("lineIP_2")
		self.lineIP_2.setInputMask("000.000.000.000")

		self.horizontalLayout.addWidget(self.lineIP_2)
		self.horizontalLayout_2.addLayout(self.horizontalLayout)
		self.bttnAdd = QtWidgets.QPushButton(self.widget)
		self.bttnAdd.setObjectName("bttnAdd")
		self.horizontalLayout_2.addWidget(self.bttnAdd)
		self.bttnDelete = QtWidgets.QPushButton(self.widget)
		self.bttnDelete.setObjectName("bttnDelete")
		self.horizontalLayout_2.addWidget(self.bttnDelete)

		self.progressBar = QtWidgets.QProgressBar(self)
		self.progressBar.setGeometry(QtCore.QRect(10, 440, 311, 23))
		#self.progressBar.setProperty("value", 60)
		self.progressBar.setObjectName("progressBar")

		self.retranslateUi(self)
		QtCore.QMetaObject.connectSlotsByName(self)

		self.tableWidget.setHorizontalHeaderLabels(('IP','Status'))

	def retranslateUi(self, DialogIP):
		_translate = QtCore.QCoreApplication.translate
		DialogIP.setWindowTitle(_translate("DialogIP", "Add IP"))
		self.label.setText(_translate("DialogIP", "Range IP"))
		self.label_2.setText(_translate("DialogIP", "to"))
		self.bttnAdd.setText(_translate("DialogIP", "Add"))
		self.bttnDelete.setText(_translate("DialogIP", "Delete"))

		self.buttonBox.accepted.connect(self.bttnSave)
		self.buttonBox.rejected.connect(self.bttnAbort)
		self.bttnAdd.clicked.connect(self.buttonAdd)
		self.bttnDelete.clicked.connect(self.buttonDelete)

		self.lineIP_1.setAlignment(QtCore.Qt.AlignCenter)
		self.lineIP_2.setAlignment(QtCore.Qt.AlignCenter)

		self.ip_temp = list() #lista temporal ip
		self.ip_temp1 = list()
		self.ip1 = list()
		self.ip2 = list()
		self.flagSave = False
		self.flagResponse = False

	def showEvent(self,event):
		#pass
		_translate = QtCore.QCoreApplication.translate
		self.buttonBox.setToolTip(_translate("self","Button Abort: Cancel the process.\r\nButton Save: Save only the active IP."))
		self.tableWidget.setToolTip(_translate("self","Show active IP"))

	def closeEvent(self,event):
		self.flagR = True
		print("closEE")
		#pass

	count = 0
	flagR = False
	flagInc = False
	flagMax = False
	fragIp = ""
	n = 0
	flagC = False
	def buttonAdd(self):
		ip_text = self.lineIP_1.text()
		ip_text2 = self.lineIP_2.text()

		self.n = 0
		self.flagC = False
		self.flagInc = False
		self.flagMax = False
		self.fragIp = ""
		self.ip1.clear()
		#self.ip_temp1.clear()
		
		if(ip_text)=='...':
			self.flagC = True
		#	msgEmpty = QtWidgets.QMessageBox()
		#	msgEmpty.information(self,'Error','Empty Ip range',QtWidgets.QMessageBox.Ok)
		else:
			for i in range(len(ip_text)): #proceso para saber si esta completo la ip1
				if (i==(len(ip_text)-1)and(ip_text[i]=='.')):
					self.flagInc = True
					break
				if(ip_text[i]=='.'):
					self.ip1.append(int(self.fragIp))
					if(self.fragIp==''):
						self.flagInc = True
						break
					
					elif(int(self.fragIp)>255):
						self.flagMax = True
						break
					self.n+=1
					self.fragIp = ""
				else:
					self.fragIp += ip_text[i]
					if(self.n == 3 and i==(len(ip_text)-1)):
						self.ip1.append(int(self.fragIp))
						if(self.fragIp==''):
							self.flagInc = True
							self.fragIp = ""
							break
						elif(int(self.fragIp)>255):
							self.flagMax = True
							self.fragIp = ""
							break

			if(ip_text2!='...'): #indica si hay ip en ip_text2
				self.n = 0
				self.flagC = False
				self.fragIp = ""
				self.ip2.clear()
				for i in range(len(ip_text2)): #proceso para saber si esta completo la ip2
					if (i==(len(ip_text2)-1)and(ip_text2[i]=='.')):
						self.flagInc = True
						break
					if(ip_text2[i]=='.'):
						self.ip2.append(int(self.fragIp))
						if(self.fragIp==''):
							self.flagInc = True
							
						elif(int(self.fragIp)>255):
							self.flagMax = True
						
						self.n+=1
						self.fragIp = ""
				
					else:
						self.fragIp += ip_text2[i]
						if(self.n == 3 and i==(len(ip_text2)-1)):
							self.ip2.append(int(self.fragIp))
							if(self.fragIp==''):
								self.flagInc = True
								self.fragIp = ""
								
							elif(int(self.fragIp)>255):
								self.flagMax = True
								self.fragIp = ""

		if(self.flagInc!=False):
			self.ip1.clear()
			self.ip2.clear()
			self.mssgIncomplete()
		
		if(self.flagMax!=False):
			self.ip1.clear()
			self.ip2.clear()
			self.mssgMax()
			
		if(self.flagC!=True):
			self.ip_temp.clear()
			if(ip_text2!='...'):#falta una ultima validacion para checar que
				self.segments() #ponerlo en list temporales tomando como numeros , 4 espacios
			else:
				self.ip_temp.append(str(self.ip1[0])+"."+str(self.ip1[1])+"."+str(self.ip1[2])+"."+str(self.ip1[3]))
				#self.ip_temp1.append(str(self.ip1[0])+"."+str(self.ip1[1])+"."+str(self.ip1[2])+"."+str(self.ip1[3]))

			#if(len(self.ip_temp)!=0): #
			self.flagR = False
			for i in range(len(self.ip_temp1)): #verifica que no este repetido las ips
				for j in range(len(self.ip_temp)):
					if(self.ip_temp1[i] == self.ip_temp[j]): #poner bloqueo!! checar esta parte
						self.flagR = True

				if(self.flagR!=False):
					print("repetido")
					rpeat = QtWidgets.QMessageBox()
					rpeat.information(self,'Error','Repeated Ip value',QtWidgets.QMessageBox.Ok)
					break

			self.progressBar.setFormat("Looking for ...")
			n = len(self.ip_temp)
			self.percentage = 100.0 / float(n)
			value = 0

			self.progressBar.setValue(value)
			time.sleep(1)

			if(self.flagR!=True):
				self.flagResponse = False
				for i in range(len(self.ip_temp)):
					QtGui.QGuiApplication.processEvents()
					response = os.system("ping -c 1 " + self.ip_temp[i]) #comando para consola

					value+= self.percentage
					self.progressBar.setValue(value)

					if(response==0): #si hay ip
						self.flagResponse = True
						self.count+=1
						self.tableWidget.setRowCount(self.count)
						lblt = QtGui.QFont("Arial",10, QtGui.QFont.Normal)
						lblt2 = QtGui.QFont("Arial",10, QtGui.QFont.Black)
						item = QtWidgets.QTableWidgetItem(self.ip_temp[i])
						item.setTextAlignment(QtCore.Qt.AlignCenter)
						item.setFont(lblt)
						item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
						self.tableWidget.setItem(self.count-1,0,item)

						self.lineIP_1.setText("")
						self.lineIP_2.setText("")

						item1 = QtWidgets.QTableWidgetItem("Active")
						item1.setTextAlignment(QtCore.Qt.AlignCenter)
						item1.setFont(lblt2)
						item1.setForeground(QtGui.QColor("white"))
						item1.setBackground(QtGui.QColor('mediumseagreen'))
						item1.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
						self.tableWidget.setItem(self.count-1,1,item1)
						self.parent.ip_active.append(self.ip_temp[i])
					
					if(self.flagR==True):
						self.flagSave = False
						break
					#else:
					#	item1 = QtWidgets.QTableWidgetItem("Desactive")
					#	item1.setTextAlignment(QtCore.Qt.AlignCenter)
					#	item1.setFont(lblt2)
					#	item1.setForeground(QtGui.QColor("white"))
					#	item1.setBackground(QtGui.QColor('crimson'))
					#	item1.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
					#	self.tableWidget.setItem(self.count-1,1,item1)

				self.progressBar.setValue(100)
				self.progressBar.setFormat("Ready!")
				self.flagSave = True

				if(self.flagResponse!=True):
					self.tableWidget.setRowCount(1)
					lblt2 = QtGui.QFont("Arial",10, QtGui.QFont.Normal)
					item2 = QtWidgets.QTableWidgetItem("-----")
					item2.setTextAlignment(QtCore.Qt.AlignCenter)
					item2.setFont(lblt2)
					item2.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
					self.tableWidget.setItem(0,0,item2)

					lblt = QtGui.QFont("Arial",10, QtGui.QFont.Black)
					item = QtWidgets.QTableWidgetItem("NO FOUND IP")
					item.setTextAlignment(QtCore.Qt.AlignCenter)
					item.setFont(lblt)
					item.setForeground(QtGui.QColor("white"))
					item.setBackground(QtGui.QColor('crimson'))
					item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
					self.tableWidget.setItem(0,1,item)

				print("Sale")
				for i in range(len(self.ip_temp)):
					self.ip_temp1.append(self.ip_temp[i])

	def buttonDelete(self):
		print("bttnDelete")

	def segments(self):
		if((self.ip1[0]==self.ip2[0]) and (self.ip1[1]==self.ip2[1]) and (self.ip1[2]==self.ip2[2])):
			if(self.ip1[3]>self.ip2[3]):
				#for i in range(self.ip1[3],self.ip2[3]-1,-1):
				for i in reversed(range(self.ip2[3],self.ip1[3]+1)):
					self.ip_temp.append(str(self.ip1[0])+"."+str(self.ip1[1])+"."+str(self.ip1[2])+"."+str(i))
			else:
				for i in range(self.ip1[3],self.ip2[3]+1):
					self.ip_temp.append(str(self.ip1[0])+"."+str(self.ip1[1])+"."+str(self.ip1[2])+"."+str(i))

		elif((self.ip1[0]==self.ip2[0]) and (self.ip1[1]==self.ip2[1])):#checar esta parte!!
			if(self.ip1[2]>self.ip2[2]):
				if(self.ip1[3]>=self.ip2[3]):
					for j in reversed(range(self.ip2[2],self.ip1[2]+1)):
						if(j==self.ip1[2]):
							#for i in reversed(range(self.ip2[3],self.ip1[3]+1)):
							for i in reversed(range(1,self.ip1[3]+1)):
								self.ip_temp.append(str(self.ip1[0])+"."+str(self.ip1[1])+"."+str(j)+"."+str(i))
						else:
							for i in reversed(range(1,255)):
								self.ip_temp.append(str(self.ip1[0])+"."+str(self.ip1[1])+"."+str(j)+"."+str(i))
								if((j==self.ip2[2]) and (i==self.ip2[3])):
									break
				else:
					for j in reversed(range(self.ip2[2],self.ip1[2]+1)):
						if(j==self.ip1[2]):
							for i in reversed(range(1,self.ip2[3])):
								if(i<=self.ip1[3]):
									self.ip_temp.append(str(self.ip1[0])+"."+str(self.ip1[1])+"."+str(j)+"."+str(i))
						else:
							for i in reversed(range(1,255)):
								self.ip_temp.append(str(self.ip1[0])+"."+str(self.ip1[1])+"."+str(j)+"."+str(i))
								if((j==self.ip2[2]) and (i==self.ip2[3])):
									break
			else:
				print("else")
				if(self.ip1[3]>=self.ip2[3]):
					for j in range(self.ip1[2],self.ip2[2]+1):
						if(j==self.ip1[2]):
							for i in range(self.ip1[3],255):
								self.ip_temp.append(str(self.ip1[0])+"."+str(self.ip1[1])+"."+str(j)+"."+str(i))
						else:
							for i in range(1,255):
								self.ip_temp.append(str(self.ip1[0])+"."+str(self.ip1[1])+"."+str(j)+"."+str(i))
								if((j==self.ip2[2]) and (i==self.ip2[3])):
									break
				else:
					print("entra")
					for j in range(self.ip1[2],self.ip2[2]+1):
						if(j==self.ip1[2]):
							for i in range(self.ip1[3],255):
								#if(i>=self.ip1[3]):
								self.ip_temp.append(str(self.ip1[0])+"."+str(self.ip1[1])+"."+str(j)+"."+str(i))
						else:
							for i in range(1,255):
								self.ip_temp.append(str(self.ip1[0])+"."+str(self.ip1[1])+"."+str(j)+"."+str(i))
								if((j==self.ip2[2]) and (i==self.ip2[3])):
									break

		elif(self.ip1[0]==self.ip2[0]):
			print("primer elemento igual")

		else:
			print("no hay elementos iguales")

	def mssgIncomplete(self):
		self.flagC = True
		incmp = QtWidgets.QMessageBox()
		incmp.information(self,'Error','Incomplete Ip range',QtWidgets.QMessageBox.Ok)

	def mssgMax(self):
		self.flagC = True
		maxvalue = QtWidgets.QMessageBox()
		maxvalue.information(self,'Error','Ip value out of range. \nMaximun 255 in each segment.',QtWidgets.QMessageBox.Ok)

	def bttnSave(self): #se debe visualizar las ip gurdadas en la pantalla principal
		print("bttnSave")
		if(self.flagSave!=False):
			for i in range(len(self.parent.ip_active)):
				self.parent.tableWidget.setRowCount(i+1)
				lblt = QtGui.QFont("Arial",10, QtGui.QFont.Normal)
				item = QtWidgets.QTableWidgetItem(self.parent.ip_active[i])
				item.setTextAlignment(QtCore.Qt.AlignCenter)
				item.setFont(lblt)
				item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
				self.parent.tableWidget.setItem(i,0,item)

			self.parent.tabItem()
			time.sleep(2) #opcional
			self.close()

	def bttnAbort(self):
		print("bttnAbort")
		time.sleep(0.3) #opcional
		self.close()

'''
if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	DialogIP = QtWidgets.QDialog()
	ui = Ui_DialogIP()
	ui.setupUi(DialogIP)
	DialogIP.show()
	sys.exit(app.exec_())
'''