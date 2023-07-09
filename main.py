#TODO Закончить разработку после достижения целей: 1) Отрисовки начальной карты с первым ходом игроков.

import Components

from PIL import Image, ImageDraw
from math import sqrt

size = 50
board = Image.new('RGB', (1200, int(1200*sqrt(3)/2)), (0, 0, 0))
draw = ImageDraw.Draw(board)
bg_map = Components.BoardGameMap(500, 500, size)

examples = [{"type": 'shop', "color": (100, 200, 100)}, {"type": 'house', "color": (200, 100, 100)},
            {"type": 'warehouse', "color": (100, 100, 100)}, {"type": 'park', "color": (100, 100, 200)}]

deck = Components.BoardGameDeck(3, examples, size)
deck.create()

frames = []
deck.pull_gex().rotate(0).deploy(bg_map, 22, 10).print(board)
frames.append(board.copy())
# deck.pull_gex().rotate(60).deploy(bg_map, 15, 4).print(board)
# frames.append(board.copy())

while len(deck.get_deck()) > 0:
    place_x, place_y, place_direction = bg_map.get_random_available_place()
    print(place_x, place_y, place_direction)
    deck.pull_gex().rotate(place_direction*60).deploy(bg_map, place_x, place_y).print(board)
    frames.append(board.copy())


board.show()
board.save("map.jpg")
frames[0].save(
    'map.gif',
    save_all=True,
    append_images=frames[1:],
    optimize=True,
    duration=500,
    loop=0
)
