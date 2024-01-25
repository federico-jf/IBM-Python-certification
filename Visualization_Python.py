#Visualization with Python
#1/25/2024
#Federico Ferrero

import numpy as np
import pandas as pd

#Open the file
df_can = pd.read_excel(
  'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Canada.xlsx',
  sheet_name='Canada by Citizenship',
  skiprows=range(20),
  skipfooter=2)

#see the 5 top rows
df_can.head()

#info about the dataset
df_can.info(verbose=False)

#size of the dataframe
df_can.shape

#add a total column with total number of immigrants per country
df_can['Total'] = df_can.sum(axis=1)
df_can['Total']

#check how many with null values
df_can.isnull().sum()

#summary statistics
df_can.describe()

#filter columns Country
df_can.Country
df_can.[['Country', 1980, 1981,1982,1983,1984]]

#filter Japon for years 1980 to 1984
df_can.loc['Japan', [1980, 1981,1982,1983,1984]]

#create a list named 'year using map function for years from 1990 to 2013. Then extract the data serues from dataframe df_can for Haiti using year list
year = list(map(str,range(1990,2014)))
haiti = df_can.loc['Haiti', year]

#filter data where AreaName is Africa and RegName is Shouthern Africa, Display it as dataframe
df_can[(df_can['AreaName']=='Africa') & (df_can['RegName']=='Southern Africa')]

#find the top 3 countries that contributes the most to immigration to Canada in the year 2010
df_can.sort_values(by='2010', ascending=False, axis=0, inplace=True)
top_3=df_can.head(3)
top_3
