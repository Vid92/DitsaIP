# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


#from DitsaNetEditorApp import MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

#from pssword import Ui_PassWord
#from form import Ui_Form


class Ui_FormEmpty(QtWidgets.QWidget):
	def __init__(self,parent=None):
		super(Ui_FormEmpty, self).__init__()
		self.parent = parent
	#def setupUi(self, Form):

		self.setObjectName("FormEmpty")
		self.resize(450, 399) #450 399
		#self.horizontalLayout = QtWidgets.QHBoxLayout(self)
		#self.horizontalLayout.setObjectName("horizontalLayout")
		
		self.label = QtWidgets.QLabel(self)
		self.label.setGeometry(QtCore.QRect(140, 90, 181, 21))
		self.label.setTextFormat(QtCore.Qt.AutoText)
		self.label.setAlignment(QtCore.Qt.AlignCenter)
		self.label.setObjectName("label")
		self.lineEdit = QtWidgets.QLineEdit(self)
		self.lineEdit.setGeometry(QtCore.QRect(140, 130, 181, 25))
		self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
		self.lineEdit.setObjectName("lineEdit")
		self.lineEdit.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[1-9]\\d{0,5}"),self)) 

		self.labelpass = QtWidgets.QLabel(self)
		self.labelpass.setGeometry(QtCore.QRect(140, 170, 181, 21))
		self.labelpass.setTextFormat(QtCore.Qt.AutoText)
		self.labelpass.setAlignment(QtCore.Qt.AlignCenter)
		self.labelpass.setObjectName("labelpass")

		self.retranslateUi(self)
		QtCore.QMetaObject.connectSlotsByName(self)

	def retranslateUi(self, FormEmpty):
		_translate = QtCore.QCoreApplication.translate
		FormEmpty.setWindowTitle(_translate("Form", "FormEmpty"))
		self.label.setText(_translate("Dialog", "Enter Password"))

		self.lineEdit.returnPressed.connect(self.on_edit)
		self.lineEdit.textChanged.connect(self.cleanEdit)
	
	def showEvent(self,event):
		print("showempty")

	def closeEvent(self,event):
		print("CloseEmpty")
		self.parent.principalForm()

	def on_edit(self):
		print("on_Edit")
		if(self.lineEdit.text()=="2022"): #default password
			self.lineEdit.setText("")
			#print("password correct!")
			#self.parent.tabWidget.removeTab(0)
			self.close()
		else:
			self.labelpass.setText("Incorrect password!")
			#self.lineEdit.setText("Incorrect password")
	
	def cleanEdit(self):
		#self.lineEdit.setText("")
		self.labelpass.setText("")

'''
if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	Form = QtWidgets.QWidget()
	ui = Ui_Form()
	ui.setupUi(Form)
	Form.show()
	sys.exit(app.exec_())
'''