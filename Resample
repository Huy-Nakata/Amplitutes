import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the CSV file from the uploaded path
file_path = "C:/Users/PC/Downloads/csi_amplitudes (3).csv"
csi_data = pd.read_csv(file_path)

# Check the first few rows to verify the contents
print(csi_data.head())

# Convert the 'Timestamp' column to datetime
csi_data['Timestamp'] = pd.to_datetime(csi_data['Timestamp'], unit='s')

# Extract the 'Amplitude' column as a list
data = csi_data['Amplitude'].tolist()

# Define the start time from the first timestamp
start_time = csi_data['Timestamp'].iloc[0]
timesteps = pd.date_range(start=start_time, periods=len(data), freq="s")

# Create the series with data from the file
series = pd.Series(data=data, index=timesteps)

# Resample the series to 1-second intervals and interpolate linearly
resampled_series = series.resample("1s").interpolate("linear")

# Perform the Fourier Transform
fft_result = np.fft.fft(resampled_series)

# Get the frequencies corresponding to the FFT result
n = len(resampled_series)
frequencies = np.fft.fftfreq(n, d=1)  # d=1 since the data is sampled at 1-second intervals

# Calculate the amplitude spectrum
amplitude_spectrum = np.abs(fft_result)

# Plot the amplitude spectrum
plt.figure(figsize=(12, 6))
plt.plot(frequencies, amplitude_spectrum)
plt.title('Amplitude Spectrum')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()
