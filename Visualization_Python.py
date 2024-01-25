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
