from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog
from Ui_mainui import Ui_Dialog

class Dialog(QDialog,  Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self,  parent = None):
        super(Dialog, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_okbtn_clicked(self):
        a = self.intxt.toPlainText()
        self.outtxt.setText(a)

if __name__ == "__main__":
    import sys
    from PyQt5 import QtWidgets

    app = QtWidgets.QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec_())
