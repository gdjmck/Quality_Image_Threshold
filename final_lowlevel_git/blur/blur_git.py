import os
import cv2
import numpy
import BlurDetection
import glob

img_path = raw_input("Please Enter Image Path: ")
assert os.path.exists(img_path), "img_path does not exists"

image_data1 = glob.glob(img_path + '/*.jpg')
a = []
for i in image_data1:

    img = cv2.imread(i)
    img_fft, val, blurry = BlurDetection.blur_detector(img)
    a.append(val)
    print(a)
    print blurry

    print "this image {0} blurry".format(["isn't", "is"][blurry])

