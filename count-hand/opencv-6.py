import cv2
import os

cap = cv2.VideoCapture(0)

FolderPath = "Fingers"
lst = os.listdir(FolderPath)
lst_2 = []
for i in lst:
    image = cv2.imread(f'{FolderPath}/{i}')
    print(f'{FolderPath}/{i}')
    lst_2.append(image)

while True:
    ret, frame = cap.read()
    
    cv2.imshow('Camera', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

