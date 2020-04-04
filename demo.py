import cv2

from CTPN.text_detect import detect_img
from ocr.ocr_test import ocr_convert

if __name__ == '__main__':
    print('----')

    a = cv2.imread('test/image01.jpg')
    sick_name_img, doctor_advice_img = detect_img(a, 'image01')

    print('----------sick--------------')
    sick_text = ocr_convert(sick_name_img)
    print(sick_text)
    print('----------sick--------------')
    print('')
    print('')
    print('----------advice--------------')
    advice_text = ocr_convert(doctor_advice_img)
    print(advice_text)
    print('----------advice--------------')
