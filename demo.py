import cv2
from os import listdir
from os.path import isfile, isdir, join, splitext
import csv

from CTPN.text_detect import detect_img
from ocr.ocr_test import ocr_convert


def get_file_extension(filename):
    arr = splitext(filename)
    return arr[len(arr) - 1]


def write_csv(file_path, table):
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        # 寫入二維表格
        writer.writerows(table)

if __name__ == '__main__':
    data = [["Index", "Disease", "Disposal_Consideration"]]

    img_folder_path = 'test'
    for file_name in listdir(img_folder_path):
        # 產生檔案的絕對路徑
        fullpath = join(img_folder_path, file_name)
        if isfile(fullpath) & (get_file_extension(file_name) == '.jpg'):
            print("檔案：", file_name)
            print("路徑 :", fullpath)

            img = cv2.imread(fullpath)
            disease_name_img, disposal_consideration_img = detect_img(img, file_name)
            disease_name_text = ocr_convert(disease_name_img)
            disposal_consideration_text = ocr_convert(disposal_consideration_img)
            data.append([file_name, disease_name_text, disposal_consideration_text])

    write_csv('nlptest.csv', data)
    print('----')

    # a = cv2.imread('test/image01.jpg')
    # sick_name_img, doctor_advice_img = detect_img(a, 'image01')
    #
    # print('----------sick--------------')
    # sick_text = ocr_convert(sick_name_img)
    # print(sick_text)
    # print('----------sick--------------')
    # print('')
    # print('')
    # print('----------advice--------------')
    # advice_text = ocr_convert(doctor_advice_img)
    # print(advice_text)
    # print('----------advice--------------')
