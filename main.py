import os
import pytesseract
import re

from PIL import Image


def OCR(image):
    # 输入的是图片的地址，返回的是从图片中读取到的学号信息。
    pytesseract.pytesseract.tesseract_cmd = 'C://Program Files (x86)//Tesseract-OCR//tesseract.exe'
    code = pytesseract.image_to_string(image, lang="chi_sim+eng")
    ret = re.findall(r'(\d+)', code)
    res = max(ret, key=len, default='')
    return res


if __name__ == '__main__':
    images = Image.open('pic/IMG_004.jpg')
    rename_file = "%s.jpg" % OCR(images)
    os.rename("pic/IMG_004.jpg", "pic/" + rename_file)
    print(OCR(images))