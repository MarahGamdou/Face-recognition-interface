import cv2 as cv
video_capture = cv.VideoCapture(0)
_,_ = video_capture.read()
while True :
    _,frame = video_capture.read()
    edges = cv.Canny(frame, 50, 100)
    cv.imshow('img', edges)
    if cv.waitKey(1) == 27:
        break  # esc to quit
cv.destroyAllWindows()
