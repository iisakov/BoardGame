from math import pi, sqrt, pow, cos, sin

from Components.BoardGameMap import BoardGameMap
from Components.BoardGameSlot import BoardGameSlot
from Components.BoardGameField import BoardGameField
from Components.BoardGameGex import BoardGameGex
from Components.BoardGameVector import BoardGameVector


class Mover:
    @staticmethod
    def deploy_gex(gex: BoardGameGex, bg_map: BoardGameMap, x: int = 0, y: int = 0):
        Mover.move_gex(gex, x, y)
        bg_map.deploy_gex(gex)
        gex.set_status('deployed')

    @staticmethod
    def move_gex(gex: BoardGameGex, x: int, y: int):
        size = gex.get_size()
        delta_x = round(x*size/2, 3)
        delta_y = round(y*size*sqrt(3)/2, 3)
        gex.get_slot().get_gex_center().set_x(gex.get_slot().get_gex_center().get_x() + delta_x)
        gex.get_slot().get_gex_center().set_y(gex.get_slot().get_gex_center().get_y() + delta_y)

        place_x, place_y = gex.get_slot().get_place()
        gex.get_slot().set_place((place_x+x, place_y+y))

        for field in gex.get_fields():
            field_x, field_y = field.get_center().get()
            field.get_center().set_x(field_x+delta_x)
            field.get_center().set_y(field_y+delta_y)
