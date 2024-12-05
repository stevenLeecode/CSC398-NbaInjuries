#Steven

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('total_injuries.csv')

X = df.loc[:, 'mp_x':'x3pa']
y = df.loc[:, 'injuries']

# Generate the train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=1)

# Define the model.
knn = KNeighborsRegressor(n_neighbors = 7, weights = 'uniform')

# "Train" the model
knn.fit(X_train, y_train)

# Run the model to make predictions based on test data
y_pred = knn.predict(X_test)
print('R squared on mp -> 3pa: ', knn.score(X_test, y_test))

#------------------------Predicting based on input------------------------------#

# Define the X columns (independent variables / features) and
# y variable (label / target - what we want to predict)

#Taking out Experience made the r squared value go up
#X = df.loc[:, 'season']
X = df[['season']]
y = df.loc[:, 'injuries']

# Generate the train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=1)


# Define the model.
knn = KNeighborsRegressor(n_neighbors = 7, weights = 'uniform')

# "Train" the model
knn.fit(X_train, y_train)

# Run the model to make predictions based on test data
y_pred = knn.predict(X_test)

print('R squared on only season variable: ', knn.score(X_test, y_test))


season = int(input('Enter season to predict: '))

prediction = knn.predict([[season]])
print(f'Predicted injuries for year {season}: {prediction[0]}')