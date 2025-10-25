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
    n_fft = 2 * n_samples_per_epoch  # Length of the FFT used for PSD computation
    n_overlap = overlap  # Overlap between segments

    # Compute PSD
    psd = raw.compute_psd(fmin=fmin, fmax=fmax, n_fft=n_fft, n_overlap=n_overlap, n_jobs=n_jobs)

    # Convert PSD to DataFrame
    df = psd.to_data_frame()
    
    return df

# Path to your .set file
file_path = r"C:\Users\User\Desktop\MU\4th year\SMART\Capstone\EEG\Final_Data\Analysis-20240421T063226Z-001\(1) P-1\actual\P-1.set"

# Load the .set file into MNE-Python
raw = mne.io.read_raw_eeglab(file_path)

# Define frequency bands
frequency_bands = {'Theta': (4, 8), 'Alpha': (8, 12), 'Beta': (12, 30)}

# Create an empty DataFrame to store all frequency band data
all_data = pd.DataFrame()

# Iterate over frequency bands
for band, (fmin, fmax) in frequency_bands.items():
    print(f"\nComputing PSD and saving data for {band} band (fmin={fmin}, fmax={fmax})")
    df = compute_psd_to_dataframe(raw, fmin, fmax)
    # Save the DataFrame to a CSV file
    csv_filename = f"{band}_psd_data.csv"
    df.to_csv(csv_filename)
    print(f"Data saved to {csv_filename}")
    # Append the DataFrame to the all_data DataFrame
    all_data = pd.concat([all_data, df], axis=1)

# Save all_data DataFrame to a single CSV file
all_data.to_csv("all_frequency_band_data.csv", index=False)
print("All frequency band data saved to all_frequency_band_data.csv")
