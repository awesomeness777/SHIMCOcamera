# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 14:12:04 2024

@author: Owner
"""

import pylablib as pll
import matplotlib.pyplot as plt
import numpy as np
pll.par["devices/dlls/picam"] = "C:\\Program Files\\Princeton Instruments\\PICam\\Runtime\\Picam.dll"
from pylablib.devices import PrincetonInstruments
print(PrincetonInstruments.list_cameras())

try:
    cam1 = PrincetonInstruments.PicamCamera('0809080002')
    #print(cam1.get_attribute_value("Pixel Format"))  # get the current pixel format
    cam1.set_attribute_value("Exposure Time", 2.5)  # set the exposure time to 10 ms
    #print(cam1.get_attribute_value("Exposure Time"))
    #print(cam1.get_all_attributes(copy=False))
    images = cam1.grab(10)
    for image in images:
        plt.imshow(image)
        plt.colorbar()
        plt.show()  
        
    cam1.close()
except:
    cam1.close()
