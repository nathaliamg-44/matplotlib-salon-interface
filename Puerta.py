import matplotlib.patches as patches
import matplotlib.pyplot as plt
import Mueble
class Puerta(Mueble.Mueble):

    def __init__(self, coordinate= (740,125)):
        self.__facecolor='#9C7C4C'
        self.__edgecolor='#463111'
        self.__linewidth=1
        self.__coordinate=coordinate
        self.__width=100
        self.__height=250
        self.estado="cerrada"
        self.__contrasena= "puerta"

    def Abrir(self, contrasena):
        if contrasena== self.__contrasena:
            self.estado="abierto"
            return "Acceso permitido"
        else:
            self.estado="cerrado"
            return "Acceso negado"

    def set_contrasena(self, contrasenaActual, contrasenaNueva):
        if contrasenaActual==self.__contrasena:
            self.__contrasena=contrasenaNueva
            return "cambiada"
        else:
            return "acceso denegado"
        
    

    def draw(self, ax):
        ax.add_patch(patches.Rectangle(self.__coordinate,self.__width,self.__height,linewidth=self.__linewidth,edgecolor=self.__edgecolor,facecolor=self.__facecolor))
        ax.add_artist(plt.Circle((self.__coordinate[0] + 20, self.__coordinate[1] + self.__height / 2), 7.5, color='#9C9C9C'))


    pass
