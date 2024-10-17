# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 15:46:34 2024

@author: Owner
"""

# Import seaborn
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Apply the default theme
sns.set_theme()

# Load a random dataset
#random_array = np.random.rand(1024, 1024)
#sns.heatmap(random_array)

# Load a gaussian dataset using matplotlib
sigma = 5
x, y = np.meshgrid(np.linspace(-1, 1, 25), np.linspace(-1, 1, 25))
gaussian = np.exp(-(x**2 + y**2) / (2 * sigma**2))
plt.imshow(gaussian)
plt.show()

xvalue = int(input("Choose an x-value "))
yvalue = int(input("Choose a y-value "))

sns.jointplot(data=gaussian)
gaussianpd = pd.DataFrame(gaussian)


# Create an empty joint grid
grid = sns.JointGrid()

# Fill the centre with our heatmap
sns.heatmap(gaussianpd, ax=grid.ax_joint, cbar=False, cmap='mako')
# Draw total bars, both with width 1, but the Y one with horizontal orientation
sns.barplot(gaussianpd.sum(), ax=grid.ax_marg_x, width=1)
sns.barplot(gaussianpd.sum(axis=1), ax=grid.ax_marg_y, orient='h', width=1)
# Offset value (just half an unit)
_off = .5

# Fix x
_xmin, _xmax = grid.ax_joint.get_xlim()
grid.ax_joint.set_xlim(_xmin+_off, _xmax+_off)
for bar in grid.ax_marg_x.containers[0]:
    bar.set_x(bar.get_x() + _off)

# Fix y
_ymin, _ymax = grid.ax_joint.get_ylim()
grid.ax_joint.set_ylim(_ymin+_off, _ymax+_off)
for bar in grid.ax_marg_y.containers[0]:
    bar.set_y(bar.get_y() + _off)

# Need to use this to set the horizontal_alignment
grid.ax_joint.set_xticklabels(
    grid.ax_joint.get_xticklabels(), 
    rotation=30,    
    ha='right'
)
grid.ax_joint.yaxis.set_tick_params(rotation=0)

#grid.ax_joint.set_xlabel('Día de votación')
#grid.ax_joint.set_ylabel('Día de creación')