import cv2
from datetime import datetime
import numpy as np

#Asks the user for the name of the pictures.
nameOne = input("Enter the first file name of picture: ")
nameTwo = input("Enter the second file name of picture: ")

# 1) Check if 2 images are equals
original = cv2.imread(nameOne)
duplicate = cv2.imread(nameTwo)

#Checks if the size and channels have the same.
if original.shape == duplicate.shape:
    print("The images have same size and channels")
    difference = cv2.subtract(original, duplicate)
    b, g, r = cv2.split(difference)

    #Checks if the images are completely Equal.
    if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
        print("The images are completely Equal")

        #Checks and prints out the time of system when the images are equal.
        now = datetime.now()

        current_time = now.strftime("%H:%M:%S")
        print("Current Time Of Same Pics =", current_time)

    else:
        #Prints out if images are not equal.
        print("But images are NOT completely equal")

else:
    print("the images are not equal")
