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
    def img_print_text(x: float or int, y: float or int, font_size, text: str, board: Image):
        draw = ImageDraw.Draw(board)
        font = ImageFont.truetype('OpenSans-Regular.ttf', font_size)
        lines = text.split('\n')
        num_line = len(text.split('\n'))
        max_len = len(sorted(lines)[0])
        x_end = x + max_len * font_size * 0.55
        y_end = y + num_line * font_size * 1.5

        draw.rectangle(xy=((x, y), (x_end, y_end)), fill=(0, 0, 0), outline=(100, 100, 100))
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
    def save_board(board, board_name, path):
        board.save(f'{path}/{board_name}.jpg', quality=95)
