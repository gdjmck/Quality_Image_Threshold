import os
import cv2
import numpy
import BlurDetection
import glob
import BlurDetection.scripts as scripts
import shutil

'''
img_path = input("Please Enter Image Path: ")
assert os.path.exists(img_path), "img_path does not exists"
'''
args = scripts.get_args()
img_path = args.image_paths[-1]

image_data1 = glob.glob(img_path + '/*.jpg')
unblur, blur = [], []
for i in image_data1:

    img1 = cv2.imread(i)
    img_fft1, val1, blurry1 = BlurDetection.blur_detector(img1)
    unblur.append(val1)

    img2 = cv2.imread(i.replace('blur0', 'blur1'))
    img_fft2, val2, blurry2 = BlurDetection.blur_detector(img2)
    blur.append(val2)
    print(i, '\t original: %.3f\tblur: %.3f'%(val1, val2))
    #print(a)
    #print(blurry)
    '''
    if blurry:
        shutil.move(i, '/home/chk/Documents/data/train_code/URL_image/blur_test/blur')
    else:
        shutil.move(i, '/home/chk/Documents/data/train_code/URL_image/blur_test/not_blur')
    '''
    #print("{0} {1} blurry".format(i, ["isn't", "is"][blurry]))

