import os
import mne
import pandas as pd

def compute_psd_to_dataframe(raw, fmin, fmax, epoch_duration=1, n_jobs=1):
    # Sampling rate
    sfreq = raw.info['sfreq']

    # Calculate number of samples per epoch
    n_samples_per_epoch = int(epoch_duration * sfreq)

    # Calculate overlap (50% overlap)
    overlap = n_samples_per_epoch // 2

    # Set parameters for PSD calculation
    n_fft = n_samples_per_epoch  # Length of the FFT used for PSD computation
    n_overlap = overlap  # Overlap between segments

    # Compute PSD
    psd = raw.compute_psd(method="welch", fmin=fmin, fmax=fmax, n_fft=n_fft, n_overlap=n_overlap, n_per_seg=n_samples_per_epoch, n_jobs=n_jobs, window='hamming')

    # Convert PSD to DataFrame
    df = psd.to_data_frame()
    
    return df

# Folder containing .set files
folder_path = r"C:\Users\User\Desktop\MU\4th year\SMART\Capstone\EEG\Analyze\EEG\P01\Virtual"

# Define frequency bands
frequency_bands = {'Theta': (4, 8), 'Alpha': (8, 12), 'Beta': (12, 30)}

# List all .set files in the folder
set_files = [file for file in os.listdir(folder_path) if file.endswith(".set")]

# Iterate over .set files
for set_file in set_files:
    file_path = os.path.join(folder_path, set_file)
    print(f"\nProcessing file: {file_path}")
    
    # Load the .set file into MNE-Python
    raw = mne.io.read_raw_eeglab(file_path)
    
    # Create a DataFrame to store mean values for each frequency band
    mean_values_df = pd.DataFrame(columns=['Frequency Band', 'Mean Value'])
    
    # Iterate over frequency bands
    for band, (fmin, fmax) in frequency_bands.items():
        print(f"\nComputing PSD for {band} band (fmin={fmin}, fmax={fmax})")
        
        # Compute PSD and get DataFrame
        df = compute_psd_to_dataframe(raw, fmin, fmax)
        
        # Calculate the mean of each column (except the first column)
        mean_values = df.iloc[:, 1:].mean()
        
        # Append mean value to the DataFrame
        mean_values_df = mean_values_df.append({'Frequency Band': band, 'Mean Value': mean_values.mean()}, ignore_index=True)
    
    # Save mean values DataFrame to a CSV file for each file
    output_file_name = f"mean_values_{set_file.split('.')[0]}.csv"
    mean_values_df.to_csv(output_file_name, index=False)
    print(f"Mean values saved to {output_file_name}")
