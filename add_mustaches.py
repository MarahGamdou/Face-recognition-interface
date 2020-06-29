import cv2
from reshape_img import image_resize

def draw_mustache(img, mustache_resized, x, y, nx, ny, nw, nh, mw, mh):
    my = y + ny + int(nh*0.6)
    mx = x + nx + int((nw - mw) / 2)

    mask = (mustache_resized[:,:,3] != 0
    for i in range(0, mh):
        for j in range(0, mw):
            if mask[i, j]:
                img[my+i,mx+j] = mustache_resized[i,j][0:3]

x=input('moustache')
adresse="mustache\mustache({}).png".format(x)
mustache = cv2.imread(adresse, -1)

face_cascade=cv2.CascadeClassifier('cascade\data\haarcascade_frontalface_default.xml')
frontal_eye_cascade=cv2.CascadeClassifier('cascade\data\\frontalEyes35x16.xml')
nose_cascade=cv2.CascadeClassifier('cascade\data\\Nose18x15.xml')
nose2_cascade=cv2.CascadeClassifier('cascade\data\\Nariz.xml')

cap=cv2.VideoCapture(0)
while True:
    ret,img=cap.read()
    if ret:
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=face_cascade.detectMultiScale(gray, scaleFactor=1.3)#,minSize=(55, 55),flags=cv2.CASCADE_SCALE_IMAGE)
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            frontal_eyes = frontal_eye_cascade.detectMultiScale(roi_gray)
            if len(frontal_eyes) > 0:
                # First Match
                (ex,ey,ew,eh) = frontal_eyes[0]
                nose = nose_cascade.detectMultiScale(roi_gray)
                mustache_resized = image_resize(mustache.copy(), width=int(ew*0.8),height=eh//2)
                mh, mw, mc = mustache_resized.shape
                for (nx,ny,nw,nh) in nose:
                    if nx>ex and abs(ny-ey-eh)<(eh//4):
                        cv2.rectangle(roi_color,(nx,ny),(nx+nw,ny+nh),(0,0,255),2)
                        draw_mustache(img, mustache_resized, x, y, nx, ny, nw, nh, mw, mh)
                        break
                else:
                    nose2 = nose2_cascade.detectMultiScale(roi_gray, minNeighbors=3, flags=cv2.CASCADE_SCALE_IMAGE)
                    for(n2x,n2y,n2w,n2h) in nose2:
                        if n2x>ex and abs(n2y-ey-eh)<(eh//4):
                            cv2.rectangle(roi_color,(n2x,n2y),(n2x+n2w,n2y+n2h),(0,255,255),2)
                            draw_mustache(img, mustache_resized, x, y, n2x, n2y, n2w, n2h, mw, mh)
                            break

        cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
