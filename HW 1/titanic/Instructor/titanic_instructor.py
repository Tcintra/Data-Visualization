""" 
Author: Thomas Cintra and Yun Zhang
Class: CS 181R
Week 2 - Data Science Overview
Homework 1
Name:
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re

### ========== TODO : Question 1 ========== ###
# Part a
path = "../Data/"
df = pd.read_csv(path + 'train.csv')
df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)

### ========== TODO : END ========== ###


### ========== TODO : Question 2 ========== ###
# Part b

def drop(column):
    df.drop(column, axis = 1, inplace = True)
    df.to_csv('train.csv')

### ========== TODO : END ========== ###


### ========== TODO : Question 3 ========== ###

# Part a
def survived(binary):
    survived_df = df.loc[df['Survived'] == binary]
    return survived_df

# Part b
def count_values(feature):
    count = survived(1)[feature].value_counts()
    total = df[feature].value_counts()
    return (count/total)

# Part c
def median(feature):
    median_df = df[[feature, 'Survived']]
    median = median_df.groupby(['Survived']).median()
    return median

def mean(feature):
    mean_df = df[[feature, 'Survived']]
    mean = mean_df.groupby(['Survived']).mean()
    return mean

### ========== TODO : END ========== ###

# Deal with missing entries
def missing_entries():
    def get_title(name):
        title = re.findall("\w+[.]", name)[0]
        return title
    df['Title'] = df['Name'].map(get_title)
    title_dictionary = {'Ms.': 'Miss.', 'Mlle.': 'Miss.', 'Dr.': 'Rare', 'Mme.': 'Mr.', 'Major.': 'Rare', 'Lady.': 'Rare', 'Sir.': 'Rare', 'Col.': 'Rare', 'Capt.': 'Rare', 'Countess.': 'Rare', 'Jonkheer.': 'Rare', 'Dona.': 'Rare', 'Don.': 'Rare', 'Rev.': 'Rare'}
    df['Title'] = df['Title'].replace(title_dictionary)
    df['MedianAge'] = df.groupby('Title')['Age'].transform("median")
    df['Age'] = df['Age'].fillna(df['MedianAge'])
    drop('MedianAge')
    df.dropna(inplace = True)
    df.to_csv('train.csv')

### ========== TODO : Question 4 ========== ###

def age_categories():
    df["Age Categories"] = pd.cut(df["Age"], 8, labels = [0,1,2,3,4,5,6,7])
    df.to_csv('train.csv')

def fare_categories():
    def helper(row):
        if row['Fare'] <= 30:
            val = '30 or Less'
        elif row['Fare'] > 30 and row['Fare'] <= 100:
            val = 'Between 30 and 100'
        else: 
            val = 'More than 100'
        return val
    df['Fare Categories'] = df.apply(helper, axis = 1)
    df.to_csv('train.csv')

### ========== TODO : END ========== ###

### ========== TODO : Question 5 ========== ###

def barplot(column, hue = None):
    sns.barplot(x = column, y = 'Survived', data = df, hue = hue, order = ["1 - 10", "11 - 20", "21 - 30", "31 - 40", "41 - 50", "51 - 60", "61 - 70", "71 - 80"])
    plt.show()

### ========== TODO : END ========== ###

### ========== TODO : Question 6 ========== ###

def family_size():
    df['Family Size'] = df['SibSp'] + df['Parch'] + 1
    df.to_csv('train.csv')

### ========== TODO : END ========== ###