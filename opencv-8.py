import cv2
print(cv2.__version__)
import time
width=640
height=360
myRadius=30
myColor=(0,0,0)
myThickness=2
myText='you are fast'
cap=cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cap.set(cv2.CAP_PROP_FPS, 30)
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"MJPG")) # Here MJPG-> Moving jpeg
tLast=time.time()
time.sleep(0.1)
# fps= frames per second is the inverse of how long it takes to do one frame.
fpsFILT=30
while True:
    dT=time.time()-tLast
    print(dT)
    fps=1/dT
    fpsFILT=fpsFILT*0.97 + fps*0.03
    print(fps)
    tLast=time.time()
    ignore, frame=cap.read()
    #frame[140:220, 280:360]=(0,0,0)
    cv2.rectangle(frame, (250,140),(390,220),(0,255,0),5)  # here 5-> linewidth
    cv2.circle(frame,(int(width/2),int(height/2)),myRadius,myColor,myThickness)
    cv2.putText(frame, myText, (120,60), cv2.FONT_HERSHEY_COMPLEX,2, (255,0,0),2)
    cv2.rectangle(frame,(0,0),(120,35), (0,0,255), -1)
    cv2.putText(frame, str(int(fps))+ "fps", (5,30), cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    cv2.putText(frame, str(int(fpsFILT))+ "fpsFILT", (40,80), cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    cv2.imshow("my webcam", frame)
    if cv2.waitKey(1) &0xff==ord('q'):
        break
cap.release()    







