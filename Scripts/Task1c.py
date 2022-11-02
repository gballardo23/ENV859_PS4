# Task 1c - Enabling user input
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
# Allows for user to specify the output name
out_feature_class = sys.argv[1]
# Allows user to set buffer distance
buffDist = sys.argv[2]

# Buffers streams.shp with user inputs
arcpy.Buffer_analysis(in_features,out_feature_class,buffDist,'','','ALL')

# Displays messages, warnings, or errors to console
print(arcpy.GetMessages())