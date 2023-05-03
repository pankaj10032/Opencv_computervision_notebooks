
import cv2
import numpy as np

while True:
     frame=np.zeros([250,250,3], dtype=np.uint8)
     frame[:,:]=(0,0,255)
     cv2.imshow("my window",frame)
     
     if cv2.waitKey(1) &0XFF==ord("q"):
         break