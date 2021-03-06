###modules #######
from tkinter import *
import cv2
import vlc
from reshape_img import image_resize
import numpy as np




##définition de toutes les fonctions utiles pour les boutons#######################################################################################################################
######fonctions_moustaches ########
def reco_webcam_moustache_fun():
    return(reco_webcam_moustache(4))
def reco_webcam_moustache_serieuse():
    return(reco_webcam_moustache(11))
def reco_webcam_moustache_insolite():
    return(reco_webcam_moustache(5))
##########fonctions_lunette ########
def reco_webcam_lunette_fun():
    return(reco_webcam_lunette(6))
def reco_webcam_lunette_serieuse():
    return(reco_webcam_lunette(10))
def reco_webcam_lunette_insolite():
    return(reco_webcam_lunette(9))
############fonctions_chapeaux ########
def reco_webcam_chapeau_fun():
    return(reco_webcam_chapeau(3))
def reco_webcam_chapeau_serieux():
    return(reco_webcam_chapeau(6))

#######ouverture de nouvelles fenêtres################################################################################################################################
######boutons_moustaches#####
def new_window_moustaches():
    new1 = Tk()
    new1.resizable(True,True)
    new1.title('moustaches')
    new1.geometry('300x300+0+0')
    new1['bg'] = 'white'
    bouton1 = Button(new1, text="moustache fun",width=16,height=2,command=reco_webcam_moustache_fun).pack()
    bouton2 = Button(new1, text ='moustache sérieuse',width=16,height=2,command=reco_webcam_moustache_serieuse).pack()
    bouton3 = Button(new1, text = 'moustache insolite',width=16,height=2,command=reco_webcam_moustache_insolite).pack()
    new1.mainloop()


######boutons_lunettes#####
def new_window_lunettes():
    new2 = Tk()
    new2.resizable(True,True)
    new2.title('lunettes')
    new2.geometry('300x300+0+0')
    new2['bg'] = 'white'
    bouton1 = Button(new2, text="lunettes fun",width=16,height=2,command=reco_webcam_lunette_fun).pack()
    bouton2 = Button(new2, text ='lunettes sérieuses',width=16,height=2,command=reco_webcam_lunette_serieuse).pack()
    bouton3 = Button(new2, text = 'lunettes insolites',width=16,height=2,command=reco_webcam_lunette_insolite).pack()
    new2.mainloop()

######boutons_couvres_chef#####
def new_window_couvres_chef():
    new3 = Tk()
    new3.resizable(True,True)
    new3.title('couvres-chef')
    new3.geometry('300x300+0+0')
    new3['bg'] = 'white'
    bouton1 = Button(new3, text="chapeau fun",width=12,height=2,command=reco_webcam_chapeau_fun).pack()
    bouton2 = Button(new3, text ='chapeau sérieux',width=12,height=2,command=reco_webcam_chapeau_serieux).pack()
    # bouton3 = Button(new3, text = "ananas de l'espace").pack()
    new3.mainloop()

######boutons_filtres#####
def new_window_filtres():
    new4 = Tk()
    new4.resizable(True,True)
    new4.title('filtres')
    new4.geometry('300x300+0+0')
    new4['bg'] = 'white'
    bouton1 = Button(new4, text="filtre rouge",width=18,height=2,command=reco_webcam_rouge).pack()
    bouton2 = Button(new4, text ='filtre vert',width=18,height=2,command=reco_webcam_vert).pack()
    bouton3 = Button(new4, text = 'filtre mystique',width=18,height=2, command=reco_webcam_mystique).pack()
    bouton4 = Button(new4, text = 'filtre invert',width=18,height=2, command=reco_webcam_invert).pack()
    bouton5 = Button(new4, text = 'filtre circle focus blur',width=18,height=2, command=reco_webcam_circle_focus_blur).pack()
    bouton6 = Button(new4, text = 'filtre portrait_mode',width=18,height=2, command=reco_webcam_portrait_mode).pack()
    new4.mainloop()

######boutons_musique_sourire#####
def new_window_sourire():
    new5 = Tk()
    new5.resizable(True,True)
    new5.title('musique')
    new5.geometry('300x300+0+0')
    new5['bg'] = 'white'
    bouton1 = Button(new5, text="musique fun",width=12,height=2,command=reco_webcam_sourire).pack()
    # bouton2 = Button(new4, text ="musique triste",command=reco_webcam_triste).pack()
    new5.mainloop()
#accesoires######################################################################################################################################################
###ajout moustaches###
def draw_mustache(img, mustache_resized, x, y, nx, ny, nw, nh, mw, mh):
    #coordonnées des moustaches
    my = y + ny + int(nh*0.6)
    mx = x + nx + int((nw - mw) / 2)
    #trouver les emplacements des pixels non vides
    mask = (mustache_resized[:,:,3] != 0)
    img[my:my+mh, mx:mx+mw][mask] = mustache_resized[mask][:,0:3]

def reco_webcam_moustache(x):
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
                roi_gray = gray[y:y+h, x:x+w]
                frontal_eyes = frontal_eye_cascade.detectMultiScale(roi_gray)
                if len(frontal_eyes) > 0:
                    # First Match
                    (ex,ey,ew,eh) = frontal_eyes[0]
                    nose = nose_cascade.detectMultiScale(roi_gray)
                    #redimensionner image
                    mustache_resized = image_resize(mustache.copy(), width=int(ew*0.8),height=eh//2)
                    mh, mw, mc = mustache_resized.shape
                    #utilisation de deux nose_cascades pour diminuer les incertitudes
                    for (nx,ny,nw,nh) in nose:
                        if nx>ex and abs(ny-ey-eh)<(eh//4):
                            draw_mustache(img, mustache_resized, x, y, nx, ny, nw, nh, mw, mh)
                            break
                    else:
                        nose2 = nose2_cascade.detectMultiScale(roi_gray, minNeighbors=3, flags=cv2.CASCADE_SCALE_IMAGE)
                        for(n2x,n2y,n2w,n2h) in nose2:
                            if n2x>ex and abs(n2y-ey-eh)<(eh//4):
                                draw_mustache(img, mustache_resized, x, y, n2x, n2y, n2w, n2h, mw, mh)
                                break

            cv2.imshow('appuyer sur echap pour quitter',img)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
    cap.release()
    cv2.destroyAllWindows()


####ajout lunettes###
def reco_webcam_lunette(x):
    adresse="glasses\glasses({}).png".format(x)
    glasses = cv2.imread(adresse, -1)

    face_cascade=cv2.CascadeClassifier('cascade\data\haarcascade_frontalface_default.xml')
    frontal_eye_cascade=cv2.CascadeClassifier('cascade\data\\frontalEyes35x16.xml')
    small_eye_cascade=cv2.CascadeClassifier('cascade\data\\haarcascade_mcs_eyepair_small.xml')

    cap=cv2.VideoCapture(0)
    while True:
        ret,img=cap.read()
        if ret:
            gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            faces=face_cascade.detectMultiScale(gray, scaleFactor=1.3)
            for (x,y,w,h) in faces:
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = img[y:y+h, x:x+w]
                frontal_eyes = frontal_eye_cascade.detectMultiScale(roi_gray)
                small_eyes=small_eye_cascade.detectMultiScale(roi_gray)
                if len(frontal_eyes) > 0:
                    # First Match
                    (ex,ey,ew,eh) = frontal_eyes[0]
                    #redimensionner image
                    glasses_resized = image_resize(glasses.copy(), width=ew, height=eh)
                    gh, gw, gc = glasses_resized.shape
                    if len(small_eyes) > 0:
                        #utilisation de deux eye_cascades pour diminuer les incertitudes
                        (sx,sy,sw,sh) = small_eyes[0]
                        if  ey<sy and eh>sh:
                            #les coordonnées des lunettes
                            gy = y + ey
                            gx = x + ex
                            #positionner les lunettes
                            mask = (glasses_resized[:,:,3] != 0)
                            img[gy:gy+gh, gx:gx+gw][mask] = glasses_resized[mask][:,0:3]
            cv2.imshow('appuyer sur echap pour quitter',img)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
    cap.release()
    cv2.destroyAllWindows()
###########ajout chapeaux###
def reco_webcam_chapeau(x):
    adresse="hat\hat{}.png".format(x)
    hat = cv2.imread(adresse, -1)
    face_cascade=cv2.CascadeClassifier('cascade\data\haarcascade_frontalface_default.xml')
    cap=cv2.VideoCapture(0)
    while True:
        ret,img=cap.read()
        if ret:
            gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            faces=face_cascade.detectMultiScale(gray, scaleFactor=1.3)
            for (x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = img[y:y+h, x:x+w]
                #redimensionner image
                hat_resized = image_resize(hat.copy(), width=int(w*1.3))
                hh, hw, hc = hat_resized.shape
                #les coordonnées du chapeau
                hy =y-int(hh*0.7)
                hx = x-(hw-h)//2
                #positionner le chapeau
                for i in range(0,hh):
                    for j in range(0,hw):
                        if hat_resized[i, j][3] != 0:
                            img[hy+i,hx+j] = hat_resized[i,j][0:3]
            cv2.imshow('appuyer sur echap pour quitter',img)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
    cap.release()
    cv2.destroyAllWindows()


#musique############################################################################################################################################################
#musique fun#########
def reco_webcam_sourire():
    sound=vlc.MediaPlayer('schtroumpfs.mp3')
    face_cascade=cv2.CascadeClassifier('cascade\data\haarcascade_frontalface_default.xml')
    mouth_cascade=cv2.CascadeClassifier('cascade\data\haarcascade_smile.xml')
    cap=cv2.VideoCapture(0)
    while True:
        ret,img=cap.read()
        if ret:
            gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            faces=face_cascade.detectMultiScale(gray, scaleFactor=1.3)#, minNeighbors=3)#,minSize=(55, 55),flags=cv2.CASCADE_SCALE_IMAGE)
            for (x,y,w,h) in faces:
                # cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                roi_gray = gray[y:y+h, x:x+w]
                smiles = mouth_cascade.detectMultiScale(roi_gray,scaleFactor= 1.7,minNeighbors=22,minSize=(25,25),flags=cv2.CASCADE_SCALE_IMAGE)
                #first Match
                if len(smiles)>0:
                    sound.play()
                    # (mx,my,mw,mh)=smiles[0]
                    # cv2.rectangle(roi_color,(mx,my),(mx+mw,my+mh),(0,255,255),2)
                else:
                    sound.stop()
            cv2.imshow('appuyer sur echap pour quitter',img)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
    cap.release()
    cv2.destroyAllWindows()



#filtres########################################################################################################################################################
####filtre vert####
def reco_webcam_vert():
    video_capture = cv2.VideoCapture(0)
    while True :
        ret, frame = video_capture.read()
        frame = cv2.flip(frame, 1)
        for i in range(len(frame)):
            for j in range(len(frame[0])):
                frame[i][j][1] = 255
        cv2.imshow('appuyer sur echap pour quitter',frame)
        if cv2.waitKey(1) == 27:
            break  # esc to quit
    cv2.destroyAllWindows()
####filtre rouge###
def reco_webcam_rouge():
    video_capture = cv2.VideoCapture(0)
    while True :
        ret, frame = video_capture.read()
        frame = cv2.flip(frame, 1)
        for i in range(len(frame)):
            for j in range(len(frame[0])):
                frame[i][j][2] = 255
        cv2.imshow('appuyer sur echap pour quitter',frame)
        if cv2.waitKey(1) == 27:
            break  # esc to quit
    cv2.destroyAllWindows()

####filtre mystique####
def reco_webcam_mystique():
    video_capture = cv2.VideoCapture(0)
    _,_ = video_capture.read()
    while True :
        _,frame = video_capture.read()
        edges = cv2.Canny(frame, 50, 100)
        cv2.imshow('appuyer sur echap pour quitter', edges)
        if cv2.waitKey(1) == 27:
            break  # esc to quit
    cv2.destroyAllWindows()
####filtre invert####
def reco_webcam_invert():
    cap=cv2.VideoCapture(0)
    while True:
        ret,img=cap.read()
        cv2.imshow('appuyer sur echap pour quitter',cv2.bitwise_not(img))
        if cv2.waitKey(1) == 27:
            break
    cap.release()
    cv2.destroyAllWindows()

####fonctions utiles aux filtre ####
def alpha_blend(frame_1, frame_2, mask):
    alpha = mask/255.0
    blended = cv2.convertScaleAbs(frame_1*(1-alpha) + frame_2*alpha)
    return blended

def verify_alpha_channel(frame):
    try:
        frame.shape[3] # 4th position
    except IndexError:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
    return frame
####filtre circle_focus_blur####
def apply_circle_focus_blur(frame, intensity=0.2):
    frame = verify_alpha_channel(frame)
    frame_h, frame_w, frame_c = frame.shape
    y = int(frame_h/2)
    x = int(frame_w/2)
    radius = int(x/2) # int(x/2)
    center = (x,y)
    mask    = np.zeros((frame_h, frame_w, 4), dtype='uint8')
    cv2.circle(mask, center, radius, (255,255,255), -1, cv2.LINE_AA)
    mask    = cv2.GaussianBlur(mask, (21,21),11 )
    blured  = cv2.GaussianBlur(frame, (21,21), 11)
    blended = alpha_blend(frame, blured, 255-mask)
    frame   = cv2.cvtColor(blended, cv2.COLOR_BGRA2BGR)
    return frame

def reco_webcam_circle_focus_blur():
    cap=cv2.VideoCapture(0)
    while True:
        ret,frame=cap.read()
        cv2.imshow('appuyer sur echap pour quitter',apply_circle_focus_blur(frame, intensity=5))
        k = cv2.waitKey(30)
        if k == 27:
            break
    cap.release()
    cv2.destroyAllWindows()
####filtre portrait_mode#######
def apply_portrait_mode(frame):
    frame= verify_alpha_channel(frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, mask = cv2.threshold(gray, 120,255,cv2.THRESH_BINARY)
    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGRA)
    blured = cv2.GaussianBlur(frame, (21,21), 11)
    blended = alpha_blend(frame, blured, mask)
    frame = cv2.cvtColor(blended, cv2.COLOR_BGRA2BGR)
    return frame

def reco_webcam_portrait_mode():
    cap=cv2.VideoCapture(0)
    while True:
        ret,frame=cap.read()
        cv2.imshow('appuyer sur echap pour quitter',apply_portrait_mode(frame))
        k = cv2.waitKey(30)
        if k == 27:
            break
    cap.release()
    cv2.destroyAllWindows()





##1ère fenêtre ouverte##################################################################################################################################
main = Tk()
main.resizable(True,True)
main.title('projet')
main.geometry('1366x780+0+0')

main['bg'] = 'white'
#ajout d'une image
can1 = Canvas(main,bg='white',height=768,width=1256)
photo = PhotoImage(file ='image.png')
item = can1.create_image(0,0,anchor=NW, image =photo)
can1.pack(side=LEFT)
#ajout des boutons
bouton1 = Button(main, text="Moustaches  ",width=12,height=2, command=new_window_moustaches).pack()
bouton2 = Button(main, text="   Lunettes    ",width=12,height=2 ,command=new_window_lunettes).pack()
bouton3 = Button(main, text="chapeaux",width=12,height=2,command=new_window_couvres_chef).pack()
bouton4 = Button(main, text="     Filtres       ",width=12,height=2,command=new_window_filtres).pack()
bouton5 = Button(main, text="     musique       ",width=12,height=2,command=new_window_sourire).pack()
main.mainloop()
