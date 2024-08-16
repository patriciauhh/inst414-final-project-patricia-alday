import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load the dataset
df = pd.read_csv('data/processed/final_food_data.csv')

# Ensure directories exist
os.makedirs('vis', exist_ok=True)

# the numeric columns along with 'County'
numeric_cols = ['MedianFamilyIncome', 'PovertyRate', 'TractSNAP']
grouped_df = df.groupby('County')[numeric_cols].mean().reset_index()

# columns present in the dataset
if 'County' in grouped_df.columns and 'MedianFamilyIncome' in grouped_df.columns and 'PovertyRate' in grouped_df.columns and 'TractSNAP' in grouped_df.columns:
    
    # Set the style for the plots
    sns.set(style="whitegrid")

    # Plot Average Income per County
    plt.figure(figsize=(10, 6))
    sns.barplot(x='County', y='MedianFamilyIncome', data=grouped_df, palette='viridis')
    plt.xticks(rotation=45, ha='right')
    plt.title('Average Income per County')
    plt.xlabel('County')
    plt.ylabel('Median Family Income ($)')
    plt.tight_layout()
    plt.savefig('vis/average_income_per_county.png')
    plt.show()

    # Plot Poverty Rate per County
    plt.figure(figsize=(10, 6))
    sns.barplot(x='County', y='PovertyRate', data=grouped_df, palette='magma')
    plt.xticks(rotation=45, ha='right')
    plt.title('Poverty Rate per County')
    plt.xlabel('County')
    plt.ylabel('Poverty Rate (%)')
    plt.tight_layout()
    plt.savefig('vis/poverty_rate_per_county.png')
    plt.show()

    # Plot SNAP Usage per County
    plt.figure(figsize=(10, 6))
    sns.barplot(x='County', y='TractSNAP', data=grouped_df, palette='coolwarm')
    plt.xticks(rotation=45, ha='right')
    plt.title('SNAP Usage per County')
    plt.xlabel('County')
    plt.ylabel('SNAP Participants')
    plt.tight_layout()
    plt.savefig('vis/snap_usage_per_county.png')
    plt.show()

else:
    print("One or more columns are missing in the dataset.")