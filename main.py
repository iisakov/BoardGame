#TODO Закончить разработку после достижения целей: 1) Отрисовки начальной карты с первым ходом игроков.

from config import n_type, m_field, patt, field_desc
import Components
from Tools.Rotater import Rotater

from PIL import Image, ImageDraw
from math import sqrt

field = Components.BoardGameField.create()
board = Image.new('RGB', (550, int(550*sqrt(3)/2)), (100, 150, 100))
draw = ImageDraw.Draw(board)
bgm = Components.BoardGameMap((10,10)).get_slots()


for num_row, row in enumerate(bgm):
    for num_vec, vec in enumerate(row):
        x = 50+vec.get_x()*50
        y = sqrt(3)/2*50+vec.get_y()*50
        coord = Components.BoardGameSlot(x, y).get_field_centres(50)

        if num_vec%3 == 0 and num_row%2 == 0:
            field = Components.BoardGameField.create(center=Components.BoardGameVector(x, y))
            Rotater.field_rotate(field, 60)
            corners = []
            for coordinates in field.get_corners():
                corners.append((coord[3][0]+coordinates.get_x() * 25, coord[3][1]+coordinates.get_y() * 25))

            draw.polygon(xy=corners, fill=(field.get_color()), outline=(0, 0, 0))
        draw.point((x, y), 'yellow')
        draw.point(coord, 'blue')
board.show()