#TODO Закончить разработку после достижения целей: 1) Отрисовки начальной карты с первым ходом игроков.

import Components

from PIL import Image, ImageDraw
from math import sqrt

speed = 1
flicker = True
size = 50
# board = Image.new('RGB', (1200, int(1200*sqrt(3)/2)), (0, 0, 0))
# draw = ImageDraw.Draw(board)
# bg_map = Components.BoardGameMap(500, 500, size)

examples = [{"type": 'shop', "color": (100, 100, 200)}, {"type": 'house', "color": (200, 100, 100)},
            {"type": 'warehouse', "color": (100, 100, 100)}, {"type": 'park', "color": (100, 200, 100)}]

for era in range(1):
    board = Image.new('RGB', (1200, int(1200 * sqrt(3) / 2)), (0, 0, 0))
    draw = ImageDraw.Draw(board)
    bg_map = Components.BoardGameMap(500, 500, size)
    deck = Components.BoardGameDeck(3, examples, size)
    deck.create()

    frames = []
    deck.pull_gex().rotate(0).deploy(bg_map, 19, 10).print(board)

    frames.append(board.copy())
    old_frame = board.copy()
    while len(deck.get_deck()) > 0:
        second_gex = deck.pull_gex()
        deployed = False
        for i, place in enumerate(bg_map.get_available_place()):
            if i == 0:
                second_gex.rotate(place[2] * 60)
            if second_gex.get_field_by_direction(place[4]).get_type() == place[3]\
                    and (place[0], place[1]) not in [(opl[0], opl[1]) for opl in bg_map.get_occupied_place()]\
                    and second_gex.get_direction() == place[2]:
                second_gex.deploy(bg_map, place[0], place[1]).print(board)
                new_frame = board.copy()
                frames.append(new_frame)
                if flicker:
                    frames.append(old_frame)
                    frames.append(new_frame)
                    old_frame = new_frame
                deployed = True
                break
            else:
                second_gex.rotate(60)
        if not deployed:
            deck.push_gex(second_gex)

    # board.show()
    board.save(f"imgs/map_{era}_{speed}_{flicker}.jpg")

    frames[0].save(
        f'gifs/map_{era}_{speed}_{flicker}.gif',
        save_all=True,
        append_images=frames[1:],
        optimize=True,
        duration=speed,
        loop=0
    )
