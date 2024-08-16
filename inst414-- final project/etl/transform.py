import pandas as pd
import logging

# Configure logging
logging.basicConfig(filename='data/transform.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def clean_foodaccess_data(df):
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
        logging.info('Access data cleaned successfully.')
        return df
    except Exception as e:
        logging.error(f"An error occurred while cleaning Access data: {e}")
        raise

def clean_foodenvironment_data(df):
    """
    Cleans ACS data by handling missing values and selecting columns.
    """
    try:
        logging.info('Cleaning environment data.')
        df.fillna(0, inplace=True)
        df = df[['GEO_ID', 'NAME', 'DP03_0062E', 'DP03_0063E', 'DP03_0064E']]
        df.columns = ['GeoID', 'RegionName', 'Income', 'PovertyRate', 'EducationLevel']
        df.drop_duplicates(inplace=True)
        logging.info('Environment data cleaned successfully.')
        return df
    except Exception as e:
        logging.error(f"An error occurred while cleaning Environment data: {e}")
        raise

  
if __name__ == "__main__":
    # Load the data into DataFrames
    foodaccess_df = pd.read_csv('data/foodaccess.csv')
    foodenvironment_df = pd.read_csv('data/foodenvironment.csv')

    # Clean the data
    cleaned_access_df = clean_foodaccess_data(foodaccess_df)
    cleaned_environment_df = clean_foodenvironment_data(foodenvironment_df)



 