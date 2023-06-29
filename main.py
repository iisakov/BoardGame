#TODO Закончить разработку после достижения целей: 1) Отрисовки начальной карты с первым ходом игроков.

from config import n_type, m_field, patt, field_desc
import Components
from Tools.Rotater import Rotater

from PIL import Image, ImageDraw
from math import sqrt

size = 50
board = Image.new('RGB', (550, int(550*sqrt(3)/2)), (100, 150, 100))
draw = ImageDraw.Draw(board)
bgm = Components.BoardGameMap(10, 10, size).get_slots()


for num_row, row in enumerate(bgm):
    for num_slot, slot in enumerate(row):
        x = slot.get_gex_center().get_x()
        y = sqrt(3)/2+slot.get_gex_center().get_y()
        coord = slot.get_field_centres()

        draw.point((x, y), 'yellow')
        draw.point(coord, 'blue')

for i in range(3):
    field = Components.BoardGameField.create(center=Components.BoardGameVector(bgm[0][0].get_field_centres()[1+2*i][0], bgm[0][0].get_field_centres()[1+2*i][1]), size=size)
    Rotater.field_rotate(field, i*60)
    draw.polygon(xy=field.get_corners(), fill=(field.get_color()), outline=(0, 0, 0))


for i in range(3):
    field = Components.BoardGameField.create(center=Components.BoardGameVector(bgm[0][1].get_field_centres()[0+2*i][0], bgm[0][1].get_field_centres()[0+2*i][1]), size=size, color=(200, 100, 100))
    Rotater.field_rotate(field, i*60+60)
    draw.polygon(xy=field.get_corners(), fill=(field.get_color()), outline=(0, 0, 0))

board.show()
