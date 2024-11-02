import cv2

img = cv2.imread('./image-1.jpg', 0)
# img = cv2.resize(img, (400, 400))

# resize
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

# rotate
img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imshow('image', img)

k = cv2.waitKey(3000)
if k == ord('s'):
    cv2.imwrite('new.jpg', img)