
# loading clean data from the transformation functions and 
# moving it into the processed data file 

def clean_Atlas_data(df): 
    '''
    Cleans Atlas data by handling missing values and 
    selecting columns. 
    '''
    # handles missing values
    df.fillna(0, inplace=True)
    df = df[['CensusTract', 'Urban', 'GroceryStores', 'Supercenters', 
             'ConvenienceStores', 'SpecialtyStores', 'SNAPAuthorizedStores', 
             'FoodInsecurityRate']]
    # removes duplicates 
    df.drop_duplicates(inplace=True)
    return df 

def clean_ACS_data(df): 
    '''
    Cleans ACS data by handling missing values 
    and selecting colums. 
    '''
    # handles missing values
    df.fillna(0, inplace=True)
    df = df[['GEO_ID', 'NAME', 'DP03_0062E', 'DP03_0063E', 'DP03_0064E']]
    df.columns = ['GeoID', 'RegionName', 'Income', 'PovertyRate', 'EducationLevel']
    # removes duplicates 
    df.drop_duplicates(inplace=True)
    return df

import pandas as pd

# actually cleaning the csv files using the funcctions created 

def load_clean_data():
    ''' 
    cleans the raw data from the transform.py
    then save cleaned data into a file
    '''
    ACS_raw_path = ('data/processed/processed_ACS_Data.csv')
    Atlas_raw_path = ('data/processed/processed_Atlas_Data.csv')
    
    # raw files 
    ACS_df = pd.read_csv(ACS_raw_path)
    Atlas_df = pd.read_csv(Atlas_raw_path)
    
    # cleaning function 
    
    cleaned_ACS_df = clean_ACS_data(ACS_df)
    cleaned_Atlast_df = clean_Atlas_data(Atlas_df)
    