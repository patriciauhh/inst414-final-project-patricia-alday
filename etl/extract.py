import pandas as pd
import os
import logging

# Configure logging
logging.basicConfig(filename='data/extract.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Ensure the data directory exists
os.makedirs('data/processed', exist_ok=True)

def extract_data():
    """
    Reads CSV files from the datasets directory and writes them to the processed data directory.
    """
    try:
        logging.info('Starting data extraction.')
        acs_data_df = pd.read_csv('datasets/ACS_Data.csv')
        atlas_data_df = pd.read_csv('datasets/Atlas_Data.csv')
        
        acs_data_df.to_csv('data/processed/processed_ACS_Data.csv', index=False)
        atlas_data_df.to_csv('data/processed/processed_Atlas_Data.csv', index=False)
        
        logging.info('Data extracted successfully.')
    except FileNotFoundError as e:
        logging.error(f"File not found: {e}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    extract_data()
    
    
    
####