#TODO Закончить разработку после достижения целей: 1) Отрисовки начальной карты с первым ходом игроков.
import random

import Components
from Tools.Rotater import Rotater
from Tools.Printer import Printer

from PIL import Image, ImageDraw
from math import sqrt

size = 50
board = Image.new('RGB', (550, int(550*sqrt(3)/2)), (0, 0, 0))
draw = ImageDraw.Draw(board)
bgm = Components.BoardGameMap(100, 100, size)

examples = [
    {"type": 'shop', "color": (100, 200, 100)},
    {"type": 'house', "color": (200, 100, 100)},
    {"type": 'warehouse', "color": (100, 100, 100)},
    {"type": 'park', "color": (100, 100, 200)}
    ]

deck = Components.BoardGameDeck(3, examples, size)
deck.create()

frames = []
while len(deck.get_deck()) > 0:
    gex = deck.pull_gex()
    Rotater.gex_rotate(gex, random.randint(0, 180))
    Printer.img_print_gex(gex, board)
    frames.append(board.copy())

# board.show()
frames[0].save(
    'gex.gif',
    save_all=True,
    append_images=frames[1:],
    optimize=True,
    duration=1,
    loop=0
)