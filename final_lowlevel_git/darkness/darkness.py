import cv2
import numpy as np

img = cv2.imread("-----enter path to image-------") #load rgb image
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #convert it to hsv
print(hsv)
print(type(hsv))
h, s, v = cv2.split(hsv)
print(v)
z = v.flatten()
print(z)
print(np.average(z))

v += 150
final_hsv = cv2.merge((h, s, v))

img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
cv2.imwrite("image_processed.jpg", img)


