import pandas as pd
import numpy as np

# Adapt march_2010_clean.csv into march_2010_dirty.csv for Homework 1

path = "../Data/"
df = pd.read_csv("../Data/march_2010_clean.csv")

# Modify all yes/no columns
columns = ["offunif","frisked", "ac_rept",  "ac_inves",  "ac_proxm" , "cs_objcs", "cs_descr", "cs_casng", "cs_lkout",  "cs_cloth", "cs_drgtr", "ac_evasv", "ac_assoc", "cs_furtv",  "ac_cgdir", "cs_vcrim", "cs_bulge", "cs_other", "ac_incid", "ac_time", "ac_stsnd", "ac_other"]
for i in columns:
    df[i] = df[i].map({1: 'Y', 0: 'N', -1 : 'N'})

# Modify column sex
df["sex"] = df["sex"].map({1: 'M', 0: 'F'})

# Modify column inout
df["inout"] = df["inout"].map({1: 'I', 0: 'O'})

df.to_csv('march_2010_dirty.csv')
print(df.head())