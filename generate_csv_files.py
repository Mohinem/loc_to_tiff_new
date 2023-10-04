
import os
import argparse
CSV_LOCATION = 'csv_files'


def create_csv_files_from_loc_file_name(loc_file_name):
    # E.g. name of each file - A20220201 (year month day)
    loc_file_name = loc_file_name.split('/')
    loc_file_name = loc_file_name[len(loc_file_name)-1]

    year = loc_file_name[1:5]
    month = loc_file_name[5:7]
    day = loc_file_name[7:9]

    for i in range(0,24):
        csv_file_name = str(year) + '-' + str(month) + '-' + str(day) + 'T' + str(i).zfill(2) + ':00:00.000Z' + '.csv'
        print(csv_file_name)
        f = open(CSV_LOCATION + '/' + csv_file_name, 'w')
        f.close()

def extract_date_and_time(line):
    # Converat the date/time to 2022-02-01T00:00:00.000Z

    line_elements = line.split(',')
    date = line_elements[0]
    time = line_elements[1]

    # Extract year, month, day, hour, form the string
    year = date[0:4]
    month = date[5:7]
    day = date[8:10]   
    hour = time[0:2]
    date_and_time = str(year) + '-' + str(month) + '-' + str(day) + 'T' + str(hour) + ':00:00.000Z'

    return date_and_time

def open_and_write_to_file(file_name_path, new_string_to_write):
    # print(file_name_path)
    file = open(file_name_path, 'a')
    file.write(new_string_to_write)
    file.close()

def write_to_loc_file(line):
    date_and_time = extract_date_and_time(line)

    file_name_to_open = str(date_and_time) + '.csv'
    # Line looks like - 2022/02/01,00:00:02.246530, -6.0943,  97.9802, 14.4, 11

    line_elements = line.split(',')
    lat = line_elements[2]
    lon = line_elements[3]

    new_string_to_write = str(date_and_time) + ',' + str(lat) + ',' + str(lon) + '\n'

    file_name_path = CSV_LOCATION + '/' + file_name_to_open

    open_and_write_to_file(file_name_path, new_string_to_write)

def generate_csv_file(loc_file_location):
    # Open the file
    loc_file = open(loc_file_location, 'r')

    # Create csv file location
    if os.path.exists(CSV_LOCATION) is False:
        os.mkdir(CSV_LOCATION)
        
    # Using loc_file name, create 24 csv files of the form 2022-02-01T00:00:00.000Z
    create_csv_files_from_loc_file_name(loc_file.name)

    for each_line in loc_file:
        write_to_loc_file(each_line)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process LOC file and convert it to a TIFF file.")
    parser.add_argument("input_file_name", help="Input LOC file name")

    args = parser.parse_args()

    generate_csv_file(args.input_file_name)

