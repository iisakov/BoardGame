#TODO Закончить разработку после достижения целей: 1) Отрисовки начальной карты с первым ходом игроков.

import Components
import Tools.Printer


speed = 1500
count = 100
flicker = True
img_save = True
gif_save = True
size = 50
frames = []

game = Components.BoardGame(num_players=4, num_gex_in_hand=2, size=size)

board = game.get_board()
draw = game.get_draw()
bg_map = game.get_map()
deck = game.get_deck()
discard = game.get_discard()


game.start()
bg_map.print_map(board)
frames.append(board.copy())

i = 0
while deck.get_num_gex_in_deck() > 0:
    i += 1
    Tools.Printer.Printer.img_print_text(x=0, y=0, x_2=1200, y_2=50, font_size=30, text=f'Ход - {i}', board=board)
    for player in game.get_players():
        for _ in range(game.get_num_gex_in_hand()):
            player.take_gex_in_hand(deck.pull_gex())

    for player in game.get_players():
        while player.get_num_gex_in_hand() > 0:
            player.deploy_gex(bg_map)
            Tools.Printer.Printer.img_print_text(x=0, y=40, x_2=1200, y_2=90, font_size=30, text=f'Игрок - {player.get_name()}', board=board)
            Tools.Printer.Printer.img_print_text(x=0, y=80, x_2=1200, y_2=130, font_size=30, text=f'{bg_map.get_statistics()}', board=board)
            Tools.Printer.Printer.img_print_text(x=0, y=130, x_2=700, y_2=350, font_size=20, text=f'{game}', board=board)

        bg_map.print_map(board)
        frames.append(board.copy())


frames[0].save(
    f'map_{speed}_{flicker}.gif',
    save_all=True,
    append_images=frames[1:],
    optimize=True,
    duration=speed,
    loop=0
)