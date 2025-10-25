import mne
import matplotlib.pyplot as plt
import pandas as pd

# Path to your .set file
file_path = r"C:\Users\User\Desktop\MU\4th year\SMART\Capstone\EEG\Final_Data\Analysis-20240421T063226Z-001\(1) P-1\actual\P-1.set"

# Load the .set file into MNE-Python
raw = mne.io.read_raw_eeglab(file_path)

# Print information about the data
print(raw.info)

# Plot the raw data
# Plot the raw data with adjusted parameters
raw.plot(n_channels=8, duration=10, scalings='auto', block=True)

# Sampling rate
sfreq = 250  # Sampling rate in Hz

# Define epoch duration
epoch_duration = 1  # Duration of each epoch in seconds

# Calculate number of samples per epoch
n_samples_per_epoch = int(epoch_duration * sfreq)

# Calculate overlap (50% overlap)
overlap = n_samples_per_epoch // 2

# Set parameters for PSD calculation
fmin = 4  # Minimum frequency
fmax = 8  # Maximum frequency
n_fft = 2 * n_samples_per_epoch  # Length of the FFT used for PSD computation (use twice the epoch length for better frequency resolution)
n_overlap = overlap  # Overlap between segments
n_jobs = 1  # Number of jobs to run in parallel

# Plot the PSD with custom parameters
psd = raw.compute_psd(fmin=fmin, fmax=fmax, n_fft=n_fft, n_overlap=n_overlap, n_jobs=n_jobs)
psd.plot()
plt.show()
print(psd)
df = psd.to_data_frame()
print(df)

# Get the mean value of each column in the DataFrame
mean_values = df.mean()
print("Mean values for each column:")
print(mean_values)






