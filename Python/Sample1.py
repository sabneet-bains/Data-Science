''' Electric Vehicle Analysis '''
# Python 3.10.5
# Author: Sabneet Bains
# Date: 08-01-2022
# Version: 0.1
# Description: This script allows users to interactively plot bar charts based on the
             # category or manufacturer of electric vehicles in the US.
import textwrap
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import RadioButtons

# Read data from csv file
df = pd.read_csv('Data1.csv')

# Separate data by columns
column1 = np.append('All', df.Category.unique())
column2 = np.append('All', df.Model.unique())
column3 = np.append('All', df.Year.unique())
column4 = np.append('All', df.Manufacturer.unique())
column5 = np.append('All', df.Range.unique())

# Create figure and axes
fig, ax = plt.subplots(figsize=(20, 9))
plt.subplots_adjust(left=0.2, bottom=0.2)

# Create radio buttons for filtering data
category_selector = RadioButtons(plt.axes([0.05, 0.7, 0.1, 0.2]), column1, activecolor='k')
manufacturer_selector = RadioButtons(plt.axes([0.05, 0.1, 0.1, 0.6]), column4, activecolor='k')

# Helper functions
def wrap_labels(ax, width, break_long_words=False):
    'Automatically wrap labels'
    labels = []
    for label in ax.get_xticklabels():
        text = label.get_text()
        labels.append(textwrap.fill(text, width=width,
                      break_long_words=break_long_words))
    ax.set_xticklabels(labels)

def label_patches(ax):
    'Labels bar chart patches'
    for rect in ax.patches:
        height = rect.get_height()
        text = f'{height}'
        ax.text(rect.get_x() + rect.get_width() / 2, rect.get_y() + height,
         text, ha='center', va='bottom')

# Fitering logic
def plot_by_category(label):
    'Logic to plot by category'
    ax.cla()

    category = df[df["Category"] == label]
    manufacturer = manufacturer_selector.value_selected

    if label == 'All':
        ax.bar(df.Manufacturer, df.Range, linewidth=0.8, edgecolor="k", alpha=0.5)
        ax.set_title('Max Range of each Electric Vehicle available in the US')
        ax.set_xticks(df.Manufacturer.unique())
        ax.set_xticklabels(df.Manufacturer.unique())
        ax.set_xlabel('Manufacturer')
    else:
        if manufacturer == 'All':
            ax.bar(category.Manufacturer, category.Range, linewidth=0.8, edgecolor="k", alpha=0.5)
            ax.set_title('Max Range of each Electric ' + label + ' available in the US')
            ax.set_xticks(category.Manufacturer.unique())
            ax.set_xticklabels(category.Manufacturer.unique())
            ax.set_xlabel('Manufacturer')
        else:
            filtered_manufacturer = category[category["Manufacturer"] == manufacturer]
            ax.bar(filtered_manufacturer.Model, filtered_manufacturer.Range, linewidth=0.8, edgecolor="k", alpha=0.5)
            ax.set_title('Max Range of each Electric ' + manufacturer + ' ' + label + ' available in the US')
            ax.set_xticks(filtered_manufacturer.Model.unique())
            ax.set_xticklabels(filtered_manufacturer.Model.unique())
            ax.set_xlabel('Model')
            label_patches(ax)

    ax.set_ylabel('Max Range (miles)')
    wrap_labels(ax, 10)
    plt.draw()

def plot_by_manufacturer(label):
    'Logic to plot by manufacturer'
    ax.cla()
    manufacturer = df[df["Manufacturer"] == label]
    category = category_selector.value_selected

    if label == 'All':
        ax.bar(df.Manufacturer, df.Range, linewidth=0.8, edgecolor="k", alpha=0.5)
        ax.set_title('Max Range of each Electric Vehicle available in the US')
        ax.set_xticks(df.Manufacturer.unique())
        ax.set_xticklabels(df.Manufacturer.unique())
        ax.set_xlabel('Manufacturer')
    else:
        if category == 'All':
            ax.bar(manufacturer.Model, manufacturer.Range, linewidth=0.8, edgecolor="k", alpha=0.5)
            ax.set_title('Max Range of each Electric ' + label + ' available in the US')
            ax.set_xticks(manufacturer.Model.unique())
            ax.set_xticklabels(manufacturer.Model.unique())
            ax.set_xlabel('Model')
            label_patches(ax)
        else:
            filtered_category = manufacturer[manufacturer["Category"] == category]
            ax.bar(filtered_category.Model, filtered_category.Range, linewidth=0.8, edgecolor="k", alpha=0.5)
            ax.set_title('Max Range of each Electric ' + label + ' ' + category + ' available in the US')
            ax.set_xticks(filtered_category.Model.unique())
            ax.set_xticklabels(filtered_category.Model.unique())
            ax.set_xlabel('Model')
            label_patches(ax)

    ax.set_ylabel('Max Range (miles)')
    wrap_labels(ax, 10)
    plt.draw()

# Callback functions for radio buttons
category_selector.on_clicked(plot_by_category)
manufacturer_selector.on_clicked(plot_by_manufacturer)

# Clean up plot
ax.tick_params(axis='x', which='major', labelsize=7)
for pos in ['top', 'right']:
    ax.spines[pos].set_visible(False)

# Show plot
plot_by_category('All')
plt.show()
