import numpy as np
import math
from osgeo import gdal
import os
import argparse

def generate_tiff_files(csv_folder_name, output_folder_name, resolution):

    csv_files = [file for file in os.listdir(csv_folder_name) if file.endswith('.csv')]

    for csv_file in csv_files:
        # Start the algorithm here.

        resolution = float(resolution)
        # Step 1. Establish the raster array, dimensions 360/resolution and 180/-resolution, and initialize 

        num_longitudes = int(360/resolution)
        num_latitudes = int(180/resolution)
        temp_array = np.zeros((num_latitudes, num_longitudes), dtype=int)

        for i in range(0,num_latitudes):
            for j in range(0, num_longitudes):
                temp_array[i,j] = 0

        # Step 2. Open the csv_file and loop through each line
        # print("CSV File - " + str(csv_file))
        file = open(csv_folder_name + csv_file, 'r')

        for each_line in file:
            line_elements = each_line.split(',')
            date = line_elements[0]
            lat = line_elements[1]
            lon = line_elements[2]

            # Round lat, lon to 1 decimal point
            lat = round(float(lat), 1)
            lon = round(float(lon), 1)
            # Step 3. Define grid coordinates

            grid_lon = (math.floor((180+lon)/resolution))%num_longitudes
            grid_lat = (math.floor((lat-90)/(-resolution)))%num_latitudes

            # Step 4 . Inrement count by 1
            try:
                temp_array[grid_lat, grid_lon] = temp_array[grid_lat, grid_lon] + 1
            except Exception as e:
                print("Failed at lat,lon = " + str(lat)+ ',' + str(lon))
                print("Grid = " + str(grid_lat) + ',' + str(grid_lon))
                print(e)
                quit()

        
        # Step 5 - Finally generate the raster file
        output_file_string = output_folder_name + date + '.tiff'
        driver = gdal.GetDriverByName('GTiff')
        output_raster = driver.Create(output_file_string, num_longitudes, num_latitudes, 1, gdal.GDT_Int32)

        output_raster.SetGeoTransform([-180, float(resolution), 0, 90, 0, -float(resolution)])
        output_raster.SetMetadata({'_Axes': 'Lat Long'})

        output_band = output_raster.GetRasterBand(1)
        output_band.SetNoDataValue(0) 

        output_band.WriteArray(temp_array)
        output_band.SetDescription("Number of Lightning Strikes")
        output_band.SetMetadata({'_Slice': 'Count'})        

        # Finally, close the csv_file
        file.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process LOC file and convert it to a TIFF file.")
    parser.add_argument("csv_folder_name", help="CSV Folder Name")
    parser.add_argument("output_folder_name", help="Output Folder Name")
    parser.add_argument("resolution", help= "Resolution")

    args = parser.parse_args()

    generate_tiff_files(args.csv_folder_name, args.output_folder_name, args.resolution)