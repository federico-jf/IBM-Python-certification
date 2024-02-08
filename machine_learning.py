# Federico Ferrero

# SIMPLE REGRESSION

#import libraries

import matplotlib.pyplot as plt
import pandas as pd
import pylab as pl
import numpy as np
%matplotlib inline

#download data
#explore dataset

df.head()
df.dscribe()

#select some variables

cdf=df[['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_COMB', 'CO2EMISSIONS']]
cdf.head(9)

#visualize
viz =df[['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_COMB', 'CO2EMISSIONS']]
viz.hist()
plt.show()
  
#scatter
plt.scatter(cdf.ENGINESIZE, cdf.CO2EMISSIONS, color='blue')
plt.xlabel("Engine Size")
plt.ylabel("Emission")
plt.show()

#train ans test split will provide a more accurate evaluation on out-of-sample accuracy (80% training, 20% test)
msk = np.random.rand(len(df))<0.8
train = cdf[msk]
test = cdf[~msk]

#use sklearn package to model data

from sklearn import linear_model
regr= linear_model. LinearRegression()
train_x = np.asanyarray(train[['ENGINESIZE']])
train_Y = np.asanyarray(train[['CO2EMISSIONS']])
regr.fit(train_x,train_y)

print('Coefficients: ', regr.coef_)
print('Intercept: ', regr.intercept_)







  
