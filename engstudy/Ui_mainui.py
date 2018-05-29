# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\pythonfile\PythonFile\engstudy\mainui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(742, 479)
        Dialog.setSizeGripEnabled(True)
        self.okbtn = QtWidgets.QPushButton(Dialog)
        self.okbtn.setGeometry(QtCore.QRect(170, 210, 141, 51))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        self.okbtn.setFont(font)
        self.okbtn.setObjectName("okbtn")
        self.clrbtn = QtWidgets.QPushButton(Dialog)
        self.clrbtn.setGeometry(QtCore.QRect(420, 210, 141, 51))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        self.clrbtn.setFont(font)
        self.clrbtn.setObjectName("clrbtn")
        self.intxt = QtWidgets.QTextEdit(Dialog)
        self.intxt.setGeometry(QtCore.QRect(60, 60, 611, 87))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(20)
        self.intxt.setFont(font)
        self.intxt.setObjectName("intxt")
        self.quitbtn = QtWidgets.QPushButton(Dialog)
        self.quitbtn.setGeometry(QtCore.QRect(590, 210, 101, 51))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        self.quitbtn.setFont(font)
        self.quitbtn.setObjectName("quitbtn")
        self.outtxt = QtWidgets.QTextEdit(Dialog)
        self.outtxt.setGeometry(QtCore.QRect(60, 330, 621, 87))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(18)
        self.outtxt.setFont(font)
        self.outtxt.setObjectName("outtxt")

        self.retranslateUi(Dialog)
        self.clrbtn.clicked.connect(self.intxt.clear)
        self.quitbtn.clicked.connect(Dialog.close)
        self.clrbtn.clicked.connect(self.outtxt.clear)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.intxt, self.okbtn)
        Dialog.setTabOrder(self.okbtn, self.outtxt)
        Dialog.setTabOrder(self.outtxt, self.clrbtn)
        Dialog.setTabOrder(self.clrbtn, self.quitbtn)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.okbtn.setText(_translate("Dialog", "确定"))
        self.clrbtn.setText(_translate("Dialog", "清除"))
        self.intxt.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'新宋体\'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.quitbtn.setText(_translate("Dialog", "退出"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

