import math

from Components.BoardGameSlot import BoardGameSlot
from Components.BoardGameField import BoardGameField
from Components.BoardGameGex import BoardGameGex
from Components.BoardGameDeck import BoardGameDeck
from Components.BoardGameMap import BoardGameMap

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


class Printer:
    corners = range(6)
    angle_degrees = [60 * corner + 30 for corner in corners]
    angle_radians = [math.pi / 180 * angle_degree for angle_degree in angle_degrees]

    @staticmethod
    def img_print_text(x, y, x_2, y_2, font_size, text, board: Image):
        draw = ImageDraw.Draw(board)
        font = ImageFont.truetype('OpenSans-Regular.ttf', font_size)
        draw.polygon(xy=((x, y), (x_2, y), (x_2, y_2), (x, y_2)), fill=(0, 0, 0), outline=(100, 100, 100))
        draw.text((x, y), text, font=font, fill=(100, 100, 100))

    @staticmethod
    def img_print_slot(bg_slot: BoardGameSlot, board: Image):
        draw = ImageDraw.Draw(board)
        draw.point(bg_slot.get_gex_center().get(), 'blue')
        draw.point(bg_slot.get_field_centers(), 'green')

    @staticmethod
    def img_print_field(bg_field: BoardGameField, board: Image):
        draw = ImageDraw.Draw(board)
        draw.polygon(bg_field.get_corners(), bg_field.get_color(), (50, 50, 50))



    @staticmethod
    def img_print_gex(bg_gex: BoardGameGex, board: Image):
        for field in bg_gex.get_fields():
            Printer.img_print_field(field, board)


    @staticmethod
    def img_print_markup(bg_map: BoardGameMap, board: Image):
        draw = ImageDraw.Draw(board)
        for row in bg_map.get_slots():
            for slot in row:
                x = slot.get_gex_center().get_x()
                y = slot.get_gex_center().get_y()
                draw.point((x, y), 'yellow')
                draw.point(slot.get_field_centers(), 'blue')

    @staticmethod
    def show_board(board):
        board.show()

    @staticmethod
    def save_board(board, board_name):
        board.save(f'{board_name}.jpg', quality=95)
