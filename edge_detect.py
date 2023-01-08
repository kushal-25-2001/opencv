import cv2 as cv
import numpy as np

img = cv.imread('Photos/boston.jpg')
cv.imshow("Cats", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap2 = np.uint8(np.absolute(lap)) # images cannot have -ve values which we get by laplassian because of negative slopes they are coverted back to positive using np.absolute
cv.imshow("Laplacian", lap2)

# sobel
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)

cv.imshow("Sobel x", sobelx)
cv.imshow("Sobel y", sobely)
combined_sobel = cv.bitwise_or(sobelx,sobely)
cv.imshow("Combined sobel", combined_sobel)

# canny
canny = cv.Canny(gray, 150, 175)
cv.imshow("Canny", canny)



cv.waitKey(0)