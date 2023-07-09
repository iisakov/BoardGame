from math import pi, sqrt, pow, cos, sin


from Components.BoardGameSlot import BoardGameSlot
from Components.BoardGameField import BoardGameField
from Components.BoardGameGex import BoardGameGex
from Components.BoardGameVector import BoardGameVector


class Rotater:
    # X = (x — x0) * cos(alpha) — (y — y0) * sin(alpha) + x0
    # Y = (x — x0) * sin(alpha) + (y — y0) * cos(alpha) + y0
    @staticmethod
    def rotate(center: BoardGameVector, vec_list: list[tuple], angle: float or int):
        angle_rad = angle * pi / 180
        new_vec = []
        for vec in vec_list:
            new_x = ((vec[0] - center.get_x()) * cos(angle_rad)) - (vec[1] - center.get_y()) * sin(angle_rad)
            new_y = ((vec[0] - center.get_x()) * sin(angle_rad)) + (vec[1] - center.get_y()) * cos(angle_rad)
            new_vec.append(BoardGameVector.create(new_x, new_y))
        return new_vec

    @staticmethod
    def slot_rotate(slot: BoardGameSlot, angle: float or int):
        slot.set_field_centers(Rotater.rotate(slot.get_gex_center(), slot.get_field_centers(), angle))
        slot.set_direction(angle/60%2)

    @staticmethod
    def field_rotate(field: BoardGameField, angle: float or int):
        field.set_corner(Rotater.rotate(field.get_center(), field.get_corners(), angle))

    @staticmethod
    def gex_rotate(gex: BoardGameGex, angle: float or int):
        Rotater.slot_rotate(gex.get_slot(), angle)
        gex.add_angle(angle)
        for nem_field, field in enumerate(gex.get_fields()):
            x = gex.get_field_center()[nem_field * 2 - 3][0]
            y = gex.get_field_center()[nem_field * 2 - 3][1]
            field.set_center(BoardGameVector.create(x, y))
            Rotater.field_rotate(field, angle)
