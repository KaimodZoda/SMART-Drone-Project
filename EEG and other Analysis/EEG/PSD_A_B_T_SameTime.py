import numpy as np
import mne
import matplotlib.pyplot as plt

# Path to your .set file
file_path = r"C:\Users\User\Desktop\MU\4th year\SMART\Capstone\Analysis\Analysis-20240415T110717Z-001\(1) P-1\actual\P-2.set"

# Load the .set file into MNE-Python
raw = mne.io.read_raw_eeglab(file_path)

# Define frequency bands
bands = {'theta': (4, 8), 'alpha': (8, 12), 'beta': (12, 30)}

# Define parameters for Welch's method
n_fft = 250  # Number of data points used in each block for the FFT
n_per_seg = 125  # Number of data points per segment
n_overlap = n_per_seg // 2  # Number of overlapped samples

# Create a figure for each channel
figs = {}
for ch_name in raw.ch_names:
    figs[ch_name] = plt.figure(figsize=(10, 8))

# Calculate and plot PSD for each channel within each frequency band
for ch_name in raw.ch_names:
    # Calculate PSD for each frequency band
    for band_name, (fmin, fmax) in bands.items():
        # Filter data within the frequency band
        data_band = mne.filter.filter_data(raw[ch_name][0], raw.info['sfreq'], fmin, fmax)
        
        # Calculate PSD using Welch's method
        freqs, psd = mne.time_frequency.psd_array_welch(data_band, sfreq=raw.info['sfreq'],
                                                         fmin=fmin, fmax=fmax, n_fft=n_fft,
                                                         n_overlap=n_overlap, n_per_seg=n_per_seg)
        
        # Plot PSD
        plt.figure(figs[ch_name].number)
        plt.plot(freqs[0], 10 * np.log10(psd), label=band_name)
        print(psd)

    # Add labels and legend to each figure
    plt.figure(figs[ch_name].number)
    plt.title(f'PSD of Channel {ch_name}')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Power Spectral Density (dB)')
    plt.legend()

# Show all figures
plt.show()
