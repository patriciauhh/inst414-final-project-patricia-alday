import pandas as pd
from transform import clean_foodaccess_data, clean_foodenvironment_data, merge_datasets
import logging

# Configure logging
logging.basicConfig(filename='data/load.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def load_and_process_data():
    """
    Loads the processed data, cleans it using functions from transform.py, merges the datasets,
    and saves the cleaned and merged data.
    """
    try:
        logging.info('Loading and processing data.')

        # Paths to the processed raw data files
        access_raw_path = 'data/processed/processed_foodaccess.csv'
        environment_raw_path = 'data/processed/processed_foodenvironment.csv'

        # Load the processed data
        access_df = pd.read_csv(access_raw_path)
        environment_df = pd.read_csv(environment_raw_path)

        # Clean the datasets
        cleaned_access_df = clean_foodaccess_data(access_df)
        cleaned_environment_df = clean_foodenvironment_data(environment_df)

        # Merge the cleaned datasets
        final_df = merge_datasets(cleaned_access_df, cleaned_environment_df)

        # Save the final cleaned and merged data
        final_df.to_csv('data/processed/final_food_data.csv', index=False)
        
        logging.info('Data loaded, processed, and saved successfully.')
    
    except FileNotFoundError as e:
        logging.error(f"File not found: {e}")
        raise
    
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise

if __name__ == "__main__":
    load_and_process_data()
