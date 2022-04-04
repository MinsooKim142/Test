from datetime import datetime
from PIL import Image
import os
import cv2

#import time

# define a video capture object
vid = cv2.VideoCapture(0)

while (True):

    # Capture the video frame
    # by frame
    ret, frame = vid.read()
    # count the number of frames

    # Read video by read() function and it
    # will extract and  return the frame
    ret, img = vid.read()

    # Put current DateTime on each frame
    font = cv2.FONT_HERSHEY_PLAIN
    cv2.putText(img, str(datetime.now()), (20, 40),
                font, 2, (255, 255, 255), 2, cv2.LINE_AA)

    # Display the resulting frame
    cv2.imshow('frame', frame)

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()



