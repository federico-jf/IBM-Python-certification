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


#MULTIPLE REGRESSION

regr= linear_model.LinearRegression()
x = np.asanyarray(train[['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_CITY', 'FUELCONSUMPTION_HWY']])
y = np.asanyarray(train[['CO2EMISSIONS']])

regr.fit(x,y)
print('Coefficients: ', regr.coef_)
y_ = regr.predict(test[['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_CITY', 'FUELCONSUMPTION_HWY']])
x = regr.predict(test[['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_CITY', 'FUELCONSUMPTION_HWY']])
y = np.asanyarray(test[['CO2EMISSIONS']])

print("Residual sum of squares (MSE): %.2f"% np.mean((y_ - y) **2))
print('Variance score: %.2f' % regr.score(x, y))

#K-NEAREST NEIGHBORS
#K-NEAREST NEIGHBORS 
#K-NEAREST NEIGHBORS 
#K-NEAREST NEIGHBORS 
#K-NEAREST NEIGHBORS 
#K-NEAREST NEIGHBORS 

!pip install scikit-learn==0.23.1

import matplotlib.pyplot as plt
import pandas as pd
import pylab as pl
import numpy as np
from sklearn import preprocessing
%matplotlib inline

#open dataset

#To use scikit-learn library, we have to convert the Pandas data frame to a Numpy array.
X=df[['region', 'tenure', 'age', 'marital', 'gender']].values #.astype(float)
X[0:5]

#what are our labels?
y=df['custcat'].values
y=[0:5]

#Normalize data: data standarization gives teh data zero mean and unit variance, it is good practice, 
#especially for algorithms such as KNN which is based on the distance of data points

X=preprocessing.StandardScaler().fit.(X).transform(X.astype(float))
X[0:5]

#Train / Test split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test =train_ytest_split(X,y, test_size=0.2, random_state=4)
print('Train set:'. X_train.shape, y_train.shape)
print('Test set:'. X_test.shape, y_test.shape)

#Classification: K-nearest neighbor

from sklearn.neighbors import KneighborsClassifier

#let's start with K=4
k=4

#train the model and predict
neigh=KneighborsClassifier(n_neighbors=k).fit(X_train,y_train)
neigh

#we can use the model to make predictions on the test set

yhat=neigh.predict(X_test)
yhat[0:5]

#accuracy evaluation using the accuracy classification score: calculates how closely the actual labels and predicted labels are matched in the test set.
from sklearn import metrics
print("Train set Accuracy K=4: ", metrics.accuracy_score(y_train, neigh.predict(X_train)))
print("Test set Accuracy K=4: ", metrics.accuracy_score(y_test, yhat))


#Now test with K=6

k=6
neigh6=KneighborsClassifier(n_neighbors=k).fit(X_train,y_train)
yhat6=neigh6.predict(X_test)
print("Train set Accuracy K=6: ", metrics.accuracy_score(y_train, neigh.predict(X_train)))
print("Test set Accuracy K=6: ", metrics.accuracy_score(y_test, yhat))

#BUT how to calculate the idead number of K?. We can calculate the accuracy of KNN for different values of K.
ks=10
mean_acc= np.zeros((Ks-1))
std_acc= np.zeros((Ks-1))

for n in range(1,Ks):
  #train the model and predict
  neigh=KNeighborsClassifier(n_neighbors=n).fit(X_train, y_train)
  yhat=neigh.predict(X_test)
  mean_acc[n-a] = metrics.accuracy_score(y_test, yhat)
  
  std_acc[n-1] = np.std(yhat==y_test)/np.sqrt(yhat.shape[0])
mean_acc

print("The best accuracy was wiyth", mean_acc.max(), "with k= ", mean_acc.argmax()+1)


######## DECISION TREES ##########
######## DECISION TREES ##########
######## DECISION TREES ##########
######## DECISION TREES ##########
######## DECISION TREES ##########
######## DECISION TREES ##########
######## DECISION TREES ##########
######## DECISION TREES ##########


#surpress warnings and call libraries
def warn(*args, **kwargs):
  pass
import warnings
warnings.warn = warn

import sys
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import sklearn.tree as tree

#upload the data

#check size of data 
my_daya.shape

#remove the column containin the target name 
X= my_date[['Age', 'Sex', 'BP', 'Cholesterol', 'Na_to_K']].values
X[0:5]

#Since Sklearn decisions tree does not handle categorical variables, we can convert these variables to numerical values.
from sklearn import preprocessing
le_sex = preprocessing.LabelEncoder()
le_sex.fit(['F','M'])
X[:,1] = le_sex.transofm(X[:,1])

#now fill the target variable
y=my_data["Drug"]
y[0:5]

#setting up the decision tree
from sklearn.model_selection import rain_test_split

X_train, X_test, y_train, y_test =train_ytest_split(X,y, test_size=0.3, random_state=3)
print('Train set:'. X_train.shape, y_train.shape)
print('Test set:'. X_test.shape, y_test.shape)

#modelling
drugTree= DecisionTreeClassifier(criterion="entropy", max_depth=4)
drugTree

#fit
drugTree.fit(X_train, y_train)

#predict
predTree = drugTree.predict(X_test)

print(predTree [0:5])
print(y_test [0:5])

#Evaluation: near 1 is better than 0.
from sklearn import metrics
import matplotlib.pyplot as plt
print("Decision Trees's Accuracy: ", metrics.accuracy_score(y_test, predTree))

#visualize the tree
!conda install -conda-forge pydotplus -y
!conda install -conda-forge python-graphviz -y

from sklearn.tree import export_graphviz
export_graphviz(drugTree, out_file='tree.dot', filled=True, feature_names=['Age', 'Sex', BP', 'Cholesterol', 'Na_to_K'])
!dot -Tpng tree.dot o- tree.npg

  
