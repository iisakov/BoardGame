from math import pi, sqrt
from Components import BoardGameField, BoardGameVector
from Components.BoardGameSlot import BoardGameSlot


class BoardGameGex:

    def __init__(self, x: int or float, y: int, fields_type: list[dict], size: float):
        self.__step_angle = 0
        self.__slot = BoardGameSlot(x/2, sqrt(3)/2*y, size)
        self.__fields = self.init_fields(fields_type)
        self.__is_pull = False
        self.__siblings = {}
        self.__corners = [BoardGameVector.create_polar(1*size, pi*(angle*60+30)/180) for angle in range(0, 6)]

    def __str__(self):
        return f'number siblings: {len(self.get_siblings())}' \
               f'\ncenter: {self.get_center()}' \
               f'\ntypes field {[f.get_type() for f in self.get_fields()]}' \
               f'\ncorners: {[x.get() for x in self.__corners]}' \
               f'\nis pulled: {"Yes" if self.is_pulled() else "No"}\n'

    def init_fields(self, fields_type):
        from Tools.Rotater import Rotater
        fields = []
        for num_type, raw_field in enumerate(fields_type):
            field = BoardGameField.create(x=self.get_field_center()[num_type*2-3][0],
                                          y=self.get_field_center()[num_type*2-3][1],
                                          f_type= raw_field['type'],
                                          size=self.get_size(),
                                          color= raw_field['color'])
            Rotater.field_rotate(field, 60*(num_type+1))
            fields.append(field)
        return fields

    def get_slot(self):
        return self.__slot

    def get_fields(self):
        return self.__fields

    def get_center(self):
        return self.__slot.get_gex_center()

    def get_field_center(self):
        return self.get_slot().get_field_centers()

    def get_corners(self):
        return [(corner.get_x()+self.__slot.get_gex_center().get_x(),
                 corner.get_y()+self.__slot.get_gex_center().get_y()) for corner in self.__corners]

    def get_siblings(self):
        return self.__siblings

    def get_size(self):
        return self.__slot.get_size()

    def is_pulled(self):
        return self.__is_pull

    def set_corners(self, corners):
        self.__corners = corners

    def set_fields(self, fields: list[BoardGameField]):
        self.__fields = fields

    def add_siblings(self, sibling_gex):
        self.__siblings.add(sibling_gex)

    def put(self):
        self.__is_put = True

    def remove(self):
        self.__is_put = False


class GexGenerator:
    pass