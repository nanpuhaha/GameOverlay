import cv2
import numpy as np

from util.image_hsv_util import testhsv
from Helpers.image_ocr_helper import get_characters_to_string

# Load image, convert to HSV format, define lower/upper ranges, and perform
# color segmentation to create a binary mask
local_image = '../../Support/ImagesTest/In_Game_Image_2.jpg'

image = cv2.imread(local_image)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

testhsv(image)

lower = np.array([0, 0, 213])
upper = np.array([165, 50, 255])
mask = cv2.inRange(hsv, lower, upper)

# Create horizontal kernel and dilate to connect text characters
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (30, 3))
dilate = cv2.dilate(mask, kernel, iterations=5)

# Find contours and filter using aspect ratio
# Remove non-text contours by filling in the contour
cnts = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
for c in cnts:
    x, y, w, h = cv2.boundingRect(c)
    ar = w / float(h)
    if ar < 5:
        cv2.drawContours(dilate, [c], -1, (0, 0, 0), -1)

# Bitwise dilated image with mask, invert, then OCR
result = 255 - cv2.bitwise_and(dilate, mask)
result_final = cv2.fastNlMeansDenoising(result, None, 30, 7, 21)
data = get_characters_to_string(result)
print(data)

cv2.imshow('mask', mask)
cv2.imshow('dilate', dilate)
cv2.imshow('result', result_final)
cv2.waitKey()