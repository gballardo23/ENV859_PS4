# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 13:48:42 2022

@author: gab44
"""


# Description: Buffers streams within 1000 km
   
# Imports system modules
import arcpy
   
# Sets local variables
in_features = "V:\ENV859_PS4\Data\streams.shp"
out_feature_class = "V:\ENV859_PS4\Scratch\StrmBuff1km.shp"
# Sets buffer distance
buffDist = "1000 kilometers"

# Uses buffer tool
arcpy.Buffer_analysis(in_features,out_feature_class,buffDist,'','','ALL')

print(arcpy.GetMessages())