
class Mueble (object) :

    def __init__(self, coordinate= (740,125)):
        self.__facecolor='#9C7C4C'
        self.__edgecolor='#463111'
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

    
