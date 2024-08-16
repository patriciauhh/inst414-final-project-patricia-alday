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
    Reads CSV files from the datasets directory, filters for Maryland, and writes them to the processed data directory.
    """
    try:
        logging.info('Starting data extraction for Maryland.')
        
        # Load the raw datasets
        foodaccess_df = pd.read_csv('data/foodaccess.csv')
        foodenvironment_df = pd.read_csv('data/foodenvironment.csv')
        
        # Filter the datasets to only include Maryland (State code 'MD')
        md_foodaccess_df = foodaccess_df[foodaccess_df['State'] == 'Maryland']
        md_foodenvironment_df = foodenvironment_df[foodenvironment_df['State'] == 'MD']
        
        # Save the filtered datasets
        md_foodaccess_df.to_csv('data/processed/processed_foodaccess.csv', index=False)
        md_foodenvironment_df.to_csv('data/processed/processed_foodenvironment.csv', index=False)
        
        logging.info('Data extracted and filtered for Maryland successfully.')
    except FileNotFoundError as e:
        logging.error(f"File not found: {e}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise

if __name__ == "__main__":
    extract_data()
