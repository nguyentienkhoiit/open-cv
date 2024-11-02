import cv2
import random

img = cv2.imread('./image-2.jpg', 1)
print(img.shape)

# for i in range(img.shape[0]):
#     for j in range(img.shape[1]):
#         img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

copy = img[0:100, 300:400]
img[300:400, 200:300] = copy

cv2.imshow('image', img)

k = cv2.waitKey()