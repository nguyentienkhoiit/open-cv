import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    width = int(cap.get(3))
    height = int(cap.get(4))
    small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    
    image = np.zeros(frame.shape, np.uint8)
    
    image[:height//2, :width//2] = small_frame
    image[height//2:, :width//2] = cv2.rotate(small_frame, cv2.ROTATE_180)
    image[:height//2, width//2:] = cv2.rotate(small_frame, cv2.ROTATE_180)
    image[height//2:, width//2:] = cv2.rotate(small_frame, cv2.ROTATE_180)
    
    cv2.imshow('Camera', image)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
