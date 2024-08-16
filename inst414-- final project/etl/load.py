import pandas as pd
from transform import clean_foodaccess_data, clean_foodenvironment_data
import logging

# Configure logging
logging.basicConfig(filename='data/load.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def load_clean_data():
    """
    Cleans the raw data using functions from transform.py and saves the cleaned data.
    """
    try:
        logging.info('Loading and cleaning data.')
        
        access_raw_path = 'data/processed/processed_foodaccess.csv'
        environment_raw_path = 'data/processed/processed_foodenvironment.csv'
        
        access_df = pd.read_csv(access_raw_path)
        environment_df = pd.read_csv(environment_raw_path)
        
        cleaned_access_df = clean_foodaccess_data(access_df)
        cleaned_environment_df = clean_foodenvironment_data(environment_df)
        
        cleaned_access_df.to_csv('data/processed/cleaned_foodaccess.csv', index=False)
        cleaned_environment_df.to_csv('data/processed/cleaned_foodenvironment.csv', index=False)
        
        logging.info('Cleaned data loaded and saved successfully.')
    except FileNotFoundError as e:
        logging.error(f"File not found: {e}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    load_clean_data()
