# Task 4 - Creating a script tool
# Gabi Ballardo
# ENV 859 Fall 2022

# Imports system modules
import arcpy

# Creates a user-input dataset variable
Dataset = arcpy.GetParameterAsText(0)

# Creates a describe object for a user-specified dataset
dsc = arcpy.da.Describe(Dataset)

# Indicates the dataset’s catalogPath property
print(dsc['catalogPath'])

# Reports XMin, YMin, XMax, and YMax properties of the dataset’s extent object

# Checks the dataset's datasetType
print(dsc['datasetType'])

# Generates warning and error messages based on the dataset
if dsc['datasetType'] == "FeatureSet":
    print(arcpy.AddWarning("The shape type is {}.".format(Dataset)))
elif dsc == "RasterDataset":
    print(arcpy.AddWarning("The format is {}.".format(Dataset)))
else: 
    print(arcpy.AddError("The dataset type is {}.".format(Dataset)))


