# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 14:12:04 2024

@author: Owner
"""

from PIXIS_PICAM import *


try:
    images = cam1.grab(10)
    for image in images:
        plt.imshow(image)
        plt.colorbar()
        plt.show()  
        
    cam1.close()
except:
    cam1.close()
