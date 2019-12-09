import cv2
import pyautogui

cap = cv2.VideoCapture(0)
while(1):
    
     # Capture frame-by-frame
    _, frameinv = cap.read()

    # flip horizontaly to get mirror image in camera
    frame = cv2.flip( frameinv, 1)
  
     # Our operations on the frame come here
    hsv = cv2.cvtColor( frame, cv2.COLOR_BGR2HSV)
	
     # Display the resulting frame
    cv2.imshow('Frame', hsv)
 
    k = cv2.waitKey(10) & 0xFF
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()