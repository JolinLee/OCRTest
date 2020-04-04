from PIL import Image
import pytesseract


def ocr_convert(img_scope):
    result = pytesseract.image_to_string(img_scope, lang='eng+chi_tra')
    return result


if __name__ == '__main__':
    print('hello')
    img = Image.open('../test2.png') # stopclass
    text = pytesseract.image_to_string(img, lang='eng+chi_tra')  # chi_tra  eng
    print(text)
