import pandas as pd

url = "https://deepchemdata.s3-us-west-1.amazonaws.com/datasets/delaney-processed.csv"
esol_data = pd.read_csv(url)

print(esol_data.shape)
print(esol_data.columns)
print(esol_data.head())

"""
Important column names: 
- "measured log solubility in mols per litre" --> this is my target, y
- "Minimum Degree", "Molecular Weight", "Number of H-Bond Donors", "Number of Rings", 
"Number of Rotatable Bonds", "Polar Surface Area" --> these pre-computed numeric descriptors
will become my X
"""

X = esol_data[["Molecular Weight", "Number of Rotatable Bonds", "Number of H-Bond Donors", "Number of Rings", "Polar Surface Area", "Minimum Degree"]]
y = esol_data["measured log solubility in mols per litre"]
X.head()
y.head()
print(X.head())
print(y.head())
#y has the measured log solubility values, which are negative. This is normal as organic
# compounds are often not very soluble

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"X_train shape (number of trained rows of data): {X_train.shape}")
print(f"X_test shape (number of tested rows of data: {X_test.shape}")

from sklearn.linear_model import LinearRegression

lr_model = LinearRegression()
lr_model.fit(X_train, y_train)

lr_predictions = lr_model.predict(X_test)

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

print(rfr_predictions[:5])
print(y_test[:5])

rfr_r2 = r2_score(y_test, rfr_predictions)
rfr_mse = mean_squared_error(y_test, rfr_predictions)

print(f"Random Forest Regressor R2 value: {rfr_r2:.3f}")
print(f"Random Forest Regressor MSE value: {rfr_mse:.3f}")