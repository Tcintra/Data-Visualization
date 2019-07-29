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

PATH = os.path.join("..", "Data")

######################################################################
# functions
######################################################################

def read(fname):
    """
    Reads the given csv file to a DataFrame
    
    Parameters
    --------------------
        fname   -- name of the csv file, string      
    
    Returns
    --------------------
        df      -- csv contents, DataFrame
    """

    ### ========== TODO : Question 1 ========== ###
    # Part a: Read the .csv file and assign it to df

    df = pd.read_csv(os.path.join(PATH, fname))

    ### ========== TODO : END ========== ###

    return df

def missing_values(df):
    """
    Finds the number of missing entries in each column of a DataFrame
    
    Parameters
    --------------------
        df      -- DataFrame to find missing entries in, DataFrame 
    
    Returns
    --------------------
        missing -- number of missing values in each column, indexed 
                   by each column name, Series
    """

    missing = df.isnull().sum()
    return missing

def survived(df, survived):
    """
    Given a DataFrame, returns a new DataFrame filtered to only
    have entries with the given survival status
    
    Parameters
    --------------------
        df          -- DataFrame to filter, DataFrame
        survived    -- whether to filter for survival or lack of survival, boolean

    Returns
    --------------------
        survived_df -- filtered DataFrame, DataFrame
    """

    ### ========== TODO : Question 3 ========== ###
    # Part a

    survived_df = df.loc[df['Survived'] == survived]
    return survived_df

    ## ========== TODO : END ========== ###

def overall_survival_rate(df):
    """
    Finds the survival rate of all entries in the given DataFrame
    
    Parameters
    --------------------
        df            -- DataFrame to find survival rate for, DataFrame      
    
    Returns
    --------------------
        survival_rate -- proportion of entries in df with 'Survived' column 
                         set to 1, float
    """
    
    survival_rate = len(survived(df, True))/len(df)
    
    return survival_rate

def survival_rates_by_feature(df, feature):
    """
    Finds the survival rates of entries in the given DataFrame
    for each unique value of the given column
    
    Parameters
    --------------------
        df        -- DataFrame to find survival rate for, DataFrame
        feature   -- name of the column in df to find survival rates for, string
    
    Returns
    --------------------
        rates     -- survival rate for each unique value of a column of df,
                     indexed by those values, Series
    """
    
    ### ========== TODO : Question 3 ========== ###
    # Part c
    
    count = survived(df, 1)[feature].value_counts()
    total = df[feature].value_counts()
    rates = count / total

    return rates

    ## ========== TODO : END ========== ###


def median(df, feature):
    """
    Finds the median value of the given column for passengers
    that survived in the given DataFrame
    
    Parameters
    --------------------
        df        -- DataFrame to find median in, DataFrame
        feature   -- name of a numeric column in df, string
    
    Returns
    --------------------
        median    -- median value of the given column in df, float/int
    """

    ### ========== TODO : Question 3 ========== ###
    # Part d

    median_df = df[[feature, 'Survived']]
    median = median_df.groupby(['Survived']).median()
    return median

    ## ========== TODO : END ========== ###

def mean(df, feature):
    """
    Finds the mean value of the given column for passengers
    that survived in the given DataFrame
    
    Parameters
    --------------------
        df        -- DataFrame to find mean in, DataFrame
        feature   -- name of a numeric column in df, string
    
    Returns
    --------------------
        median    -- mean value of the given column in df, float
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
    Fills in each missing value in the 'Age' column of the given DataFrame 
    with the median value for 'Age' of entries with the same title in the 
    'Name' column 
    
    Parameters
    --------------------
        df        -- DataFrame to modify, DataFrame
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
    Generates a new 'Age Categories' column in the given DataFrame that lists
    which of 8 evenly spaced intervals the 'Age' of each entry falls into.
    
    Parameters
    --------------------
        df        -- DataFrame to modify, DataFrame
    """

    ### ========== TODO : Question 4 ========== ###
    # part a

    df["Age Categories"] = pd.cut(df["Age"], 8, labels = [0,1,2,3,4,5,6,7])

    ## ========== TODO : END ========== ###

def fare_categories(df):
    """
    Generates a new 'Fare Categories' column in the given DataFrame that lists
    whether each entry's 'Fare' is 30 or less, between 30 and 100, or more than
    100.
    
    Parameters
    --------------------
        df        -- DataFrame to modify, DataFrame
    """

    ### ========== TODO : Question 4 ========== ###
    # part b

    df["Fare Categories"] = pd.cut(x = df["Fare"], bins = (0, 30, 100, 513), labels = ['30 or Less', 'Between 30 and 100', 'More than 100'])

    ## ========== TODO : END ========== ###



def barplot(df, column, hue = None):
    """
    Creates and displays a barplot of survival rates for each of the unique values 
    of a given column. An optional second column can be provided to show survival 
    rates for each combination of unique values in the two columns.
    
    Parameters
    --------------------
        df      -- data to graph, DataFrame
        column  -- name of (categorical) column to filter by on x-axis, string
        hue     -- optional name of second (categorical) column to filter by,
                   represented by bar colors, string
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
    Generates a new 'Family Size' column in the given DataFrame, representing
    the total number of family members that each passenger boarded with
    (including themselves).
    
    Parameters
    --------------------
        df        -- DataFrame to modify, DataFrame
    """
    
    ### ========== TODO : Question 6 ========== ###
    # part a

    df['Family Size'] = df['SibSp'] + df['Parch'] + 1

    ### ========== TODO : END ========== ###

######################################################################
# main
######################################################################

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

if __name__ == "__main__":
    main()