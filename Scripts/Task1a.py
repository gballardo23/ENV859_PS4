# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 13:48:42 2022

@author: gab44
"""

# Description: Select roads of Class 4 from major roads tin the gnatcatcher habitat study area
   
# Import system modules
import arcpy
   
# Set workspace
arcpy.env.workspace = "V:\ENV859_PS4\Data"
   
# Set local variables
in_features = "streams.shp"
out_feature_class = "V:\ENV859_PS4\Scratch\StrmBuff1km.shp"
buffDist = "1000 kilometers"
arcpy.Buffer_analysis(in_features,out_feature_class,buffDist,'','','ALL')

print(arcpy.GetMessages())
