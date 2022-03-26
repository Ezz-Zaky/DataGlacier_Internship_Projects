# Simple Linear Regression

"""## Importing the libraries"""

import numpy as np
import pandas as pd
import pickle

"""## Importing the dataset"""

dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

"""## Splitting the dataset into the Training set and Test set"""

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

"""## Training the Simple Linear Regression model on the Training set"""

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

"""## Predicting the Test set results"""

y_pred = regressor.predict(X_test)


"""# Saving model to disk"""
pickle.dump(regressor, open('model.pkl','wb'))

"""# Loading model to compare the results"""
model = pickle.load(open('model.pkl','rb'))
print(model.predict([[5]]))