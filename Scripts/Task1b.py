# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 14:30:16 2022

@author: gab44
"""

# Description: Buffers streams within 1000 km
   
# Imports system modules
import arcpy
   
# Sets the ArcPy workspace environment to Data folder in ENV859_PS4 folder
arcpy.env.workspace = "V:\ENV859_PS4\Data"
# Allows script outputs to be overwritten
arcpy.env.overwriteOutput = True
   
# Sets local variables
in_features = "streams.shp"
out_feature_class = "V:\ENV859_PS4\Scratch\StrmBuff1km.shp"
# Sets buffer distance
buffDist = "1000 kilometers"

# Uses buffer tool
arcpy.Buffer_analysis(in_features,out_feature_class,buffDist,'','','ALL')

print(arcpy.GetMessages())