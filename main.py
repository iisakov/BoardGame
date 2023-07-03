#TODO Закончить разработку после достижения целей: 1) Отрисовки начальной карты с первым ходом игроков.
import random

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

for k in range(10):
    board = Image.new('RGB', (550, int(550 * sqrt(3) / 2)), (0, 0, 0))
    gexs = [Components.BoardGameGex(random.randint(5, 14), random.randint(2, 8), ['black', 'black', 'black'], size) for _ in range(20)]

    for i, gex in enumerate(gexs):
        Rotater.gex_rotate(gex, 30*random.randint(0, 6))
        Printer.img_print_slot(gex.get_slot(), board)
        Printer.img_print_gex(gex, board)

    for i in bgm.get_slots():
        for j in i:
            Printer.img_print_slot(j, board)

# board.show()
    board.save(f'size_{k}.jpg')
