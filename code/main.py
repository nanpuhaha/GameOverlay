import cv2
import Helpers.image_ocr_helper as ocr_helper
import Helpers.image_processing_helper as processing_helper

img = cv2.imread('../Support/ImagesTest/OCR_Test2.png')

if __name__ == '__main__':
    image = processing_helper.get_grayscale(img)
    ocr_helper.get_characters_to_string(image)
