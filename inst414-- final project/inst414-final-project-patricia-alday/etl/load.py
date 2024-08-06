import pandas as pd
from transform import clean_atlas_data, clean_acs_data
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
        acs_raw_path = 'data/processed/processed_ACS_Data.csv'
        atlas_raw_path = 'data/processed/processed_Atlas_Data.csv'
        
        acs_df = pd.read_csv(acs_raw_path)
        atlas_df = pd.read_csv(atlas_raw_path)
        
        cleaned_acs_df = clean_acs_data(acs_df)
        cleaned_atlas_df = clean_atlas_data(atlas_df)
        
        cleaned_acs_df.to_csv('data/processed/cleaned_ACS_Data.csv', index=False)
        cleaned_atlas_df.to_csv('data/processed/cleaned_Atlas_Data.csv', index=False)
        
        logging.info('Cleaned data loaded and saved successfully.')
    except FileNotFoundError as e:
        logging.error(f"File not found: {e}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    load_clean_data()