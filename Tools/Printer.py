import math

from Components.BoardGameGex import BoardGameGex
from Components.BoardGameDeck import BoardGameDeck
from Components.BoardGameMap import BoardGameMap

from PIL import Image
from PIL import ImageDraw


class Printer:
    corners = range(6)
    angle_degrees = [60 * corner + 30 for corner in corners]
    angle_radians = [math.pi / 180 * angle_degree for angle_degree in angle_degrees]

    @staticmethod
    def console_print_gex(bg_gex: BoardGameGex):
        for i in bg_gex.get_gex():
            print(i)

    @staticmethod
    def console_print_deck(bg_deck: BoardGameDeck):
        str1, str2 = '', ''
        for gex_num, gex in enumerate(bg_deck.get_deck()):
            str_list = gex.get_gex()
            str1 += ' ' + str_list[0]
            str2 += ' ' + str_list[1]
            if (gex_num + 1) % (bg_deck.n_type * 2) == 0:
                print(f'{str1}\n{str2}')
                str1, str2 = '', ''
        print()

    @staticmethod
    def img_print_gex(bg_gex: BoardGameGex, board: Image, radius=None, coord_x=None, coord_y=None):
        pass

    @staticmethod
    def img_print_map(bg_map: BoardGameMap, board: Image, coord_x=None, coord_y=None):
        pass

    @staticmethod
    def img_print_markup(bg_map: BoardGameMap, board: Image):
        draw = ImageDraw.Draw(board)
        for row in bg_map.get_slots():
            for slot in row:
                x = slot.get_gex_center().get_x()
                y = slot.get_gex_center().get_y()
                draw.point((x, y), 'yellow')
                draw.point(slot.get_field_centres(), 'blue')

    @staticmethod
    def show_board(board):
        board.show()

    @staticmethod
    def save_board(board, board_name):
        board.save(f'{board_name}.jpg', quality=95)
