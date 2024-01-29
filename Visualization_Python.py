#Visualization with Python
#1/25/2024
#Federico Ferrero


################################################################################# LAB 1: Exploring and preprocessing data
#################################################################################
#################################################################################

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

################################################################################# LAB 2: LINE PLOT
#################################################################################
#################################################################################


import numpy as np
import pandas as pd

#Open the file
df_can = pd.read_excel(
  'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Canada.xlsx',
  sheet_name='Canada by Citizenship',
  skiprows=range(20),
  skipfooter=2)

#set Country as the index to plot charts easily, by refering to the country names as index values
df_can.set_index('Country', inplace=True)

#convert the years to strings:it will help later when plotting
years=list(map(str,range(1980,2014)))

#import matplotlib
#we are using the inline backend
%matplotlib line
import matplotlib as mpl
import matplotlib.pyplot as plt

#first, extract the data series for Haiti
#Since converted the years to string. Let's declare a variable as list of years.
years= list(map(str, range(1980,2014)))
#creating data series
haiti = df_can.loc['Haiti', years]
haiti.head()

#next plot 
haiti.plot()

#add labels
haiti.plot(kind='line)

plt.title('Immigration from Haiti')
plt.ylabel('Number of immigrants')
plt.xlabel('Years')

plt.show()

#add a note with "2010 Earthquake"
haiti.index=haiti.index.map(int) #change the index values to integer: we need to specify teh location of the text (y=6000 and x=2000)
haiti.plot(kind='line')

plt.title('Immigration from Haiti')
plt.ylabel('Number of immigrants')
plt.xlabel('Years')

plt.text(2000,6000,'210 Earthquak')
plt.show()

#now get the dataset for China and India and display it as dataframe
df_CI=df_can.loc[['India', 'China'], years]
df_CI

#first transpose the dataframe /  We did not have to transpose in the case of Haiti because it was not a dataframe but a series.
df_CI = df_CI.transpose()
df_CI.head()

#now plot
df_CI.index=haiti.index.map(int) #change the index values to integer
df_CI.plot(kind='line')

plt.title('Immigration from China and India')
plt.ylabel('Number of immigrants')
plt.xlabel('Years')

plt.show()

#compare the trends of top 5 countries that contributed the most to immigration to Canada
inplace = True
df_can.sort_values(by='Total', ascending=False, axis=0, inplace=True)
top_5=df_can.head(5)
top_5

df_top5 = df_top5[years].transpose()
df_top5.head()

#now plot
df_top5.index=haiti.index.map(int) #change the index values to integer
df_top5.plot(kind='line')

plt.title('Top 5 Countries that Contributed the Most to Immigration to Canada')
plt.ylabel('Number of immigrants')
plt.xlabel('Years')

plt.show()

################################################################################# LAB 3: ADVANCED VISUALIZATIONS
#################################################################################
#################################################################################


import numpy as np
import pandas as pd


#import matplotlib
#we are using the inline backend
%matplotlib line
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.style.use('ggplot') # for ggplot-like style

#Open the file
df_can = pd.read_excel(
  'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Canada.xlsx',
  sheet_name='Canada by Citizenship',
  skiprows=range(20),
  skipfooter=2)

df_can.head

print(df_can.shape)

#set Country as the index to plot charts easily, by referring to the country names as index values
df_can.set_index('Country', inplace=True)

#create list of years from 1080-2013
years= list(map(str, range(1980,2014)))

######## AREA PLOT (describe the MAGNITUD and PROPORTION)
########
########

#THIS IS THE CODE WHEN WE USE THE SCRIPTING LAYER (procedureal method, we use matplotlib)

df_can.sort_values(by='Total', ascending=False, axis=0, inplace=True)
top_5=df_can.head(5)
top_5 = df_top5[years].transpose()

df_top5.head()

#now plot
df_top5.index= df_top5.index.map(int) #change the index values to integer
df_top5.plot(kind='area',
             alpha=0.25,  #alpha changes the transparency
             stacked=False,
            figsize=(20,10))

plt.title('Immigration Trend of Top 5 Countries')
plt.ylabel('Number of immigrants')
plt.xlabel('Years')

plt.show()

# THIS IS CODE WHEN WE USE THE ARTIST LAYER (using axes): use the artist layer (use ax.) to create an unstacked plot of the 5 countries that contributed the least to immigration to Canada. Transparency value of 0.55

df_least5 = df_can.tail(5)
df_least5 = df_least5[years].transpose()
df_least5.head()

df_least5.index= df_least5.index.map(int) #change the index values to integer
ax = df_least5.plot(kind='area',
             alpha=0.55,  #alpha changes the transparency
             stacked=False,
            figsize=(20,10))

ax.set_title('Immigration Trend of 5 Countries with Less Contribution to Immigration')
ax.set_ylabel('Number of immigrants')
ax.set_xlabel('Years')


######## HISTOGRAM
########
########

#bin_edges is a list of bin intervals
count, bin_edges = np.histogram(df_can['2013'])

df_can['2013'].plot(kind='hist',figsize=(8,5), xticks = bin_edges)
plt.title('Histogram of Immigration to Canada from 195 Countries in 2013')
plt.ylabel('Number of Countries')
plt.xlabel('Number of Immigrants')

plt.show()

# plot multiple histograms on the same plot

df_t = df_can.loc['Denmark', 'Norway', 'Sweden'], years.transpose()

df_t.plot(kind='hist',figsize=(10,6))
plt.title('Histogram of Immigration from Denmark, Norway, and Sweden from 1980 - 2013')
plt.ylabel('Number of Years')
plt.xlabel('Number of Immigrants')

plt.show()

# improve the previous plot

count, bin_edges = np.histogram(df_t, 15) #increase the bin size to 15

df_t.plot(kind='hist',figsize=(10,6), bins = 15, alpha =0.6, xticks=bin_edges, color=['coral', 'darkslateblue', 'mediumseagreen'])
plt.title('Histogram of Immigration from Denmark, Norway, and Sweden from 1980 - 2013')
plt.ylabel('Number of Years')
plt.xlabel('Number of Immigrants')

plt.show()

######## BAR CHARTS
########
########

df_iceland = df_can.loc['Iceland', years]
df_iceland.head()

#next plot 
df_iceland.plot(kind='bar', figsize=(10,6))

plt.title('Icelandic immigrants to Canada from 10980 to 2013')
plt.ylabel('Number of immigrants')
plt.xlabel('Years')

#annotate arrow
plt.annotate('',
              xy=(32,70),
              xytext=(28,20),
              xycoords='data',
              arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='blue',lw=2)
              
#annotate text
plt.annotate('2008-2011 Financial Crisis',
             xy=(28,30),
             rotation=72.5,
             va='bottim',
             ha='left,)
plt.show()


# barh is to generate horizontal bar charts

######## PIE CHART
########
########

import numpy as np
import pandas as pd


#import matplotlib
#we are using the inline backend
%matplotlib line
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.style.use('ggplot') # for ggplot-like style

#Open the file
df_can = pd.read_excel(
  'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Canada.xlsx',
  sheet_name='Canada by Citizenship',
  skiprows=range(20),
  skipfooter=2)

df_can.head

print(df_can.shape)

#set Country as the index to plot charts easily, by referring to the country names as index values
df_can.set_index('Country', inplace=True)

#create a list of years from 1980- 2013
years = list(map(str,range(1980, 2014)

#group countries by continent and apply a sum
df_continents = df_can.groupby('Continent', axis=0).sum()

#plot
df_continents['Total'].plot(kind='pie',
                            figsize=(5,6),
                           autopct='%1.1f%%', 
                           startangle=90,
                          labels=None,
                            pctdistance=1.12,
                           shadow=True,
                           )

plt.title('Immigration to Canada by Contnent from 1980 to 2013')
plt.axis('equal')
plt.legend(labels=+df_continents.index, loc='upper left', fontsize=7)

plt.show()
             

######## BOXPLOT
########
########
df_CI= df_can.loc[['China', 'India'], years].transpose()

df_japan= df_can.loc[['Japan'], years].transpose()
df_japan.plot(kind='box', figsize=(8,6))

plt.title('Box plot of Japanese Immigrants to Canada from 1980 to 2013')
plt.ylabel('Number of immigrants')

plt.show()

df_japan.describe()
                    
#horizontal boxplot: add vert at the end of this line of code: df_japan.plot(kind='box', figsize=(8,6), vert=False)

####SUBPLOTS: SEE more than one plot in the page

fig = plt.figure() #create a figure
ax0 = fig.add_subplot(1,2,1) #add subplot 1(1row, 2 columns, first plot)
ax1 = fig.add_subplot(1,2,2) #add subplot 1(1row, 2 columns, second plot)

#subplot 1: boxplot
df_CI.plot(kind='box',figsize=(20,6), ax=ax0)
ax0.set_title('Boxplot')
ax0.set_xlabel('xlabel')
ax0.set_ylabel('ylabel')

#subplot 2: linechart
df_CI.plot(kind='line',figsize=(20,6), ax=ax1)
ax0.set_title('line chart')
ax0.set_xlabel('xlabel')
ax0.set_ylabel('ylabel')

plt.show()

#create alis of all years in decades 80s 90s 00s. Then sum.
years_80= list(map(str, range(1980, 1990)))
years_90= list(map(str, range(1990, 2000)))
years_00= list(map(str, range(2000, 2010)))

df_80 = df_top15.loc[:,years_80].sum(axis=1)
df_90 = df_top15.loc[:,years_90].sum(axis=1)
df_00 = df_top15.loc[:,years_00].sum(axis=1)

 new_df = pd.DataFrame({'1980s':df_80, '1990s':df_90, '2000s':df_00})
 new_df.head()


######## SCATTER PLOT
########
########

df_tot.plot(kind='scatter', x='year', y='total', figsize=(10,6), color='darkblue')

plt.title('Total Immigration to Canada from 1980 to 2013')
plt.xlabel('Years')
plt.ylabel('Number of Immigrants')

plt.show()

#fit a linear line
x= df_tot['year']
y= df_tot['total']
fit= np.polyfit(x,y, deg=1)
fit

df_tot.plot(kind='scatter', x='year', y='total', figsize=(10,6), color='darkblue')

plt.title('Total Immigration to Canada from 1980 to 2013')
plt.xlabel('Years')
plt.ylabel('Number of Immigrants')

plt.plot(x,fit[0] * x + fit[1], color = 'red')
plt. annotate('y={0:.0f} x + {1:.0f}'.format(fit[0], fit[1], xy=(2000, 150000))

plt.show()

#create a scatterplot with totals for Denmark, Norway, Sweden
#create dataframe
df_countries = df_can.loc[['Denmark', 'Norway', 'Sweden'], years].transpose()
#create df_total
df_total = pd.DataFrame(df_countries.sum(axis=1))
#reset index in place
df_total.reset_index(inplace=True)
#rename columns
df_total.columns=['year', 'total']
#change year form string to int
df_total['year'] = df_total['year'].astype(int)
df_total.head()

df_total.plot(kind='scatter', x='year', y='total', figsize=(10,6), color='darkblue')

plt.title('Total Immigration to Canada from 1980 to 2013: Denmark, Seweden, Norway')
plt.xlabel('Years')
plt.ylabel('Number of Immigrants')

######## BUBBLE PLOT
######## variation of scatter plot that displays three dimension data (x,y,z)
########

#normalize data
norm_china = (df_can_t['China'] - df_can_t['China'].min()) / (df_can_t['China'].max() - df_can_t['China'].min())
norm_india = (df_can_t['India'] - df_can_t['India'].min()) / (df_can_t['India'].max() - df_can_t['India'].min())

#now plot
#China
ax0 = df_can_t.plot(kind='scatter',
                    x='Year',
                    y='China',
                    figsize=(14,8),
                    alpha=0.5,
                    color='green',
                    s=norm_china *2000+10,
                    xlim=(1975,2015)
                   )
#Indian
ax1 = df_can_t.plot(kind='scatter',
                    x='Year',
                    y='India',
                    figsize=(14,8),
                    alpha=0.5,
                    color='blue',
                    s=norm_india *2000+10,
                    ax=ax0
                   )

ax0.set_ylabel('Number of Immigrants')
ax0.set_title('Immigration from China and India from 1980 - 2013')
ax0.legend(['China', 'India'], loc='upper left', fontsize='x-large')

######## WAFFLE CHART
######## 
########

!pip install pywaffle

#import Waffle from pywaffle
from pywaffle import Waffle

#Set up the Waffle chart figure

fig = plt.figure(FigureClass = Waffle,
                 rows = 20, columns = 30, #number of rows and columns for the waffle
                 values = df_dsn['Total'], #the data to be used for display
                 cmap_name= 'tab20', #color scheme
                 legend = {'labels': [f"{k} ({v})" for k, v in zip (df_dsn.index.values, df_dsn.Total)],
                           'loc':'lower left', 'bbox_to_anchor':(0,-0,1), 'ncol':2}
                  )
plt.show

#create a waffle chart to display the proportion of China and India total immigrant contribution

df_CI=df_can.loc[['China', 'India'], :]
fig = plt.figure(FigureClass = Waffle,
                 rows = 20, columns = 30, 
                 values = df_CI['Total'], 
                 cmap_name= 'tab20', 
                )
plt.show

######## WORD CLOUDS
######## 
########

from wordcloud import WordClous, STOPWORDS

import urllib
#open file from url

stopwords=set(STPWORDS)

...

######## REGRESSION PLOT
######## 
######## USE SEABORN! IT simplifies everything

#call seaborn library
   
df_countries=df_can.loc[['Denmark', 'Norway', 'Sweden'], years].transpose()
df_total=pd.DataFrame(df_countries.sum(axis=1))
df_total.reset_index(inplace=True)
df_total.columns=['year', 'total']
df_total['year'] = df_total['year'].astype(int)

plt.figure(figsize=(15,10))

sns.set(font_scale=1.5)
sns.set_style('whitegrid')

ax=sns.regplot(x='year', y='total', data=df_total, color='green', marker='+', scatter_kws={'s':200})
ax.set(xlabel='Year', ylabel='Total Immigration')
ax.set_title('Total Immigration from Denmark, Sweden, and Norway to Canada from 1980 to 2013')

                   
          
