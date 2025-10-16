import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('20241028_122740.png')
org_img = img.copy()
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(img_gray,127,255,0)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

img = cv2.drawContours(img, contours[3], -1, (255,0,0), 9)

plt.subplot(1,2,1),plt.imshow(org_img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(1,2,2),plt.imshow(img,cmap = 'gray')
plt.title('contours'), plt.xticks([]), plt.yticks([])

plt.show()
