import pandas as pd

def clean_Atlas_data(df): 
    '''
    Cleans Atlas data by handling missing values and 
    selecting columns. 
    '''
    df = df[['CensusTract', 'Urban', 'GroceryStores', 'Supercenters', 
             'ConvenienceStores', 'SpecialtyStores', 'SNAPAuthorizedStores', 
             'FoodInsecurityRate']]
    return df 

def clean_ACS_data(df): 
    '''
    Cleans ACS data by handling missing values 
    and selecting colums. 
    '''
    df = df[['GEO_ID', 'NAME', 'DP03_0062E', 'DP03_0063E', 'DP03_0064E']]
    df.columns = ['GeoID', 'RegionName', 'Income', 'PovertyRate', 'EducationLevel']
    return df