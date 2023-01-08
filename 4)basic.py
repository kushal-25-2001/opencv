import cv2 as cv

img = cv.imread('Photos/boston.jpg')
cv.imshow('Boston', img)

#converting to gray scale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# Blur - to remove some of noise in image
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
# cv.imshow("Blur",blur)

# Edge Cascade
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Edges',canny)

cannyLessEdges = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges - Less',cannyLessEdges)

# Dilating the images
dilated = cv.dilate(cannyLessEdges, (7,7), iterations=3) 
cv.imshow("Dilated", dilated)

# Eroding
eroded = cv.erode(dilated, (3,3), iterations=3)
cv.imshow("Eroded", eroded)

# Resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow("resized",resized)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)