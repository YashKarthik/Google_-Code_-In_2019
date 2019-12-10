import cv2
import numpy as np

cap = cv2.VideoCapture(0)
#Color to check for
wish = input("Which color would you like to detect?")

while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Red color
    low_red = np.array([161, 155, 84])
    high_red = np.array([179, 255, 255])
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    red = cv2.bitwise_and(frame, frame, mask=red_mask)

    # Blue color
    low_blue = np.array([94, 80, 2])
    high_blue = np.array([126, 255, 255])
    blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
    blue = cv2.bitwise_and(frame, frame, mask=blue_mask)

    # Yellow color
    low_yellow = np.array([25, 52, 72])
    high_yellow = np.array([102, 255, 255])
    yellow_mask = cv2.inRange(hsv_frame, low_yellow, high_yellow)
    yellow = cv2.bitwise_and(frame, frame, mask=yellow_mask)

    # Every color except white
    low = np.array([0, 42, 0])
    high = np.array([179, 255, 255])
    mask = cv2.inRange(hsv_frame, low, high)
    no_white = cv2.bitwise_and(frame, frame, mask=mask)

    #For Red
    if wish=='red':
        cv2.imshow("Red", red)
    
    #For Blue
    elif wish=='blue':
        cv2.imshow('Blue', blue)

    #For Yellow
    elif wish=='yellow':
        cv2.imshow("Yellow", yellow)

    #For all except white
    elif wish=='no white':
        cv2.imshow("No White", no_white)

    #For everything
    elif wish=='everything':
        cv2.imshow("Frame", frame)
        cv2.imshow("Red", red)
        cv2.imshow("Blue", blue)
        cv2.imshow("Yellow", yellow)
        cv2.imshow("Result", no_white)

    key = cv2.waitKey(1)
    if key == 5:
        break
