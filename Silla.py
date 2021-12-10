import matplotlib.patches as patches

class Silla:

    def __init__(self,coordinate = (225,60)):
        self.__facecolor='#A3752F'
        self.__edgecolor='none'
        self.__linewidth=1
        self.__coordinate= coordinate
        self.__width=75
        self.__height=50

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
        ax.add_patch(patches.Rectangle((self.__coordinate[0]+130,self.__coordinate[1]),self.__width,self.__height,linewidth=self.__linewidth,edgecolor=self.__edgecolor,facecolor=self.__facecolor))
