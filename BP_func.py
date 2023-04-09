
import pandas as pd
import seaborn as sns
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt

def sns_bp_func(df, col_nm, by_nm, size=(12,6), cols=['red', 'blue'], xlabel='x', ylabel='y', xticks=90, title='BoxPlot'):
    '''
    Function to create a boxplot of a column in a DataFrame by a specified column using Seaborn.
    
    Parameters:
        - df (pd.DataFrame): DataFrame for which to create the boxplot.
        - col_nm (str): Name of the column for which to create the boxplot.
        - by_nm (str): Name of the column to group by for the boxplot.
        - size (tuple): Size of the figure, default is (12,6), enter as a tuple.
        - cols (list): Colors of the mean and median lines, default is ['red', 'blue'], enter as a list.
        - xlabel (str): X-axis label, default is 'x', enter as a string.
        - ylabel (str): Y-axis label, default is 'y', enter as a string.
        - xticks (int): X-axis ticks rotation, default is 90, enter as an integer.
        - title (str): Title of the boxplot, default is 'Boxplot', enter as a string.
    '''

    # Create a boxplot of the ratings for each category using Seaborn
    plt.figure(figsize=size)
    sns.boxplot(data=df, x=by_nm, y=col_nm, showfliers=False, showmeans=True,
                meanline=True, meanprops={'color': cols[0]}, medianprops={'color': cols[1]})
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=xticks)
    plt.tight_layout()
    plt.show()
