import os
import pytesseract
import re

from PIL import Image


def OCR(image):
    pytesseract.pytesseract.tesseract_cmd = 'C://Program Files (x86)//Tesseract-OCR//tesseract.exe'
    code = pytesseract.image_to_string(image, lang="chi_sim+eng")
    ret = re.findall(r'(\d+)', code)
    res = max(ret, key=len, default='')
    return res


if __name__ == '__main__':
    image = Image.open('pic/IMG_001.jpg')
    # rename_file = "%s.jpg" % OCR(image)
    # os.rename("pic/IMG_001.jpg", rename_file)
    print(OCR(image))
