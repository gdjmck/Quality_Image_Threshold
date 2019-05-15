import os
import cv2
import numpy
import glob
import shutil

'''
import sys
missing_path = '/home/chk/Documents/data/Quality_Image_Threshold/final_lowlevel_git/blur/BlurDetection'
sys.path.append(missing_path)
print('Add ', missing_path)
'''
import BlurDetection

'''
img_path = input("Please Enter Image Path: ")
assert os.path.exists(img_path), "img_path does not exists"
'''
'''
args = BlurDetection.parser.parse_args()
img_path = args.image_paths[-1]
print('img_path', img_path)

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
'''
    #print(a)
    #print(blurry)

if __name__ == '__main__':
    import numpy as np
    img = np.random.randint(0, 255, (512, 512, 3), np.uint8)
    print(img.shape)
    img_fft, val, blurry = BlurDetection.blur_detector(img)
    print(val)