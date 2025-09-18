#hsv pㄱocessing 사이트 확인 

import cv2
import numpy as np
'''
cap = cv2.VideoCapture('tracking2.avi')
while(cap.isOpened()):
    ret, frame = cap.read()
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # Color Space를 HSV로 바꾸는 것 

# define range of blue color in HSV
    lower_blue = np.array([10,128,128]) # 색상, 채도(낮을수록 흰색이 됨), 명도(낮을수록 어두워짐) 순 
    upper_blue = np.array([120,255,255]) # lower 는 최소값, upper는 최대값 채도와 명도의 값은 0~255임

# Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

# Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask) # 최소, 최대값 사이의 정한 값이 존재 할 경우 흰색으로 표시
    cv2.imshow('res',res) # 정한 값을 출력하는 화면 
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()

#코드는 정리되었고 영상을 찍어 그 색상에 대한 HSV 값만 정확히 넣으면 과제 끝 
'''


green = np.uint8([[[0,0,0 ]]])
hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
print(hsv_green)