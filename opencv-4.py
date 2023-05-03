import cv2

rows=int(input("How many Rows do you want?"))
columns=int(input("And How many Columns?"))

width=1280
height=720
cap=cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cap.set(cv2.CAP_PROP_FPS, 30)
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"MJPG")) # Here MJPG-> Moving jpeg
while True:
    ignore, frame=cap.read()
    frame=cv2.resize(frame, (int(width/columns), int(height/columns)))
    # opencv many times crash if it doesn't have any integar value.
    # x, y should be inside parentheses inside small brackets.
    for i in range(0, rows,1):
        for j in range(0, columns,1):
            windName="window" +str(i) + "x" + str(j)
            cv2.imshow(windName, frame)
            cv2.moveWindow(windName, int(width/columns)*j, int(height/columns)*i)
    if cv2.waitKey(1) &0xff==ord('q'):
        break
cap.release()    
