import matplotlib.patches as patches
from Mesa import *
from Puerta import *
from Tv import *
from Tablero import *
from Silla import *
from Ventana import *

class Salon:

    def __init__(self):
        self.__facecolor='none'
        self.__edgecolor='r'
        self.__linewidth=1
        self.__width=2000
        self.__height=2000
        self.__puerta=Puerta()
        self.__puerta1=Puerta((1615, 1500))
        self.__puerta2=Puerta((1900,1500))
        self.__puerta3=Puerta((1900,985))
        self.__ventana=Ventana()
        self.__ventana1=Ventana((20, 325))
        self.__ventana2=Ventana((20, 600))
        self.__ventana3=Ventana((20, 875))
        self.__ventana4=Ventana((20, 1150))
        self.__ventana5=Ventana((20, 1425))
        self.__ventana6=Ventana((20, 1700))
        self.__tablero=Tablero()
        self.__silla=Silla()
        self.__silla1=Silla((225,315))
        self.__silla2=Silla((225,570))
        self.__silla3=Silla((225,810))
        self.__silla4=Silla((225,1050))
        self.__silla5=Silla((930,1050))
        self.__silla6=Silla((930,810))
        self.__silla7=Silla((930,570))
        self.__silla8=Silla((1325,1275))
        self.__tv=Tv()
        self.__mesa=Mesa()
        self.__mesa1=Mesa((150,400))
        self.__mesa2=Mesa((150,650))
        self.__mesa3=Mesa((150,900))
        self.__mesa4=Mesa((150,1150))
        self.__mesa5=Mesa((850,1150))
        self.__mesa6=Mesa((850,900))
        self.__mesa7=Mesa((850,650))
        self.__mesa8=Mesa((1250,1350))

    def get_facecolor(self):
        return self.__facecolor

    def set_facecolor(self, facecolor):
        self.__facecolor = facecolor

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def draw(self, ax):
        ax.add_patch(patches.Rectangle((1250,0),750,1250,linewidth=4,edgecolor=self.__edgecolor,facecolor=self.__facecolor))
        ax.add_patch(patches.Rectangle((1625,1250),375,750,linewidth=4,edgecolor=self.__edgecolor,facecolor=self.__facecolor))
        ax.add_patch(patches.Rectangle((750,0),500,500,linewidth=4,edgecolor=self.__edgecolor,facecolor=self.__facecolor))
        self.__puerta.draw(ax)
        self.__puerta1.draw(ax)
        self.__puerta2.draw(ax)
        self.__puerta3.draw(ax)
        self.__silla.draw(ax)
        self.__silla1.draw(ax)
        self.__silla2.draw(ax)
        self.__silla3.draw(ax)
        self.__silla4.draw(ax)
        self.__silla5.draw(ax)
        self.__silla6.draw(ax)
        self.__silla7.draw(ax)
        self.__silla8.draw(ax)
        self.__mesa.draw(ax)
        self.__mesa1.draw(ax)
        self.__mesa2.draw(ax)
        self.__mesa3.draw(ax)
        self.__mesa4.draw(ax)
        self.__mesa5.draw(ax)
        self.__mesa6.draw(ax)
        self.__mesa7.draw(ax)
        self.__mesa8.draw(ax)
        self.__tv.draw(ax)
        self.__ventana.draw(ax)
        self.__ventana1.draw(ax)
        self.__ventana2.draw(ax)
        self.__ventana3.draw(ax)
        self.__ventana4.draw(ax)
        self.__ventana5.draw(ax)
        self.__ventana6.draw(ax)
        self.__tablero.draw(ax)
