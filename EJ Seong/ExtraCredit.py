#extra credit


data=open("c:\\python\\test.txt","r") #use short list. 
a=""

for x in data:
    b=x[:]
    a=b+a

alist=list(a) 




import pygame
import sys
from pygame.locals import*

pygame.init()

delay=20

#create a variable for window color
black=0,0,0
navy=0,0,128
lightblue=173,216,230
rose=255,255,255
limegreen=50,205,50
gold=255,215,0
red=205,92,92
brown=244,164,96
orange=255,165,0
purple=147,112,219
violet=239,130,238
pink=255,20,147
yellow=255,255,0
green=127,255,212
slateblue=106,90,205
khaki=240,230,140
cornsilk=255,248,220
peach=255,218,185
lemon=255,250,205
gray=190,190,190
sky=135,206,250
olive=85,107,47

#create game window
size=width,heigth=500,500
screen=pygame.display.set_mode(size)

#create variables


Irect=None
Lrect=None
Vrect=None
Frect=None
Mrect=None
Crect=None
Arect=None
Grect=None
Prect=None
Trect=None
Srect=None
Yrect=None
Wrect=None
Qrect=None
Nrect=None
Hrect=None
Erect=None
Drect=None
Krect=None
Rrect=None
Stoprect=None

#create variables size
rectangleheight=30
rectanglewidth=30




def show():
    global alist,Irect,Lrect,Vrect,Frect,Mrect,Crect,Arect,Grect,Prect,Trect,Srect,Yrect,Wrect,Qrect,Nrect,Hrect,Erect,Drect,Krect,Rrect,Stoprect
    global rectangleheight, rectanglewidth
    while(True):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()

        screen.fill(black)
       
        
        for i in range(len(alist)):
            if alist[i]=='I':
                Irect = pygame.Rect((i*10,i*10),(rectangleheight,rectanglewidth))
                pygame.draw.rect(screen,navy,Irect)
            elif alist[i]=='L':
                Lrect = pygame.Rect((i*10,i*10),(rectangleheight,rectanglewidth))
                pygame.draw.rect(screen,lightblue,Lrect)
            elif alist[i]=='V':
                Vrect= pygame.Rect((i*10,i*10),(rectangleheight,rectanglewidth))
                pygame.draw.rect(screen,rose,Vrect)
            elif alist[i]=='F':
                Frect=pygame.Rect((i*10,i*10),(rectangleheight,rectanglewidth))
                pygame.draw.rect(screen,limegreen,Frect)
            elif alist[i]=='M': 
                Mrect=pygame.Rect((i*10,i*10),(rectangleheight,rectanglewidth))
                pygame.draw.rect(screen,gold,Mrect)
            elif alist[i]=='C':
                Crect=pygame.Rect((i*10,i*10),(rectangleheight,rectanglewidth))
                pygame.draw.rect(screen,red,Crect)
            elif alist[i]=='A':
                Arect=pygame.Rect((i*10,i*10),(rectangleheight,rectanglewidth))
                pygame.draw.rect(screen,brown,Arect)
            elif alist[i]=='G':    
                Grect=pygame.Rect((i*10,i*10),(rectangleheight,rectanglewidth))
                pygame.draw.rect(screen,orange,Grect)
            elif alist[i]=='P':
                Prect=pygame.Rect((i*10,i*10),(rectangleheight,rectanglewidth))
                pygame.draw.rect(screen,purple,Prect)
            elif alist[i]=='T':
                Trect=pygame.Rect((i*10,i*10),(rectangleheight,rectanglewidth))
                pygame.draw.rect(screen,violet,Trect)
            elif alist[i]=='S':        
                Srect=pygame.Rect((i*10,i*10),(rectangleheight,rectanglewidth))
                pygame.draw.rect(screen,pink,Srect)
            elif alist[i]=='Y':   
                Yrect=pygame.Rect((i*10,i*10),(rectangleheight,rectanglewidth))     
                pygame.draw.rect(screen,yellow,Yrect)
            elif alist[i]=='W':    
                Wrect=pygame.Rect((i*10,i*10),(rectangleheight,rectanglewidth))    
                pygame.draw.rect(screen,green,Wrect)
            elif alist[i]=='Q':   
                Qrect=pygame.Rect((i*10,i*10),(rectangleheight,rectanglewidth))     
                pygame.draw.rect(screen,slateblue,Qrect)
            elif alist[i]=='N':        
                Nrect=pygame.Rect((i*10,i*10),(rectangleheight,rectanglewidth))
                pygame.draw.rect(screen,khaki,Nrect)
            elif alist[i]=='H':   
                Hrect=pygame.Rect((i*10,i*10),(rectangleheight,rectanglewidth))     
                pygame.draw.rect(screen,cornsilk,Hrect)
            elif alist[i]=='E':
                Erect=pygame.Rect((i*10,i*10),(rectangleheight,rectanglewidth))        
                pygame.draw.rect(screen,peach,Erect)
            elif alist[i]=='D':        
                Drect=pygame.Rect((i*10,i*10),(rectangleheight,rectanglewidth))
                pygame.draw.rect(screen,lemon,Drect)
            elif alist[i]=='K':        
                Krect=pygame.Rect((i*10,i*10),(rectangleheight,rectanglewidth))
                pygame.draw.rect(screen,gray,Krect)
            elif alist[i]=='R':        
                Rrect=pygame.Rect((i*10,i*10),(rectangleheight,rectanglewidth))
                pygame.draw.rect(screen,sky,Rrect)
            else:
                Stoprect=pygame.Rect((i*10,i*10),(rectangleheight,rectanglewidth))
                pygame.draw.rect(screen,love,Stoprect)

        pygame.display.flip()
        pygame.time.delay(delay)



show()




