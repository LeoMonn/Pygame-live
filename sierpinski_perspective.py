# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 10:07:59 2020

@author: monniello
"""
import pygame as pg
import numpy as np

pg.init()

WIDTH=900
HEIGHT=900
ecran = pg.display.set_mode((WIDTH,HEIGHT))
centre=(WIDTH/2,HEIGHT/2)
pg.display.set_caption('Tapis De Sierpinski')
clock = pg.time.Clock()

C=(1000,1000,1000)
XPLAN = 1500
lam=(XPLAN-C[0])/(C[0]-0)
centre2D = (C[1]+lam*C[1],C[2]+lam*C[2])
start=True

class carre():
    def __init__(self,centre,longueur):
        self.centre=centre
        self.longueur=longueur
        
    def draw(self,ecran,couleur):
        pg.draw.rect(ecran,couleur,[self.centre[0]-self.longueur/2,\
                                    self.centre[1]-self.longueur/2,self.longueur,self.longueur])

class cube():
    def __init__(self,centre,longueur):
        self.centre=centre
        self.longueur=longueur
        self.centre2D=((self.centre[0]-self.centre[1])/np.sqrt(2)+WIDTH/2,\
                       self.centre[2]*np.sqrt(2/3)-(self.centre[0]+self.centre[1])/np.sqrt(6)+HEIGHT/2)
        
    
        self.coord=[(self.centre[0]-self.longueur/2,self.centre[1]+self.longueur/2,self.centre[2]-self.longueur/2),\
                    (self.centre[0]-self.longueur/2,self.centre[1]+self.longueur/2,self.centre[2]+self.longueur/2),\
                    (self.centre[0]+self.longueur/2,self.centre[1]+self.longueur/2,self.centre[2]+self.longueur/2),\
                    (self.centre[0]+self.longueur/2,self.centre[1]+self.longueur/2,self.centre[2]-self.longueur/2),\
                    (self.centre[0]-self.longueur/2,self.centre[1]-self.longueur/2,self.centre[2]+self.longueur/2),\
                    (self.centre[0]+self.longueur/2,self.centre[1]-self.longueur/2,self.centre[2]+self.longueur/2),\
                    (self.centre[0]+self.longueur/2,self.centre[1]-self.longueur/2,self.centre[2]-self.longueur/2),\
                    ]
        self.vect=[(C[0]-coord[0],C[1]-coord[1],C[2]-coord[2]) for coord in self.coord]
        self.lam=[(XPLAN-C[0])/vect[0] for vect in self.vect]
        self.coord2D=[(C[1]+lambd*vect[1]+WIDTH/2-centre2D[0],\
                       C[2]+lambd*vect[2]+HEIGHT/2-centre2D[1]) for lambd,vect in zip(self.lam,self.vect)  ]
       #print(self.coord2D)
        
    def draw(self,ecran):
        pg.draw.polygon(ecran,(0,255,0),[self.coord2D[0],\
                                          self.coord2D[1],\
                                          self.coord2D[2],\
                                          self.coord2D[3]])
        pg.draw.polygon(ecran,(255,0,0),[self.coord2D[1],\
                                          self.coord2D[2],\
                                          self.coord2D[5],\
                                          self.coord2D[4]])
        pg.draw.polygon(ecran,(0,0,255),[self.coord2D[2],\
                                          self.coord2D[3],\
                                          self.coord2D[6],\
                                          self.coord2D[5]])
        
        
    def drawiso(self,ecran):
        pg.draw.polygon(ecran,(0,255,0),[(self.centre2D[0],self.centre2D[1]-self.longueur),\
                                          (self.centre2D[0]-self.longueur*np.sqrt(3)/2,self.centre2D[1]-self.longueur/2),\
                                          (self.centre2D[0],self.centre2D[1]),\
                                          (self.centre2D[0]+self.longueur*np.sqrt(3)/2,self.centre2D[1]-self.longueur/2)])
        pg.draw.polygon(ecran,(255,0,0),[(self.centre2D[0]-self.longueur*np.sqrt(3)/2,self.centre2D[1]-self.longueur/2),\
                                          (self.centre2D[0],self.centre2D[1]),\
                                          (self.centre2D[0],self.centre2D[1]+self.longueur),\
                                          (self.centre2D[0]-self.longueur*np.sqrt(3)/2,self.centre2D[1]+self.longueur/2)])
        pg.draw.polygon(ecran,(0,0,255),[(self.centre2D[0],self.centre2D[1]),\
                                          (self.centre2D[0]+self.longueur*np.sqrt(3)/2,self.centre2D[1]-self.longueur/2),\
                                          (self.centre2D[0]+self.longueur*np.sqrt(3)/2,self.centre2D[1]+self.longueur/2),\
                                          (self.centre2D[0],self.centre2D[1]+self.longueur)])
            
Cube=[cube((0,0,0),400)]
while start:
    ecran.fill((0,0,0))
    for evenement in pg.event.get():
        if evenement.type == pg.QUIT:
            start=False
            
            
    if Cube[0].longueur>10:
        liste=[]
        for cub in Cube:
            cub.drawiso(ecran)
            for x in range(1,-2,-1):
                for y in range(1,-2,-1):
                    for z in range(1,-2,-1):
                        if (x!=0 or y!=0) and (x!=0 or z!=0) and (y!=0 or z!=0) :
                            l=cub.longueur/3
                            centre=cub.centre
                            Cu = cube((centre[0]+x*l,centre[1]+y*l,centre[2]+z*l),l)
                            liste.append(Cu)                        
        Cube=liste 
    else:
        for cub in Cube:
            cub.drawiso(ecran)
                
                        
    # if Carre[0].longueur>3:
    #     liste=[]
    #     for square in Carre:
    #         square.draw(ecran,(255,255,255))
    #         for x in range(-1,2):
    #             for y in range(-1,2):
    #                 if x!=0 or y!=0 :
    #                     l=square.longueur/3
    #                     centre=square.centre
    #                     Ca = carre((centre[0]+x*l,centre[1]+y*l),l)
    #                     liste.append(Ca)

    #     Carre=liste            
    # else :
    #     for square in Carre:
    #         square.draw(ecran,(255,255,255))        
    clock.tick(2)
    pg.display.update()
    
pg.quit()