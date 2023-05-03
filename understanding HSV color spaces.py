import numpy as np
import cv2
print(cv2.__version__)
#we can create a blank Picture from np.zeros function
evt=0
xPos=0
yPos=0
def mouseclick(event,xPos,yPos,flags,params):
#here we want to grab that color under the cursor when left mouse button will become down.
    global evt
    global xVal
    global yVal
    if event==cv2.EVENT_LBUTTONDOWN:
        print(event)
        evt=event#Global variabkle is equal to Local Variable
        xVal=xPos
        yVal=yPos
    if event==cv2.EVENT_RBUTTONUP:
        evt=event
        print(event)

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
cv2.namedWindow("my webcam")
cv2.setMouseCallback("my webcam", mouseclick)
while True:
    ignore, frame=cap.read()
    #frame[140:220, 280:360]=(0,0,0)
    if evt==1:
        x=np.zeros([250,250,3],dtype=np.uint8)# Here 3->number of colors, blue, Green, Red
        y=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        # We will capture frame in the order of first Row and then Column
        clr=y[yVal][xVal]# yVal->Rows, xval->Rows
        print(clr)
        # now it will print values in the order of hue,saturation, value and Here our hue(oth value) tells us about color.  
        #x[:,:]-> all Rows and all Columns
        x[:,:]=clr
        cv2.putText(x,str(clr),(0,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),1)# here first one-> font size and other final->thicknessx
        cv2.imshow("color picker",x)
        cv2.moveWindow("color picker", width,0)
        evt=0
    cv2.imshow("my webcam", frame)
    if cv2.waitKey(1) &0xff==ord('q'):
        break
cap.release()    


    

    

    

    

    
