# =============================================================================
#         Pandas + NumPy - Day 03 | Advanced Analytics Using Statistics
#         CDAC Dataset — Full Code with Line-by-Line Comments
# =============================================================================

import numpy as np          # NumPy for numerical operations and array handling
import pandas as pd         # Pandas for DataFrames (tabular data)
import matplotlib.pyplot as plt  # Matplotlib for plotting and visualization
import seaborn as sns        # Seaborn for statistical visualizations (built on matplotlib)
import os                   # OS module for interacting with the file system


# =============================================================================
# SECTION 1: Setting Working Directory & Loading Data
# =============================================================================

# os.chdir(): Change current working directory so Python finds files easily
os.chdir("/content/drive/MyDrive/Advanced_Analytics_using_statistics")
# After this, all file paths are relative to the above folder

# pd.read_excel(): Read an Excel file into a Pandas DataFrame
# 'sheet_name' specifies which sheet to load from the Excel workbook
df = pd.read_excel('CDAC_DataBook.xlsx', sheet_name='ERPData')
# df now holds the entire ERPData sheet as a DataFrame with columns:
# MaterialID | Location | Quantity


# =============================================================================
# SECTION 2: Basic DataFrame Exploration
# =============================================================================

# df.head(): Shows FIRST 5 rows by default (pass a number to change, e.g. head(10))
df.head()
# Output: first 4 rows:
# MaterialID  Location  Quantity
#    TMI-43T     MWH-4        34
#    AXCP-78     MWH-1        67
#    LXCV-21     MWH-2        27
#    AXCP-78     MWH-5        65

# display(df): Same as df but renders a styled interactive table in Jupyter/Colab
display(df)

# df.tail(): Shows LAST 5 rows — useful to confirm data loaded till the end
df.tail()

# df.dtypes: Shows the data type of each column (int64, float64, object, etc.)
df.dtypes

# df.count(): Count of NON-NULL values in each column
df.count()


# =============================================================================
# SECTION 3: Removing Duplicates
# =============================================================================

# df.drop_duplicates(): Removes rows where ALL column values are exactly the same
# Returns a NEW DataFrame — original df is not changed
df1 = df.drop_duplicates()

df1.head()      # Check first 5 rows of cleaned data
df1.count()     # Count remaining rows after removing duplicates


# =============================================================================
# SECTION 4: Checking for Missing/Null Values
# =============================================================================

# df.isnull(): Returns True/False for each cell — True if value is NaN/missing
# .sum(): Adds up the True values per column → total missing count per column
print(df1.isnull().sum())
# Output example:
# MaterialID    0
# Location      0
# Quantity      0
# dtype: int64  (0 means no missing values in this dataset)


# =============================================================================
# SECTION 5: Visualization — Boxplot & Heatmap
# =============================================================================

# sns.boxplot(): Visualizes distribution of a numerical column
# Shows: median, IQR (box), whiskers, and outlier points
sns.boxplot(x=df1['Quantity'])
# x='Quantity' → horizontal boxplot for Quantity column

# ❌ Note: boxplot on a categorical column like 'Location' shows limited info
# sns.boxplot(x=df1['Location'])  → not meaningful for string categories

# sns.set(color_codes=True): Enables shorthand color codes ('r','b','g') in seaborn
sns.set(color_codes=True)

# Correlation Heatmap — shows correlation between numerical columns
plt.figure(figsize=(10, 5))       # Set figure size (width=10, height=5 inches)

# df1.select_dtypes(include=['number']): Filter only numeric columns for correlation
# .corr(): Compute pairwise Pearson correlation (-1 to +1)
c = df1.select_dtypes(include=['number']).corr()

# sns.heatmap(): Visualize correlation matrix with color coding
# annot=True → show the numeric value inside each cell
# cmap="BrBG" → color scheme (brown to blue-green)
sns.heatmap(c, cmap="BrBG", annot=True)
c   # Also display the raw correlation DataFrame

# Scatter Plot — both axes are Quantity (just a demo/diagonal line)
fig, ax = plt.subplots(figsize=(10, 6))    # Create figure with axes
ax.scatter(df['Quantity'], df['Quantity']) # Plot Quantity vs Quantity (always diagonal)
ax.set_xlabel('Quantity')                  # Label x-axis
ax.set_ylabel('Quantity')                  # Label y-axis
plt.show()                                 # Render the plot


# =============================================================================
# SECTION 6: Bar Chart — Value Counts
# =============================================================================

# ❌ ERROR: df1 was used before it was defined — NameError
# df1.MaterialID.value_counts().nlargest(40).plot(kind='bar', figsize=(10,5))
# → NameError: name 'df1' is not defined
# FIX: define df1 first (e.g., df1 = df.drop_duplicates()), then run this

# Correct version:
# .value_counts(): Count how many times each MaterialID appears
# .nlargest(40): Keep top 40 most frequent values
# .plot(kind='bar'): Draw a bar chart
df1.MaterialID.value_counts().nlargest(40).plot(kind='bar', figsize=(10, 5))
plt.title("Number of material_id")     # Chart title
plt.ylabel('Number of locations')      # Y-axis label
plt.xlabel('MaterialID')               # X-axis label
# plt.show() or plt.xlabel(...) with semicolon suppresses extra output in notebooks


# =============================================================================
# SECTION 7: Unique Values & Column Info
# =============================================================================

# np.unique(df1['MaterialID']): Returns sorted array of unique MaterialID values
np.unique(df1['MaterialID'])        # Same as np.unique(df1.MaterialID)

# len(np.unique(...)): How many distinct MaterialIDs exist
len(np.unique(df1.MaterialID))

# Get unique Locations and their count
np.unique(df1['Location'])
len(np.unique(df1.Location))

# df1.columns.values: Returns array of column header names
df1.columns.values      # array(['MaterialID', 'Location', 'Quantity'])

# Access a specific column name by index
df1.columns.values[0]   # 'MaterialID' — first column name

# Rename a column by directly assigning to the index position
df1.columns.values[0] = 'MatID'    # Renames 'MaterialID' → 'MatID'

# df.dtypes: Confirm data types of each column
df1.dtypes

# print(df1): Prints all rows of the DataFrame
print(df1)
print(df)   # Print original unmodified DataFrame


# =============================================================================
# SECTION 8: Filtering Rows with np.where() + iloc
# =============================================================================

# np.where(condition): Returns INDICES where condition is True
# Here: find rows where Quantity >= 70
ind = np.where(df1.Quantity >= 70)
ind             # Example: (array([ 1,  3,  4, ...]),)

len(ind[0])     # Count how many rows satisfy Quantity >= 70

# Alternative: Boolean sum — counts True values directly
(df1.Quantity >= 70).sum()   # Same count, simpler syntax

# df.iloc[ind]: Integer-location based indexing — select rows by position
df2 = df1.iloc[ind]     # DataFrame of rows where Quantity >= 70
df2

# AND condition (&): Rows where Quantity >= 70 AND Location is 'MWH-1'
df3 = np.where((df1.Quantity >= 70) & (df1.Location == 'MWH-1'))
df3     # Returns indices satisfying BOTH conditions

# Full workflow: filter AND + iloc on original df
ind = np.where((df.Quantity >= 70) & (df.Location == 'MWH-1'))
len(ind[0])         # Count of rows matching both conditions
df1 = df.iloc[ind]  # Select those rows from df
df1                 # Display result

# OR condition (|): Rows where Quantity >= 70 OR Location is 'MWH-1'
ind = np.where((df.Quantity >= 70) | (df.Location == 'MWH-1'))
len(ind[0])         # More rows since OR includes either condition being True
df2 = df.iloc[ind]
df2

# Boxplot on the filtered subset
sns.boxplot(x=df2['Quantity'])

# Find rows where Location is exactly 'MWH-2'
np.where(df1['Location'] == 'MWH-2')

# One-liner: extract rows for MWH-2 and store as temp
temp = df.iloc[np.where(df.Location == 'MWH-2')]
temp

# sum(): Total Quantity for MWH-2 location
sum(temp.Quantity)

# Same in one line — nested inline version
sum(df.iloc[np.where(df.Location == 'MWH-2')].Quantity)

# Count rows where Quantity < 50
(df.Quantity < 50).sum()


# =============================================================================
# SECTION 9: Dropping Rows (df.drop)
# =============================================================================

# Find indices of rows where Quantity < 50
ind = np.where(df.Quantity < 50)
ind     # Returns tuple of arrays with matching row positions

# df.drop(index_list): Remove rows by their INDEX LABELS (not positions)
# ind[0] gives the array of positions → drop those rows
df1 = df.drop(ind[0])
df1             # Remaining rows (only where Quantity >= 50)

df1.shape       # (rows, columns) of the filtered DataFrame

# df1.head(10): Show first 10 rows
df1.head(10)

# Basic stats on filtered data
print('Min', min(df1.Quantity))   # Minimum Quantity value
print('Max', max(df1.Quantity))   # Maximum Quantity value


# =============================================================================
# SECTION 10: Adding a New Column Using a For Loop (Grade Classification)
# =============================================================================

# METHOD 1 — Using ranges 10–40 = A, 50–100 = B, else = C
temp = []                       # Empty list to hold Grade values
for i in df.Quantity:           # Loop through every Quantity value
    if 10 <= i <= 40:           # If Quantity is between 10 and 40 (inclusive)
        temp.append('A')        # Grade A
    elif 50 <= i <= 100:        # If Quantity is between 50 and 100 (inclusive)
        temp.append('B')        # Grade B
    else:                       # All other values (< 10, between 41-49, or > 100)
        temp.append('C')        # Grade C

# Convert the plain Python list to a Pandas Series so it aligns with df
temp = pd.Series(temp)

# Assign the Series as a new column 'Grade' in the DataFrame
df['Grade'] = temp

df.head()       # Verify the new Grade column is added correctly
print(df)       # Print entire DataFrame with Grade column

# Boxplot on categorical Grade column — shows distribution per grade
sns.boxplot(x=df['Grade'])

# METHOD 2 — Slightly different boundaries: <=50 = A, <100 = B, else = C
grd = []
for ctr in df.Quantity:     # Loop through every Quantity
    if ctr <= 50:           # 50 and below → A
        grd.append('A')
    elif ctr < 100:         # 51 to 99 → B
        grd.append('B')
    else:                   # 100 and above → C
        grd.append('C')

df['Grade'] = grd           # Directly assign list (no need to convert to Series)
df                          # Display updated DataFrame

# Count how many items fall in each grade
df.Grade.value_counts()
# Example output:
# A    20
# B    12
# C     6

# sns.barplot(): Bar chart (requires x, y, and data args — shown as placeholder)
sns.barplot()   # ← Incomplete call; needs: sns.barplot(x='Grade', y='Quantity', data=df)

# For reference:
# For loop  → use when number of iterations is KNOWN before starting
# While loop → use when loop runs as long as a condition is True


# =============================================================================
# SECTION 11: Loading Employee Data & Handling Null Values
# =============================================================================

# Load a different sheet from the same Excel file
df = pd.read_excel('CDAC_DataBook.xlsx', sheet_name='EmpInfo')
df      # Display the Employee Info DataFrame (columns: EmpID, Name, Deptt, Passport, etc.)

# Find rows where 'Deptt' column is NULL/NaN
ind = np.where(df.Deptt.isnull())   # Returns indices where Deptt is missing
ind

# Drop rows where Deptt is null (remove employees with no department)
df1 = df.drop(ind[0])   # Drop by row position labels
df1                      # Remaining rows — all have a valid Deptt value

# Extract ONLY the null rows (to inspect them)
df2 = df.iloc[ind[0]]                              # Select null-Deptt rows
df2 = df.iloc[ind[0]].reset_index(drop=True)       # Reset index to 0, 1, 2...
# reset_index(drop=True): Remove old index, start fresh from 0
df2

df     # Display full original DataFrame

# Find rows where BOTH EmpID AND Deptt are null (double condition)
ind = np.where((df.EmpID.isnull()) & (df.Deptt.isnull()))
ind     # Rows where both columns are missing

# df.iloc[row_positions, column_position]: Set specific cell values
# Here: for rows where Deptt is null, set column at position 2 to 'Fresher'
df.iloc[ind[0], 2] = 'Fresher'
df      # Verify: null Deptt rows now show 'Fresher'

# Alternative one-liner (inline np.where):
df.iloc[np.where(df.Deptt.isnull())[0], 2] = 'Fresher'
df      # Same effect — fills remaining null Deptt with 'Fresher'

# df.EmpID: Access the EmpID column as a Series
df.EmpID

# df.dropna(): Drop ALL rows that have ANY null value in ANY column
temp = df.dropna()
temp    # Only rows with zero missing values across all columns

# df.info(): Summary of DataFrame — column names, non-null counts, dtypes, memory
df.info()
# Output includes: RangeIndex, column names, Non-Null Count, Dtype

# Drop duplicate EmpID rows — keeps FIRST occurrence by default
drp = df.drop_duplicates('EmpID')
drp     # Each EmpID appears only once


# =============================================================================
# SECTION 12: Handling Duplicates with duplicated()
# =============================================================================

# df.Passport.duplicated(): Returns True for rows that are DUPLICATES
# (by default, first occurrence is NOT a duplicate → False)
ind = np.where(df.Passport.duplicated())
ind     # Indices of duplicate Passport values (excluding first occurrence)

# keep=False: Mark ALL occurrences of duplicates as True (including the first)
ind = np.where(df.Passport.duplicated(keep=False))
ind     # All rows that share a Passport value with any other row

# keep='first': Default — mark duplicates EXCEPT the first occurrence
ind = np.where(df.Passport.duplicated(keep='first'))
ind

# keep='last': Mark duplicates EXCEPT the last occurrence
ind = np.where(df.Passport.duplicated(keep='last'))
ind

df      # View the full DataFrame for context


# =============================================================================
# SECTION 13: GROUP BY — Single Column
# =============================================================================

# Reload ERPData fresh for groupby exercises
import pandas as pd
df = pd.read_excel('CDAC_DataBook.xlsx', sheet_name='ERPData')

# df.groupby('column'): Groups rows by unique values of that column
# Returns a DataFrameGroupBy object — NOT a DataFrame yet
grp1 = df.groupby('Location')

print(grp1)     # Shows object info: <DataFrameGroupBy object>

# .groups: Dictionary of {group_key: [row_indices]}
grp1.groups
# Example: {'MWH-1': [1, 9, 24, 25, ...], 'MWH-2': [2, 7, 8, ...], ...}

# .get_group('key'): Extract ALL rows belonging to one specific group
grp1.get_group('MWH-2')     # All rows where Location == 'MWH-2'

# reset_index(drop=True): Reset row numbers starting from 0
df1 = grp1.get_group('MWH-2').reset_index(drop=True)
df1     # Clean DataFrame for MWH-2 only

# .count(): Number of non-null values in each column of the group
df1.Quantity.count()    # Number of rows in MWH-2 group

# pd.concat(): Combine multiple DataFrames vertically (stack rows)
# Here: combine MWH-2 and MWH-3 groups into one DataFrame
sp = pd.concat([grp1.get_group('MWH-2'), grp1.get_group('MWH-3')])
sp
sp.count()      # Count of non-null values in the combined group


# =============================================================================
# SECTION 14: GROUP BY Aggregation with .agg()
# =============================================================================

# grp1.Quantity.agg(np.sum): Sum of Quantity for EACH Location group
grp1.Quantity.agg(np.sum)
# Output: a Series with Location as index and summed Quantity as values

# Store as dframe and inspect
dframe = grp1.Quantity.agg(np.sum)
dframe

type(dframe)    # pandas.core.series.Series — it's a Series, not a DataFrame

dframe.index    # Index = Location names ('MWH-1', 'MWH-2', ...)

# reset_index(drop=True): Reset to 0,1,2... index — Location labels are LOST
df0 = grp1.Quantity.agg(np.sum).reset_index(drop=True)
print(df0)      # Just numbers without Location labels

# reset_index(): Convert the Location index back into a regular COLUMN
df2 = grp1.Quantity.agg(np.sum).reset_index()
print(df2)      # Now has 'Location' and 'Quantity' as proper columns
df2             # Display as table

# Manual check: 889 / 11 = avg (just verifying calculation)
889 / 11

# Multiple aggregations in one call using a LIST of function names
grp1.Quantity.agg(np.sum)                       # Only sum
grp1.Quantity.agg(['sum', 'mean', 'size'])      # Sum + mean + count per group

# Store the multi-agg result
SMS = grp1.Quantity.agg(['sum', 'mean', 'size'])
SMS     # DataFrame with columns: sum | mean | size (for each Location)


# =============================================================================
# SECTION 15: Multi-Index DataFrame (Grouping on 2 Levels)
# =============================================================================

# Create lists for a multi-level indexed DataFrame
locn   = ['Mumbai', 'Mumbai', 'Mumbai', 'Pune', 'Pune']    # Level 0 index
course = ['AI', 'ML', 'DS', 'AI', 'DS']                    # Level 1 index
marks1 = [45, 78, 65, 35, 89]                               # Column: Gajendra
marks2 = [89, 76, 59, 82, 49]                               # Column: Rathod

# pd.MultiIndex.from_arrays(): Create a 2-level hierarchical index
# pd.DataFrame(..., index=MultiIndex): Assign the multi-level index
mydf = pd.DataFrame(
    {'Gajendra': marks1, 'Rathod': marks2},
    index=pd.MultiIndex.from_arrays([locn, course])
)
mydf    # Display: rows indexed by (Location, Subject)

# Assign names to index levels for clarity
mydf.index.names = ['Location', 'Subject']
mydf    # Now shows named levels: Location | Subject

# .loc['Mumbai']: Select ALL rows where Level 0 (Location) == 'Mumbai'
mydf.loc['Mumbai']
# Returns all 3 Mumbai rows (AI, ML, DS)

# .loc['Mumbai', 'DS']: Select specific row: Location=Mumbai, Subject=DS
mydf.loc['Mumbai', 'DS']
# Returns: Gajendra=65, Rathod=59

# .xs(key, level='level_name'): Cross-section — select by INNER level
# Here: get all rows where Subject == 'AI' (regardless of Location)
mydf.xs('AI', level='Subject')
# Returns Mumbai/AI and Pune/AI rows
