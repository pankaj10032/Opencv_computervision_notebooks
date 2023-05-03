import cv2
import numpy as np
print(cv2.__version__)
# Here we are taking 4 Trackbars of Hue to see Red color(detect Red Object) clearly visible. 
def onTrack1(val):
    global hueLow
    hueLow=val
    print("Hue Low",hueLow)

def onTrack2(val):
    global hueHigh
    hueHigh=val
    print("Hue high", hueHigh)
def onTrack7(val):
    global hueLow2
    hueLow2=val
    print("Hue Low 2",hueLow2)

def onTrack8(val):
    global hueHigh2
    hueHigh2=val
    print("Hue high 2", hueHigh2)
def onTrack3(val):
    global saturationLow
    saturationLow=val
    print("saturation Low", saturationLow)
def onTrack4(val):
    global saturationHigh
    saturationHigh=val
    print("saturation high", saturationHigh)
def onTrack5(val):
    global valLow
    valLow=val
    print("value low", valLow)
def onTrack6(val):
    global valHigh
    valHigh=val
    print("value high", valHigh)
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

cv2.namedWindow("myTracker")
cv2.moveWindow("myTracker", width,0)
cv2.resizeWindow("myTracker",400,500)
# We have to set our initial value to call our callback function.

hueLow=10
heHigh=20
satuationLow=10
saturationHigh=250
valLow=10
valHigh=250 
#Here 10 is not low value it is start value. All Trackbars start at zero

cv2.createTrackbar("Hue low","myTracker",10,179,onTrack1)
cv2.createTrackbar("Hue high","myTracker",20,179,onTrack2)
cv2.createTrackbar("Hue low 2","myTracker",10,179,onTrack7)
cv2.createTrackbar("Hue high 2","myTracker",20,179,onTrack8)
cv2.createTrackbar("saturatioin low","myTracker",10,255,onTrack3)
cv2.createTrackbar("saturation high","myTracker",250,255,onTrack4)
cv2.createTrackbar("value low","myTracker",10,255,onTrack5)
cv2.createTrackbar("value high","myTracker",250,255,onTrack6)
# Here we have kert Really wide saturation and value Range and very narrow hue Range.
while True:
    ignore, frame=cap.read()
    #frame[140:220, 280:360]=(0,0,0)
    frameHSV=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    # Here lowerBound and upperBound are the corner or edges of our box.
    lowerBound=np.array([hueLow,saturationLow,valLow])
    upperBound=np.array([hueHigh,saturationHigh,valHigh])

    lowerBound2=np.array([hueLow2,saturationLow,valLow])
    upperBound2=np.array([hueHigh2,saturationHigh,valHigh])
    # Here we want to create two mask where our first mash will Track 1st color and 2nd mask will Track 2nd color.4
    #mymask=cv2.bitwise_not(mymask)
    mymask=cv2.inRange(frameHSV, lowerBound, upperBound)
    mymask2=cv2.inRange(frameHSV, lowerBound2, upperBound2)
    mymaskcomposite=mymask | mymask2 # or mymaskcomposite=cv2.add(mymask,mymask2)

    contours,junk=cv2.findContours(mymask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(frame, contours,-1,(255,0,0),3)
    for contour in contours: # step through contours
        area=cv2.contourArea(contour)# find area of the contour that we are interested in.
        if area>=100:
            cv2.drawContours(frame, [contour],0,(255,0,0),3) # Here we are passing an array of contours to it.
        # Here we will draw only first element of that array of contour.
        # Here we willl find the box that will contain this contour.
            x,y,w,h=cv2.boundingRect(contour)# it wants only a single contour.
            # Here bounding Rect willl return x and y coirdinate, width and height of bounding Rectangle.
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)
    myobject=cv2.bitwise_and(frame, frame, mask=mymaskcomposite)
    myObjectSmall=cv2.resize(myobject,(int(width/2), int(height/2)))
    cv2.imshow("my object", myObjectSmall)
    cv2.moveWindow("my object", int(width/2),int(height))
    # if none of our pixel of image will be in range of mask then mask will be completely black.
   
    mymasksmall2=cv2.resize(mymask2,(int(width/2), int(height/2)))
    cv2.imshow('my mask 2', mymasksmall2)
    cv2.moveWindow("my mask 2",0,height+ int(height/2)+ 30)
    cv2.imshow("my webcam", frame)
    if cv2.waitKey(1) &0xff==ord('q'):
        break
cap.release() 
