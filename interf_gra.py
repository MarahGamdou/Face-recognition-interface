from tkinter import *
import cv2 as cv
import numpy as np




##définition de toutes les fonctions utiles


#ouverture de nouvelles fenêtres

def new_window_moustaches():
    new1 = Tk()
    new1.resizable(False,False)
    new1.title('moustaches')
    new1.geometry('300x300+600+300')
    new1['bg'] = 'red'
    bouton1 = Button(new1, text="moustache fun").pack()
    bouton2 = Button(new1, text ='moustache sérieuse').pack()
    bouton3 = Button(new1, text = 'moustache insolite').pack()
    new1.mainloop()
    
    
    
def new_window_lunettes():
    new2 = Tk()
    new2.resizable(False,False)
    new2.title('lunettes')
    new2.geometry('300x300+300+600')
    new2['bg'] = 'red'
    bouton1 = Button(new2, text="lunettes fun").pack()
    bouton2 = Button(new2, text ='lunettes sérieuses').pack()
    bouton3 = Button(new2, text = 'lunettes insolites').pack()
    new2.mainloop()
    

def new_window_couvres_chef():
    new3 = Tk()
    new3.resizable(False,False)
    new3.title('couvres-chef')
    new3.geometry('300x300+700+700')
    new3['bg'] = 'red'
    bouton1 = Button(new3, text="chapeau fun").pack()
    bouton2 = Button(new3, text ='chapeau sérieuse').pack()
    bouton3 = Button(new3, text = "ananas de l'espace").pack()
    new3.mainloop()
    
    
def new_window_filtres():
    new4 = Tk()
    new4.resizable(False,False)
    new4.title('filtres')
    new4.geometry('300x300+600+600')
    new4['bg'] = 'red'
    bouton1 = Button(new4, text="filtre rouge",command=reco_webcam_rouge).pack()
    bouton2 = Button(new4, text ='filtre vert',command=reco_webcam_vert).pack()
    bouton3 = Button(new4, text = 'filtre mystique', command=reco_webcam_mystique).pack()
    new4.mainloop()


#filtres

def reco_webcam_vert():
    video_capture = cv.VideoCapture(0)
    while True :
        ret, frame = video_capture.read()
        frame = cv.flip(frame, 1)
        for i in range(len(frame)):
            for j in range(len(frame[0])):
                frame[i][j][1] = 255
        cv.imshow('appuyer sur echap pour quitter',frame)
        if cv.waitKey(1) == 27:
            break  # esc to quit
    cv.destroyAllWindows()

def reco_webcam_rouge():
    video_capture = cv.VideoCapture(0)
    while True :
        ret, frame = video_capture.read()
        frame = cv.flip(frame, 1)
        for i in range(len(frame)):
            for j in range(len(frame[0])):
                frame[i][j][2] = 255
        cv.imshow('appuyer sur echap pour quitter',frame)
        if cv.waitKey(1) == 27:
            break  # esc to quit
    cv.destroyAllWindows()
    
    
def reco_webcam_mystique():
    video_capture = cv.VideoCapture(0)
    _,_ = video_capture.read()
    while True :
        _,frame = video_capture.read()
        edges = cv.Canny(frame, 50, 100) 
        cv.imshow('appuyer sur echap pour quitter', edges)
        if cv.waitKey(1) == 27:
            break  # esc to quit
    cv.destroyAllWindows()



##1ère fenêtre ouverte
main = Tk()
main.resizable(False,False)
main.title('zooo')
main.geometry('1920x1080+0+0')
main['bg'] = 'blue'
bouton1 = Button(main, text="Moustaches", command=new_window_moustaches).pack()
bouton2 = Button(main,text='Lunettes', command=new_window_lunettes).pack()
bouton3 = Button(main, text="Couvres-chef",command=new_window_couvres_chef).pack()
bouton4 = Button(main, text='Filtres',command=new_window_filtres).pack()
main.mainloop()