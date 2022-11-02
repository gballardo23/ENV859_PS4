# Task 1a - Creating the initial buffer script
# Gabi Ballardo
# ENV 859 Fall 2022


# Description: Buffers streams within 1000 meters
   
# Imports system modules
import arcpy
   
# Sets local variables

# Creates string variable that includes path to streams.shp
in_features = "V:\ENV859_PS4\Data\streams.shp"
# Creates string variable that sets path and filename of buffer tool output
out_feature_class = "V:\ENV859_PS4\Scratch\StrmBuff1km.shp"
# Sets buffer distance
buffDist = "1000 kilometers"

# Buffers streams.shp 1000 meters
arcpy.Buffer_analysis(in_features,out_feature_class,buffDist,'','','ALL')

# Displays messages, warnings, or errors to console
print(arcpy.GetMessages())