''' Data science skills and employment analysis '''
# Python 3.10.5
# Author: Sabneet Bains
# Date: 08-01-2022
# Version: 0.1
# Description: This script allows users to interactively plot histograms based on each
             # data science skill and the corresponding job recruitment boolean: Yes or No.
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.widgets import RadioButtons

# Read data from csv file
df = pd.read_csv('Data3.csv')

# Separate data into yes and no
yes = df[df["Job"] == "Yes"]
no = df[df["Job"] == "No"]

# Create figure and axes
fig, ax = plt.subplots(figsize=(11, 7))
plt.subplots_adjust(left=0.3)
plt.ylim(0, 20)
fig.text(0.02, 0.47, 'Job = Yes', rotation=90, size=12, color='green')
fig.text(0.02, 0.2, 'Job = No', rotation=90, size=12, color='red')

# Create radio buttons for filtering data
skill_selector = RadioButtons(plt.axes([0.05, 0.7, 0.15, 0.2]), ('Python', 'Sql', 'ML', 'Tableau', 'Excel'), activecolor='k')

# Filtering logic
def plot_by_skill(label):
    'Logic to plot by skill'
    ax.cla()
    ax.set_title('Distribution of Job Recruitment by skills in ' + label)
    ax.set_xlabel('Normalized Score')
    ax.set_ylabel('Count')

    if label == 'Python':
        ax.hist(yes.Python, color='green', alpha=0.5, histtype='step', fill=False)
        ax.hist(no.Python, color='red', alpha=0.5, histtype='step', fill=False)

        fig.text(0.05, 0.42, yes.Python.describe().to_string(), {'multialignment':'right'},
        size=11.4, bbox=dict(boxstyle="round", ec=(0.5, 1, 0.5), fc=(0.8, 1, 0.8)))

        fig.text(0.05, 0.15, no.Python.describe().to_string(), {'multialignment':'right'},
        size=12, bbox=dict(boxstyle="round", ec=(1, 0.5, 0.5), fc=(1, 0.8, 0.8)))

    elif label == 'Sql':
        ax.hist(yes.Sql, color='green', alpha=0.5, histtype='step', fill=False)
        ax.hist(no.Sql, color='red', alpha=0.5, histtype='step', fill=False)

        fig.text(0.05, 0.42, yes.Sql.describe().to_string(), {'multialignment':'right'},
        size=11.4, bbox=dict(boxstyle="round", ec=(0.5, 1, 0.5), fc=(0.8, 1, 0.8)))

        fig.text(0.05, 0.15, no.Sql.describe().to_string(), {'multialignment':'right'},
        size=12, bbox=dict(boxstyle="round", ec=(1, 0.5, 0.5), fc=(1, 0.8, 0.8)))

    elif label == 'ML':
        ax.hist(yes.ML, color='green', alpha=0.5, histtype='step', fill=False)
        ax.hist(no.ML, color='red', alpha=0.5, histtype='step', fill=False)

        fig.text(0.05, 0.42, yes.ML.describe().to_string(), {'multialignment':'right'},
        size=11.4, bbox=dict(boxstyle="round", ec=(0.5, 1, 0.5), fc=(0.8, 1, 0.8)))

        fig.text(0.05, 0.15, no.ML.describe().to_string(), {'multialignment':'right'},
        size=12, bbox=dict(boxstyle="round", ec=(1, 0.5, 0.5), fc=(1, 0.8, 0.8)))

    elif label == 'Tableau':
        ax.hist(yes.Tableau, color='green', alpha=0.5, histtype='step', fill=False)
        ax.hist(no.Tableau, color='red', alpha=0.5, histtype='step', fill=False)

        fig.text(0.05, 0.42, yes.Tableau.describe().to_string(), {'multialignment':'right'},
        size=11.4, bbox=dict(boxstyle="round", ec=(0.5, 1, 0.5), fc=(0.8, 1, 0.8)))

        fig.text(0.05, 0.15, no.Tableau.describe().to_string(), {'multialignment':'right'},
        size=12, bbox=dict(boxstyle="round", ec=(1, 0.5, 0.5), fc=(1, 0.8, 0.8)))

    elif label == 'Excel':
        ax.hist(yes.Excel, color='green', alpha=0.5, histtype='step', fill=False)
        ax.hist(no.Excel, color='red', alpha=0.5, histtype='step', fill=False)

        fig.text(0.05, 0.42, yes.Excel.describe().to_string(), {'multialignment':'right'},
        size=11.4, bbox=dict(boxstyle="round", ec=(0.5, 1, 0.5), fc=(0.8, 1, 0.8)))

        fig.text(0.05, 0.15, no.Excel.describe().to_string(), {'multialignment':'right'},
        size=12, bbox=dict(boxstyle="round", ec=(1, 0.5, 0.5), fc=(1, 0.8, 0.8)))

    ax.set_ylim(0, 20)
    plt.draw()

# Callback function for radio buttons
skill_selector.on_clicked(plot_by_skill)

# Clean up plot
for pos in ['top', 'right']:
    ax.spines[pos].set_visible(False)

# Show plot
plot_by_skill('Python')
plt.show()
