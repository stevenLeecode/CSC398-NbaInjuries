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

X = df.loc[:, 'mp_x':'x3pa']
y = df.loc[:, 'injuries']

#----------------Linear Regression Model-----------------------# 

# Generate the train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=1)

# Create the model
lr_model = LinearRegression()

# Train the model
lr_model.fit(X_train, y_train)

# Make predictions
y_pred = lr_model.predict(X_test)
y_pred = np.round(y_pred, 2)

# model evaluation
print('Mean absolute error : ', mean_absolute_error(y_test, y_pred))
print('R squared : ', r2_score(y_test, y_pred))

print('Coefficients: ', lr_model.coef_)
print('Intercept: ', lr_model.intercept_)