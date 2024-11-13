# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 13:18:52 2024

@author: hayde
"""
               
from PyQt5 import QtCore, QtWidgets
import threading
import time
import datetime
import os
import numpy as np

from PIXIS_PICAM import *   


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        
        # Pause Button
        self.pauseButton = QtWidgets.QPushButton(Form)
        self.pauseButton.setGeometry(QtCore.QRect(100, 130, 90, 50))
        self.pauseButton.setObjectName("pause")
        self.pauseButton.setText("Pause")
        self.pauseButton.clicked.connect(self.pauseCapture)
        self.pauseButton.setEnabled(False)
        
        # Resume Button
        self.resumeButton = QtWidgets.QPushButton(Form)
        self.resumeButton.setGeometry(QtCore.QRect(200, 130, 90, 50))
        self.resumeButton.setObjectName("resume")
        self.resumeButton.setText("Start")
        self.resumeButton.clicked.connect(self.resumeCapture)
        
        self.stopButton = QtWidgets.QPushButton(Form)
        self.stopButton.setGeometry(QtCore.QRect(155, 200, 90, 50))
        self.stopButton.setObjectName("stopButton")
        self.stopButton.setText("Stop")
        
        self.Exposure = QtWidgets.QSpinBox(Form)
        self.Exposure.setGeometry(QtCore.QRect(33, 70, 90, 22))
        self.Exposure.setObjectName("Exposure Time")
        self.Exposure.setMaximum(10000)
        self.Exposure.setValue(10)
        
        self.Frame = QtWidgets.QSpinBox(Form)
        self.Frame.setGeometry(QtCore.QRect(156, 70, 90, 22))
        self.Frame.setObjectName("Frame Period")
        self.Frame.setMaximum(10000)  
        self.Frame.setValue(20)
        
        self.Temperature = QtWidgets.QSpinBox(Form)
        self.Temperature.setGeometry(QtCore.QRect(289, 70, 90, 22))
        self.Temperature.setObjectName("Temperature")
        self.Temperature.setMaximum(10000) 
        self.Temperature.setMinimum(-100)
        self.Temperature.setValue(-70)  
        
        # Exposure Time Label
        self.exp = QtWidgets.QLabel(Form)
        self.exp.setGeometry(QtCore.QRect(33, 50, 90, 16))
        self.exp.setObjectName("Exp")
        
        # Frame Period Label
        self.Fp = QtWidgets.QLabel(Form)
        self.Fp.setGeometry(QtCore.QRect(156, 50, 90, 16))
        self.Fp.setObjectName("Fp")
        
        # Temperature Label
        self.Temp = QtWidgets.QLabel(Form)
        self.Temp.setGeometry(QtCore.QRect(289, 50, 90, 16))
        self.Temp.setObjectName("Temp")

        self.stopButton.clicked.connect(self.stopFunction)

        self.stop = False
        self.cam_open = True
        self.paused = True
        
        # Start the image capture thread
        self.capture_thread = threading.Thread(target=self.capture_images)
        self.capture_thread.start()
        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def stopFunction(self):
        self.stop = True
        self.cam_open = False

    def capture_images(self):
        while self.cam_open:
            if self.paused:
                time.sleep(1)
                continue
            
            if not self.stop:
                cam1.set_attribute_value('Exposure Time', self.Exposure.value())
                cam1.set_attribute_value('Frame Period', self.Frame.value())
                cam1.set_attribute_value('Temperature', self.Temperature.value())

                image = cam1.grab(1) 
                current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                filename = f"{current_time}.txt"
                file_path = os.path.join("C:\\Program Files\\Princeton Instruments\\PICam\\Images", filename)    
                np.savetxt(file_path, image, fmt="%s")
                
            else:
                break
            time.sleep(2)

    def pauseCapture(self):
        self.paused = True
        self.pauseButton.setEnabled(False)
        self.resumeButton.setEnabled(True)

    def resumeCapture(self):
        self.paused = False
        self.resumeButton.setEnabled(False)
        self.pauseButton.setEnabled(True)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.exp.setText(_translate("Form", "Exposure Time"))
        self.Fp.setText(_translate("Form","Frame Period"))
        self.Temp.setText(_translate("Form","Temperature"))
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())



