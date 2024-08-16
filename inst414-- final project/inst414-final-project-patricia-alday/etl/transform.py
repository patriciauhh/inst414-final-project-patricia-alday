import pandas as pd
import logging

# Configure logging
logging.basicConfig(filename='data/transform.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def clean_atlas_data(df):
    """
    Cleans Atlas data by handling missing values and selecting columns.
    """
    try:
        logging.info('Cleaning Atlas data.')
        df.fillna(0, inplace=True)
        df = df[['CensusTract', 'Urban', 'GroceryStores', 'Supercenters',
                 'ConvenienceStores', 'SpecialtyStores', 'SNAPAuthorizedStores',
                 'FoodInsecurityRate']]
        df.drop_duplicates(inplace=True)
        logging.info('Atlas data cleaned successfully.')
        return df
    except Exception as e:
        logging.error(f"An error occurred while cleaning Atlas data: {e}")
        raise

def clean_acs_data(df):
    """
    Cleans ACS data by handling missing values and selecting columns.
    """
    try:
        logging.info('Cleaning ACS data.')
        df.fillna(0, inplace=True)
        df = df[['GEO_ID', 'NAME', 'DP03_0062E', 'DP03_0063E', 'DP03_0064E']]
        df.columns = ['GeoID', 'RegionName', 'Income', 'PovertyRate', 'EducationLevel']
        df.drop_duplicates(inplace=True)
        logging.info('ACS data cleaned successfully.')
        return df
    except Exception as e:
        logging.error(f"An error occurred while cleaning ACS data: {e}")
        raise

if __name__ == "__main__":
    clean_atlas_data()
    clean_acs_data()
    
    
    
    ##