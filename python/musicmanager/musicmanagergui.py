__author__ = 'destr'

import sys
import os

from PyQt5.QtCore import QCoreApplication, QByteArray
from PyQt5.QtCore import QSettings
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QHeaderView
from ui_musicmanager import Ui_MusicManager

from checkablefilesystemmodel import CheckableFileSystemModel

class MusicManager(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.ui = Ui_MusicManager()
        self.ui.setupUi(self)

        self.existingdirs = list()

        self.model = CheckableFileSystemModel(self.ui.treeView)
        self.ui.treeView.setModel(self.model)
        self.ui.treeView.hideColumn(1)
        self.ui.treeView.hideColumn(2)
        self.ui.treeView.header().setSectionResizeMode(QHeaderView.ResizeToContents)

        self.ui.widgetMusicDir.setPlaceholderText("Select music dir...")
        self.ui.widgetMusicDir.setTitle("Music dir")
        self.ui.widgetMusicDir.directorySelected.connect(self.setDir)

        self.ui.widgetFlashDir.setPlaceholderText("Select flash dir...")
        self.ui.widgetFlashDir.setTitle("Flash dir")
        self.ui.widgetFlashDir.directorySelected.connect(self.setFlashDir)

        self.ui.comboBoxAction.currentIndexChanged.connect(self.actionChanged)

        self.ui.pushButtonCancel.clicked.connect(self.cancel)

        self.__loadSettings()

        self.actionChanged(0)

    def setDir(self, value):
        self.model.setRootPath(value)
        self.ui.treeView.setRootIndex(self.model.index(value))

    def setFlashDir(self, value):
        valuelen = len(value) + 1
        for root, dirs, files in os.walk(value):
            subroot = root[valuelen:]
            self.existingdirs.append(subroot)
            for file in files:
                self.existingdirs.append("{0}/{1}".format(subroot, file))

        self.model.setExistingDirs(value, self.existingdirs)


    def actionChanged(self, index):
        en = index != 0
        self.ui.widgetFlashDir.setEnabled(en)

    def closeEvent(self, event):
        self.__saveSettings()

    def cancel(self):
        self.close()

    def selectMusicDir(self):
        path = QFileDialog.getExistingDirectory(self, "Select music dir", os.path.expanduser('~'))
        if path:
            self.ui.lineEditMusicDir.setText(path)

    def __saveSettings(self):
        sets = QSettings()
        sets.beginGroup("MusicManager")
        sets.setValue("geometry", self.saveGeometry())
        sets.endGroup()

        self.ui.widgetMusicDir.saveSettings(sets)
        self.ui.widgetFlashDir.saveSettings(sets)

    def __loadSettings(self):
        sets = QSettings()
        sets.beginGroup("MusicManager")
        self.restoreGeometry(sets.value("geometry", QByteArray()))
        sets.endGroup()
        self.ui.widgetMusicDir.loadSettings(sets)
        self.ui.widgetFlashDir.loadSettings(sets)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    QCoreApplication.setApplicationName("MusicManager")
    QCoreApplication.setOrganizationName("destr")
    QSettings.setDefaultFormat(QSettings.IniFormat)
    mm = MusicManager()
    mm.show()
    sys.exit(app.exec_())

