from math import pi, sqrt
from Components import BoardGameVector


class BoardGameSlot:
    def __init__(self, x: int, y: int, size: float):
        self.__place = None
        self.__size = size
        self.__gex_center = BoardGameVector.create(x*size+size, y*size+size)
        self.__field_centers = [BoardGameVector.create_polar(0.5*size, pi*(angle*60+30)/180) for angle in range(0, 6)]

    @staticmethod
    def create(x: int, y: int, size: float):
        return SlotGenerator.gen(x, y, size)

    def get_gex_center(self):
        return self.__gex_center

    def get_field_centers(self):
        return [(center.get_x()+self.__gex_center.get_x(), center.get_y()+self.__gex_center.get_y()) for center in self.__field_centers]

    def get_place(self):
        return self.__place

    def get_size(self):
        return self.__size

    def set_field_centers(self, field_centers):
        self.__field_centers = field_centers

    def __str__(self):
        return f'place: {"empty" if self.__place is None else self.__place}\n' \
               f'center: {self.__gex_center}\n'


class SlotGenerator:
    @staticmethod
    def gen(x: int,
            y: int,
            size: float):
        return BoardGameSlot(x, y, size)
