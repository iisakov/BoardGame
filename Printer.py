import math

from BoardGameGex import BoardGameGex
from BoardGameDeck import BoardGameDeck
from BoardGameMap import BoardGameMap

from PIL import Image
from PIL import ImageDraw

class Printer:
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
        coord_x = board.size[0]/2 if coord_x is None else coord_x
        coord_y = board.size[1]/2 if coord_y is None else coord_y
        radius = board.size[1]/10 if radius is None else radius
        width = radius * 2
        height = math.sqrt(3) / 2 * width

        font_size = round(radius/3)
        gex_polygon = []
        fields_polygon = [[(coord_x, coord_y)], [(coord_x, coord_y)], [(coord_x, coord_y)]]

        for corner in range(6):
            angle_deg = 60 * corner + 30
            angle_rad = math.pi / 180 * angle_deg
            corner_coord = (coord_x + radius * math.sin(angle_rad), coord_y + radius * math.cos(angle_rad))
            gex_polygon.append(corner_coord)

        for i in range(1, len(fields_polygon)+1):
            for corner in range(2*i, 2*i+3):
                angle_deg = 60 * corner + 30
                angle_rad = math.pi / 180 * angle_deg
                corner_coord = (coord_x + radius * math.sin(angle_rad), coord_y + radius * math.cos(angle_rad))
                fields_polygon[i-1].append(corner_coord)

        draw = ImageDraw.Draw(board)
        draw.polygon(xy=gex_polygon, fill='blue', outline=(255, 255, 255))

        for i, field in enumerate(bg_gex.get_fields()):
            draw.polygon(xy=fields_polygon[i], fill=field.get_color(), outline=(255, 255, 255))

    @staticmethod
    def img_print_map(bg_map: BoardGameMap, board: Image, radius=None, coord_x=None, coord_y=None):
        coord_x = board.size[0] / 2 if coord_x is None else coord_x
        coord_y = board.size[1] / 2 if coord_y is None else coord_y
        radius = board.size[1] / 10 if radius is None else radius
        width = radius * 2
        height = math.sqrt(3) / 2 * width

        gex_position = [(coord_x, coord_y), (coord_x-(3/4*width), coord_y-height/2), (coord_x-(3/4*width), coord_y+height/2),
                        (coord_x, coord_y+height), (coord_x+(3/4*width), coord_y+height/2), (coord_x+(3/4*width), coord_y-height/2),
                        (coord_x, coord_y-height)]
        for i, gex in enumerate(bg_map.get_map()):
            Printer.img_print_gex(gex, board, coord_x=gex_position[i][0], coord_y=gex_position[i][1])


    @staticmethod
    def show_board(board):
        board.show()

    @staticmethod
    def save_board(board, board_name):
        board.save(f'{board_name}.jpg', quality=95)
