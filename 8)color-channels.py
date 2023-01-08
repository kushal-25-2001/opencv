import cv2 as cv
import numpy as np

img = cv.imread('Photos/boston.jpg')
cv.imshow("Boston", img)

blank = np.zeros(img.shape[:2], dtype='uint8')

b, g, r = cv.split(img)

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('Blue', b)
cv.imshow("Green", g)
cv.imshow("Red", r)

cv.imshow('Blue2', blue)
cv.imshow("Green2", green)
cv.imshow("Red2", red)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b,g,r])
cv.imshow("Merged", merged)

cv.waitKey(0)