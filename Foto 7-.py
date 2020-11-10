from tkinter import *
from tkinter.ttk import *
import cv2
import sys

def todo():
    x=input('Nombre de la foto: ')

    def general():
        camara=cv2.VideoCapture(0)
        leido,frame=camara.read()
        if leido==True:
            cv2.imwrite(x+'.png',frame)
            print('se tomo con exito la foto')
        else:
            print('Error camara no existe, esta apagado o no configurada')
        camara.release()
        
        pantalla=Tk()
        pantalla.geometry('640x480')
        pantalla.title('Foto')
        
        foto=PhotoImage(file=x+'.png')
        fondo=Label(pantalla,image=foto).place(x=0,y=0)
        
        pantalla.mainloop()
        
        def op():
            y=input('Deseas tomarte otra foto si/no: ')
            if y=='si':
                todo()
            elif y=='no':
                sys.exit()
            else:
                print('Opcion no disponible da enter para continuar')
                input()
                op()
        op()
        
    general()
todo()

