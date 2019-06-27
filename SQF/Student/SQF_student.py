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

path = os.path.join("..", "Data")

def main():

    print()

    # read csv file onto df
    df = pd.read_csv(os.path.join(path, 'march_2010.csv'))

    # call pie_chart(df, column)
    

    # list of columns to revert to binary
    cols_to_change = ["offunif", "frisked", "ac_rept", "ac_inves", "ac_proxm" , 
        "cs_objcs", "cs_descr", "cs_casng", "cs_lkout", "cs_cloth", "cs_drgtr", 
        "ac_evasv", "ac_assoc", "cs_furtv", "ac_cgdir", "cs_vcrim", "cs_bulge", 
        "cs_other", "ac_incid", "ac_time", "ac_stsnd", "ac_other", "sex", "inout"]

    # call binary(columns)
    

    # print find_proportions(...)
    

    # print find_mean(...)
    

    # lists for plotting
    race_proportions = []
    race_means = []

    # loop for plotting
    for race in df["race"].unique():
        race_proportions += [find_proportions(df, "frisked", race)]
        race_means += [find_mean(df, "age", race)]

    # uncomment this block to use plot_proportions
    # plot_proportions(race_proportions, df["race"].unique(), df["frisked"].unique(), xlabel = "race", ylabel = "proportion frisked", title = "frisked")

    # uncomment this block to use plot_means
    # plot_means(race_means, df["race"].unique(), xlabel = "race", ylabel = "age", title = "age")

def pie_chart(df, column):
    """
    Input:

    Output:
    """
    plt.axis('equal') 
    ### ========== TODO : Question 1 ========== ###
        # part a: create a pie chart
    
    pass

    ### ========== TODO : END ========== ###
    

def binary(df, columns):
    """
    Input:

    Output:
    """
    ### ========== TODO : Question 3 ========== ###
    # change all the Y/N entries to binary, as well as the entries of 2 other columns
    
    pass

    ### ========== TODO : END ========== ###

    

def find_proportions(df, column, race = None):
    """
    Input:

    Output:
    """
    # Drop rows with nan entries for column
    df = df.dropna(subset=[column])

    # Filter by race if provided
    if race:
        ### ========== TODO : Question 3 ========== ###
        # part c: race filtering

        pass

        ### ========== TODO : END ========== ###
            
    df_col = df[column]

    ### ========== TODO : Question 3 ========== ###
    # part a: proportions

    proportions = pd.Series()

    ### ========== TODO : END ========== ###

    return proportions

def find_mean(df, column, race = None):
    """
    Input:

    Output:
    """
    # Drop rows with nan entries for column
    df = df.dropna(subset=[column])

    if race:
        ### ========== TODO : Question 3 ========== ###
        # part c: race filtering

        pass

        ### ========== TODO : END ========== ###    
    
    df_col = df[column].astype(float)

    ### ========== TODO : Question 3 ========== ###
    # part b: mean

    mean = 0.0

    ### ========== TODO : END ========== ###

    return mean

def plot_proportions(figures, xlabels, bar_labels, xlabel = None, ylabel = None, title = None):
    """
    Input:

    Output:
    """
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
    """
    Input:

    Output:
    """
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

# --------------------------------- END --------------------------------- #

if __name__ == "__main__":
    main()