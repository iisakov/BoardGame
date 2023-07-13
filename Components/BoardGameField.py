from Components import BoardGameVector
from math import pi, sqrt


class BoardGameField:
    def __init__(self,
                 direction: int,
                 x: float = 0,
                 y: float = 0,
                 f_type: str = 'default',
                 color: str = 'gray',
                 size: float = 1,
                 ):
        self.__f_type = f_type
        self.__color = color
        self.__center = BoardGameVector(x, y)
        self.__size = size
        self.__corners = [BoardGameVector.create_polar(sqrt(3)*size/2 if x % 2 == 0 else 1*size/2, x/2*pi) for x in range(1, 5)]
        self.__direction = direction

    @staticmethod
    def create(direction: int,
               x: float,
               y: float,
               f_type: str = 'default',
               color: str or tuple = 'gray',
               size: float = 1):
        return FieldGenerator.gen(direction, x, y, f_type, color, size)

    def print(self, board):
        from Tools.Printer import Printer
        Printer.img_print_field(self, board)
        return self

    def get_type(self):
        return self.__f_type

    def get_color(self):
        return self.__color

    def get_center(self):
        return self.__center

    def get_corners(self):
        return [(vec.get_x()+self.__center.get_x(), vec.get_y()+self.__center.get_y()) for vec in self.__corners]

    def get_direction(self):
        return self.__direction

    def set_center(self, center: BoardGameVector):
        self.__center = center

    def set_corner(self, corners):
        self.__corners = corners

    def set_direction(self, direction):
        self.__direction = direction

    def add_direction(self, direction):
        self.__direction = (self.__direction-direction) % 3

    def set_type(self, f_type: str, color: tuple):
        self.__f_type = f_type
        self.__color = color

class FieldGenerator:
    @staticmethod
    def gen(direction,
            x,
            y,
            f_type: str,
            color: str,
            size: float = 1):
        return BoardGameField(direction, x, y, f_type, color, size)