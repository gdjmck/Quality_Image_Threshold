from PIL import Image
import os
import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
import os

def change_contrast(img, level):
    factor = (259 * (level + 255)) / (255 * (259 - level))
    def contrast(c):
        return 128 + factor * (c - 128)
    return img.point(contrast)


j = os.listdir("-----enter path to images-------")

for i in range(len(j)):
    print(j[i])
    c = change_contrast(Image.open("-----enter path to images to open -----" + j[i]), 100)
    c.save("-----enter path to store images -------- " + "/contrast_" + j[i])
