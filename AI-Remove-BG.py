//เราจะใช้ Library 2 ตัวคือ CV2 และ Numpy 
  โดย CV2 เป็นตัวทำ Image-Processing 
  และ Numpy เป็นตัวประมวลผล //

import cv2
import numpy as np

//Input รูป //
cv2.nameWindow('Result', cv2.WINDOW_NORMAL)
imgOutput = cv2.imread('img/รูปคน.jpg')
height,width = imgOutput.shape[:2]


mask = np.zeros(imgOutput.shape[:2],np.uint8)

backgroundModel = np.zeros((1,65),np.float64)

forgrondModel = np.zeros((1,65),np.float64)
rect = (10,10,width-30, height-30)
cv2.grabCut(imgOutput,mask,rect,backgroundModel,forgrondModel,5,cv2.GC_INIT_WITH_RECT)
mask = np.where((mask==2) (mask==0),0,1).astype('uint8')
image_1 = imgOutput*mask[:,:,np.newaxis]

//ส่วนที่นำพื้นหลังออก//
background = imgOutput-image_1

background =  [np.where((background > [0,0,0]).all(axis = 2))] = [255,255,255]
final = background + image_1
cv2.imshow("Result", final)
key = cv2.waitkey(0)
if key == 2:
    cv2.destroyAllWindow()
