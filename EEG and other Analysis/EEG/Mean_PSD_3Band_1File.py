import mne
import matplotlib.pyplot as plt
import pandas as pd

def compute_psd_and_mean(raw, fmin, fmax, epoch_duration=1, n_jobs=1):
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
    psd = raw.compute_psd(method="welch", fmin=fmin, fmax=fmax, n_fft=n_fft, n_overlap=n_overlap, n_jobs=n_jobs, window='hamming')

    # Convert PSD to DataFrame
    df = psd.to_data_frame()

    # Get the mean value of each column in the DataFrame
    mean_values = df.mean()
    
    return mean_values

# Path to your .set file
file_path = r"C:\Users\User\Desktop\MU\4th year\SMART\Capstone\EEG\Final_Data\Analysis-20240421T063226Z-001\(1) P-1\actual\P-1.set"

# Load the .set file into MNE-Python
raw = mne.io.read_raw_eeglab(file_path)

# Plot the raw data
# Plot the raw data with adjusted parameters
raw.plot(n_channels=8, duration=10, scalings='auto', block=True)

# Define frequency bands
frequency_bands = {'Theta': (4, 8), 'Alpha': (8, 12), 'Beta': (12, 30)}

# Iterate over frequency bands
for band, (fmin, fmax) in frequency_bands.items():
    print(f"\nComputing PSD and mean values for {band} band (fmin={fmin}, fmax={fmax})")
    mean_values = compute_psd_and_mean(raw, fmin, fmax)
    print("Mean values for each column:")
    print(mean_values)
