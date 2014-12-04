__author__ = 'destr'

import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtCore import QSettings
from PyQt5.QtWidgets import QDialog, QApplication
from ui_musicmanager import Ui_MusicManager

class MusicManager(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.ui = Ui_MusicManager()
        self.ui.setupUi(self)

        self.ui.pushButtonCancel.clicked.connect(self.cancel)

    def closeEvent(self, event):
        print("CloseEvent")

    def cancel(self):
        print("Cancel")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    QCoreApplication.setApplicationName("MusicManager")
    QCoreApplication.setOrganizationName("destr")
    QSettings.setDefaultFormat(QSettings.IniFormat)
    mm = MusicManager()
    mm.show()
    sys.exit(app.exec_())

