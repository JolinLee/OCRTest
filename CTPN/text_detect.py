import cv2


def detect_img(img, fileName):
    sick_name = None
    doctor_advice = None

    if fileName == 'image01':
        sick_name = img[240:400, 40:580]
        doctor_advice = img[400:650, 40:580]

    if fileName == 'image02':
        sick_name = img[210:350, 40:560]
        doctor_advice = img[370:450, 40:580]

    if fileName == 'image03':
        sick_name = img[100:300, 40:780]
        doctor_advice = img[340:550, 40:800]

    if fileName == 'image04':
        sick_name = img[250:300, 60:550]
        doctor_advice = img[300:400, 60:550]

    if fileName == 'image05':
        sick_name = img[480:600, 200:9000]
        doctor_advice = img[600:1000, 200:9000]

    return sick_name, doctor_advice


if __name__ == '__main__':
    a = cv2.imread('../test/image05.jpg')
    sick_name_img, doctor_advice_img = detect_img(a, 'image05')

    cv2.imshow('sick_name', sick_name_img)
    cv2.imshow('advice', doctor_advice_img)

    cv2.waitKey()
    cv2.destroyAllWindows()

