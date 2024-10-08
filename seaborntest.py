# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 15:46:34 2024

@author: Owner
"""

# Import seaborn
import seaborn as sns
import matplotlib as plt
import numpy as np

# Apply the default theme
sns.set_theme()

# Load an example dataset
random_array = np.random.rand(1024, 1024)
sns.heatmap(random_array)

xvalue = input("Choose an x-value ")
yvalue = input("Choose a y-value ")