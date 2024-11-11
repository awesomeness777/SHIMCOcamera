# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import time



class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.inputButton = QtWidgets.QPushButton(Form)
        self.inputButton.setGeometry(QtCore.QRect(60, 130, 93, 28))
        self.inputButton.setObjectName("inputButton")
        self.stopButton = QtWidgets.QPushButton(Form)
        self.stopButton.setGeometry(QtCore.QRect(240, 130, 93, 28))
        self.stopButton.setObjectName("stopButton")
        self.inputValue = QtWidgets.QSpinBox(Form)
        self.inputValue.setGeometry(QtCore.QRect(170, 130, 42, 22))
        self.inputValue.setObjectName("inputValue")
        self.inputButton.clicked.connect(self.testFunction(self.inputValue.value(), False))
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(160, 110, 71, 16))
        self.label.setObjectName("label")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        #self.stopButton.clicked.connect(break)

    def testFunction(self, number, stop):
        while(stop==False):
            print(number)
            time.sleep(2)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.inputButton.setText(_translate("Form", "Input"))
        self.stopButton.setText(_translate("Form", "Stop"))
        self.label.setText(_translate("Form", "Input value"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())