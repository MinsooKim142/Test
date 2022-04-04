import cv2
from datetime import datetime
import numpy as np


cap = cv2.VideoCapture(0)

frame_no = 0
while(cap.isOpened()):
    cap.set(cv2.CAP_PROP_POS_MSEC, (frame_no * 1000))
    frame_exists, curr_frame = cap.read()
    ts = cap.get(cv2.CAP_PROP_POS_MSEC)
    if frame_exists:
        print("for frame : " + str(frame_no) + "   timestamp is: ", str(cap.get(cv2.CAP_PROP_POS_MSEC)))
        now = datetime.now()

        #Gets the system's time of each frame.
        current_time = now.strftime("%H:%M:%S")
        print("Current Time Of Same Pics =", current_time)
    else:
        break
iuhoiuhkujlkj

cap.release()