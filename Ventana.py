import matplotlib.patches as patches

class Ventana:

    def __init__(self, coordinate = (20,50)):
        self.__facecolor='#92E7CD'
        self.__edgecolor='#4D5658'
        self.__linewidth=1
        self.__coordinate=coordinate
        self.__width=100
        self.__height=250

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
        ax.add_patch(patches.Rectangle(self.__coordinate,self.__width / 2,self.__height / 2,linewidth=self.__linewidth,edgecolor=self.__edgecolor,facecolor=self.__facecolor))
        ax.add_patch(patches.Rectangle((self.__coordinate[0] + self.__width / 2, self.__coordinate[1] + self.__height / 2),self.__width / 2,self.__height / 2,linewidth=self.__linewidth,edgecolor=self.__edgecolor,facecolor=self.__facecolor))
