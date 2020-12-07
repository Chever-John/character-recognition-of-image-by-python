import pytesseract
from PIL import Image

# OCR是否可以正常使用
# pytesseract.pytesseract.tesseract_cmd = 'C://Program Files (x86)//Tesseract-OCR//tesseract.exe'
# image = Image.open('pic/IMG_001.jpg')
# code = pytesseract.image_to_string(image, lang="chi_sim+eng")
# print(code)


def OCR(image):
    pytesseract.pytesseract.tesseract_cmd = 'C://Program Files (x86)//Tesseract-OCR//tesseract.exe'
    code = pytesseract.image_to_string(image, lang="chi_sim+eng")
    return code


if __name__ == '__main__':
    image = Image.open('pic/IMG_001.jpg')
    print(OCR(image))