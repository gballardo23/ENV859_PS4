# Task 1b - Setting environment values in the script
# Gabi Ballardo
# ENV 859 Fall 2022
   
# Imports system modules
import arcpy
   
# Sets the ArcPy workspace environment to Data folder in ENV859_PS4 folder
arcpy.env.workspace = "V:\ENV859_PS4\Data"
# Allows script outputs to be overwritten
arcpy.env.overwriteOutput = True
   
# Sets local variables

# Creates string variable that includes just the file name streams.shp
in_features = "streams.shp"
# Creates string variable that sets path and filename of buffer output (hard-coded)
out_feature_class = "V:\ENV859_PS4\Scratch\StrmBuff1km.shp"
# Sets buffer distance
buffDist = "1000 kilometers"

# Buffers streams.shp 1000 meters
arcpy.Buffer_analysis(in_features,out_feature_class,buffDist,'','','ALL')

# Displays messages, warnings, or errors to console
print(arcpy.GetMessages())