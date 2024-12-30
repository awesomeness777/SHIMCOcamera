# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 20:26:28 2024

@author: hayde
"""

import numpy as np
import matplotlib.pyplot as plt

def display_image(filepath):
    with open(filepath, 'rb') as f:
    # Load the data from the text file
        data = f.read()
        image_array = np.frombuffer(data, dtype=np.uint8).reshape((1024, 2048))
        # Display the data as an image
        plt.imshow(image_array, cmap='Blues', interpolation='nearest')
        plt.colorbar()
        plt.title("Image")
        plt.show()

display_image("C:\\Users\\Owner\\PICAM\\images\\None_2024-12-05_15-16-14.bin")
