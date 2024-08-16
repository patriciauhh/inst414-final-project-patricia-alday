import os
import logging
import pandas as pd
from etl.extract import extract_data
from etl.transform import clean_atlas_data, clean_acs_data
from etl.load import load_clean_data
from analysis.evaluate import evaluate_model, visualize_results, save_evaluation_metrics
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from analysis.evaluate import select_features_and_target
from analysis.evaluate import split_data
from analysis.evaluation import train_model

# Configure logging
logging.basicConfig(filename='data/main.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Ensure necessary directories exist
os.makedirs('data/processed', exist_ok=True)
os.makedirs('data/evaluation', exist_ok=True)

def main():
    """
    Main function to run the ETL pipeline, train the model, evaluate, and visualize results.
    """
    # ETL Process
    extract_data()
    load_clean_data()

    # Load cleaned data
    atlas_df = pd.read_csv('data/processed/cleaned_Atlas_Data.csv')

    # Feature Selection
    features = ['GroceryStores', 'Supercenters', 'ConvenienceStores', 'SpecialtyStores', 'SNAPAuthorizedStores']
    target = 'FoodInsecurityRate'
    X, y = select_features_and_target(atlas_df, features, target)

    # Train-Test Split
    X_train, X_test, y_train, y_test = split_data(X, y)

    # Model Training
    model = train_model(X_train, y_train)

    # Model Evaluation
    mse, rmse, mae, r2, adjusted_r2, mape, y_pred = evaluate_model(model, X_test, y_test)

    # Save evaluation metrics
    save_evaluation_metrics([mse, rmse, mae, r2, adjusted_r2, mape], 'data/evaluation/linear_regression_evaluation.csv')

    # Visualize Results
    visualize_results(y_test, y_pred, 'data/evaluation/actual_vs_predicted.png')

    # Print evaluation metrics
    print(f"Mean Squared Error: {mse}")
    print(f"R-squared: {r2}")


if __name__ == "__main__":
    main()


###