# Task 2 - Iterating through road type codes
# Gabi Ballardo
# ENV 859 Fall 2022

# Imports system modules
import arcpy
   
# Allows script outputs to be overwritten
arcpy.env.overwriteOutput = True
   
# Sets local variables

# Creates a string variable containing the path to the Roads.shp feature class
in_features = "V:\ENV859_PS4\Data\Roads.shp"
# Creates a multi-value string variable of road type class values
road_type_class = "0;201;203"
# Creates a list variable by splitting the values
road_class_list = road_type_class.split(";")

# Creates string variable that sets path of the select output (hard-coded)
output_path = "V:\ENV859_PS4\Scratch\\roads_"

# Create a cursor (this is like opening a file)
rows = arcpy.da.SearchCursor(in_features,'ROAD_TYPE')

# Iterates through each of the road class types in the list
for row in rows:
    road_type = row[0]
    out_feature_class = output_path +str(road_type) +".shp"
    print(out_feature_class)
    # Selects 
    arcpy.Select_analysis(in_features,output_path,road_type)
    # Creates three distinct shapefile outputs
 
   
    # Displays messages, warnings, or errors to console
    print(arcpy.GetMessages())