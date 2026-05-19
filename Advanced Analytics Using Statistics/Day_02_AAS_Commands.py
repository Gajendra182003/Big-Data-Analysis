#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 19 17:33:18 2026

@author: gajendra06
"""

# =============================================================================
#         Pandas & NumPy - Day 02 | Advanced Analytics Using Statistics
#         Full Code with Line-by-Line Comments
# =============================================================================

import numpy as np
import pandas as pd


# =============================================================================
# SECTION 1: NumPy Set Operations
# =============================================================================

arr1 = np.array([3,7,6,1,8,9])
arr2 = np.array([2,4,5,8,10,3,6])

# Common elements between arr1 and arr2
np.intersect1d(arr1, arr2)
# Output: array([3, 6, 8])

# Unique elements from both arrays combined
np.union1d(arr1, arr2)
# Output: array([ 1,2,3,4,5,6,7,8,9,10 ])

# Elements present in arr1 but not in arr2
np.setdiff1d(arr1, arr2)
# Output: array([1,7,9])

# Elements present in arr2 but not in arr1
np.setdiff1d(arr2, arr1)
# Output: array([ 2,4,5,10 ])

# Elements not common in both arrays
np.setxor1d(arr1, arr2)
# Output: array([ 1,2,4,5,7,9,10 ])


# =============================================================================
# SECTION 2: Membership Checking
# =============================================================================

# Check whether each element of arr1 exists in arr2
np.isin(arr1, arr2)
# Output: array([ True, False, True, False, True, False ])

# Get positions where elements are common
np.where(np.isin(arr1, arr2))
# Output: (array([0,2,4]),)

# Explanation:
# arr1[0] = 3 exists in arr2
# arr1[2] = 6 exists in arr2
# arr1[4] = 8 exists in arr2


# =============================================================================
# SECTION 3: Dot Product & Cross Product
# =============================================================================

mat1 = np.array([2,3,-4])
mat2 = np.array([3,-2,1])

# Dot Product
np.dot(mat1, mat2)

# Formula:
# (2*3) + (3*-2) + (-4*1)
# = 6 - 6 - 4
# = -4

# Output: -4


# Cross Product
np.cross(mat1, mat2)

# Output: array([ -5, -14, -13 ])

# Cross product returns a vector perpendicular to both vectors


# =============================================================================
# SECTION 4: Determinant of Matrix
# =============================================================================

mat3 = np.array([
    [1,2,3],
    [0,1,2],
    [1,1,0]
])

np.linalg.det(mat3)

# Output: -1.0

# Determinant helps identify:
# 1. Singular / Non-singular matrix
# 2. Invertibility
# 3. Linear independence


# =============================================================================
# SECTION 5: Random Number Generation
# =============================================================================

from numpy import random

# Random decimal values between 0 and 1
np.random.rand(10)

# Random integer between 5 and 50
np.random.randint(5,50)

# 15 random integers
np.random.randint(5,50,15)

# Generate one random integer
np.random.randint(5,50,1)


# =============================================================================
# SECTION 6: Pandas Series Creation
# =============================================================================

pds1 = [4,8,4,3,2]

type(pds1)
# Output: list


# =============================================================================
# SECTION 7: Common Errors While Creating Series
# =============================================================================

# ❌ ERROR — 'series' should start with capital 'S'
# pds1 = pd.series(pds1)
# AttributeError

# Correct
pds1 = pd.Series(pds1)

# Output:
# 0    4
# 1    8
# 2    4
# 3    3
# 4    2


# ❌ ERROR — Series belongs to pandas, not numpy
# np.Series(pds1)
# AttributeError


# =============================================================================
# SECTION 8: Series with Custom Index
# =============================================================================

pds2 = pd.Series(pds1, index=['A','B','C','D','E'])

# Output:
# A    4
# B    8
# C    4
# D    3
# E    2


# =============================================================================
# SECTION 9: Accessing Series Elements
# =============================================================================

# iloc -> position based indexing
pds2.iloc[2]
# Output: 4

# loc -> label based indexing
pds2.loc['C']
# Output: 4


# ❌ ERROR — labels are case-sensitive
# pds2.loc['c']
# KeyError


# Multiple positions
pds2.iloc[[1,2]]

# Output:
# B    8
# C    4


# =============================================================================
# SECTION 10: Duplicate Index Example
# =============================================================================

pds3 = pd.Series(
    [1,2,3,4,5],
    index=['A','A','B','A','B']
)

# Access all rows with label 'A'
pds3.loc['A']

# Output:
# A    1
# A    2
# A    4


# =============================================================================
# SECTION 11: Concatenation
# =============================================================================

pds4 = pd.Series([3,9], index=['F','G'])

# ❌ ERROR — pds1 is still a Python list
# pd.concat([pds1,pds2])
# TypeError

# Correct
pnds1 = pd.concat([pds2,pds4])

# Output:
# A    4
# B    8
# C    4
# D    3
# E    2
# F    3
# G    9


# =============================================================================
# SECTION 12: Modifying Series Values
# =============================================================================

# Change value at position 4
pds2.iloc[4] = 9

# Access updated value
pds2.loc['E']
# Output: 9


# =============================================================================
# SECTION 13: Drop Operations
# =============================================================================

# Drop by label
pds2 = pds2.drop(['E'])

# Drop by position
pds2.drop(pds2.index[2])

# ❌ ERROR — wrong syntax
# pds2.drop(pds2.index[2,4])
# IndexError

# Correct
# pds2.drop(pds2.index[[2,4]])


# =============================================================================
# SECTION 14: value_counts()
# =============================================================================

s4 = pd.Series([
1,2,3,4,5,6,5,4,3,2,2,1,
4,5,6,7,8,3,2,2,2,1,1,1,
1,4,4,4,5,5,6,7,7,8,8
])

s4.value_counts()

# Output:
# 1    6
# 2    6
# 4    6
# 5    5
# 3    3
# 6    3
# 7    3
# 8    3

# Counts frequency of unique values


# =============================================================================
# SECTION 15: np.where() with Series
# =============================================================================

np.where(pds2 == 4)

# Output:
# (array([0,2]),)

# Get actual labels
pds2.index[np.where(pds2 == 4)[0]]

# Output:
# Index(['A','C'])


# =============================================================================
# SECTION 16: Length of Matching Elements
# =============================================================================

a1 = np.array([3,5,4,3,3,3,7,8,9])

np.where(a1 == 3)

# Output:
# (array([0,3,4,5]),)

# Number of occurrences
len(np.where(a1 == 3)[0])

# Output: 4


# ❌ ERROR
# len(np.where(a1==3),[0])
# TypeError


# =============================================================================
# SECTION 17: DataFrame Creation
# =============================================================================

mydata = [
['A',1234,20000],
['B',1239,35000],
['C',1238,30000],
['D',1238,50000],
['E',1237,12000],
['F',1236,21000],
['G',1234,25000],
['H',1235,20060]
]

# ❌ ERROR — 'Index' should be lowercase
# Index=[...]

# Correct
mydf = pd.DataFrame(
    mydata,
    columns=['Name','AccNo','Balance'],
    index=[
        'Gajendra','Akash','Abhi','Dev',
        'Sujal','Putin','Radhe','Sayali'
    ]
)

# Output:
#          Name  AccNo  Balance
# Gajendra    A   1234    20000
# Akash       B   1239    35000
# ...


# =============================================================================
# SECTION 18: loc vs iloc in DataFrame
# =============================================================================

# ❌ ERROR — index labels are names, not integers
# mydf.loc[[1,2]]
# KeyError

# Correct position based indexing
mydf.iloc[[1,2]]

# Extract single value
mydf.iloc[1,2]
# Output: 35000

# Extract full row
mydf.iloc[2]

# Output:
# Name           C
# AccNo       1238
# Balance    30000


# =============================================================================
# SECTION 19: reset_index()
# =============================================================================

df2 = mydf.iloc[[1,2]].reset_index(drop=True)

# Output:
#   Name  AccNo  Balance
# 0    B   1239    35000
# 1    C   1238    30000


# Keep old index
dfF2 = mydf.iloc[[1,2]].reset_index()

# Output:
#    index Name AccNo Balance
# 0  Akash   B  1239   35000
# 1   Abhi   C  1238   30000


# =============================================================================
# SECTION 20: DataFrame from Dictionary
# =============================================================================

stud_info = {
    'name':['A','B','C','D'],
    'roll_no':[1,2,3,4],
    'marks':[50,60,75,80]
}

df1 = pd.DataFrame(stud_info)

# Output:
#   name  roll_no  marks
# 0    A        1     50
# 1    B        2     60


# =============================================================================
# SECTION 21: Adding New Rows using concat()
# =============================================================================

newdf = pd.DataFrame(
    [['E',5,85],['F',6,88]],
    columns=df1.columns
)

# ❌ ERROR
# pd.concat(df1,newdf)
# TypeError

# Correct
DF = pd.concat([df1,newdf]).reset_index(drop=True)

# Output:
#   name  roll_no  marks
# 0    A        1     50
# 1    B        2     60
# 2    C        3     75
# 3    D        4     80
# 4    E        5     85
# 5    F        6     88


# =============================================================================
# SECTION 22: iat Accessor
# =============================================================================

# ❌ ERROR — column index 3 does not exist
# DF.iat[1,3]
# IndexError

# Correct
DF.iat[1,2]
# Output: 60

# iat is used for fast scalar access


# =============================================================================
# SECTION 23: Extract Multiple Rows
# =============================================================================

DF.iloc[[0,1,3]]

# Output:
#   name  roll_no  marks
# 0    A        1     50
# 1    B        2     60
# 3    D        4     80


# Reset index after extraction
df3 = DF.iloc[[0,1,3]].reset_index(drop=True)


# =============================================================================
# SECTION 24: Extract Multiple Columns
# =============================================================================

mysubject = DF[['name','marks']]

# Output:
#   name  marks
# 0    A     50
# 1    B     60
# ...


# =============================================================================
# SECTION 25: Adding New Column
# =============================================================================

m1 = [50,60,70,80,90,75]

DF['marks2'] = m1

# Output:
#   name roll_no marks marks2
# 0   A      1     50    50
# ...


# =============================================================================
# SECTION 26: Extract Specific Columns using iloc
# =============================================================================

DF.iloc[:,[1,2]]

# Output:
#    roll_no  marks


DF.iloc[:,[1,2,3]]

# Output:
#    roll_no  marks  marks2



# =============================================================================
# SECTION 27: Working Directory & Reading Excel File
# =============================================================================

# os module is used for interacting with the operating system
import os


# =============================================================================
# Change Current Working Directory
# =============================================================================

# chdir() = change directory
# Used to move Python execution to a specific folder

os.chdir("/content/drive/MyDrive/Advanced_Analytics_using_statistics")

# Explanation:
# Now Python will search files from this folder location

# NOTE:
# This path is generally used in Google Colab with Google Drive mounted


# =============================================================================
# Import Pandas
# =============================================================================

import pandas as pd


# =============================================================================
# Read Excel File
# =============================================================================

# read_excel() is used to load Excel files into a DataFrame

df = pd.read_excel(
    'CDAC_DataBook.xlsx',
    sheet_name='ERPData'
)

# Parameters:
#
# 'CDAC_DataBook.xlsx'
# → Excel file name
#
# sheet_name='ERPData'
# → Reads only the ERPData sheet from workbook


# =============================================================================
# Display First 5 Rows
# =============================================================================

df.head()

# head() by default shows first 5 rows

# Useful for:
# 1. Checking data loaded correctly
# 2. Understanding structure
# 3. Inspecting column names
# 4. Initial data analysis


# =============================================================================
# Common Variations
# =============================================================================

# Show first 10 rows
# df.head(10)

# Show last 5 rows
# df.tail()

# Show last 10 rows
# df.tail(10)


# =============================================================================
# Common Errors
# =============================================================================

# ❌ ERROR — File not found
#
# pd.read_excel('wrongfile.xlsx')
#
# FileNotFoundError


# ❌ ERROR — Wrong sheet name
#
# pd.read_excel('CDAC_DataBook.xlsx',sheet_name='ABC')
#
# ValueError:
# Worksheet named 'ABC' not found


# ❌ ERROR — openpyxl missing
#
# ImportError:
# Missing optional dependency 'openpyxl'
#
# Install using:
# pip install openpyxl


# =============================================================================
# Important Interview Concepts
# =============================================================================

# os.chdir()
# → Changes current working directory

# pd.read_excel()
# → Reads Excel file into DataFrame

# sheet_name
# → Selects specific sheet from workbook

# head()
# → Displays first n rows

# tail()
# → Displays last n rows


# =============================================================================
# Real-Time Use Cases
# =============================================================================

# 1. Reading ERP system data
# 2. Financial reports
# 3. Student records
# 4. Banking transaction sheets
# 5. HR employee databases
# 6. Sales analytics reports


# =============================================================================
# Quick Summary
# =============================================================================

# import os
# → Access operating system functions

# os.chdir(path)
# → Change folder location

# pd.read_excel()
# → Load Excel data

# df.head()
# → Preview top rows of dataset


# =============================================================================
# FINAL SUMMARY
# =============================================================================

# Topics Covered:
#
# 1. NumPy Set Operations
# 2. Membership Functions
# 3. Dot Product & Cross Product
# 4. Determinant
# 5. Random Number Generation
# 6. Pandas Series
# 7. loc vs iloc
# 8. Duplicate Index
# 9. concat()
# 10. drop()
# 11. value_counts()
# 12. DataFrames
# 13. reset_index()
# 14. iat()
# 15. Column Extraction
# 16. Adding Columns
#
# Most Common Errors:
#
# ❌ pd.series()      → ✅ pd.Series()
# ❌ np.Series()      → ✅ pd.Series()
# ❌ Index=           → ✅ index=
# ❌ pds2.concat()    → ✅ pd.concat()
# ❌ loc['c']         → ✅ loc['C']
# ❌ drop(index[2,4]) → ✅ drop(index[[2,4]])
#
# Important Interview Concepts:
#
# loc   → label based indexing
# iloc  → position based indexing
# iat   → fast scalar access
# concat() → combine Series/DataFrames
# value_counts() → frequency counting
# np.where() → find matching positions


