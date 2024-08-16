import os
import logging
import pandas as pd
from etl.extract import extract_data
from etl.transform import clean_foodaccess_data, clean_foodenvironment_data, merge_datasets
from etl.load import load_and_process_data
from analysis.evaluate import select_features_and_target, split_data, train_model, evaluate_model, save_evaluation_metrics, visualize_results
from analysis.model import visualize_average_income_per_county, visualize_poverty_rate_per_county, visualize_snap_usage_per_county

# Configure logging
logging.basicConfig(filename='data/main.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    """
    Main function to execute the data pipeline.
    """
    try:
        logging.info('Pipeline execution started.')

        # Step 1: Extract the data
        extract_data()

        # Step 2: Load and process the extracted data
        load_and_process_data()

        # Step 3: Load the final processed data
        df = pd.read_csv('data/processed/final_food_data.csv')

        # Step 4: Define features and target for modeling
        features = [
            'PovertyRate', 'MedianFamilyIncome', 'LowIncomeTracts', 'Urban',
            'LATracts_half'
        ]
        target = 'TractSNAP'

        # Step 5: Select features and target
        X, y = select_features_and_target(df, features, target)

        # Step 6: Split the data into training and testing sets
        X_train, X_test, y_train, y_test = split_data(X, y)

        # Step 7: Train the model
        model = train_model(X_train, y_train)

        # Step 8: Evaluate the model
        mse, r2, y_pred = evaluate_model(model, X_test, y_test)
        print(f"Mean Squared Error: {mse}")
        print(f"R-squared: {r2}")

        # Step 9: Save evaluation metrics
        save_evaluation_metrics(mse, r2, 'data/evaluation/evaluation_metrics.csv')

        # Step 10: Visualize the actual vs predicted results
        visualize_results(y_test, y_pred, 'data/evaluation/actual_vs_predicted.png')

        # Step 11: Visualize the aggregated data per county
        visualize_average_income_per_county(df)
        visualize_poverty_rate_per_county(df)
        visualize_snap_usage_per_county(df)

        logging.info('Pipeline execution completed successfully.')

    except Exception as e:
        logging.error(f"An error occurred during pipeline execution: {e}")
        raise

if __name__ == "__main__":
    main()
