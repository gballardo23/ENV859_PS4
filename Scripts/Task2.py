# Task 2 - Iterating through road type codes
# Gabi Ballardo
# ENV 859 Fall 2022

# Imports system modules
import arcpy
   
# Allows script outputs to be overwritten
arcpy.env.overwriteOutput = True
   
# Sets local variables

# Creates a multi-value string variable of road type class values
road_type_class = "0;201;203"
# Creates a list variable by splitting the values
road_class_list = road_type_class.split(";")

# Iterates through each of the road class types in the list
for road_type in road_class_list:
    
    #Assigns variables
    
    # Creates a string variable containing the path to the Roads.shp feature class
    in_features = "V:\ENV859_PS4\Data\Roads.shp"
    
    out_feature_class = f"V:\ENV859_PS4\Scratch\\roads_{road_type}.shp"
    
    where_clause = f'ROAD_TYPE={road_type}'
    
    # Selects for road types in the list
    arcpy.Select_analysis(in_features,out_feature_class,where_clause)
 
    # Displays messages, warnings, or errors to console
    print(arcpy.GetMessages())