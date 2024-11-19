# print(" श्री ")
print("|| Shree Ganeshay Namah: ||")
import pandas as pd 
import numpy as np
# df = pd.read_csv('data.csv')

# reading the Text File and adding the seperator to display the data
df = pd.read_csv('data.txt',delimiter="\t")
# print(df.head(6))
# print(df.head(5))   
# print(df.tail(5))

# reading Data in pandas
# print(df.columns) #this will return the list of Columns

# look at the specific Column
# print(df['Name'][0:6])
# print(df.Name[0:5])

# print multiple Columns 
# print(df[['Name','Type 1', 'Type 2', 'HP']][0:10])

# Print each row by the location which you want to Print
 
# print(df.iloc[0:4])
# print(df.iloc[2:1])

# Itterate over the row

# for index, rows in df.iterrows():
#     print(index ,"\n", rows[['Name','Type 1']])


# print(df.loc[df['Type 1']=="Fire"])
# print(df.describe())

# print(df.sort_values('Name' ,ascending=False))
# print(df.sort_values(['Name', "Type 1"], ascending=[True,False]))

# Making some changes into data
df['total'] = df['HP']+df.Attack+df.Defense+ df['Sp. Atk']+df['Sp. Def']+df['Speed']
# print(df.head(5))
# df= df.drop(columns=['total'])
# print(df.head(5))


# df['Total'] = df.iloc[:,4:10].sum(axis=1)
# print(df.head(5))
# columns =  list(df.columns.values)
# print(columns)


# Modification of the columns
df["total"] = df.iloc[:,4:10].sum(axis=1)

cols =list (df.columns.values)

# print((cols))
df = df[cols[0:4]+[cols[-1]]+cols[4:12]]
# print(df.iloc(6))
# df.to_csv('modifid.csv',index=False)
# Dont miss to add the seperator
# df.to_csv('modified.txt',index=False,sep="\t")


# Rows are converted into columns and columns are get converted into rows
# df = df.T  # transpose of The current 
# print(df) 

# convert data frame into the  numpi array
# array = df.to_numpy()
# print(array) 

# print(df)


# print(df.loc[[1,2],:]) # print only two rows

# print(df.loc[:,[1,2]])
# newdf = df.copy()
# # print(newdf.drop([1,5], axis=0))
# newdf  = newdf.drop([1,5],axis=0)
# newdf.reset_index() # this will rest the index and again start from 1 to n

# print(newdf.head(6))


# ndf = pd.DataFrame({"name": ['Alfred', 'Batman', 'Catwoman'],
#                    "toy": [np.nan, 'Batmobile', 'Bullwhip'],
#                    "born": [pd.NaT, pd.Timestamp("1940-04-25"),
#                             pd.NaT]})

# print(ndf)
# print()
# ndf = ndf.dropna()
# print(ndf)
# print()
# print()
# df = pd.DataFrame({
#     'brand': ['Yum Yum', 'Yum Yum', 'Indomie', 'Indomie', 'Indomie'],
#     'style': ['cup', 'cup', 'cup', 'pack', 'pack'],
#     'rating': [4, 4, 3.5, 15, 5]
# })
# print(df)
# df = df.drop_duplicates(subset=['brand','style'],keep='last')
# print("\n\n",df)
# # df.drop_duplicates()


# newdf = df.loc[df['Speed']>140]
# print("Printing the Records over Hp > 80")
# # print()
# newdf.to_csv('Speed_90.csv',index=False)


# import re 
df = df.loc[(df['Name'].str.contains("Mega")) & (df['Speed']>140)]
# df = df.loc[(df['Name'].str.contains("Mega")) & (df['Speed'] > 100)]
print("Printing DF")
print(df)