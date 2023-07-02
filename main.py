#TODO Закончить разработку после достижения целей: 1) Отрисовки начальной карты с первым ходом игроков.

from config import n_type, m_field, patt, field_desc
import Components
from Tools.Rotater import Rotater
from Tools.Printer import Printer

from PIL import Image, ImageDraw
from math import sqrt

size = 50
board = Image.new('RGB', (550, int(550*sqrt(3)/2)), (0, 0, 0))
draw = ImageDraw.Draw(board)
bgm = Components.BoardGameMap(10, 10, size)

field = Components.BoardGameField(x=100, y=100, size=size)

gex = Components.BoardGameGex(3, 3, ['red', 'green', 'blue'], size)
Rotater.gex_rotate(gex, 30)
Printer.img_print_slot(gex.get_slot(), board)
Printer.img_print_gex(gex, board)

Printer.img_print_field(gex.get_fields()[0], board)
Printer.img_print_field(gex.get_fields()[1], board)
Printer.img_print_field(gex.get_fields()[2], board)


Rotater.field_rotate(field, 90)
Printer.img_print_field(field, board)

board.show()
# board.save('size_100.jpg')
