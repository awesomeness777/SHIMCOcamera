# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 14:12:04 2024

@author: Owner
"""

import pylablib as pll
pll.par["devices/dlls/picam"] = "path/to/dlls"
from pylablib.devices import PrincetonInstruments
cam1 = PrincetonInstruments.PicamCamera('number')
cam1.get_attribute_value("Pixel Format")  # get the current pixel format
cam1.set_attribute_value("Exposure Time", 10)  # set the exposure time to 10 ms
cam1.get_attribute_value("Exposure Time")
cam1.get_all_attributes(copy=False)
