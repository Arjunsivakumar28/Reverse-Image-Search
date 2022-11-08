# -*- coding: utf-8 -*-
"""
Created on Mon May 30 20:21:20 2022

@author: sarju
"""

import colordescriptor
import cv2
import argparse
import glob



# arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required = True,
                help = "Path to directory with image to be indexed")
ap.add_argument("-i", "--index", required = True,
                help = "Path to storage of index")
args = vars(ap.parse_args())

#Set the bins here
cd = colordescriptor.ColorDescriptor((8, 12, 3))

output = open(args["index"], "w")

for imagePath in glob.glob(args["dataset"] + "/*.jpg"):

    imageID = imagePath[imagePath.find("\\") + 1:]
    image = cv2.imread(imagePath)
    
    features = cd.describe(image)
    

    features = [str(f) for f in features]
    output.write("%s, %s\n" % (imageID, ",".join(features)))

output.close()
    