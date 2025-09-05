import numpy as np
import cv2
img = np.zeros((512,512,3), np.uint8)

img = cv2.imread('mclaren-750s-driving-dynamic-hero-1280x516px.jpg')

img = cv2.line(img,(0,0),(1280,516),(255,123,123),5)

img = cv2.rectangle(img,(310,0),(510,128),(0,255,0),3)

img = cv2.circle(img,(447,63), 63, (0,0,255),1)

img = cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)

font = cv2.FONT_HERSHEY_COMPLEX_SMALL
cv2.putText(img,'CAR',(10,500), font, 9,(0,0,0),12,cv2.LINE_AA)


cv2.imshow('frame',img)
k = cv2.waitKey(0)
if k == 27:
 # wait for ESC key to exit
 cv2.destroyAllWindows()