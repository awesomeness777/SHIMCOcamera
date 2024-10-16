import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# Define Gaussian function
sigma = 5
x, y = np.meshgrid(np.linspace(-1, 1, 1024), np.linspace(-1, 1, 1024))
gaussian = np.exp(-(x**2 + y**2) / (2 * sigma**2))

# Create the histogram values for y
y_hist_values = gaussian.sum(axis=0)

# Create the histogram values for x
x_hist_values = gaussian.sum(axis=1)

cmap = cm.get_cmap("Blues")
darkest_blue = cmap(1.0)

# Create the figure and grid layout
fig = plt.figure(figsize=(8, 8))
grid = plt.GridSpec(3, 3, hspace=0.5, wspace=0.5)

# Add the Gaussian heatmap in the center
ax_center = fig.add_subplot(grid[1:, :2])
sns.heatmap(gaussian, ax=ax_center, cmap="Blues", cbar=False, xticklabels=False, yticklabels=False)
ax_center.set_title('Gaussian Heatmap')

# Add a black border around the heatmap using axes spines
for spine in ax_center.spines.values():
    spine.set_visible(True)
    spine.set_edgecolor('black')
    spine.set_linewidth(1)

# Add the x bar plot on top of the heatmap using Matplotlib
ax_top = fig.add_subplot(grid[0, :2])
ax_top.bar(np.linspace(1, 1024, 1024), x_hist_values, width=1.0, color=darkest_blue)  # Use the extracted color
ax_top.set_title('X Intensity')
ax_top.set_ylim(995, 1020)
ax_top.set_xlim(0, 1024)

# Add the y bar plot to the right of the heatmap using Matplotlib
ax_right = fig.add_subplot(grid[1:, 2])
ax_right.barh(np.linspace(1, 1024, 1024), y_hist_values, height=1.0, color=darkest_blue)  # Use the extracted color
ax_right.set_title('Y Intensity')
ax_right.set_xlim(995, 1020)
ax_right.set_ylim(0, 1024)

# Show the combined figure
plt.show()
