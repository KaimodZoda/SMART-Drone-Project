% Add EEGLAB to the MATLAB path (change the path to where EEGLAB is installed on your machine)
addpath('C:\Users\hp\AppData\Roaming\MathWorks\MATLAB Add-Ons\Collections\EEGLAB');

% Load EEGLAB
eeglab;

% Load the datasets
EEG_preTraining_actual = pop_loadset('filename', 'P-Base.set', 'filepath', 'C:\Users\hp\Desktop\EEG.dat\(1) P-1\virtual');
EEG_preTraining_virtual = pop_loadset('filename', 'P-Base.set', 'filepath', 'C:\Users\hp\Desktop\EEG.dat\(1) P-1\virtual');
EEG_game1_actual = pop_loadset('filename', 'P-1.set', 'filepath', 'C:\Users\hp\Desktop\EEG.dat\(1) P-1\actual');
EEG_game1_virtual = pop_loadset('filename', 'P-1.set', 'filepath', 'C:\Users\hp\Desktop\EEG.dat\(1) P-1\virtual');
EEG_game2_actual = pop_loadset('filename', 'P-2.set', 'filepath', 'C:\Users\hp\Desktop\EEG.dat\(1) P-1\actual');
EEG_game2_virtual = pop_loadset('filename', 'P-2.set', 'filepath', 'C:\Users\hp\Desktop\EEG.dat\(1) P-1\virtual');
EEG_postTraining_actual = pop_loadset('filename', 'P-TLX.set', 'filepath', 'C:\Users\hp\Desktop\EEG.dat\(1) P-1\actual');
EEG_postTraining_virtual = pop_loadset('filename', 'P-TLX.set', 'filepath', 'C:\Users\hp\Desktop\EEG.dat\(1) P-1\virtual');

% Define frequency bands
freq_bands = {'Delta', 1, 4; 'Theta', 4, 8; 'Alpha', 8, 12; 'Beta', 12, 30; 'Gamma', 30, 80};
n_bands = size(freq_bands, 1);

% Prepare to store mean PSD data
n_stages = 4; % Pre-Training, Game 1, Game 2, Post-Training
n_modalities = 2; % Actual, Virtual
mean_psd_data = zeros(EEG_preTraining_actual.nbchan, n_bands, n_stages, n_modalities);

% Calculate mean PSD for each condition, modality, and frequency band
for i = 1:n_bands
    band_range = [freq_bands{i, 2}, freq_bands{i, 3}];
    
    % Actual training data
    mean_psd_data(:, i, 1, 1) = calculate_mean_psd(EEG_preTraining_actual, band_range);
    mean_psd_data(:, i, 2, 1) = calculate_mean_psd(EEG_game1_actual, band_range);
    mean_psd_data(:, i, 3, 1) = calculate_mean_psd(EEG_game2_actual, band_range);
    mean_psd_data(:, i, 4, 1) = calculate_mean_psd(EEG_postTraining_actual, band_range);
    
    % Virtual training data
    mean_psd_data(:, i, 1, 2) = calculate_mean_psd(EEG_preTraining_virtual, band_range);
    mean_psd_data(:, i, 2, 2) = calculate_mean_psd(EEG_game1_virtual, band_range);
    mean_psd_data(:, i, 3, 2) = calculate_mean_psd(EEG_game2_virtual, band_range);
    mean_psd_data(:, i, 4, 2) = calculate_mean_psd(EEG_postTraining_virtual, band_range);
end

% Plotting each band and stage separately
stage_names = {'Pre-Training', 'Trial 1', 'Trial 2', 'Post-Training'};
modality_names = {'Actual', 'Virtual'};
for i = 1:n_bands
    figure; % New figure for each frequency band
    for j = 1:n_stages
        subplot(1, n_stages, j);
        b = bar(1:EEG_preTraining_actual.nbchan, squeeze(mean_psd_data(:, i, j, :)), 'grouped');
        title([freq_bands{i, 1}, ' - ', stage_names{j}]);
        legend(modality_names);
        xlabel('Channels');
        ylabel('Power Spectral Density');
        set(gca, 'XTick', 1:EEG_preTraining_actual.nbchan, 'XTickLabel', {'F3', 'F4', 'P3', 'P4', 'P5', 'P6', 'O1', 'O2'});
        grid on;
    end
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
