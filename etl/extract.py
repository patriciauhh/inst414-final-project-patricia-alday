#Extract

# Include a .py for this stage and write the code to extract data from your identified data sources. 
# This might involve making API requests, web scraping, querying databases, or loading flat files.
# Store the raw extracted data its own directory in ` data/`

import pandas as pd 

def extract_data(): 
    acs_data_df = pd.read_csv('datasets/ACS_Data.csv')
    Atlast_data_df = pd.read_csv('datasets/Atlast_data_df')
    
    Atlast_data_df.to_csv('data/processed/Atlas_Data.csv', index=False)
    acs_data_df.to_csv('data/processed/ACS_raw.csv', index=False)
    
    print("Data extracted.")
    
if __name__ == "__main__":
    extract_data()