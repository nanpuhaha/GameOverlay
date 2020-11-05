import cv2
import Helpers.image_ocr_helper as ocr_helper
import Helpers.image_processing_helper as processing_helper

image = cv2.imread('../Support/ImagesTest/In_Game_Image_edited.jpg')

if __name__ == '__main__':
    image = processing_helper.get_grayscale(image)
    image = processing_helper.deskew(image)
    image = processing_helper.thresholding(image)
    cv2.imshow('img', image)
    cv2.waitKey(0)

