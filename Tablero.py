import matplotlib.patches as patches

class Tablero:

    def __init__(self):
        self.__facecolor='#FFFFFF'
        self.__edgecolor='#000000'
        self.__linewidth=1
        self.__coordinate=(350,1600)
        self.__width=600
        self.__height=300

    def get_facecolor(self):
        return self.__facecolor

    def set_facecolor(self, facecolor):
        self.__facecolor = facecolor

    def get_coordinate(self):
        return self.__coordinate

    def set_coordinate(self, coordinate):
        self.__coordinate = coordinate

    def get_width(self):
        return self.__width

    def set_width(self, width):
        self.__width = width

    def get_height(self):
        return self.__height

    def set_height(self, height):
        self.__height = height

    def draw (self, ax):
        ax.add_patch(patches.Rectangle(self.__coordinate,self.__width,self.__height,linewidth=self.__linewidth,edgecolor=self.__edgecolor,facecolor=self.__facecolor))

