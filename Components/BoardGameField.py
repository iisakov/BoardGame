from Components import BoardGameVector
from math import pi, sqrt


class BoardGameField:
    def __init__(self,
                 x: float = 0,
                 y: float = 0,
                 f_type: str = 'default',
                 color: str = 'gray',
                 size: float = 1):
        self.__f_type = f_type
        self.__color = color
        self.__center = BoardGameVector(x, y)
        self.__size = size
        self.__corners = [BoardGameVector.create_polar(sqrt(3)*size/2 if x % 2 == 0 else 1*size/2, x/2*pi) for x in range(1, 5)]

    @staticmethod
    def create(x: float,
               y: float,
               f_type: str = 'default',
               color: str or tuple = 'gray',
               size: float = 1):
        return FieldGenerator.gen(x, y, f_type, color, size)

    def get_type(self):
        return self.__f_type

    def get_color(self):
        return self.__color

    def get_center(self):
        return self.__center

    def get_corners(self):
        return [(vec.get_x()+self.__center.get_x(), vec.get_y()+self.__center.get_y()) for vec in self.__corners]

    def set_center(self, center):
        self.__center = center

    def set_corner(self, corners):
        self.__corners = corners


class FieldGenerator:
    @staticmethod
    def gen(x,
            y,
            f_type: str,
            color: str,
            size: float = 1):
        return BoardGameField(x, y, f_type, color, size)