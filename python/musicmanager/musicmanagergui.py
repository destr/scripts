__author__ = 'destr'

import sys
import os

from PyQt5.QtCore import QCoreApplication, QByteArray
from PyQt5.QtCore import QSettings
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from ui_musicmanager import Ui_MusicManager

from checkablefilesystemmodel import CheckableFileSystemModel

class MusicManager(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.ui = Ui_MusicManager()
        self.ui.setupUi(self)

        self.model = CheckableFileSystemModel(self.ui.treeView)
        self.ui.treeView.setModel(self.model)

        self.ui.pushButtonCancel.clicked.connect(self.cancel)
        self.ui.pushButtonSelectMusicDir.clicked.connect(self.selectMusicDir)
        self.ui.lineEditMusicDir.textChanged.connect(self.setDir)

        self.__loadSettings()

    def setDir(self, value):
        self.model.setRootPath(value)
        self.ui.treeView.setRootIndex(self.model.index(value))

    def closeEvent(self, event):
        self.__saveSettings()

    def cancel(self):
        print("Cancel")

    def selectMusicDir(self):
        path = QFileDialog.getExistingDirectory(self, "Select music dir", os.path.expanduser('~'))
        if path:
            self.ui.lineEditMusicDir.setText(path)

    def __saveSettings(self):
        sets = QSettings()
        sets.beginGroup("MusicManager")
        sets.setValue("geometry", self.saveGeometry())
        sets.setValue("musicdir", self.ui.lineEditMusicDir.text())
        sets.endGroup()

    def __loadSettings(self):
        sets = QSettings()
        sets.beginGroup("MusicManager")
        self.ui.lineEditMusicDir.setText(sets.value("musicdir"))
        self.restoreGeometry(sets.value("geometry", QByteArray()))
        sets.endGroup()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    QCoreApplication.setApplicationName("MusicManager")
    QCoreApplication.setOrganizationName("destr")
    QSettings.setDefaultFormat(QSettings.IniFormat)
    mm = MusicManager()
    mm.show()
    sys.exit(app.exec_())

