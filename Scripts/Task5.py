# Task 5
# Gabi Ballardo
# ENV 859 Fall 2022

# Imports system modules
import sys,os,arcpy

# Sets the environment workspace
arcpy.env.workspace = "V:\ENV859_PS4\Data"

# Allow arcpy to overwrite output
arcpy.env.overwriteOutput = True

# Enables two inputs from the user: a feature class and a field name

# Allows for user to specify the feature class
feature_class = sys.argv[1]
# Allows for user to specify the field from that feature class
field_name = sys.argv[2]

# Creates a point object
point = arcpy.Point(587000, 265000)

# Creates a SearchCursor from the feature class
cur = arcpy.da.SearchCursor(feature_class,['SHAPE@',field_name])

# For each row, print the WELL_ID and WELL_TYPE fields, and
# the feature's x,y coordinates
with arcpy.da.SearchCursor(feature_class, field_name) as cursor:
    for feature in cursor:
        recShape = feature
        if Point in recShape:
            attrib = getattr(field_name)
            arcpy.AddMessage(f'The field value is: {attrib}')
    