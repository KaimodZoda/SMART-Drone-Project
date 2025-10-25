import numpy as np
import mne
import matplotlib.pyplot as plt

# Path to your .set file
file_path = r"C:\Users\User\Desktop\MU\4th year\SMART\Capstone\EEG\Final_Data\Analysis-20240421T063226Z-001\(1) P-1\actual\P-1.set"

# Load the .set file into MNE-Python
raw = mne.io.read_raw_eeglab(file_path)

# Define parameters for Welch's method
n_fft = 250  # Number of data points used in each block for the FFT
n_per_seg = 125  # Number of data points per segment
n_overlap = n_per_seg // 2  # Number of overlapped samples

# Calculate PSD for each channel
psd_results = {}
for ch_name in raw.ch_names:
    # Extract data for the channel
    data, _ = raw[ch_name]

    # Calculate PSD using Welch's method
    freqs, psd = mne.time_frequency.psd_array_welch(data, sfreq=raw.info['sfreq'],
                                                     fmin=0, fmax=np.inf, n_fft=n_fft,
                                                     n_overlap=n_overlap, n_per_seg=n_per_seg)

    # Store the results
    psd_results[ch_name] = (freqs, psd)

# Plot PSD for each channel
for ch_name, (freqs, psd) in psd_results.items():
    plt.figure()
    plt.plot(freqs[0], 10 * np.log10(psd), color='black')  # Convert to dB
    plt.title('PSD of Channel: ' + ch_name)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Power Spectral Density (dB)')
    plt.show()
