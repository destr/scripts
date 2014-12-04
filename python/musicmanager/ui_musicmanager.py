# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'musicmanager.ui'
#
# Created: Thu Dec  4 21:56:43 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MusicManager(object):
    def setupUi(self, MusicManager):
        MusicManager.setObjectName("MusicManager")
        MusicManager.resize(630, 646)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(MusicManager)
        self.verticalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.groupBoxMusicDir = QtWidgets.QGroupBox(MusicManager)
        self.groupBoxMusicDir.setObjectName("groupBoxMusicDir")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBoxMusicDir)
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEditMusicDir = QtWidgets.QLineEdit(self.groupBoxMusicDir)
        self.lineEditMusicDir.setObjectName("lineEditMusicDir")
        self.horizontalLayout.addWidget(self.lineEditMusicDir)
        self.pushButtonSelectMusicDir = QtWidgets.QPushButton(self.groupBoxMusicDir)
        self.pushButtonSelectMusicDir.setObjectName("pushButtonSelectMusicDir")
        self.horizontalLayout.addWidget(self.pushButtonSelectMusicDir)
        self.verticalLayout_6.addWidget(self.groupBoxMusicDir)
        self.groupBoxContent = QtWidgets.QGroupBox(MusicManager)
        self.groupBoxContent.setObjectName("groupBoxContent")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBoxContent)
        self.verticalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lineEditFilter = QtWidgets.QLineEdit(self.groupBoxContent)
        self.lineEditFilter.setObjectName("lineEditFilter")
        self.verticalLayout_4.addWidget(self.lineEditFilter)
        self.treeView = QtWidgets.QTreeView(self.groupBoxContent)
        self.treeView.setObjectName("treeView")
        self.verticalLayout_4.addWidget(self.treeView)
        self.verticalLayout_6.addWidget(self.groupBoxContent)
        self.groupBoxActions = QtWidgets.QGroupBox(MusicManager)
        self.groupBoxActions.setObjectName("groupBoxActions")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBoxActions)
        self.verticalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayoutAction = QtWidgets.QVBoxLayout()
        self.verticalLayoutAction.setObjectName("verticalLayoutAction")
        self.labelAction = QtWidgets.QLabel(self.groupBoxActions)
        self.labelAction.setObjectName("labelAction")
        self.verticalLayoutAction.addWidget(self.labelAction)
        self.comboBoxAction = QtWidgets.QComboBox(self.groupBoxActions)
        self.comboBoxAction.setObjectName("comboBoxAction")
        self.comboBoxAction.addItem("")
        self.comboBoxAction.addItem("")
        self.verticalLayoutAction.addWidget(self.comboBoxAction)
        self.horizontalLayout_3.addLayout(self.verticalLayoutAction)
        self.verticalLayoutVa = QtWidgets.QVBoxLayout()
        self.verticalLayoutVa.setObjectName("verticalLayoutVa")
        self.checkBoxVa = QtWidgets.QCheckBox(self.groupBoxActions)
        self.checkBoxVa.setObjectName("checkBoxVa")
        self.verticalLayoutVa.addWidget(self.checkBoxVa)
        self.lineEditVaName = QtWidgets.QLineEdit(self.groupBoxActions)
        self.lineEditVaName.setObjectName("lineEditVaName")
        self.verticalLayoutVa.addWidget(self.lineEditVaName)
        self.horizontalLayout_3.addLayout(self.verticalLayoutVa)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayoutButton = QtWidgets.QVBoxLayout()
        self.verticalLayoutButton.setObjectName("verticalLayoutButton")
        self.pushButtonGo = QtWidgets.QPushButton(self.groupBoxActions)
        self.pushButtonGo.setObjectName("pushButtonGo")
        self.verticalLayoutButton.addWidget(self.pushButtonGo)
        self.pushButtonCancel = QtWidgets.QPushButton(self.groupBoxActions)
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.verticalLayoutButton.addWidget(self.pushButtonCancel)
        self.horizontalLayout_3.addLayout(self.verticalLayoutButton)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.horizontalLayoutMounted = QtWidgets.QHBoxLayout()
        self.horizontalLayoutMounted.setObjectName("horizontalLayoutMounted")
        self.labelMountedFlash = QtWidgets.QLabel(self.groupBoxActions)
        self.labelMountedFlash.setObjectName("labelMountedFlash")
        self.horizontalLayoutMounted.addWidget(self.labelMountedFlash)
        self.comboBoxMountedFlash = QtWidgets.QComboBox(self.groupBoxActions)
        self.comboBoxMountedFlash.setObjectName("comboBoxMountedFlash")
        self.horizontalLayoutMounted.addWidget(self.comboBoxMountedFlash)
        self.horizontalLayoutMounted.setStretch(1, 1)
        self.verticalLayout_5.addLayout(self.horizontalLayoutMounted)
        self.verticalLayout_6.addWidget(self.groupBoxActions)

        self.retranslateUi(MusicManager)
        QtCore.QMetaObject.connectSlotsByName(MusicManager)

    def retranslateUi(self, MusicManager):
        _translate = QtCore.QCoreApplication.translate
        MusicManager.setWindowTitle(_translate("MusicManager", "MusicManager"))
        self.groupBoxMusicDir.setTitle(_translate("MusicManager", "Music dir"))
        self.lineEditMusicDir.setPlaceholderText(_translate("MusicManager", "Select music dir..."))
        self.pushButtonSelectMusicDir.setText(_translate("MusicManager", "Select..."))
        self.groupBoxContent.setTitle(_translate("MusicManager", "Content"))
        self.lineEditFilter.setPlaceholderText(_translate("MusicManager", "Filter by name"))
        self.groupBoxActions.setTitle(_translate("MusicManager", "Actions"))
        self.labelAction.setText(_translate("MusicManager", "Action"))
        self.comboBoxAction.setItemText(0, _translate("MusicManager", "Write tags"))
        self.comboBoxAction.setItemText(1, _translate("MusicManager", "Copy to car flash"))
        self.checkBoxVa.setText(_translate("MusicManager", "Various artist"))
        self.lineEditVaName.setPlaceholderText(_translate("MusicManager", "Artist name"))
        self.pushButtonGo.setText(_translate("MusicManager", "Go"))
        self.pushButtonCancel.setText(_translate("MusicManager", "Cancel"))
        self.labelMountedFlash.setText(_translate("MusicManager", "Mounted flash"))

