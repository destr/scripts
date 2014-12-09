# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dirselector.ui'
#
# Created: Tue Dec  9 21:14:36 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DirSelector(object):
    def setupUi(self, DirSelector):
        DirSelector.setObjectName("DirSelector")
        DirSelector.resize(703, 76)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(DirSelector)
        self.horizontalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(DirSelector)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setPlaceholderText("")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButtonSelect = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonSelect.setObjectName("pushButtonSelect")
        self.horizontalLayout.addWidget(self.pushButtonSelect)
        self.horizontalLayout_2.addWidget(self.groupBox)

        self.retranslateUi(DirSelector)
        QtCore.QMetaObject.connectSlotsByName(DirSelector)

    def retranslateUi(self, DirSelector):
        _translate = QtCore.QCoreApplication.translate
        DirSelector.setWindowTitle(_translate("DirSelector", "Form"))
        self.pushButtonSelect.setText(_translate("DirSelector", "Select..."))

