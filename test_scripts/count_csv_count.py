import os
import csv

def count_lines_in_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return sum(1 for line in file)

def check_count(loc_file_location, csv_folder_location):
    # Count the lines in the LOC file
    loc_line_count = count_lines_in_file(loc_file_location)
    
    # List all CSV files in the folder
    csv_files = [file for file in os.listdir(csv_folder_location) if file.endswith('.csv')]
    
    csv_line_count = 0
    # Compare LOC file line count with each CSV file in the folder
    for csv_file in csv_files:
        csv_file_path = os.path.join(csv_folder_location, csv_file)
        csv_line_count = csv_line_count + count_lines_in_file(csv_file_path)
        
        print(f"File: {csv_file}, LOC Line Count: {loc_line_count}, CSV Line Count: {csv_line_count}, Equal: {loc_line_count == csv_line_count}")

# Example usage
check_count('/home/mohinem/Downloads/Feb2022/A20220201.loc', '/home/mohinem/loc_to_tiff_new/csv_files')
