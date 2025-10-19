import csv
from tkinter import filedialog
import tkinter as tk

# Read data from a text file
def read_data_from_file(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()
    return data

# Assuming a constant time interval between each data point
time_interval = 1  # Example time interval in seconds

# Create a Tkinter root window
root = tk.Tk()
root.withdraw()  # Hide the root window

# Ask the user to select the input text file
input_file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])

if input_file_path:
    # Read data from the selected text file
    lines = read_data_from_file(input_file_path)

    # Process all data from the file
    imu_data = {}
    imu_set_count = {}

    for line in lines:
        if line.strip():  # Check if line is not empty
            imu_id, imu_values = line.split(':')
            imu_id = imu_id.strip()
            imu_values = imu_values.strip().split(',')
            if imu_id not in imu_data:
                imu_data[imu_id] = []
                imu_set_count[imu_id] = 0
            imu_data[imu_id].append([float(val.strip()) for val in imu_values])
            imu_set_count[imu_id] += 1

    print("IMU Data:", imu_data)
    print("IMU Set Count:", imu_set_count)

    # Ask the user to select save location and file name
    output_file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])

    if output_file_path:
        # Save last 60 data points to the selected file
        with open(output_file_path, mode='w') as file:  # Remove newline=''
            writer = csv.writer(file)
            
            # Write header
            header = ['Time']
            for imu_id in range(4):
                for axis in ['ax', 'ay', 'az']:
                    header.append(f'imu{imu_id}_{axis}')
            writer.writerow(header)
            
            # Write last 60 data points for all sets
            num_samples = min(len(imu_data[next(iter(imu_data))][0]) // 3, 60)  # Use minimum of 60 and available samples
            for set_index in range(max(imu_set_count.values())):
                for i in range(num_samples):
                    row_data = [(set_index * num_samples + i) * time_interval]
                    for imu_id, imu_values_list in imu_data.items():
                        if set_index < imu_set_count[imu_id]:
                            imu_values = imu_values_list[set_index]
                            for j in range(3):
                                row_data.append(imu_values[-(num_samples*3) + i*3 + j])
                        else:
                            # If the set_index exceeds the available sets for an IMU, fill with NaN or a placeholder
                            for j in range(3):
                                row_data.append('NaN')
                    writer.writerow(row_data)

        print(f"Last 60 data points saved to {output_file_path}")
    else:
        print("No file selected for saving. Data not saved.")
else:
    print("No input file selected.")
