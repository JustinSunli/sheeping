# -*- coding: utf-8 -*-

from PIL import Image
import pytesseract

if __name__ == "__main__":
    #
    text = pytesseract.image_to_string(Image.open(r'C:\Users\Michael\Desktop\image.png'))
    print(text)