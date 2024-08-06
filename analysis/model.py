from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Load cleaned data
atlas_df = pd.read_csv('data/processed/cleaned_Atlas_Data.csv')

features = ['GroceryStores', 'Supercenters', 'ConvenienceStores', 'SpecialtyStores', 'SNAPAuthorizedStores']
target = 'FoodInsecurityRate'
X, y = atlas_df[features], atlas_df[target]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Model Training
model = LinearRegression()
model.fit(X_train, y_train)

# Step 4: Model Evaluation
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)


# Print evaluation metrics
print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")
#
## Visualize Results and Regression Line
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, label='Predicted vs Actual')
plt.xlabel("Actual Food Insecurity Rate")
plt.ylabel("Predicted Food Insecurity Rate")
plt.title("Actual vs Predicted Food Insecurity Rate")
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', label='Regression Line')  # Regression line
plt.legend()
plt.savefig('vis/actual_vs_predicted.png')
plt.show()



##