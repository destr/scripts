#coding:utf-8
__author__ = 'destr'

from PyQt5.QtWidgets import QWidget, QFileDialog
from PyQt5.QtCore import pyqtSignal, QSettings
from ui_dirselector import Ui_DirSelector

class DirSelector(QWidget):
    directorySelected = pyqtSignal(['QString'])

    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        self.ui = Ui_DirSelector()
        self.ui.setupUi(self)

        self.ui.pushButtonSelect.clicked.connect(self.selectDir)
        self.ui.lineEdit.textChanged.connect(self.directorySelected)

    def selectDir(self):
        dirname = QFileDialog.getExistingDirectory(self, self.ui.lineEdit.placeholderText())
        if dirname:
            self.ui.lineEdit.setText(dirname)

    def setTitle(self, title):
        self.ui.groupBox.setTitle(title)
        self.setObjectName(title)

    def setPlaceholderText(self, text):
        self.ui.lineEdit.setPlaceholderText(text)

    def saveSettings(self, sets):
        sets.beginGroup(self.objectName())
        sets.setValue("dir", self.ui.lineEdit.text())
        sets.endGroup()

    def loadSettings(self, sets):
        sets.beginGroup(self.objectName())
        self.ui.lineEdit.setText(sets.value("dir"))
        sets.endGroup()

