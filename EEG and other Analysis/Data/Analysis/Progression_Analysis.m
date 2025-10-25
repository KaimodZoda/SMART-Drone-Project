% Add EEGLAB to the MATLAB path (change the path to where EEGLAB is installed on your machine)
addpath('C:\Users\hp\AppData\Roaming\MathWorks\MATLAB Add-Ons\Collections\EEGLAB');

% Load EEGLAB
eeglab;

% Load the datasets
EEG_game1 = pop_loadset('filename', 'P-1.set', 'filepath', 'C:\Users\hp\Desktop\EEG.dat\(1) P-1\virtual');
EEG_game2 = pop_loadset('filename', 'P-2.set', 'filepath', 'C:\Users\hp\Desktop\EEG.dat\(1) P-1\virtual');

% Define frequency bands
freq_bands = {'Delta', 1, 4; 'Theta', 4, 8; 'Alpha', 8, 12; 'Beta', 12, 30; 'Gamma', 30, 80};
n_bands = size(freq_bands, 1);

% Prepare to store mean PSD data
mean_psd_data = zeros(EEG_game1.nbchan, n_bands, 2); % 2 game conditions, n bands, channels

% Calculate mean PSD for each game condition and each frequency band
for i = 1:n_bands
    band_name = freq_bands{i, 1};
    band_range = [freq_bands{i, 2}, freq_bands{i, 3}];
    
    mean_psd_data(:, i, 1) = calculate_mean_psd(EEG_game1, band_range);
    mean_psd_data(:, i, 2) = calculate_mean_psd(EEG_game2, band_range);
end

% Plotting each band separately
for i = 1:n_bands
    figure; % New figure for each band
    b = bar(1:EEG_game1.nbchan, squeeze(mean_psd_data(:, i, :)), 'grouped');
    xlabel('Channels');
    ylabel('Power Spectral Density');
    title(['PSD Progression in ', freq_bands{i, 1}, ' Band from Game 1 to Game 2']);
    legend('Trial 1', 'Trial 2');
    set(gca, 'XTick', 1:EEG_game1.nbchan, 'XTickLabel', {'F3', 'F4', 'P3', 'P4', 'P5', 'P6', 'O1', 'O2'});
    grid on;
end

% Function to extract mean PSD across specified frequency range for each channel
function mean_psd = calculate_mean_psd(EEG, freq_range)
    [psd, freqs] = spectopo(EEG.data, 0, EEG.srate, 'plot', 'off');
    fprintf('Frequency range in PSD: %f to %f Hz\n', min(freqs), max(freqs));
    freq_inds = freqs >= freq_range(1) & freqs <= freq_range(2);
    if any(freq_inds)
        mean_psd = mean(10*log10(psd(:, freq_inds)), 2); % Mean across the specified frequency range
    else
        error('Specified frequency range does not exist in the calculated frequencies.');
    end
end
