import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import os

# Ensure the evaluation directory exists
os.makedirs('data/evaluation', exist_ok=True)

def select_features_and_target(df, features, target):
    """
    selects the features and target variable from the DataFrame.
    """
    try:
        X = df[features]
        y = df[target]
        return X, y
    except KeyError as e:
        print(f"Key error: {e}")
        raise
    except Exception as e:
        print(f"An error occurred while selecting features and target: {e}")
        raise

def split_data(X, y, test_size=0.2, random_state=42):
    """
    splits the data into training and testing sets.
    """
    try:
        return train_test_split(X, y, test_size=test_size, random_state=random_state)
    except Exception as e:
        print(f"An error occurred while splitting data: {e}")
        raise

def train_model(X_train, y_train):
    """
    trains a linear regression model on the training data.
    """
    try:
        model = LinearRegression()
        model.fit(X_train, y_train)
        return model
    except Exception as e:
        print(f"An error occurred while training the model: {e}")
        raise

def evaluate_model(model, X_test, y_test):
    """
    evaluates the model's performance on the test data.
    """
    try:
        y_pred = model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        return mse, r2
    except Exception as e:
        print(f"An error occurred while evaluating the model: {e}")
        raise

def save_evaluation_metrics(mse, r2, filepath):
    """
    saves the evaluation metrics to a CSV file.
    """
    try:
        evaluation_metrics = {
            'Metric': ['Mean Squared Error', 'R-squared'],
            'Value': [mse, r2]
        }
        evaluation_df = pd.DataFrame(evaluation_metrics)
        evaluation_df.to_csv(filepath, index=False)
    except Exception as e:
        print(f"An error occurred while saving evaluation metrics: {e}")
        raise

def visualize_results(y_test, y_pred, filepath):
    """
    visualizes the actual vs predicted values and saves the plot.
    """
    try:
        plt.figure(figsize=(10, 6))
        plt.scatter(y_test, y_pred)
        plt.xlabel("Actual Food Insecurity Rate")
        plt.ylabel("Predicted Food Insecurity Rate")
        plt.title("Actual vs Predicted Food Insecurity Rate")
        plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red')  # Line for reference
        plt.savefig(filepath)
        plt.show()
    except Exception as e:
        print(f"An error occurred while visualizing results: {e}")
        raise
