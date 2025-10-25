import pandas as pd
import os

def separate_csv(input_file, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Read input Excel file
    df = pd.read_csv(input_file)

    # Group rows by label (assuming label is in the third column)
    grouped = df.groupby(df.columns[3])

    # Write groups to separate CSV files based on labels
    for label, group in grouped:
        output_file = os.path.join(output_folder, f"{label}.csv")
        group.to_csv(output_file, index=False)

# Example usage
input_file = r"C:\Users\User\Desktop\MU\4th year\SMART\Capstone\Analysis\EEG\T-Test\3Bands\Theta\Virtual.csv"
output_folder = r"C:\Users\User\Desktop\MU\4th year\SMART\Capstone\Analysis\EEG\T-Test\3Bands\Theta\Virtual"
separate_csv(input_file, output_folder)
