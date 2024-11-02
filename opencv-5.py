import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))
    
    img = cv2.line(frame, (0, 0), (width, height), (0, 0, 0), 5)
    img = cv2.line(frame, (0, height), (width, 0), (255, 255, 255), 5)
    
    img = cv2.rectangle(frame, (10, 10), (100, 100), (0, 0, 0), 5)
    
    img = cv2.circle(frame, (200, 200), 70, (255, 56, 255), -1)
    
    fonts = cv2.ACCESS_FAST
    img = cv2.putText(frame, 'Hello world', (100, 100), fonts, 3, 150)
    
    cv2.imshow('Camera', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
