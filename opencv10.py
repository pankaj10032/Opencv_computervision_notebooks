import cv2
print(cv2.__version__)
width=640
height=360
snipW=120
snipH=60

boxCR=int(height/2)# center row of our box
boxCC=int(width/2) # center column of our box 
# here each time we will move our box by some pixels.
deltaRow=1 # we are going througn 1 pixel in row direction.
deltaColumn=1 # We are going through 1 pixel in column direction.


cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

while True:
    ignore,frame=cam.read()
    #in case of indexing always make integar
    frameROI=frame[int(boxCR-snipH/2):int(boxCR+ snipH/2), int(boxCC-snipW/2):int(boxCC+ snipW/2)]
    frame=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame=cv2.cvtColor(frame,cv2.COLOR_GRAY2BGR)
    frame[int(boxCR-snipH/2):int(boxCR+ snipH/2), int(boxCC-snipW/2):int(boxCC+ snipW/2)]=frameROI # shows a little green square on main frame
    cv2.imshow('My ROI', frameROI)
    cv2.moveWindow("My ROI", width,0)
    cv2.imshow("my WEBcam", frame)
    cv2.moveWindow("my WEBcam", 0, 0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()