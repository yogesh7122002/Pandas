# import pandas as pd 

# # DifferantWays to create data Frames

# data  = [['John', 25, 'Austin',70],
#         ['Cataline', 30, 'San Francisco',80],
#         ['Matt', 35, 'Boston',90]]

# columns = ["Name", "Age", "City", "Marks"]
# df = pd.DataFrame(data=data,columns=columns)


# data = {'Name': ['John', 'Cataline', 'Matt'],
#         'Age': [50, 45, 30],
#         'City': ['Austin', 'San Francisco', 'Boston'],
#         'Marks' : [70, 80, 95]}

# df = pd.DataFrame(data=data)
# df.drop([0,1],axis=1)
# print(df)
# print(df.reindex())


import pandas as pd

data = [['John', 50, 'Male', 'Austin', 70],
        ['Cataline', 45 ,'Female', 'San Francisco', 80],
        ['Matt', 30 ,'Male','Boston', 95]]

# Column labels of the DataFrame
columns = ['Name','Age','Sex', 'City', 'Marks']

# Create a DataFrame df
df = pd.DataFrame(data, columns=columns)

count = df['Sex'].value_counts()
print(count)

# What is pandas in Python?
# Pandas is an open-source Python library with powerful and built-in methods to efficiently clean, analyze, and manipulate datasets. Developed by Wes McKinney in 2008, this powerful package can easily blend with various other data science modules in Python.

# 2. How do you quickly access the top 5 rows and last 5 rows of a pandas DataFrame?

# The head() method in pandas is used to access the first 5 rows of a DataFrame, and the tail() method is used to access the last 5 rows.

# To access the top 5 rows: dataframe_name.head()

# To access the last 5 rows: dataframe_name.tail()


# 3. Why doesn’t DataFrame.shape have parenthesis?
# In pandas, shape is an attribute and not a method. So, you should access it without parentheses.

# DataFrame.shape outputs a tuple with the number of rows and columns in a DataFrame.

# 4. What is the difference between a Series and a DataFrame?
# DataFrame: The pandas DataFrame will be in tabular format with multiple rows and columns where each column can be of different data types.

# Series: The Series is a one-dimensional labeled array that can store any data type, but all of its values should be of the same data type. The Series data structure is more like single column of a DataFrame.

# The Series data structure consumes less memory than a DataFrame. So, certain data manipulation tasks are faster on it.

# However, DataFrame can store large and complex datasets, while Series can handle only homogeneous data. So, the set of operations you can perform on DataFrame is significantly higher than on Series data structure.


# Pandas is built on top of the NumPy library, i.e., its data structures Series and DataFrame are the upgraded versions of NumPy arrays.



# 5. What is an index in pandas?
# The index is a series of labels that can uniquely identify each row of a DataFrame. The index can be of any datatype like integer, string, hash, etc.,

# df.index prints the current row indexes of the DataFrame df.


# Explain pandas reindexing

import pandas as pd

data = [['John', 50, 'Austin', 70],
        ['Cataline', 45 , 'San Francisco', 80],
        ['Matt', 30, 'Boston' , 95]]

columns = ['Name', 'Age', 'City', 'Marks']

#row indexes
idx = ['x', 'y', 'z']

df = pd.DataFrame(data, columns=columns, index=idx)

print(df)

# Reindex with new set of indexes:


new_idx = ['a', 'y', 'z']

new_df = df.reindex(new_idx)

print(new_df)

# 8. What is the difference between loc and iloc?
# Both loc and the iloc methods in pandas are used to select subsets of a DataFrame. Practically, these are widely used for filtering DataFrame based on conditions.

# We should use the loc method to select data using actual labels of rows and columns, while the iloc method is used to extract data based on integer indices of rows and columns.

# How do you get the count of all unique values of a categorical column in a DataFrame?

import pandas as pd

data = [['John', 50, 'Male', 'Austin', 70],
        ['Cataline', 45 ,'Female', 'San Francisco', 80],
        ['Matt', 30 ,'Male','Boston', 95]]

# Column labels of the DataFrame
columns = ['Name','Age','Sex', 'City', 'Marks']

# Create a DataFrame df
df = pd.DataFrame(data, columns=columns)

df['Sex'].value_counts()


#  How do you optimize the performance while working with large datasets in pandas?

# Load less data
# Avoid loops
# Use data aggregation
# Use the right data types
# Parallel processing


# What is the difference between the .join() and .merge() methods in pandas?
# Join: Joins two DataFrames based on their index. However, there is an optional argument ‘on’ to explicitly specify if you want to join based on columns. By default, this function performs left join.

# Syntax: df1.join(df2)

# Merge: The merge function is more versatile, allowing you to specify the columns on which you want to join the DataFrames. It applies inner join by default, but can be customized to use different join types like left, right, outer, inner, and cross.

# Syntax: pd.merge(df1, df2, on=”column_names”)

#  How do you sort a DataFrame based on columns?


# We have the sort_values() method to sort the DataFrame based on a single column or multiple columns.

# Syntax: df.sort_values(by=[“column_names”])

# Example code:


import pandas as pd

data = [['John', 50, 'Male', 'Austin', 70],
['Cataline', 45 ,'Female', 'San Francisco', 80],
['Matt', 30 ,'Male', 'Boston', 95],
['Oliver',35,'Male', 'New york', 65]]

# Column labels of the DataFrame
columns = ['Name','Age','Sex', 'City', 'Marks']

# Create a DataFrame df
df = pd.DataFrame(data, columns=columns)

# Sort values based on ‘Age’ column
df.sort_values(by=['Age'])

df.head()

# 17. Show two different ways to filter data

import pandas as pd

data = {'Name': ['John', 'Cataline', 'Matt'],
        'Age': [50, 45, 30],
        'City': ['Austin', 'San Francisco', 'Boston'],
        'Marks' : [70, 80, 95]}

# Create a DataFrame df
df = pd.DataFrame(data)

new_df = df[(df.Name == "John") | (df.Marks > 90)]
print (new_df)


df.query('Name == "John" or Marks > 90')
print (new_df)


# Difference between fillna() and interpolate() methods
# fillna() –

# fillna() fills the missing values with the given constant. Plus, you can give forward-filling or backward-filling inputs to its ‘method’ parameter.

# interpolate() –

# By default, this function fills the missing or NaN values with the linear interpolated values. However, you can customize the interpolation technique to polynomial, time, index, spline, etc., using its ‘method’ parameter.


# How do you perform one-hot encoding using pandas?
# We perform one hot encoding to convert categorical values to numeric ones so that can be fed to the machine learning algorithm.


import pandas as pd

data = {'Name': ['John', 'Cateline', 'Matt', 'Oliver'],
        'ID': [1, 22, 23, 36]}

df = pd.DataFrame(data)

#one hot encoding 
new_df = pd.get_dummies(df.Name)
new_df.head()

# What is the pandas method to get the statistical summary of all the columns in a DataFrame?

df.describe()