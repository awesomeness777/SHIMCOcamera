# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 12:07:46 2024

@author: hayde
"""

import numpy as np
import matplotlib.pyplot as plt

# Define Gaussian function
sigma = 5
x, y = np.meshgrid(np.linspace(-1, 1, 100), np.linspace(-1, 1, 100))
gaussian = np.exp(-(x**2 + y**2) / (2 * sigma**2))

# Create the histogram values for y
y_hist_values = []
for j in range(100):
    y_sum = 0
    for i in range(100):
        y_sum += gaussian[i, j]
    y_hist_values.append(y_sum)

# Create the histogram values for x
x_hist_values = []
for j in range(100):
    x_sum = 0
    for i in range(100):
        x_sum += gaussian[j, i]
    x_hist_values.append(x_sum)

# Create the figure and grid layout
fig = plt.figure(figsize=(8, 8))
grid = plt.GridSpec(3, 3, hspace=0.5, wspace=0.5)

# Add the Gaussian heatmap in the center
ax_center = fig.add_subplot(grid[1:, :2])
ax_center.imshow(gaussian, extent=[-1, 1, -1, 1])
ax_center.set_title('Gaussian Heatmap')

# Add the x bar plot on top of the heatmap
ax_top = fig.add_subplot(grid[0, :2])
ax_top.bar(np.linspace(1, 100, 100), x_hist_values, width=1.0, color = 'red')  # Use bar plot instead of line plot
ax_top.set_title('X Intensity')
ax_top.set_xlabel('X')
ax_top.set_ylabel('Intensity')

# Add the y bar plot to the right of the heatmap
ax_right = fig.add_subplot(grid[1:, 2])
ax_right.barh(np.linspace(1, 100, 100), y_hist_values, height=1.0, color = 'red')  # Use horizontal bar plot
ax_right.set_title('Y Intensity')
ax_right.set_xlabel('Intensity')
ax_right.set_ylabel('Y')

# Show the combined figure
plt.show()

