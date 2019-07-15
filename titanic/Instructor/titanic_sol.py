""" 
Author      : Thomas Cintra and Yun Zhang
Class       : CS 181R
Date        : 2019 June 20
Description : Titanic data analysis
Name        :
Homework 1
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

    # read the dataframe
    df = read('titanic.csv')

    # print missing entries
    print('Missing Values:')
    print()
    print(missing_values(df))
    print()

    df.drop('Cabin', axis = 1, inplace = True)

    # call age_categories(df)
    age_categories(df)

    # call fare_categories(df)
    fare_categories(df)

    # call fill_age(df)
    fill_age(df)

    # call family_size(df)
    family_size(df)

    # print overall survival rate
    print('Overall Survival Rate:', overall_survival_rate(df))
    print()

    # print survival_rates
    print('Survival rates:')
    print()
    print(survival_rates_by_feature(df, 'Sex'))
    print()

    # print median
    print('Medians:')
    print()
    print(median(df, 'Age'))
    print()

    # print mean
    print('Means:')
    print()
    print(mean(df, 'Age'))
    print()

    # plot barplot
    barplot(df, 'Pclass', 'Sex')

    # plot histogram
    histogram(df, 'Age')

    # plot pair pointplot
    pointplot(df, 'Sex')

def read(file):
    """
    Input: takes in a csv file

    Output: reads the csv file onto df
    """
    ### ========== TODO : Question 1 ========== ###
    # Part a: Read the .csv file and assign it to df

    df = pd.read_csv(os.path.join(path, file))

    ### ========== TODO : END ========== ###

    return df

def missing_values(df):
    """
    Input: takes in a DataFrame

    Output: outputs a Pandas series of the missing values in each column
    """
    missing = df.isnull().sum()
    return missing

def survived(df, b):
    """
    Input: takes in a DataFrame and a binary digit

    Output: outputs a new DataFrame with only the surviving passengers
    """
    ### ========== TODO : Question 3 ========== ###
    # Part a

    survived_df = df.loc[df['Survived'] == b]
    return survived_df

    ## ========== TODO : END ========== ###

def overall_survival_rate(df):
    """
    Input: takes in a DataFrame

    Output: outputs the survival rates for all passengers aboard the titanic
    """
    return len(survived(df, 1))/len(df)

def survival_rates_by_feature(df, feature):
    """
    Input: takes in a DataFrame and one of its features

    Output: outputs the survival rates for passengers belonging to each unique value in the given feature
    """
    ### ========== TODO : Question 3 ========== ###
    # Part c

    count = survived(df, 1)[feature].value_counts()
    total = df[feature].value_counts()
    return (count/total)

    ## ========== TODO : END ========== ###


def median(df, feature):
    """
    Input:takes in a DataFrame and one of its numeric features

    Output: outputs the median value for this feature for surviving passengers
    """
    ### ========== TODO : Question 3 ========== ###
    # Part d

    median_df = df[[feature, 'Survived']]
    median = median_df.groupby(['Survived']).median()
    return median

    ## ========== TODO : END ========== ###

def mean(df, feature):
    """
    Input: takes in a DataFrame and one of its numeric features

    Output: outputs the mean value for this feature for surviving passengers
    """
    ### ========== TODO : Question 3 ========== ###
    # Part d

    mean_df = df[[feature, 'Survived']]
    mean = mean_df.groupby(['Survived']).mean()
    return mean

    ## ========== TODO : END ========== ###

# Run this function to fill in missing entries in age
def fill_age(df):
    """
    Input: takes in a DataFrame

    Output: fills in all missing entries in 'Age' using the median age for each passenger's title
    """
    def get_title(name):
        title = re.findall("\w+[.]", name)[0]
        return title
    df['Title'] = df['Name'].map(get_title)
    title_dictionary = {'Ms.': 'Miss.', 'Mlle.': 'Miss.', 
        'Dr.': 'Rare', 'Mme.': 'Mr.', 'Major.': 'Rare', 
        'Lady.': 'Rare', 'Sir.': 'Rare', 'Col.': 'Rare', 
        'Capt.': 'Rare', 'Countess.': 'Rare', 'Jonkheer.': 
        'Rare', 'Dona.': 'Rare', 'Don.': 'Rare', 'Rev.': 'Rare'}
    df['Title'] = df['Title'].replace(title_dictionary)
    df['MedianAge'] = df.groupby('Title')['Age'].transform("median")
    df['Age'] = df['Age'].fillna(df['MedianAge'])
    df.drop(['MedianAge', 'Title'], axis = 1, inplace = True)
    df.dropna(inplace = True)

def age_categories(df):
    """
    Input: takes in a DataFrame

    Output: generates a new column in the DataFrame called 'Age Categories'
    """
    ### ========== TODO : Question 4 ========== ###
    # part a

    df["Age Categories"] = pd.cut(df["Age"], 8, labels = [0,1,2,3,4,5,6,7])

    ## ========== TODO : END ========== ###

def fare_categories(df):
    """
    Input: takes in a DataFrame

    Output: generates a new column in the DataFrame called 'Fare Categories'
    """
    ### ========== TODO : Question 4 ========== ###
    # part b

    df["Fare Categories"] = pd.cut(x = df["Fare"], bins = (0, 30, 100, 513), labels = [0,1,2])

    ## ========== TODO : END ========== ###



def barplot(df, column, hue = None):
    """
    Input: takes in a DataFrame, one of its columns and optionally, another column

    Output: outputs a barplot with survival rate on the y axis and the column on the x axis, optional hue argument
    """
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

def histogram(df, column):
    g1 = sns.distplot(survived(df, 1)['Age'], color = 'Green')
    g2 = sns.distplot(survived(df, 0)['Age'], color = 'Red')
    plt.show()

def pointplot(df, column):
    sns.pointplot(x= df[column], y= df['Survived'])
    plt.show()

def family_size(df):
    """
    Input: takes in a DataFrame

    Output: generates a new column called 'Family Size'
    """
    ### ========== TODO : Question 6 ========== ###
    # part a

    df['Family Size'] = df['SibSp'] + df['Parch'] + 1

    ### ========== TODO : END ========== ###

# --------------------------------- END --------------------------------- #

if __name__ == "__main__":
    main()