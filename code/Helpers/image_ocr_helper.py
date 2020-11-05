import re
import cv2
from pytesseract import Output, pytesseract

# custom config for tesseract
# custom_config = r'--oem 3 --psm 6 outputbase digits'
# custom_config = r'-c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyz --psm 6' pegar apenas essas letras
# custom_config = r'-c tessedit_char_blacklist=abcdefghijklmnopqrstuvwxyz --psm 6' Qualquer coisa menos essas letras
# custom_config = r' -c preserve_interword_spaces=1 -l jpn --psm 6' tratar espaços gerados pelo ocr
# print(pytesseract.image_to_string(img, config=custom_config))


def get_characters_and_outline_positions(image):
    custom_config = r'-l jpn+eng --psm 6'
    h, w, c = image.shape
    boxes = pytesseract.image_to_boxes(image, config=custom_config)
    for b in boxes.splitlines():
        b = b.split(' ')
        img_result = cv2.rectangle(image, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 1)

    cv2.imshow('img', img_result)
    cv2.waitKey(0)


def get_characters_to_string(image):
    custom_config = r'-c preserve_interword_spaces=1 -l jpn --psm 6'
    result = pytesseract.image_to_string(image, config=custom_config)
    print(result)


def get_words_and_outline_positions(image):
    d = pytesseract.image_to_data(image, output_type=Output.DICT)
    n_boxes = len(d['text'])
    for i in range(n_boxes):
        if int(d['conf'][i]) > 60:
            (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
            image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('img', image)
    cv2.waitKey(0)


def get_text_from_image_with_regex(image):
    d = pytesseract.image_to_data(image, output_type=Output.DICT)
    keys = list(d.keys())

    regex_pattern = '^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[012])/(19|20)\d\d$'
    regex_pattern = '/japanese/gim'

    n_boxes = len(d['text'])
    for i in range(n_boxes):
        if int(d['conf'][i]) > 60:
            if re.match(regex_pattern, d['text'][i]):
                (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
                image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('img', image)
    cv2.waitKey(0)
