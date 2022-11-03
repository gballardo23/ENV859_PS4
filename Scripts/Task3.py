# Task 3 - Splitting a point feature class
# Gabi Ballardo
# ENV 859 Fall 2022

# Imports system modules
import sys,os,arcpy

arcpy.env.workspace = "V:\ENV859_PS4\Data"

# Allow arcpy to overwrite output
arcpy.env.overwriteOutput = True

# Set local variables

# Ensures the ArcPy product edition used is “ArcInfo “
if arcpy.CheckProduct("ArcInfo") == "Available":
    arcpy.PolygonToLine_management("Counties", "CountyLines")
else:
    msg = 'ArcGIS for Desktop Advanced license not available'
    print(msg)
    sys.exit(msg)
    
# Uses the ListFeatureClasses function to return a list of BMR shapefiles.
featureclasses = arcpy.ListFeatureClasses("BMR*")

# Copy shapefiles to a file geodatabase
for fc in featureclasses:
    arcpy.CopyFeatures_management(
        fc, os.path.join("V:\ENV859_PS4\scratch.gdb",
                         os.path.splitext(fc)[0]))
    
# Split  features in current BMR feature class by county features in TriCounties feature
BMR = "Habitat_Analysis.gdb/vegtype"
splitFeatures = "TriCounties.shp"
splitField = "CO_NAME"
outWorkspace = "C:/output/Output.gdb"

arcpy.analysis.Split(BMR, splitFeatures, splitField, outWorkspace)