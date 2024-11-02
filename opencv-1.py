import cv2

img = cv2.imread('./image-1.jpg', 0)

cv2.imshow('image', img)

k = cv2.waitKey()