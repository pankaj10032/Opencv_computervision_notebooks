import cv2

width=640
height=360
myRadius=30
myColor=(0,0,0)
myThickness=2
cap=cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cap.set(cv2.CAP_PROP_FPS, 30)
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"MJPG")) # Here MJPG-> Moving jpeg
while True:
    ignore, frame=cap.read()  # ROI-> Region of interest.
    frameROI=frame[150:210, 250:390] # 150:210=> 60 rows that are in the middle.
    frameROIGray=cv2.cvtColor(frameROI, cv2.COLOR_BGR2GRAY)
    frameROIBGR=cv2.cvtColor(frameROIGray, cv2.COLOR_GRAY2BGR)
    cv2.imshow("my Gray ROI", frameROIGray)
    cv2.moveWindow("my Gray ROI", 650,180)
    #frame[140:220, 280:360]=(0,0,0)
    frame[150:210, 250:390]=frameROIBGR
    cv2.imshow("my ROI",frameROI)
    cv2.moveWindow("my Gray ROI", 650,90)
    cv2.imshow("my webcam", frame)
    cv2.moveWindow('my webcam', 0,0)
    cv2.moveWindow("my ROI", 650,0)
    if cv2.waitKey(1) &0xff==ord('q'):
        break
cap.release()    