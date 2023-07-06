#TODO Закончить разработку после достижения целей: 1) Отрисовки начальной карты с первым ходом игроков.

import Components

from PIL import Image, ImageDraw
from math import sqrt

size = 50
board = Image.new('RGB', (550, int(550*sqrt(3)/2)), (0, 0, 0))
draw = ImageDraw.Draw(board)

examples = [{"type": 'shop', "color": (100, 200, 100)}, {"type": 'house', "color": (200, 100, 100)},
            {"type": 'warehouse', "color": (100, 100, 100)}, {"type": 'park', "color": (100, 100, 200)}]

deck = Components.BoardGameDeck(3, examples, size)
deck.create()

frames = []

while len(deck.get_deck()) > 7:
    deck.pull_gex().deploy(9, 4).print(board)
    frames.append(board.copy())
    deck.pull_gex().deploy(6, 5).print(board)
    frames.append(board.copy())
    deck.pull_gex().deploy(6, 3).print(board)
    frames.append(board.copy())
    deck.pull_gex().deploy(9, 2).print(board)
    frames.append(board.copy())
    deck.pull_gex().deploy(12, 3).print(board)
    frames.append(board.copy())
    deck.pull_gex().deploy(12, 5).print(board)
    frames.append(board.copy())
    deck.pull_gex().deploy(9, 6).print(board)
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
