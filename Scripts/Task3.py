# Task 3 - Splitting a point feature class
# Gabi Ballardo
# ENV 859 Fall 2022

# Imports system modules
import sys,os,arcpy

# Sets the environment workspace
arcpy.env.workspace = "V:\ENV859_PS4\Data"

# Allow arcpy to overwrite output
arcpy.env.overwriteOutput = True

# Ensures the ArcPy product edition used is “ArcInfo"
if arcpy.CheckProduct("ArcInfo") == "Available":
    ArcInfo = True
else:
    msg = 'ArcGIS for Desktop Advanced license not available'
    print(msg)
    sys.exit(msg)
    
# Uses the ListFeatureClasses function to return a list of BMR shapefiles.
featureclasses = arcpy.ListFeatureClasses("BMR*")

# Creates BMR list of folder names
BMR_folder_list = ["BMR_exc","BMR_fair","BMR_good","BMR_gf"]

# Creates new folder for each BMR shapefile
for folder in BMR_folder_list:
    arcpy.CreateFolder_management("V:\ENV859_PS4\Scratch",folder)

# Splits feature class by counties and moves them to their associated new folders
for fc in featureclasses:
    arcpy.analysis.Split(fc, "TriCounties.shp","CO_NAME",folder)







