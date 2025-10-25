import pandas as pd

def select_last_60_rows(csv_file_path):
    # Read CSV file into a DataFrame
    df = pd.read_csv(csv_file_path)

    # Select the last 60 rows
    last_60_rows = df.tail(60)

    return last_60_rows

# Replace 'your_file.csv' with the actual path to your CSV file
csv_file_path = 'Petch\PetchBackward.csv'
last_60_rows = select_last_60_rows(csv_file_path)

# Display the selected data
print(last_60_rows)
