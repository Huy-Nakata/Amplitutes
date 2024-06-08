import csv
import numpy as np
import os


# Function to read CSI data from a file
def read_csi_file(file_path):
    csi_records = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith("CSI_DATA"):
                parts = line.split(',')
                timestamp = float(parts[-1])
                csi_string = parts[-2].strip('[]')
                csi_values = list(map(int, csi_string.split()))
                csi_records.append((timestamp, csi_values))
    return csi_records


# Function to select a pair index from the first packet
def select_pair():
    while True:
        try:
            pair_index = int(input("Enter the pair index (0-63) to select: "))
            if 0 <= pair_index < 64:
                return pair_index
            else:
                print("Invalid index. Please enter a number between 0 and 63.")
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 63.")


# Function to filter packets within 1 minute of the given timestamp
def filter_packets_within_minute(csi_records, start_timestamp):
    return [record for record in csi_records if start_timestamp <= record[0] < start_timestamp + 60]


# Main function to process the CSI data
def process_csi_data(file_path, start_timestamp):
    csi_records = read_csi_file(file_path)
    filtered_records = filter_packets_within_minute(csi_records, start_timestamp)

    if not filtered_records:
        raise ValueError("No packets found within 1 minute of the given timestamp.")

    # Select a pair index from the first packet of the timestamp
    pair_index = select_pair()

    # Calculate amplitudes for the selected pair
    amplitudes = [(timestamp, np.sqrt(csi_values[2 * pair_index] ** 2 + csi_values[2 * pair_index + 1] ** 2)) for
                  timestamp, csi_values in filtered_records]

    # Save results to a CSV file
    output_file = 'csi_amplitudes.csv'
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Timestamp', 'Amplitude'])
        writer.writerows(amplitudes)

    print(f'Results saved to {output_file}')


# Define the file path and the start timestamp
file_path = r'D:\Wifi CSI data\Data1min\Nhap\Test.csv'
start_timestamp = 1717692179.3986897  # Example timestamp, replace with your actual timestamp

# Process the CSI data
process_csi_data(file_path, start_timestamp)
