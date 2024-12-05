#Steven

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import numpy as np

df = pd.read_csv('total_injuries.csv')

# Define the X columns (independent variables / features) and
# y variable (label / target - what we want to predict)

#taking out experience increases r squared by 0.03 percent
X = df.loc[:, 'mp_x':'x3pa']
y = df.loc[:, 'injuries']

# Generate the train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=1)

#----------------Random Forest Regression Model-----------------------# 

# Create the model
rf_regr = RandomForestRegressor(max_depth=2, random_state=1)

# Train the model
rf_regr.fit(X_train, y_train)

# Make predictions
y_pred = rf_regr.predict(X_test)

# Evaluate
print("Random Forest Regression Model: ")
print('R squared: ', rf_regr.score(X_test, y_test))
