import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('image.jpg.png')
k=3
blur = cv2.GaussianBlur(img,(k,k),0)
median = cv2.medianBlur(img,k) #얘 ㅈㄴ 중요함 가장 높은 수가 남은 평균을 망치는 것을 막고자 가눙데 숫자에 있는 값을 송출 

plt.subplot(121),plt.imshow(median),plt.title('median')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('GaussianBlur')
plt.xticks([]), plt.yticks([])

plt.show()
