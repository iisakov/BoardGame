from math import pi
from Components import BoardGameVector


class BoardGameSlot:
    def __init__(self, x, y):
        self.__gex_center = BoardGameVector.create(x, y)
        self.__field_centers = [BoardGameVector.create_polar(0.5, pi*(angle*60+30)/180) for angle in range(0, 6)]

    def get_gex_center(self):
        return self.__gex_center

    def get_field_centres(self, size):
        return [(center.get_x()*size+self.__gex_center.get_x(), center.get_y()*size+self.__gex_center.get_y()) for center in self.__field_centers]
