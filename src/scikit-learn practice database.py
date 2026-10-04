""""

Learning scikit-learn workflow using its own built-in datasets:
Eg. load_diabetes or fetch_california_house with a simple Linear Regression Model
train_test_split | .fit() | .predict() | mean_squared_error / r2_score  |

scikit-learn expects X as a 2D array-like structure/features (rows=samples, columns=features),
and y as a 1D array (the target you're predicting).

Starting with a toy dataset workflow: sklearn.datasets.fetch_california_housing()
This returns housing data where you predict median house value from features like income,
number of rooms, location.

from sklearn.preprocessing import StandardScaler

"""

from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd

data = fetch_california_housing()
pd.DataFrame(data.data, columns=data.feature_names)
""" 
pd.DataFrame is the command that builds the spreadsheet from the array of numbers.
data.data is the actual grid/array of numbers with no columns
columns=data.feature_names says use this list as the column headers.
We then assign this to X (the 2D array): 
"""

X = pd.DataFrame(data.data, columns=data.feature_names)
X.head()
print(X.head())

y = data.target

""" print(data.data.shape)
#This tells us how many (rows, columns) of data there is: (20640, 8)
print(data.feature_names)
#This tells us the names of the columns: ['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms',
#'Population', 'AveOccup', 'Latitude', 'Longitude']
print(data.target[:5])
#This tells us the first 5 target values (house prices) """

""".data is the features, .feature_names is what each column means .target is what i'm trying 
to predict (the house prices)"""

#The train/test split - we split the data into 2:
#1. a training set - the data the model learns patterns from
#2. a test set - data the model hasn't seen, to test on
#It's counter-intuitive to test the model on the same data it trained from, the model would
#just be memorising and regurgitating data, instead of identifying a pattern

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#test_size=0.2 means we are testing the model on 20% of the data, and training/predicting 80%
#random_state=42, the integer can be anything, it's a seed number that controls the "shuffle"
#before splitting the data 20/80, without it, everytime the code runs, the random split is different.

#Now we can run the data: print(X_train.shape), print(y_train.shape)

print(X_train.shape)
print(X_test.shape)

#Step 4: Creating and fitting the model
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)
"""
- To create an instance of a class, apply parentheses to the end, this makes the 
(LinearRegression) model usable.
- model.fit is how we will train the model on the seen data, so we use X_train and y_train
as this is the data  the Linear Regression model will be trained on, it will see this data,
then apply it to the unseen X_test, y_test data later.
"""

#Upon running with no errors, the model has now learned patterns from the X_train, y_train data
#and is ready for prediction on the test set: X_test, y_test

lr_predictions = model.predict(X_test)
#Essentially, make predictions using X_test data only, as y_test is our target/answers we will
#be comparing it to - it would be useless to feed the predictor the answers.
print(lr_predictions[:5])
print(y_test[:5])

from sklearn.metrics import mean_squared_error, r2_score
lr_r2 = r2_score(y_test, lr_predictions)
lr_mse = mean_squared_error(y_test, lr_predictions)

print(f"Linear Regression R2 value: {lr_r2:.3f}")
print(f"Linear Regression MSE value: {lr_mse:.3f}")

from sklearn.ensemble import RandomForestRegressor

rfr_model = RandomForestRegressor()
rfr_model.fit(X_train, y_train)

rfr_predictions = rfr_model.predict(X_test)

rfr_r2 = r2_score(y_test, rfr_predictions)
rfr_mse = mean_squared_error(y_test, rfr_predictions)

print(f"Random Forest Regressor R2 value: {rfr_r2:.3f}")
print(f"Random Forest Regressor MSE value: {rfr_mse:.3f}")