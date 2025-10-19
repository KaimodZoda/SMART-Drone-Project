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

    # Filter the data to consider only the last two sets of data for each IMU
    num_sets = 8  # Assuming each IMU has 2 sets of data
    filtered_lines = lines[-num_sets:]

    # Process the filtered data
    imu_data = {}
    imu_set_count = {}

    for line in filtered_lines:
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
        # Save the data to the selected file
        with open(output_file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            
            # Write header
            header = ['Time']
            for imu_id in sorted(imu_data.keys()):  # Sort IMU IDs for consistent order
                for axis in ['ax', 'ay', 'az']:
                    header.append(f'imu{imu_id}_{axis}')
            writer.writerow(header)
            
            # Write data rows for each set
            for set_index in range(max(imu_set_count.values())):
                for i in range(len(imu_data[next(iter(imu_data))][0]) // 3):
                    row_data = [(set_index * len(imu_data[next(iter(imu_data))][0]) // 3 + i) * time_interval]
                    for imu_id in sorted(imu_data.keys()):  # Sort IMU IDs for consistent order
                        if set_index < imu_set_count[imu_id]:
                            imu_values = imu_data[imu_id][set_index]
                            for j in range(3):
                                row_data.append(imu_values[3*i + j])
                        else:
                            # If there are no values for the current set, add placeholders
                            row_data.extend([0, 0, 0])
                    writer.writerow(row_data)

        print(f"Data saved to {output_file_path}")
    else:
        print("No file selected for saving. Data not saved.")
else:
    print("No input file selected.")