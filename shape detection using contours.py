import cv2
import numpy as np
cap=cv2.VideoCapture(0)

framewidth=640
frameheight=480

cap.set(3,framewidth)
cap.set(4, frameheight)

def stackimages(scale,imgArray):
    rows=len(imgArray)
    cols=len(imgArray[0])
    rowsAvailable=isinstance(imgArray[0], list)
    width=imgArray[0][0].shape[1]
    height=imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0,cols):
                if imgArray[x][y].shape[0:2] == imgArray[0][0].shape[0:2]:
                    imgArray[x][y]=cv2.resize(imgArray[x][y], (0,0),None,scale,scale)
                else:
                   imgArray[x][y]=cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1],imgArray[0][0].shape[0
                                                                        ], None,scale,scale)
                
        
        imageBlank=np.zeros((height,width,3), np.uint8)
        hor=[imageBlank]*rows
        hor_con=[imageBlank]*rows
        for x in range(0,rows):
            hor[x]=np.hstack(imgArray[x])
        ver=np.vstack(hor) # we use vstcak fr combining the array vertically.
        
        else:
            for x range(0,rows):
                if imgArray[x].shape[0:2] == imgArray[0].shape[0:2]:
                     imgArray[x]=cv2.resize(imgArray, (0,0),None,scale,scale)
                else:
                    imgArray[x]=cv2.resize(imgArray[x], (imgArray[0].shape[1],imgArray[0].shape[0
                 ], None,scale,scale)
               
                if len(imgArray[x].shape) == 2:
                    imgArray[x]=cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
            hor=np.hstack(imgArray)
            ver=hor
     return ver
 
    
while True:
    success, image=cap.read()
    
    imgBlur=cv2.GaussianBlur(img,(7,7),1)
    imgGray=cv2.cvtColor(imgBlur,COLOR_BGR2GRAY)
    
    imgstack=stackImages(0.8, (img,imgBlur,imgGray]))  # Here 0.8-> Scale.
    cv2.imshow('Results',imgstack)
    if cv2.waiKey(1) &0XFF ==ord("q"):
        break
    
    
                                          
                
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
                    
    