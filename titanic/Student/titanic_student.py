""" 
Author: Thomas Cintra and Yun Zhang
Class: CS 181R
Week 2 - Data Science Overview
Homework 1
Name:
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

# re module
import re

# --------------------------------- START --------------------------------- #

path = os.path.join("..", "Data")

def main():

    print()

    ### ========== TODO : Question 1 ========== ###

    # read the dataframe
    df = None

    ### ========== TODO : END ========== ###
    
    ### ========== TODO : Question 2 ========== ###

    # print missing values series

    # drop column
    

    ### ========== TODO : END ========== ###


    ### ========== TODO : Question 4 ========== ###

    # call age_categories(df)
    

    # call fare_categories(df)


    ### ========== TODO : END ========== ###

    ### ========== TODO : INTERMEDIARY ========== ##

    # call fill_age(df)

    ### ========== TODO : END ========== ###

    ### ========== TODO : Question 6 ========== ###

    # call family_size(df)

    ### ========== TODO : END ========== ###

    ### ========== TODO : Question 3 ========== ###

    # print overall survival rate

    # print survival_rates

    # print median

    # print mean

    ### ========== TODO : END ========== ###


    ### ========== TODO : Question 5 ========== ###

    # plot barplot


    # plot histogram


    # plot pair pointplot

    ### ========== TODO : END ========== ###

def read(file):
    ### ========== TODO : Question 1 ========== ###
    # Part a: Read the .csv file and assign it to df

    df = None

    ### ========== TODO : END ========== ###

    return df

def missing_values(df):
    ### ========== TODO : Question 2 ========== ###
    # Part a: Return all the missing values in df

    missing = None
    return missing

    ### ========== TODO : END ========== ###

def survived(df, b):
    ### ========== TODO : Question 3 ========== ###
    # Part a: Return a Pandas DataFrame with all the passengers that survived

    survived_df = None

    ## ========== TODO : END ========== ###

    return survived_df

def survival_rates(df, feature):
    ### ========== TODO : Question 3 ========== ###
    # Part c: Return a Pandas series for the proportion of passengers that survived grouped by a given feature

    return

    ## ========== TODO : END ========== ###

def median(df, feature):
    ### ========== TODO : Question 3 ========== ###
    # Part d: Return the median value for feature for surviving passengers

    median = None

    ## ========== TODO : END ========== ###

    return median

def mean(df, feature):
    ### ========== TODO : Question 3 ========== ###
    # Part d: Return the mean value for feature for surviving passengers

    mean = None

    ## ========== TODO : END ========== ###

    return mean

# Run this function to fill in missing entries in age
def fill_age(df):
    def get_title(name):
        title = re.findall("\w+[.]", name)[0]
        return title
    df['Title'] = df['Name'].map(get_title)
    title_dictionary = {'Ms.': 'Miss.', 'Mlle.': 'Miss.', 'Dr.': 'Rare', 'Mme.': 'Mr.', 'Major.': 'Rare', 'Lady.': 'Rare', 'Sir.': 'Rare', 'Col.': 'Rare', 'Capt.': 'Rare', 'Countess.': 'Rare', 'Jonkheer.': 'Rare', 'Dona.': 'Rare', 'Don.': 'Rare', 'Rev.': 'Rare'}
    df['Title'] = df['Title'].replace(title_dictionary)
    df['MedianAge'] = df.groupby('Title')['Age'].transform("median")
    df['Age'] = df['Age'].fillna(df['MedianAge'])
    df.drop(['MedianAge', 'Title'], axis = 1, inplace = True)
    df.dropna(inplace = True)

def age_categories(df):
    ### ========== TODO : Question 4 ========== ###
    # part a: Create a new column in df labelled 'Age Categories'

    df["Age Categories"] = None

    ## ========== TODO : END ========== ###

def fare_categories(df):
    ### ========== TODO : Question 4 ========== ###
    # part b: Create a new column in df labelle 'Fare Categories'

    def helper(row):
        if row['Fare'] <= None:
            val = ''
        elif row['Fare'] <= None:
            val = ''
        else: 
            val = ''
        return val
        
    df['Fare Categories'] = None
    

    ## ========== TODO : END ========== ###

def barplot(df, column, hue = None):
    ### ========== TODO : Question 5 ========== ###
    # part a
    if column == 'Age Categories':
        g1 = None
    elif column == 'Fare Categories':
        g1 = None
    else:
        g1 = None
    plt.show()

    ### ========== TODO : END ========== ###

def histogram(df, column):
    g1 = None
    g2 = None

def pointplot(df, column):
    g1 = None

def family_size(df):
    ### ========== TODO : Question 6 ========== ###
    # part a

    df['Family Size'] = None

    ### ========== TODO : END ========== ###


# --------------------------------- END --------------------------------- #