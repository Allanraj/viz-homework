#!/usr/bin/env python3

import os

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns
import plotly.express as px

# Loading dataset
df = pd.read_csv('data/TSLA.csv',
                 sep=',',
                 header=0)

# Creating figure
os.makedirs('plots/TSLA-matplotlib_multiple_plot_axes', exist_ok=True)

plt.style.use("ggplot")

fig, axes = plt.subplots(1, 1, figsize=(5, 5))

# plot multiple plots on the same axes, to get some perspective on their comparisons
# axes.scatter(df['Date'], df['Close'], alpha=0.2, label='Close', s= 0.4, color='red')
# axes.scatter(df['Date'], df['High'], alpha=0.2, label='High', s= 0.4, color='blue')
# axes.scatter(df['Date'], df['Low'], alpha=0.2, label='Low', s= 0.4, color='green')
#
# axes.set_xlabel('Date')
# axes.set_ylabel('Close Stocks')
# axes.set_title(f'Stocks comparisons')
# axes.legend()
# plt.savefig(f'plots/TSLA-matplotlib_multiple_plot_axes/multiplot_scatter.png', dpi=300)
#
# plt.close()

# plot multiple plots on the same axes, to get some perspective on their comparisons

# axes.scatter(df['High'], df['Low'], s=(df['High']) ** 0.5,
#              label=f'High Vs Low', color='orange', marker='o', edgecolors='w', alpha=0.7)
#
# axes.set_xlabel('High')
# axes.set_ylabel('Low')
# axes.set_title(f'Stocks comparisons')
#
# axes.legend()
# plt.savefig(f'plots/TSLA-matplotlib_multiple_plot_axes/multiplot_scatter_with_size.png', dpi=300)
# plt.close()

# Example of creating a 3D plot
# fig = plt.figure()
# axes = fig.add_subplot(1, 1, 1, projection='3d')
#
# High = df['High']
# Low = df['Low']
# Close = df['Close']
# #axes.legend (High, Low, Close)
# axes.set_xlabel('High')
# axes.set_ylabel('Low')
# axes.set_zlabel('Close')
# axes.scatter (High, Low, Close)
# plt.savefig('plots/TSLA-matplotlib_multiple_plot_axes/TSLA_3d.png')
#
# plt.close()
#
# #plotting the data using seaborn
#
# sns.pairplot(df[["Open", "High", "Close", "Volume"]], diag_kind="kde")
# plt.savefig('plots/TSLA-matplotlib_multiple_plot_axes/TSLA_seaborngrid.png')
# plt.close()
#
# #using plotly
fig = px.line(df, x='Date', y='Close')
fig.show()
#fig.write_image('plots/TSLA-matplotlib_multiple_plot_axes/TSLA_plotly.png')

