#TODO Закончить разработку после достижения целей: 1) Отрисовки начальной карты с первым ходом игроков.

from config import n_type, m_field, patt, field_desc
import Components

from PIL import Image, ImageDraw

field = Components.BoardGameField.create()
board = Image.new('RGB', (500, 500), (100, 150, 100))

print(field.get_corner())
corners = []
for coord in field.get_corner():
    corners.append((250+coord[0] * 25, 250+coord[1] * 25))
draw = ImageDraw.Draw(board)
draw.polygon(xy=corners, fill=(field.get_color()), outline=(0, 0, 0))
board.show()
