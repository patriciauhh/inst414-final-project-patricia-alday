import pandas as pd

# functions to clean the data 


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


if __name__ == "__main__":
    clean_Atlas_data()
    clean_ACS_data()
    

