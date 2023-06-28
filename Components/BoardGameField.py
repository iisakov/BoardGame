from Components import BoardGameVector
from math import pi, sqrt


class BoardGameField:
    def __init__(self,
                 f_type: str = 'default',
                 color: str = 'gray',
                 center: BoardGameVector = BoardGameVector.create(0, 0)):
        self.__f_type = f_type
        self.__color = color
        self.__center = center
        self.__corners = [BoardGameVector.create_polar(sqrt(3) if x % 2 == 0 else 1, x/2*pi) for x in range(1, 5)]

    @staticmethod
    def create(f_type: str = 'default',
               color: str = 'gray',
               center: BoardGameVector = BoardGameVector.create(0, 0)):
        return FieldGenerator.gen(f_type, color, center)

    def get_type(self):
        return self.__f_type

    def get_color(self):
        return self.__color

    def get_siblings(self):
        return self.__siblings

    def get_center(self):
        return self.__center

    def get_corners(self):
        return [x for x in self.__corners]

    def set_corner(self, corners):
        self.__corners = corners


class FieldGenerator:
    @staticmethod
    def gen(f_type: str,
            color: str,
            center: BoardGameVector):
        return BoardGameField(f_type, color, center)