# Medical Insurance Lab
# 1/24/2024
# Federico Ferrero 


#      IMPORT THE DATASET 
# Import libraries 
import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 
import seaborn as sns 
from sklearn.pipeline import Pipeline 
from sklearn.preprocessing import StandardScaler, PolynomialFeatures 
from sklearn.linear_model import LinearRegression, Ridge 
from sklearn.metrics import mean_squared_error, r2_score 
from sklearn.model_selection import cross_val_score, train_test_split 
 
# download the dataset 
 
# print the first 10 rows 
df = pd.read_csv(path, header=None) 
print(df.head(10)) 
 
# add headers to dataset 
headers = ["age", "gender", "bmi", "no_of_children", "smoker", "region", "charges"] 
df.columns = headers 
 
# now replace the ‘?’ with NaN 
df.replace(‘?’, np.nan, inplace = True) 
 
#        DATA WRANGLING 
# use dataframe. Info() to identify the columns that have some Null inform 
print(df.info()) 
 
# smoker is a categorical attribute, replace with most frequent entry 
is_smoker = df[‘smoker’].value_counts().idxmax() 
df[“smoker”].replace(np.nan, is_smoker, inplace=True) 
 
# age is a continuous attribute, replace with mean age 
mean_age = df[‘age’].astype(‘float’).mean(axis=0) 
df[“age”].replace(np.nan, mean_age, inplace=True) 
 
# update data types 
df[[“age”, “smoker”]] = df [[“age”, “smoker”]]. astype(“int”) 
 
# print and now we have to have the same number (2771) with non-null in each variable. Check also the types of variables. 
print (df.info()) 
 
# round to 2 decimal places the variable charge 
df[[“charges”]] = np.round(df[[“charges”]],2) 
print(df.head()) 
 
#        EXPLORATORY DATA ANALYSIS (EDA) 
# regression plot for charges with respect to bmi 
width = 12 
height = 10 
plt.figure(figsize=(width,height)) 
sns.regplot(x=”bmi”, y=”charges”, data=df, line_kws={“color”: “red”}) 
plt.ylim(0,) 
 
# regression plot for charges with respect to smoker 
width = 12 
height = 10 
plt.figure(figsize=(width,height)) 
sns.regplot(x=”smoker”, y=”charges”, data=df, line_kws={“color”: “red”}) 
plt.ylim(0,) 
 
# print the correlation matrix for the dataset. Higher correlations with charges are: smoker, age, and bmi. 
print(df.corr()) 
 
 
#            MODEL DEVELOPMENT 
# fit linear regression model: y=charges, x= smoker. Print the r squared. 
lm = LinearRegression() 
X=df[[‘smoker’]] 
Y=df[‘charges’] 
lm.fit(X,Y) 
print(‘The R-squared is: ’, lm.score(X,Y)) 
 
# another alternative to code the fit line 
lm.fit(df[[‘smoker]], df [[‘charges’]]) 
 
# fit multiple regression with all the variables in the dataset. Print r squared and see the improvement. 
Z=df[[‘age’, ‘gender’, ‘bmi’,’no_of_children’, ‘smoker’, ‘region’]] 
lm.fit(Z, df[‘charges’]) 
print(‘The R-squared is: ’, lm.score(Z,Y)) 
 
# create a training pipeline that uses StandardScaler(), PolynomialFeatures() and LinearRegression() to create a model that can predict the charges value using all the other attributes of the dataset. There should be even further improvement in the performance. 
# Y and Z use the same values as defined previously. 
Input=[(‘scale’, StandardScaler()), (‘polynomial’, PolynomialFeatures(include_bias=False)), (‘model’, LinearRegression())] 
pipe=Pipeline(Input) 
Z= Z.astype(float) 
pipe.fit(Z,Y) 
ypipe=pipe.predict(Z) 
print(r2_score(Y,ypipe)) 
 
#                MODEL REFINEMENT 
# split the data into training and testing subtests, assuming that 20% of the data will be reserved for testing. 
x_train, x_test, y_train, y_test = train_test_split(Z, Y, test_size=0.20,random_state=0) 
print(“Number of test samples: ”, x_test.shape[0]) 
print(“Number of training samples: ”, x_train.shape[0]) 
 
# Initialize a Ridge regressor that used hyperparameter alpha = 0.1. Fit the model using training data data subset. Print the r squared scores for the testing data. 
# x_train, x_test, y_train, y_test hold same values as reviously. 
RidgeModel = Ridge(alpha=0.1) 
RidgeModel.fit(x_train, y_train) 
yhat =  RidgeModel.predict(x_test) 
print(r2_score(y_test,yhat)) 
 
# Apply polynomial transformation to the training parameters with degree = 2. Use this transformed feature set to fit the same regression model, as above, using the training subset. Print the R squared score for the training subset. 
# x_train, x_test, y_train, y_test hold same values as previously. 
pr=PolynomialFeatures(degree=2) 
x_train_pr = pr.fit_transform(x_train) 
x_test_pr = pr.fit_transform(x_test) 
RidgeModel.fit(x_train_pr, y_train) 
y_hat =  RidgeModel.predict(x_test_pr) 
print(‘The R-squared is: ’, r2_score(y_test,y_hat)) 
