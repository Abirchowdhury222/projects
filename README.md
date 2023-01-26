We have some several steps in our project - 

1.Importing the dependencies  

I run my project on google colaboratory environment from the option .after uploaded my dataset firstly I import the library such as numpy pandas etc. 

Basic library- import numpy as np 

For framing data- Import pandas as pd 

Import sklearn.model_selection import train_test_split 

I use a logistic regression model so from sklearn.linear_model I import logistic regression . 

For accuracy score from sklearn.metrics imported accuracy_score 

Numpy will help us for creating numpy array . 

Pandas will help us for creating data frames. 

2.Data collection and processing  

Load my data or csv file to the pandas data frame by using pd function .i use the path of csv file to load it into the pandas data frame. 

The last attribute in every row is the target attribute. I have to predict this particular target values it can be 0 or 1. I name it heart_data of my data frame. 

 
 

heart_data.head() -show us first five rows . 

heart_data.tail() - show us last five rows . 

heart_data.shape -show us number of rows and columns in the dataset. 

heart_data.info() -show us total num of entries in my dataframe. 

Heart_data.isnull().sum() -checking for missing values. 

3.Splitting the features and target 

It’s the prediction of wether the person has heart disease or not.so its either 0 or 1. so we need to remove this target from this data frame store it separately. 

I creat two variable x & y .so I can store all the features in the variable x and store the target column in the variable y. 

4. Splitting data into training data & test data  

I creat my variables here x_train, x_test, y_train, y_test. So we can split x & yin it. 

5.Model training  

Model.fit function will try to find relationship pattern  between the features and the target .so once we train the model we can use this trained model to predict new values . 

6.Model evaluation  

How well it is performing ? Now it is the big question ! 

We need to use to use accuracy score & our evaluation metric .we have already imported this ones .we now evaluate the model on training data & test data. 

7.Building a predictive system  

Successfully predicted our target value for given data.and for that we have to build the predictive system. 
