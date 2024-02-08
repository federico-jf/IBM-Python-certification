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
train_y = np.asanyarray(train[['CO2EMISSIONS']])
regr.fit(train_x,train_y)

print('Coefficients: ', regr.coef_)
print('Intercept: ', regr.intercept_)

#plot the fit line over the data
plt.scatter(cdf.ENGINESIZE, cdf.CO2EMISSIONS, color='blue')
plt.plot(train_x, regr.coef_[0][0]*train_x + regr.intercept_[0], 'r')
plt.xlabel("Engine Size")
plt.ylabel("Emission")
plt.show()

#evaluation of the model: compare actual values with the predicted values. (R2)
from sklearn.metrics import r2_score

test_x = np.asanyarray(test[['ENGINESIZE']])
test_y = np.asanyarray(test[['CO2EMISSIONS']])
test_y_ = regr.predict(test_x)

print("Mean absolute error: %.2f" % np.mean(np.absolute(test_y_ - test_y)))
print("Residual sum of squares (MSE): %.2f" % np.mean((test_y_ - test_y) **2))
print("R2-score: %.2f" % r2_score(test_y - test_y_))








  
