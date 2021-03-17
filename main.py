import matplotlib.pyplot as plt
import numpy as np
import imutils
import cv2

def showimg(image):
	cv2.imshow('image', image)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

image = cv2.imread('bir_belge.jpg')
#showimg(image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#showimg(gray)

ret,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)
#showimg(thresh)

kernel = np.ones((5,5), np.uint8)
img_dilation = cv2.dilate(thresh, kernel, iterations=1)
showimg(img_dilation)

im2,ctrs, hier = cv2.findContours(img_dilation.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

sorted_ctrs = sorted(ctrs, key=lambda ctr: cv2.boundingRect(ctr)[0])

for i, ctr in enumerate(sorted_ctrs):
    # Get bounding box
    x, y, w, h = cv2.boundingRect(ctr)

    if w < 10 or h < 10:
    	continue

    # Getting ROI
    roi = image[y:y+h, x:x+w]

    # show ROI
    #cv2.imshow('segment no:'+str(i),roi)
    cv2.rectangle(image,(x,y),( x + w, y + h ),(90,0,255),2)
    #cv2.waitKey(0)

showimg(image)
