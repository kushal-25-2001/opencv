import cv2 as cv

#for image
# img = cv.imread('Photos/cat_large.jpg')
# cv.imshow('cat',img)

def rescaleFrame(frame, scale = 0.75): #for images,video,live video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width,height): #only for live video
    capture.set(3,width)
    capture.set(4,height)

# img2 = rescaleFrame(img,0.3)
# cv.imshow('cat smol',img2)

# cv.waitKey(0)

# for video
capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue,frame = capture.read()
    frame_resized = rescaleFrame(frame,0.2)

    cv.imshow('Video',frame)
    cv.imshow('Videos',frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
    