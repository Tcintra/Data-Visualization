""" 
Authors     : Thomas Cintra and Yun Zhang
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

path = os.path.join("..", "Data")

######################################################################
# functions
######################################################################

def read(file):
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

    df = None

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

    ### ========== TODO : Question 2 ========== ###
    # Part a: Return all the missing values in df

    missing = None
    return missing

    ### ========== TODO : END ========== ###

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
    # Part a: Return a Pandas DataFrame with all the passengers that survived

    survived_df = None

    ## ========== TODO : END ========== ###

    return survived_df

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

    ### ========== TODO : Question 3 ========== ###
    # Part b: Return the survival rates of the entire titanic.csv dataset

    return 

    ## ========== TODO : END ========== ###

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
    # Part c: Return a Pandas series for the proportion of passengers that survived grouped by a given feature

    return

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
    # Part d: Return the median value for feature for surviving passengers

    median = None

    ## ========== TODO : END ========== ###

    return median

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
    # Part d: Return the mean value for feature for surviving passengers

    mean = None

    ## ========== TODO : END ========== ###

    return mean

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
    # part a: Create a new column in df labelled 'Age Categories'

    df["Age Categories"] = None

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
    # part b: Create a new column in df labelle 'Fare Categories'

    df['Fare Categories'] = None
    
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
        g1 = None
    elif column == 'Fare Categories':
        g1 = None
    else:
        g1 = None
    plt.show()

    ### ========== TODO : END ========== ###

def histogram(df, column):
    g1 = sns.distplot(survived(df, 1)['Age'], color = 'Green')
    g2 = sns.distplot(survived(df, 0)['Age'], color = 'Red')

def pointplot(df, column):
    sns.pointplot(x= df[column], y= df['Survived'])

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

    df['Family Size'] = None

    ### ========== TODO : END ========== ###

######################################################################
# main
######################################################################

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

    # print survival_rates_by_feature

    # print median

    # print mean

    ### ========== TODO : END ========== ###


    ### ========== TODO : Question 5 ========== ###

    # plot barplot


    # plot histogram


    # plot pair pointplot

    ### ========== TODO : END ========== ###

if __name__ == "__main__":
    main()