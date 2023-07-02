from math import pi
from Components import BoardGameField, BoardGameVector, BoardGameSlot
from Components.BoardGameSlot import BoardGameSlot


class BoardGameGex:

    def __init__(self, x: int, y: int, fields_type: list[str], size: float):
        self.__step_angle = 0
        self.__slot = BoardGameSlot(x, y, size)
        self.__fields = fields_type
        self.__is_put = False
        self.__siblings = {}
        self.__corners = [BoardGameVector.create_polar(1*size, pi*(angle*60+30)/180) for angle in range(0, 6)]

    def __str__(self):
        return f'{len(self.get_siblings())} {self.get_siblings() = }' \
               f'\ncenter: {self.get_center()}' \
               f'\n{len(self.get_fields())} {self.get_fields() = }' \
               f'\ncorners: {[x.get() for x in self.__corners]}' \
               f'\n{self.is_putted() = }\n'

    def get_fields(self):
        return self.__fields

    def get_center(self):
        return self.__slot.get_gex_center()

    def get_corners(self):
        return [(corner.get_x()*self.__slot.get_size()+self.__slot.get_gex_center().get_x(), corner.get_y()*self.__slot.get_size()+self.__slot.get_gex_center().get_y()) for corner in self.__corners]

    def get_siblings(self):
        return self.__siblings

    def get_size(self):
        return self.__slot.get_size()

    def get_step_angel(self):
        return self.__step_angle

    def is_putted(self):
        return self.__is_put

    def set_fields(self, fields: list[BoardGameField]):
        self.__fields = fields

    def set_center(self, center: tuple):
        self.__center = center

    def set_step_angel(self, step: int):
       self.__step_angle = step

    def add_siblings(self, sibling_gex):
        self.__siblings.add(sibling_gex)

    def put(self):
        self.__is_put = True

    def remove(self):
        self.__is_put = False


class GexGenerator:
    pass