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
x, y = np.meshgrid(np.linspace(-1, 1, 100), np.linspace(-1, 1, 100))
gaussian = np.exp(-(x**2 + y**2) / (2 * sigma**2))
plt.imshow(gaussian)
plt.show()

xvalue = int(input("Choose an x-value "))
yvalue = int(input("Choose a y-value "))

sns.jointplot(data=gaussian)

#X = 100
#Y = 100
#gaussianpd = pd.DataFrame({'xvalue': np.repeat(range(1, X + 1), Y),
#                  'yvalue': np.tile(range(Y), X),
#                   'Intensity': gaussian[int('xvalue'),int('yvalue')]})
# change the random gaussianpd to have some rows/columns stand out (debugging, checking)
#gaussianpd.loc[gaussianpd['yvalue'] == 10, 'Intensity'] = 0.5
#gaussianpd.loc[gaussianpd['yvalue'] == 12, 'Intensity'] = 0.34
#gaussianpd.loc[gaussianpd['xvalue'] == 20, 'Intensity'] = 0.78

#g = sns.jointplot(data=gaussianpd, x='xvalue', y='yvalue', kind='hist', bins=(X, Y))
#g.ax_marg_y.cla()
#g.ax_marg_x.cla()
#sns.heatmap(data=gaussianpd['Intensity'].to_numpy().reshape(X, Y).T, ax=g.ax_joint, cbar=False, cmap='Blues')

#g.ax_marg_y.barh(np.arange(0.5, Y), gaussianpd.groupby(['yvalue'])['Intensity'].sum().to_numpy(), color='navy')
#g.ax_marg_x.bar(np.arange(0.5, X), gaussianpd.groupby(['xvalue'])['Intensity'].sum().to_numpy(), color='navy')

#g.ax_joint.set_xticks(np.arange(0.5, X))
#g.ax_joint.set_xticklabels(range(1, X + 1), rotation=0)
#g.ax_joint.set_yticks(np.arange(0.5, Y))
#g.ax_joint.set_yticklabels(range(Y), rotation=0)

# remove ticks between heatmao and histograms
#g.ax_marg_x.tick_params(axis='x', bottom=False, labelbottom=False)
#g.ax_marg_y.tick_params(axis='y', left=False, labelleft=False)
# remove ticks showing the heights of the histograms
#g.ax_marg_x.tick_params(axis='y', left=False, labelleft=False)
#g.ax_marg_y.tick_params(axis='x', bottom=False, labelbottom=False)

#g.fig.set_size_inches(20, 8)  # jointplot creates its own figure, the size can only be changed afterwards
# g.fig.subplots_adjust(hspace=0.3) # optionally more space for the tick labels
#g.fig.subplots_adjust(hspace=0.05, wspace=0.02)  # less spaced needed when there are no tick labels
#plt.show()
