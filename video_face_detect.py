import cv2 as cv

cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    haar_cascade = cv.CascadeClassifier('haar_face.xml')

    # Detect and draw rectangle over the face
    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor = 1.5, minNeighbors = 1)
    for (x,y,w,h) in faces_rect:
        cv.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), thickness= 2)

    cv.imshow("Video", frame)

    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()