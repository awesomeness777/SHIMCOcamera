# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 11:57:58 2024

@author: hayde
"""
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def load_bin_file(file_path, num_frames, frame_width, frame_height):
    with open(file_path, 'rb') as f:
        data = np.fromfile(f, dtype=np.uint16)
    return data.reshape((num_frames, frame_height, frame_width))

arr = load_bin_file('frames_0009.bin', 1, 1024, 1024)

plt.imshow(arr[0,:,:])
plt.colorbar()
plt.show()

# Create the histogram values for y
y_hist_values = arr.sum(axis=0)

# Create the histogram values for x
x_hist_values = arr.sum(axis=1)

# Create the figure and grid layout
fig = plt.figure(figsize=(8, 8))
grid = plt.GridSpec(3, 3, hspace=0.5, wspace=0.5)

# Add the heatmap in the center
ax_center = fig.add_subplot(grid[1:, :2])
sns.heatmap(arr, ax=ax_center, cbar=False, xticklabels=False, yticklabels=False)
ax_center.set_title('Heatmap')

# Add a black border around the heatmap using axes spines
for spine in ax_center.spines.values():
    spine.set_visible(True)
    spine.set_edgecolor('black')
    spine.set_linewidth(1)

# Add the x bar plot on top of the heatmap using Matplotlib
ax_top = fig.add_subplot(grid[0, :2])
ax_top.bar(np.linspace(1, 1024, 1024), x_hist_values, width=1.0)
ax_top.set_title('X Intensity')
#ax_top.set_ylim(995, 1020)
#ax_top.set_xlim(0, 1024)

# Add the y bar plot to the right of the heatmap using Matplotlib
ax_right = fig.add_subplot(grid[1:, 2])
ax_right.barh(np.linspace(1, 1024, 1024), y_hist_values, height=1.0,)
ax_right.set_title('Y Intensity')
#ax_right.set_xlim(995, 1020)
#ax_right.set_ylim(0, 1024)

# Show the combined figure
plt.show()