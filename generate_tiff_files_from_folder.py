import argparse
import generate_csv_files as g_csv
import generate_tiff_files as g_tiff
import os

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process folder and convert it to a TIFF file.")
    parser.add_argument("input_folder_name", help="Input Folder Name")
    parser.add_argument("csv_folder_name", help="CSV Folder Name")
    parser.add_argument("output_folder_name", help="Output Folder Name")
    parser.add_argument("resolution", help= "Resolution")

    args = parser.parse_args()

    if not os.path.exists(args.csv_folder_name):
    # If it doesn't exist, create it
        os.makedirs(args.csv_folder_name)

    if not os.path.exists(args.output_folder_name):
    # If it doesn't exist, create it
        os.makedirs(args.output_folder_name)

    input_files = [file for file in os.listdir(args.input_folder_name) if file.endswith('.csv')]

    for each_file in input_files:
        g_csv.generate_csv_file(args.input_folder_name + '/' + each_file)

    g_tiff.generate_tiff_files(args.csv_folder_name, args.output_folder_name, args.resolution)
    print("NIGGA")