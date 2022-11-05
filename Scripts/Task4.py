# Task 4 - Creating a script tool
# Gabi Ballardo
# ENV 859 Fall 2022

# Imports system modules
import arcpy

# Sets the environment workspace
arcpy.env.workspace = "V:\ENV859_PS4\Data"

# Allow arcpy to overwrite output
arcpy.env.overwriteOutput = True

# Creates a user-input dataset variable
Dataset = arcpy.GetParameterAsText(0)

# Creates a describe object for a user-specified dataset
dsc = arcpy.da.Describe(Dataset)

# Indicates the dataset’s catalogPath property
catalog_path = dsc['catalogPath']

# Extracts out the extent from describe object: dsc
extent = dsc['extent']

# Extracts XMin, YMin, XMax, and YMax
xmin = round(extent.XMin,1)
ymin = round(extent.YMin,1)
xmax = round(extent.XMax,1)
ymax = round(extent.YMax,1)

# Reports XMin, YMin, XMax, and YMax properties of the dataset’s extent object
arcpy.AddMessage(f'X min: {xmin}')
arcpy.AddMessage(f'Y min: {ymin}')
arcpy.AddMessage(f'X max: {xmax}')
arcpy.AddMessage(f'Y max: {ymax}')

# Sets variables to get shape type, format type, and dataset type
shape_type = dsc['shapeType']
format_type = dsc['baseName']
dataset_type = dsc['datasetType']

# Generates warning and error messages based on the dataset
# If dataset is a feature set, adds warning and shape type
if dsc['datasetType'] == "FeatureSet":
    arcpy.AddWarning("The shape type is {}.".format(shape_type))
# If dataset is a raster dataset, adds warning, format type, and #rows and #columns
elif dsc == "RasterDataset":
    arcpy.AddWarning("The format is {}.".format(format_type))
    # number of rows, and the number of columns in the dataset
    rows = extent.rows
    columns = extent.columns
    arcpy.AddWarning("# of rows: {rows}")
    arcpy.AddWarning("# of columns: {columns}")
# If dataset is neither, adds error message of the dataset type
else: 
    arcpy.AddError("The dataset type is {}.".format(dataset_type))



