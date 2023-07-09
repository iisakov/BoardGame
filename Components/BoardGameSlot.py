from math import pi, sqrt
from Components import BoardGameVector


class BoardGameSlot:
    def __init__(self, x: int or float, y: int or float, size: float):
        self.__place = (x, y)
        self.__size = size
        self.__gex_center = BoardGameVector.create(x*size+size, y*size+size)
        self.__field_centers = [BoardGameVector.create_polar(0.5*size, pi*(angle*60+30)/180) for angle in range(0, 6)]
        self.__direction = 0

    @staticmethod
    def create(x: int or float, y: int or float, size: float):
        return SlotGenerator.gen(x, y, size)

    def get_gex_center(self):
        return self.__gex_center

    def get_field_centers(self):
        return [(center.get_x()+self.__gex_center.get_x(), center.get_y()+self.__gex_center.get_y()) for center in self.__field_centers]

    def get_place(self):
        return self.__place

    def get_size(self):
        return self.__size

    def get_direction(self):
        return self.__direction

    def set_field_centers(self, field_centers):
        self.__field_centers = field_centers

    def set_place(self, place):
        self.__place = place

    def set_direction(self, direction):
        self.__direction = direction

    def __str__(self):
        return f'place: {"empty" if self.__place is None else self.__place}\n' \
               f'center: {self.__gex_center}\n' \
               f'direction: {self.get_direction()}'


class SlotGenerator:
    @staticmethod
    def gen(x: int,
            y: int,
            size: float):
        return BoardGameSlot(x, y, size)
