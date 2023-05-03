# Here we want a Trackbar that define how big our frame is.
# Also we want another Trackbar taht will move our window from left to right and uo to down.
import cv2
print(cv2.__version__)
def mycallback1(val):
    global xPos
    print("xPos",val)
    xPos=val
def mycallback2(val):
    global yPos
    print("yPos",val)
    yPos=val
def mycallback3(val):
    width=val
    height=int(width*9/16)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH,width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT,height) 
# here for height and width stanadard ratio should be 9:16.
xPos=0
yPos=0
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
cv2.namedWindow("my Trackbars")
cv2.resizeWindow("my Trackbars",400,150)
cv2.moveWindow("my Trackbars", width,0)
cv2.createTrackbar("xPos","my Trackbars",0,2000,mycallback1)
cv2.createTrackbar("yPos","my Trackbars",0,1000,mycallback2)
# when 3rd Trackbar is called then only camera Resolution will change.
cv2.createTrackbar("width","my Trackbars",width,1920,mycallback3)
cv2.createTrackbar("height","my Trackbars",0,1000,mycallback3)
while True:
    ignore, frame=cap.read()
    #frame[140:220, 280:360]=(0,0,0)
    cv2.imshow("my webcam", frame)
    cv2.moveWindow("my webcam",xPos,yPos)
    if cv2.waitKey(1) &0xff==ord('q'):
        break
cap.release()    


    

    

    

    

    
