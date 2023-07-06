from math import pi, sqrt, pow, cos, sin


from Components.BoardGameSlot import BoardGameSlot
from Components.BoardGameField import BoardGameField
from Components.BoardGameGex import BoardGameGex
from Components.BoardGameVector import BoardGameVector


class Mover:
    @staticmethod
    def deploy_gex(gex: BoardGameGex, x: int = 0, y: int = 0):
        Mover.move_gex(gex, x, y)
        gex.set_status('deployed')

    @staticmethod
    def move_gex(gex: BoardGameGex, x: int, y: int):
        size = gex.get_size()
        delta_x = round(x*size/2, 3)
        delta_y = round(y*size*sqrt(3)/2, 3)
        gex.get_slot().get_gex_center().set_x(gex.get_slot().get_gex_center().get_x() + delta_x)
        gex.get_slot().get_gex_center().set_y(gex.get_slot().get_gex_center().get_y() + delta_y)
        for field in gex.get_fields():
            field_x, field_y = field.get_center().get()
            field.get_center().set_x(field_x+delta_x)
            field.get_center().set_y(field_y+delta_y)
