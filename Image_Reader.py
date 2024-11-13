# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 20:26:28 2024

@author: hayde
"""

import numpy as np
import matplotlib.pyplot as plt

def display_image(filepath):
    # Load the data from the text file
    data = np.loadtxt(filepath)
    
    # Display the data as an image
    plt.imshow(data, cmap='Blues', interpolation='nearest')
    plt.colorbar()
    plt.title("Image")
    plt.show()

display_image("C:\\Program Files\\Princeton Instruments\\PICam\\Images\\2024-11-12_20-15-33.txt")