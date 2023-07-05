import Components
from Tools.Rotater import Rotater
from Tools.Printer import Printer

from PIL import Image, ImageDraw
from math import sqrt
import random

size = 50
board = Image.new('RGB', (550, int(550*sqrt(3)/2)), (0, 0, 0))
draw = ImageDraw.Draw(board)
bgm = Components.BoardGameMap(100, 100, size)


def rc(r, g, b):
    rc = [(random.randint(1*r, round(2*r, 0))), (random.randint(1*r, round(2*r, 0))), (random.randint(1*r, round(2*r, 0)))]
    gc = [(random.randint(1*g, round(2*g, 0))), (random.randint(1*g, round(2*g, 0))), (random.randint(1*g, round(2*g, 0)))]
    bc = [(random.randint(1*b, round(2*b, 0))), (random.randint(1*b, round(2*b, 0))), (random.randint(1*b, round(2*b, 0)))]
    c = [(rc[i], gc[i], bc[i]) for i in range(3)]
    return c[0], c[1], c[2]

frames = []
for k in range(1, 20):
    board = Image.new('RGB', (1550, int(550 * sqrt(3) / 2)), (0, 0, 0))
    gexs = [Components.BoardGameGex(random.randint(2, 150), random.randint(1, 22), rc(10, 10, 10), 20) for _ in range(100)]


    for i, gex in enumerate(gexs):
        Rotater.gex_rotate(gex, 30*random.randint(0, 6))
        Printer.img_print_slot(gex.get_slot(), board)
        Printer.img_print_gex(gex, board)

    for l in range(1, 13):
        title_gexs = [Components.BoardGameGex(30, 4, rc(50, 100, 50), size),
                      Components.BoardGameGex(27, 5, rc(50, 100, 50), size),
                      Components.BoardGameGex(27, 3, rc(50, 100, 50), size),
                      Components.BoardGameGex(30, 2, rc(50, 100, 50), size),
                      Components.BoardGameGex(33, 3, rc(50, 100, 50), size),
                      Components.BoardGameGex(33, 5, rc(50, 100, 50), size),
                      Components.BoardGameGex(30, 6, rc(50, 100, 50), size),
                      ]
        for t_gex in title_gexs:
            Rotater.gex_rotate(t_gex, 30*l)
            Printer.img_print_gex(t_gex, board)

        frames.append(board.copy())

    # board.show()
frames[0].save(
    'gex.gif',
    save_all=True,
    append_images=frames[1:],
    optimize=True,
    duration=10,
    loop=0
)