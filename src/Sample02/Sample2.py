'''YouTube Subscribers Analysis '''
# Python 3.10.5
# Author: Sabneet Bains
# Date: 08-01-2022
# Version: 0.1
# Description: This script allows users to interactively plot pie charts based on the
             # top YouTube categories or countries by subscriber shrare.
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.widgets import RadioButtons

# Read data from csv file
df = pd.read_csv('Data2.csv')

# Create figure and axes
fig, ax = plt.subplots(figsize=(12, 7))
plt.subplots_adjust(left=0.2, bottom=0.2)

# Create radio buttons for filtering data
selector = RadioButtons(plt.axes([0.05, 0.7, 0.1, 0.2]), ('By Category', 'By Country'),
                        activecolor='red')

# Helper functions
def clean_labels(patches, texts, pcts):
    'Automatically colors and orients labels'
    for i, patch in enumerate(patches):
        if int(pcts[i].get_text()[:-1]) > 10:
            plt.setp(pcts[i], color="white", fontsize=20, fontweight='bold')
            plt.setp(texts[i], color=patch.get_facecolor(), fontsize=13, fontweight='bold')
        
        elif int(pcts[i].get_text()[:-1]) > 9:
            plt.setp(pcts[i], color="white", fontsize=16, fontweight='bold')
            plt.setp(texts[i], color=patch.get_facecolor(), fontsize=12, fontweight='bold')
        
        elif int(pcts[i].get_text()[:-1]) > 3:
            plt.setp(pcts[i], color="white", fontsize=12, fontweight='bold')
            plt.setp(texts[i], color=patch.get_facecolor(), fontsize=11, fontweight='bold')
        
        elif int(pcts[i].get_text()[:-1]) > 1:
            plt.setp(pcts[i], color="white", fontsize=9, fontweight='bold')
            plt.setp(texts[i], color=patch.get_facecolor(), fontsize=10, fontweight='bold')
        
        elif int(pcts[i].get_text()[:-1]) < 2:
            plt.setp(pcts[i], color="white", fontsize=5, fontweight='bold')
            plt.setp(texts[i], color=patch.get_facecolor(), fontsize=7, fontweight='bold')

# Fitering logic
def plot_by(label):
    'Logic to plot by one of the filters'
    ax.cla()

    if label == 'By Category':
        patches, texts, pcts = ax.pie(df.Category.value_counts(), labels=df.Category.value_counts().index, autopct='%1.0f%%',
        pctdistance=0.8, labeldistance=1.05, wedgeprops={"alpha":0.7, "linewidth": 1, "edgecolor": "white"}, rotatelabels=True)
        ax.set_title('Most subscribed YouTube categories', fontsize=20)
        clean_labels(patches, texts, pcts)

    elif label == 'By Country':
        patches, texts, pcts = ax.pie(df.Country.value_counts(), labels=df.Country.value_counts().index, autopct='%1.0f%%',
        pctdistance=0.8, labeldistance=1.05, wedgeprops={"alpha":0.7, "linewidth": 1, "edgecolor": "white"}, rotatelabels=True)
        ax.set_title('Countries with most YouTube subscribers', fontsize=20)
        clean_labels(patches, texts, pcts)

    plt.draw()

# Callback function for radio buttons
selector.on_clicked(plot_by)

# Show plot
plot_by('By Category')
plt.show()
