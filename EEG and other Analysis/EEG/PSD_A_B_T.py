import numpy as np
import mne
import matplotlib.pyplot as plt

# Path to your .set file
file_path = r"C:\Users\User\Desktop\MU\4th year\SMART\Capstone\EEG\Final_Data\Analysis-20240421T063226Z-001\(1) P-1\actual\P-1.set"

# Load the .set file into MNE-Python
raw = mne.io.read_raw_eeglab(file_path)

# Define frequency bands
bands = {'theta': (4, 8), 'alpha': (8, 12), 'beta': (12, 30)}

# Define parameters for Welch's method
n_fft = 250  # Number of data points used in each block for the FFT
n_per_seg = 125  # Number of data points per segment
n_overlap = n_per_seg // 2  # Number of overlapped samples

# Calculate PSD for each channel within each frequency band
psd_results = {}
for ch_name in raw.ch_names:
    # Extract data for the channel
    data, _ = raw[ch_name]
    
    # Initialize PSD dictionary for the channel
    psd_results[ch_name] = {}
    
    # Calculate PSD using Welch's method for each frequency band
    for band_name, (fmin, fmax) in bands.items():
        # Filter data within the frequency band
        data_band = mne.filter.filter_data(data, raw.info['sfreq'], fmin, fmax)
        
        # Calculate PSD using Welch's method
        freqs, psd = mne.time_frequency.psd_array_welch(data_band, sfreq=raw.info['sfreq'],
                                                         fmin=fmin, fmax=fmax, n_fft=n_fft,
                                                         n_overlap=n_overlap, n_per_seg=n_per_seg)
        
        # Store the results
        psd_results[ch_name][band_name] = (freqs[0], 10 * np.log10(psd))

# Plot PSD for each channel within each frequency band
for ch_name, band_data in psd_results.items():
    for band_name, (freqs, psd) in band_data.items():
        plt.figure()
        plt.plot(freqs, psd, color='black')  # Plot PSD
        plt.title(f'PSD of Channel {ch_name} ({band_name.capitalize()} Band)')
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Power Spectral Density (dB)')
        plt.show()
