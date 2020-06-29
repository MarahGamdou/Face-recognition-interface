import cv2
from reshape_img import image_resize

glasses = cv2.imread("glasses\glasses(5).png", -1)
mustache = cv2.imread("mustache.png", -1)
hat = cv2.imread("hat\hat3.png", -1)

face_cascade=cv2.CascadeClassifier('cascade\data\haarcascade_frontalface_default.xml')
eye_cascade=cv2.CascadeClassifier('cascade\data\\frontalEyes35x16.xml')
nose_cascade=cv2.CascadeClassifier('cascade\data\\Nose18x15.xml')
cap=cv2.VideoCapture(0)
while True:
    ret,img=cap.read()
    if ret:
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            # cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            hat_resized = image_resize(hat.copy(), width=w)
            hw, hh, hc = hat_resized.shape
            for i in range(0, hw):
                for j in range(0, hh):
                    if hat_resized[i, j][3] != 0:
                        img[i,x+ j] = hat_resized[i,j,0]



            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex,ey,ew,eh) in eyes:
                # cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
                glasses_resized = image_resize(glasses.copy(), width=w)

                gw, gh, gc = glasses_resized.shape
                for i in range(0, gw):
                    for j in range(0, gh):
                        if glasses_resized[i, j][3] != 0:
                            img[y+ey+i, x+j] = glasses_resized[i,j,0]

            nose = nose_cascade.detectMultiScale(roi_gray)
            for (nx,ny,nw,nh) in nose:
                # cv2.rectangle(roi_color,(nx,ny),(nx+nw,ny+nh),(0,0,255),2)
                mustache_resized = image_resize(mustache.copy(), width=w)

                mw, mh, mc = mustache_resized.shape
                for i in range(0, mw):
                    for j in range(0, mh):#print(glasses[i, j]) #RGBA
                        if mustache_resized[i, j][3] != 0: # alpha 0
                            img[y+ny+i, x+j] = mustache[i,j,0]
                break

        cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
