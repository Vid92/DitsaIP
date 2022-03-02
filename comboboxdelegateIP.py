# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

class ComboBoxDelegateIP(QtWidgets.QStyledItemDelegate):
	def __init__(self,data,parent=None):
		super(ComboBoxDelegateIP,self).__init__(parent=None)
		self.parent = parent
		self.data = data

	def createEditor(self, parent, option, index):
		cb = QtWidgets.QComboBox(parent)
		#cb.setEditable(True)
		#cb.lineEdit().setAlignment(QtCore.Qt.AlignCenter)
		for i in range(len(self.data)):
			cb.addItem(self.data[i])
		return cb

	def setEditorData(self, editor, index):
		cbIndex = index.model().data(index,QtCore.Qt.EditRole)
		editor.setCurrentText(cbIndex)

	def setModelData(self,editor,model,index):
		self.flag = False
		model.setData(index,editor.currentText(),QtCore.Qt.EditRole)


'''
if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())
'''