import cv2 as cv

img = cv.imread('img/cat.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
faceCascade = cv.CascadeClassifier('detect.xml')   #載入辨識模型

cv.waitKey(0)
