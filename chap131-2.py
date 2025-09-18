import cv2
import numpy as np

def nothing(x):
   pass

font = cv2.FONT_HERSHEY_SIMPLEX
img_origin = cv2.imread('image1.jpg') 
drawing=False
mode= True
ix,iy=-1,-1
img = img_origin.copy()

def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode,img
    img = img_origin.copy()
    if event==cv2.EVENT_LBUTTONDOWN:
        drawing=True
        ix,iy=x,y
 
    elif event==cv2.EVENT_MOUSEMOVE:
        txt = 'Mouse Position ('+str(x)+','+str(y)+')'+str(img[y,x])
        cv2.putText(img,txt,(30,60), font, 2,(255,255,255),2,cv2.LINE_AA)
        if drawing==True:
            if mode== True:
             cv2.rectangle(img,(ix,iy),(x,y),(0,0,255),-1)
            else:
             cv2.circle(img,(x,y),5,(0,0,255),-1)
    
    elif event==cv2.EVENT_LBUTTONUP:
        drawing=False
        if mode== True:
            cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
        else:
            cv2.circle(img,(x,y),5,(0,0,255),-1)

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.createTrackbar('R','image',0,255,nothing)

cv2.setMouseCallback('image',draw_circle)

while(1):
    r=cv2.getTrackbarPos('R','image')
    print(r)
    cv2.imshow('image',img)
    k=cv2.waitKey(1)&0xFF
    if k== ord('m'):
        mode=not mode
    elif k==27:
        break
cv2.destroyAllWindows()


'''
cv2.namedWindow('image')

img[100:200, 100:200, 2] = 255

while(1):
    cv2.imshow('image',img)
    k=cv2.waitKey(1)&0xFF
    if k== 27:
        break

cv2.destroyAllWindows()
'''