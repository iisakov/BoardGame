from math import pi, sqrt
from Components import BoardGameField, BoardGameVector
from Components.BoardGameSlot import BoardGameSlot
from Components.BoardGameMap import BoardGameMap


class BoardGameGex:

    def __init__(self, x: int or float, y: int, fields_type: list[dict], size: float):
        self.__step_angle = 0
        self.__slot = BoardGameSlot(x/2, sqrt(3)/2*y, size)
        self.__fields = self.init_fields(fields_type)
        self.__status = False
        self.__angle = 0
        self.__siblings = {}

    def __str__(self):
        return f'number siblings: {len(self.get_siblings())}' \
               f'\ncenter: {self.get_center()}' \
               f'\nplace: {self.get_place()}' \
               f'\ntypes field: {[f.get_type() for f in self.get_fields()]}' \
               f'\nangle: {self.__angle}' \
               f'\nstatus: {self.get_status()}\n'

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

    def deploy(self, bg_map: BoardGameMap, x=0, y=0):
        if self.__status not in ('deployed', 'in deck'):
            from Tools.Mover import Mover
            Mover.deploy_gex(self, bg_map, x, y)
            return self
        else:
            print('gex not deploy - is', self.__status)
            return False

    def move(self, x, y):
        if self.__status not in ('deployed', 'in deck'):
            from Tools.Mover import Mover
            Mover.move_gex(self, x, y)
            return self
        else:
            print('gex not move - is', self.__status)
            return False

    def rotate(self, angle):
        if self.__status not in ('deployed', 'in deck'):
            from Tools.Rotater import Rotater
            Rotater.gex_rotate(self, angle)
            return self
        else:
            print('gex not rotate - is', self.__status)
            return False

    def print(self, board):
        if self.__status in ('deployed'):
            from Tools.Printer import Printer
            Printer.img_print_gex(self, board)
            return self
        else:
            print('gex not print - is', self.__status)
            return False

    def get_slot(self):
        return self.__slot

    def get_direction(self):
        return self.__slot.get_direction()

    def set_direction(self, direction):
        self.__slot.set_direction(direction)

    def get_fields(self):
        return self.__fields

    def get_center(self):
        return self.__slot.get_gex_center()

    def get_place(self):
        return self.__slot.get_place()

    def get_field_center(self):
        return self.get_slot().get_field_centers()

    def get_siblings(self):
        return self.__siblings

    def get_size(self):
        return self.__slot.get_size()

    def get_angle(self):
        return self.__angle

    def add_angle(self, angle):
        self.__angle += angle

    def get_status(self):
        return self.__status

    def set_status(self, status: str):
        self.__status = status

    def set_fields(self, fields: list[BoardGameField]):
        self.__fields = fields

    def add_siblings(self, sibling_gex):
        self.__siblings.add(sibling_gex)


class GexGenerator:
    pass