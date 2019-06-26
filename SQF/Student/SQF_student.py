"""
Author      : Huey Fields
Class       : HMC CS 181R
Date        : 2019 June 11
Description : SQF Data Analysis

Modifications made by Thomas Cintra
"""
# seaborn module
import seaborn as sns

# python modules
import os

# numpy module
import numpy as np

# pandas module
import pandas as pd

# matplotlib module
import matplotlib.pyplot as plt
from matplotlib import colors as mcolors

# --------------------------------- START --------------------------------- #

# TODO Read the DataFrame onto your python script
path = "../Data/"
df = None

### ========== TODO : Question 2 ========== ###

def binary(columns):
    # TODO Implement binary(columns)
    """
    Input:

    Output:
    """
    
### ========== TODO : END ========== ###


### ========== TODO : Question 3 ========== ###

def find_proportions(df, column, race = None):
    # TODO Implement find_proportions
    """
    Input:

    Output:
    """
    # Drop rows with nan entries for column
    df = df.dropna(subset=[column])

    # Filter by race if provided
    if race:
        # part c: race filtering

        pass

    df_col = df[column]
    # part a: proportions

    proportions = pd.Series()

    return proportions

def find_mean(df, column, race = None):
    # TODO Implement find_mean
    """
    Input:

    Output:
    """
    # Drop rows with nan entries for column
    df = df.dropna(subset=[column])

    if race:
        # part c: race filtering

        pass
    
    df_col = df[column].astype(float)
    # part b: mean

    mean = 0.0

    return mean

### ========== TODO : END ========== ###

def plot_proportions(figures, xlabels, bar_labels, xlabel = None, ylabel = None, title = None):
    # data to plot 
    n_groups = len(figures)

    # Get bars to plot
    bars = []

    for label in bar_labels:
        bars += [[x[label] if label in x.index else 0 for x in figures]]

    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

    # create plot 
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 1.0 / len(figures[0])
    opacity = 0.8

    for i in range(len(bars)):
        bar = bars[i]
        plt.bar(index + i * bar_width, bar, bar_width, alpha=opacity, color = colors[i % len(colors)], label = bar_labels[i])

    plt.title = title
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(index, xlabels)
    plt.legend()

    plt.tight_layout()
    plt.show()  

def plot_means(means, xlabels, xlabel = None, ylabel = None, title = None):
    # data to plot 
    n_groups = len(means)

    # create plot 
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 1.0
    opacity = 0.8

    plt.bar(index, means, bar_width, alpha=opacity, color = "steelblue", label = "mean")

    plt.title = title
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(index, xlabels)
    plt.legend()

    plt.tight_layout()
    plt.show()  

def main():
    print(find_proportions(df, "race"))
    print(find_mean(df, "weight"))
    
    """
    race_proportions = []
    race_means = []

    # TODO edit the for loop
    for race in df["race"].unique():
        race_proportions += [find_proportions(df, "frisked", race)]
        race_means += [find_mean(df, "age", race)]

    plot_proportions(race_proportions, df["race"].unique(), df["frisked"].unique(), \
        xlabel = "race", ylabel = "proportion frisked", title = "frisked")

    plot_means(race_means, df["race"].unique(), \
        xlabel = "race", ylabel = "age", title = "age")
    """

if __name__ == "__main__":
    main()


# --------------------------------- END --------------------------------- #