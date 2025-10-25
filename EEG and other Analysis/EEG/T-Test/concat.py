import pandas as pd
import os

def concat_csv_files(folder_path, output_file):
    # Get list of all CSV files in the folder
    csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]

    # Initialize an empty list to store DataFrames
    dfs = []

    # Iterate through each CSV file, read it and append to the list
    for file in csv_files:
        file_path = os.path.join(folder_path, file)
        df = pd.read_csv(file_path)
        dfs.append(df)

    # Concatenate all DataFrames in the list
    concatenated_df = pd.concat(dfs, ignore_index=True)

    # Write the concatenated DataFrame to a single CSV file
    concatenated_df.to_csv(output_file, index=False)

# Example usage
input_folder = r"C:\Users\User\Desktop\MU\4th year\SMART\Capstone\Analysis\EEG\T-Test\3Bands\Theta\Virtual"
output_file = r"C:\Users\User\Desktop\MU\4th year\SMART\Capstone\Analysis\EEG\T-Test\3Bands\Theta\Sorted_Virtual_T.csv"
concat_csv_files(input_folder, output_file)
