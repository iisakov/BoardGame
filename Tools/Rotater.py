from math import pi, sqrt, pow, cos, sin

from Components.BoardGameField import BoardGameField
from Components.BoardGameVector import BoardGameVector


class Rotater:
    @staticmethod
    def field_rotate(field: BoardGameField, angle: float or int):
        # X = (x — x0) * cos(alpha) — (y — y0) * sin(alpha) + x0
        # Y = (x — x0) * sin(alpha) + (y — y0) * cos(alpha) + y0
        angle_rad = angle*pi/180
        new_corners = []
        for corner in field.get_corners():
            new_x = ((corner[0] - field.get_center().get_x()) * cos(angle_rad)) - (corner[1] - field.get_center().get_y()) * sin(angle_rad)
            new_y = ((corner[0] - field.get_center().get_x()) * sin(angle_rad)) + (corner[1] - field.get_center().get_y()) * cos(angle_rad)
            new_corners.append(BoardGameVector.create(new_x, new_y))
        field.set_corner(new_corners)
