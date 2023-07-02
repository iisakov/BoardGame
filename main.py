#TODO Закончить разработку после достижения целей: 1) Отрисовки начальной карты с первым ходом игроков.

from config import n_type, m_field, patt, field_desc
import Components
from Tools.Rotater import Rotater
from Tools.Printer import Printer

from PIL import Image, ImageDraw
from math import sqrt

size = 50
board = Image.new('RGB', (550, int(550*sqrt(3)/2)), (100, 150, 100))
draw = ImageDraw.Draw(board)
bgm = Components.BoardGameMap(10, 10, size)

gex = Components.BoardGameGex(1, 1, ["str" for _ in range(3)], size)

print(gex)
# Printer.img_print_markup(bgm, board)
# Printer.show_board(board)

# board.show()
# board.save('size_100.jpg')
