import cv2
print(cv2.__version__)                                                                                                                    
width=640
height=360
myRadius=30
myColor=(0,0,0)
myThickness=2
cap=cv2.VideoCapture(0)
while True:
    ignore, frame=cap.read()
    #frame[140:220, 280:360]=(0,0,0)
    cv2.imshow("my webcam", frame)
    if cv2.waitKey(1) &0xff==ord('q'):
        break
cap.release()    


    

    

    

    

    
