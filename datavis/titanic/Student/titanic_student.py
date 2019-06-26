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

### ========== TODO : Question 1 ========== ###

# Part a: Read the .csv file
df = None

### ========== TODO : END ========== ###


def drop(df, column):
    """
    Input:

    Output:
    """
    ### ========== TODO : Question 2 ========== ###
    # Part b: Drop columns with too many missing entries

    return df # you will change this
    ### ========== TODO : END ========== ###


### ========== TODO : Question 3 ========== ###

# Part a
def survived():
    """
    Input:

    Output:
    """
    return ""
    

# Part b
def count_values(feature):
    """
    Input:

    Output:
    """
    

# Part c
def median(feature):
    """
    Input:

    Output:
    """
    

def mean(feature):
    """
    Input:

    Output:
    """
    

### ========== TODO : END ========== ###

# Deal with missing entries, uncomment this block.

def missing_entries(df):
    def get_title(name):
        title = re.findall("\w+[.]", name)[0]
        return title
    df['Title'] = df['Name'].map(get_title)
    title_dictionary = {'Ms.': 'Miss.', 'Mlle.': 'Miss.', 'Dr.': 'Rare', 'Mme.': 'Mr.', 'Major.': 'Rare', 'Lady.': 'Rare', 'Sir.': 'Rare', 'Col.': 'Rare', 'Capt.': 'Rare', 'Countess.': 'Rare', 'Jonkheer.': 'Rare', 'Dona.': 'Rare', 'Don.': 'Rare', 'Rev.': 'Rare'}
    df['Title'] = df['Title'].replace(title_dictionary)
    df['MedianAge'] = df.groupby('Title')['Age'].transform("median")
    df['Age'] = df['Age'].fillna(df['MedianAge'])
    df.drop('MedianAge')
    df.dropna(inplace = True)
    df.to_csv('train.csv')

### ========== TODO : Question 4 ========== ###

def age_categories():
    """
    Input:

    Output:
    """
    
# Part b: Complete this function using teh Pandas method .apply
def fare_categories():
    """
    Input:

    Output:
    """
    def helper(row):
        if row['Fare'] <= 30:
            val = '<30'
        

### ========== TODO : END ========== ###

### ========== TODO : Question 5 ========== ###

def barplot(column, hue = None):
    """
    Input:

    Output:
    """
    

### ========== TODO : END ========== ###

### ========== TODO : Question 6 ========== ###

def family_size():
    """
    Input:

    Output:
    """
    

### ========== TODO : END ========== ###

# --------------------------------- END --------------------------------- #