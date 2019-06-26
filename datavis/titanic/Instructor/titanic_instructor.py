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

def main():

    # read the dataframe
    df = read('titanic.csv')
    
    # print missing entries
    print(missing_values(df))

    # Call age_categories(df)
    age_categories(df)

    # Call fare_categories(df)
    fare_categories(df)

    # print survival_rates
    print(survival_rates(df, 'Sex'))

    # print median
    print(median(df, 'Age'))

    # print mean
    print(mean(df, 'Age'))

    # plot barplot
    barplot(df, 'Pclass', 'Sex')
    plt.show()

def read(file):
    ### ========== TODO : Question 1 ========== ###
    # Part a: Read the .csv file and assign it to df

    path = "../Data/"
    df = pd.read_csv(path + file)

    ### ========== TODO : END ========== ###
    return df

def missing_values(df):
    missing = df.isnull().sum()
    return missing

def survived(df):
    ### ========== TODO : Question 3 ========== ###
    # Part a

    survived_df = df.loc[df['Survived'] == 1]
    return survived_df

    ## ========== TODO : END ========== ###

def survival_rates(df, feature):
    ### ========== TODO : Question 3 ========== ###
    # Part c

    count = survived(df)[feature].value_counts()
    total = df[feature].value_counts()
    return (count/total)

    ## ========== TODO : END ========== ###


def median(df, feature):
    ### ========== TODO : Question 3 ========== ###
    # Part d

    median_df = df[[feature, 'Survived']]
    median = median_df.groupby(['Survived']).median()
    return median

    ## ========== TODO : END ========== ###

def mean(df, feature):
    ### ========== TODO : Question 3 ========== ###
    # Part d

    mean_df = df[[feature, 'Survived']]
    mean = mean_df.groupby(['Survived']).mean()
    return mean

    ## ========== TODO : END ========== ###

# Run this function to fill in missing entries in age
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
    path = "../Data/"
    df.to_csv(path + 'titanic.csv')

def age_categories(df):
    ### ========== TODO : Question 4 ========== ###
    # part a

    df["Age Categories"] = pd.cut(df["Age"], 8, labels = [0,1,2,3,4,5,6,7])

    ## ========== TODO : END ========== ###

def fare_categories(df):
    ### ========== TODO : Question 4 ========== ###
    # part b

    def helper(row):
        if row['Fare'] <= 30:
            val = '30 or Less'
        elif row['Fare'] > 30 and row['Fare'] <= 100:
            val = 'Between 30 and 100'
        else: 
            val = 'More than 100'
        return val
    df['Fare Categories'] = df.apply(helper, axis = 1)

    ## ========== TODO : END ========== ###

def barplot(df, column, hue = None):
    ### ========== TODO : Question 5 ========== ###
    # part a
    if column == 'Age Categories':
        sns.barplot(x = column, y = 'Survived', data = df, hue = hue, order = [0,1,2,3,4,5,6,7])
    elif column == 'Fare Categories':
        sns.barplot(x = column, y = 'Survived', data = df, hue = hue, order = ['30 or Less', 'Between 30 and 100', 'More than 100'])
    else:
        sns.barplot(x = column, y = 'Survived', data = df, hue = hue)
    plt.show()

    ### ========== TODO : END ========== ###

def family_size(df):
    ### ========== TODO : Question 6 ========== ###
    # part a

    df['Family Size'] = df['SibSp'] + df['Parch'] + 1
    path = "../Data/"
    df.to_csv(path + 'titanic.csv')

    ### ========== TODO : END ========== ###


# --------------------------------- END --------------------------------- #