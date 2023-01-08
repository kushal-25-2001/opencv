import cv2 as cv

img = cv.imread('Photos/kushal_aadhar.jpg')
cv.imshow('Person', img)

def rescaleFrame(frame, scale = 0.75): 
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img2 = rescaleFrame(img, 0.5)
cv.imshow("Scaled down image", img2)

gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor = 2, minNeighbors = 1)

print(f'Number of faces found = {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img2, (x,y), (x+w,y+h), (0,255,0), thickness=2)

cv.imshow("Detected faces", img2)

cv.waitKey(0)