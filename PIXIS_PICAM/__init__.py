# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 15:29:38 2024

@author: Owner
"""

import matplotlib.pyplot as plt
import numpy as np
import pylablib as pll

#modify based on your path
pll.par["devices/dlls/picam"] = "C:\\Program Files\\Princeton Instruments\\PICam\\Runtime\\Picam.dll"

from pylablib.devices import PrincetonInstruments

print(PrincetonInstruments.list_cameras())

cam1 = PrincetonInstruments.PicamCamera('0809080002')

cam1.set_attribute_value('Exposure Time', 10)
