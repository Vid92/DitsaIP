# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class LineEditDelegateIP(QtWidgets.QStyledItemDelegate):
	def __init__(self):
		super(LineEditDelegateIP,self).__init__()

	def createEditor(self, parent, option, index):
		line = QtWidgets.QLineEdit(parent)
		line.setAlignment(QtCore.Qt.AlignCenter)
		line.setInputMask("000.000.000.000")
		return line

	def setEditorData(self, editor, index):
		cbIndex = index.model().data(index,QtCore.Qt.EditRole)
		editor.setText(cbIndex)

	def setModelData(self,editor,model,index):
		model.setData(index,editor.text(),QtCore.Qt.EditRole)
