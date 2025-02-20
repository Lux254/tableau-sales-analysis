import pandas as pd

def clean_data(file_path, output_path):
    # Load the dataset
    dirty_data = pd.read_csv(file_path)
    
    # Replace "UNKNOWN" and "ERROR" values with NaN in categorical columns
    categorical_columns = ['Location', 'Payment Method', 'Item']
    for col in categorical_columns:
        dirty_data[col] = dirty_data[col].replace(["UNKNOWN", "ERROR"], pd.NA)
    
    # Fill missing values in categorical columns with the mode
    for col in categorical_columns:
        dirty_data[col].fillna(dirty_data[col].mode()[0], inplace=True)
    
    # Replace "UNKNOWN" and "ERROR" values with NaN in numerical columns
    numerical_columns = ['Total Spent', 'Price Per Unit', 'Quantity']
    for col in numerical_columns:
        dirty_data[col] = dirty_data[col].replace(["UNKNOWN", "ERROR"], pd.NA)
    
    # Convert numerical columns to the correct data type
    for col in numerical_columns:
        dirty_data[col] = pd.to_numeric(dirty_data[col], errors='coerce')
    
    # Fill missing values in numerical columns with the mean
    for col in ['Price Per Unit', 'Quantity']:
        dirty_data[col].fillna(dirty_data[col].mean(), inplace=True)
    
    # Recalculate 'Total Spent' for missing values
    dirty_data.loc[dirty_data['Total Spent'].isna(), 'Total Spent'] = (
        dirty_data['Quantity'] * dirty_data['Price Per Unit']
    )
    
    # Clean 'Transaction Date' column
    dirty_data['Transaction Date'] = dirty_data['Transaction Date'].replace(["UNKNOWN", "ERROR"], pd.NA)
    dirty_data['Transaction Date'] = pd.to_datetime(dirty_data['Transaction Date'], errors='coerce')
    dirty_data['Transaction Date'].fillna(dirty_data['Transaction Date'].mode()[0], inplace=True)
    
    # Save the cleaned dataset
    dirty_data.to_csv(output_path, index=False)
    print(f"Cleaned data saved to {output_path}")

