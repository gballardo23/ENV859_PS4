# Task 1e -  Iterating through buffer distances
# Gabi Ballardo
# ENV 859 Fall 2022
   
# Imports system modules
import sys,arcpy
   
# Sets the ArcPy workspace environment to Data folder in ENV859_PS4 folder
arcpy.env.workspace = "V:\ENV859_PS4\Data"
# Allows script outputs to be overwritten
arcpy.env.overwriteOutput = True
   
# Sets local variables

# Creates string variable that includes just the file name streams.shp
in_features = "streams.shp"

# Sets buffer distances 
buffDistList = [100,200,300,400,500]

# Creates path name for outputs
output_path = "V:\ENV859_PS4\Scratch\\buff_"

# Iterates through each of the buffer distances in the list
for buffer in buffDistList:
    # Buffers streams.shp with buffer distances from the list
    arcpy.Buffer_analysis(in_features,output_path,buffer,'','','ALL')
    # Creates output feature class with separate output names for each distance
    out_feature_class = output_path +str(buffer) +"m.shp"
    print(out_feature_class)

    # Displays messages, warnings, or errors to console
    print(arcpy.GetMessages())