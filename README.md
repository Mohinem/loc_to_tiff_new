# loc_to_tiff_new
Converts loc file to TIFF file
There are 3 python scripts-

1. generate_csv_files.py -> This takes an input file name (path to the place where input file is located) and generates CSV files at the location defined by 'CSV_LOCATION' variable in the script. The default name is 'csv_files'.

2. generate_tiff_files.py -> Takes the CSV folder name as input, an output folder name, and the resolution (0.1,1.0 etc)

3. generate_tiff_files_from_folder.py -> Takes the input folder name, csv folder name (right now, please sync with the name in script 1), output folder name, and resolution. It generates TIFF files from all loc files present in folder, making use of the above scripts.
