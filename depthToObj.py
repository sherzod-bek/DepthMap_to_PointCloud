#import libraries
import cv2
import numpy as np
from matplotlib import pyplot as plt

# creating .obj file with texture
def textured_obj(im_color, depth, filename):

    # creating .obj file
    f = open(filename, "w")

    for y in range(depth.shape[0]):
        for x in range(depth.shape[1]):
            # reverse distance(far/close)
            # depth[y,x] = 255 - depth[y,x]

            # for RGB colormap
            # f.write("v %d %d %d %d %d %d \n" % (y, x, depth[y,x], im_color[y,x,0], im_color[y,x,1], im_color[y,x,2] ))

            # for BGR colormap
            f.write("v %d %d %d %d %d %d \n" % (y, x, depth[y,x], im_color[y,x,2], im_color[y,x,1], im_color[y,x,0] ))

    print('textured point cloud (done)...')

# creating .obj file without texture
def point_obj(depth, filename):

    # creating .obj file
    f = open(filename, "w")

    for y in range(depth.shape[0]):
        for x in range(depth.shape[1]):
            # reverse distance(far/close)
            # depth[y,x] = 255 - depth[y,x]

            # without texture / just chose pixel values, default = 155
            f.write("v %d %d %d %d %d %d \n" % (y, x, depth[y,x], 200, 200, 200))

    print('point cloud (done)...')





# creating .obj file with texture
# -----------------------------------------------------------------
depth = cv2.imread('depth.bmp', 0) #reading depth image (grayscale)
im_color = cv2.imread('color.jpg', 1) #reading color image (RGB)
filename='textured_3D.obj'
textured_obj(im_color, depth, filename)

# creating .obj file without texture
# -----------------------------------------------------------------
depth = cv2.imread('depth.bmp', 0) #reading depth image (grayscale)
filename='point_3D.obj'
point_obj(depth, filename)
