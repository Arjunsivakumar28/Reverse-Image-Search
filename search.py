# -*- coding: utf-8 -*-
"""
Created on Tue May 31 16:24:39 2022

@author: sarju
"""

import colordescriptor
import searcher
import argparse
import cv2

#arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--index", required = True,
                help = "Path to index storage")
ap.add_argument("-q", "--query", required = True,
                      help = "Path to query image")
ap.add_argument("-r", "--result-path", required = True,
                      help = "Path to the result")
args = vars(ap.parse_args())

cd = colordescriptor.ColorDescriptor((8, 12, 3))

path = args["query"]
im = cv2.imread(path)
scale_percent = 25 # scaling percent
width = int(im.shape[1] * scale_percent / 100)
height = int(im.shape[0] * scale_percent / 100)
dim = (width, height)
query = cv2.resize(im, dim)

features = cd.describe(query)

# do the search
searcher = searcher.Searcher(args["index"])
results = searcher.search(features)

# show input image
cv2.imshow("Query", query)



# show outputs
for (score, resultID) in results:
	
    res_path = args["result_path"] + "/" + resultID
    
    ims = cv2.imread(res_path)
    scale_percent = 25 # percent of original size
    width = int(ims.shape[1] * scale_percent / 100)
    height = int(ims.shape[0] * scale_percent / 100)
    dim = (width, height)
    result = cv2.resize(ims, dim)
    cv2.imshow("Result", result)
    cv2.waitKey(0)





