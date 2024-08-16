import pandas as pd
import logging

# Configure logging
logging.basicConfig(filename='data/transform.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def clean_foodaccess_data(df):
    """
    Cleans food access data by handling missing values, selecting relevant columns, and removing duplicates.
    """
    try:
        logging.info('Cleaning food access data.')
        
        # Handle missing values with .loc to avoid SettingWithCopyWarning
        df.loc[:, 'PovertyRate'] = df['PovertyRate'].fillna(0)
        df.loc[:, 'MedianFamilyIncome'] = df['MedianFamilyIncome'].fillna(0)
        df.loc[:, 'LowIncomeTracts'] = df['LowIncomeTracts'].fillna(0)
        df.loc[:, 'TractSNAP'] = df['TractSNAP'].fillna(0)
        
        # Select relevant columns (ensure these columns exist in your DataFrame)
        relevant_columns = [
            'CensusTract', 'State', 'County', 'Urban', 'PovertyRate', 
            'MedianFamilyIncome', 'LowIncomeTracts', 
            'LATracts_half', 'TractSNAP',
        ]
        
        # Use .loc[] to avoid SettingWithCopyWarning
        df = df.loc[:, relevant_columns]
        
        # Remove duplicates
        df = df.drop_duplicates()
        
        logging.info('Food access data cleaned successfully.')
        return df
    except Exception as e:
        logging.error(f"An error occurred while cleaning food access data: {e}")
        raise


def clean_foodenvironment_data(df):
    """
    Cleans food environment data by pivoting Variable_Code and handling missing values.
    """
    try:
        logging.info('Cleaning food environment data.')
        
        # Pivot the data to turn Variable_Code into columns
        df_pivot = df.pivot_table(index=['FIPS', 'State', 'County'], 
                                  columns='Variable_Code', 
                                  values='Value').reset_index()
        
        # Handle missing values
        df_pivot.fillna(0, inplace=True)
        
        logging.info('Food environment data cleaned successfully.')
        return df_pivot
    except Exception as e:
        logging.error(f"An error occurred while cleaning food environment data: {e}")
        raise

def merge_datasets(df_access, df_environment):
    """
    Merges the cleaned food access and food environment datasets on CensusTract and FIPS.
    """
    try:
        logging.info('Merging datasets.')
        
        # Merge on FIPS code and CensusTract
        merged_df = pd.merge(df_access, df_environment, how='left', 
                             left_on=['CensusTract', 'State', 'County'], 
                             right_on=['FIPS', 'State', 'County'])
        
        logging.info('Datasets merged successfully.')
        return merged_df
    except Exception as e:
        logging.error(f"An error occurred while merging datasets: {e}")
        raise

if __name__ == "__main__":
    # Load the data into DataFrames
    foodaccess_df = pd.read_csv('data/foodaccess.csv')
    foodenvironment_df = pd.read_csv('data/foodenvironment.csv')

    # Clean the data
    cleaned_access_df = clean_foodaccess_data(foodaccess_df)
    cleaned_environment_df = clean_foodenvironment_data(foodenvironment_df)

    # Merge the datasets
    final_df = merge_datasets(cleaned_access_df, cleaned_environment_df)
    
    # Save the final transformed data
    final_df.to_csv('data/processed/final_food_data.csv', index=False)
    logging.info('Final transformed data saved successfully.')
