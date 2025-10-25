import mne
import pandas as pd

def compute_psd_and_mean(raw, fmin, fmax, epoch_duration=1, n_jobs=1):
    sfreq = raw.info['sfreq']
    n_samples_per_epoch = int(epoch_duration * sfreq)
    overlap = n_samples_per_epoch // 2
    n_fft = n_samples_per_epoch
    n_overlap = overlap

    psd = raw.compute_psd(method="welch", fmin=fmin, fmax=fmax, n_fft=n_fft, n_overlap=n_overlap,n_per_seg=n_samples_per_epoch, n_jobs=n_jobs, window='hamming')
    df = psd.to_data_frame()
    mean_values = df.mean()
    
    return mean_values

file_path = r"C:\Users\User\Desktop\MU\4th year\SMART\Capstone\EEG\Final_Data\Analysis-20240421T063226Z-001\(1) P-1\actual\P-1.set"
raw = mne.io.read_raw_eeglab(file_path)

# Define frequency bands
frequency_bands = {'Theta': (4, 8), 'Alpha': (8, 12), 'Beta': (12, 30)}

for band, (fmin, fmax) in frequency_bands.items():
    print(f"\nComputing PSD and mean values for {band} band (fmin={fmin}, fmax={fmax})")
    mean_values = compute_psd_and_mean(raw, fmin, fmax)
    print("Mean values for each column:")
    print(mean_values)
    
    # Save mean values to CSV
    output_file = f"{band}_mean_values.csv"
    mean_values.to_csv(output_file)
    print(f"Mean values saved to {output_file}")
