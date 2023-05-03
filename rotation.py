import numpy as np
import cv2

image=cv2.imread("donut.jpg")
cv2.imshow("original",image)
cv2.waitKey(0)

(h,w)=image.shape[:2]
center=(w//2,h//2)

M=cv2.getRotationMatrix2D(center,45,1.0)
rotated=cv2.warpAffine(image,M,(w,h))

cv2.imshow("Rotated by 45 degrees", rotated)
cv2.waitKey(0)

M=cv2.getRotationMatrix2D(center, -90,1.0)
rotated=cv2.warpAffine(image,M,(w,h))
cv2.imshow("Rotated by -90 degrees",rotated)
cv2.waitKey(0)

def rotate(image,angle,center=None, scale=1.0):
    (h,w)=image.shape[0:2]
    
    if center is None:
        center=(w//2, h//2)
    
    M=cv2.getRotationMatrix2D(center, angle,scale)
    rotated=cv2.warpAffine(image,M,(w,h))
    return rotated



