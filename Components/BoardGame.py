from Components.BoardGameMap import BoardGameMap
from Components.BoardGamePlayer import BoardGamePlayer
from Components.BoardGameDeck import BoardGameDeck

from PIL import Image, ImageDraw
from math import sqrt


class BoardGame:
    __examples = [{"type": 'shop', "color": (150, 150, 255)},
                  {"type": 'house', "color": (255, 150, 150)},
                  {"type": 'warehouse', "color": (170, 170, 170)},
                  {"type": 'park', "color": (150, 255, 150)}]

    def __init__(self, num_players, num_gex_in_hand, num_steps, size,  examples=None, board=None, map=None, center_delta_x = 0, center_delta_y = 0):
        self.__count_slots = 24
        self.__num_players = num_players
        self.__num_gex_in_hand = num_gex_in_hand
        self.__num_steps = num_steps
        self.center_delta_x = center_delta_x
        self.center_delta_y = center_delta_y
        self.__players = [BoardGamePlayer(f'Playr_{num}', num_gex_in_hand) for num in range(1, num_players+1)]
        self.__deck = BoardGameDeck.create(3, self.__examples if examples is None else examples, size)
        self.__discard = BoardGameDeck(3, self.__examples if examples is None else examples, size)
        self.__map = BoardGameMap() if map is None else map
        self.__board = Image.new('RGB',
                                 (size*self.__count_slots, int(size*self.__count_slots * sqrt(3) / 2)),
                                 (245, 245, 245)) if board is None else board
        self.__draw = ImageDraw.Draw(self.__board)

    def __str__(self):
        return f'Количество игроков: {self.__num_players}' \
               f'\nДоступное количество карт на руках: {self.__num_gex_in_hand}' \
               f'\nКарт в колоде: {self.__deck.get_num_gex_in_deck()}' \
               f'\nКарт в сбросе: {self.__discard.get_num_gex_in_deck()}' \
               f'\nКарт на поле: {self.__map.get_num_deployed_gex()}'

    def start(self):
        self.__deck.pull_gex().rotate(0).deploy(bg_map=self.__map, x=self.__count_slots+self.center_delta_x, y=self.__count_slots/2+self.center_delta_y)
        self.__deck.pull_gex().rotate(0).deploy(bg_map=self.__map, x=self.__count_slots-3+self.center_delta_x, y=self.__count_slots/2+1+self.center_delta_y)
        self.__deck.pull_gex().rotate(0).deploy(bg_map=self.__map, x=self.__count_slots-3+self.center_delta_x, y=self.__count_slots/2-1+self.center_delta_y)
        self.__deck.pull_gex().rotate(0).deploy(bg_map=self.__map, x=self.__count_slots+self.center_delta_x, y=self.__count_slots/2-2+self.center_delta_y)
        self.__deck.pull_gex().rotate(0).deploy(bg_map=self.__map, x=self.__count_slots+3+self.center_delta_x, y=self.__count_slots/2-1+self.center_delta_y)
        self.__deck.pull_gex().rotate(0).deploy(bg_map=self.__map, x=self.__count_slots+3+self.center_delta_x, y=self.__count_slots/2+1+self.center_delta_y)
        self.__deck.pull_gex().rotate(0).deploy(bg_map=self.__map, x=self.__count_slots+self.center_delta_x, y=self.__count_slots/2+2+self.center_delta_y)

        if self.__deck.get_num_gex_in_deck() - (self.__num_players*self.__num_gex_in_hand*self.__num_steps) < 0:
            for _ in range(self.__deck.get_num_gex_in_deck() % (self.__num_players * self.__num_gex_in_hand)):
                self.__discard.push_gex(self.__deck.pull_gex())
        else:
            for _ in range(self.__deck.get_num_gex_in_deck() - (self.__num_players*self.__num_gex_in_hand*7)):
                self.__discard.push_gex(self.__deck.pull_gex())

        return self

    def get_num_players(self):
        return self.__num_players

    def get_num_gex_in_hand(self):
        return self.__num_gex_in_hand

    def get_options(self):
        return {'num_gex_in_hand': self.__num_gex_in_hand,
                'num_players': self.__num_players}

    def get_players(self) -> list[BoardGamePlayer]:
        return self.__players

    def get_deck(self) -> BoardGameDeck:
        return self.__deck

    def get_num_gex_in_deck(self):
        return self.get_deck().get_num_gex_in_deck()

    def get_discard(self) -> BoardGameDeck:
        return self.__discard

    def get_map(self) -> BoardGameMap:
        return self.__map

    def get_board(self) -> Image:
        return self.__board

    def get_draw(self) -> ImageDraw:
        return self.__draw

    @staticmethod
    def print_text(x, y, text, font_size, board):
        from Tools.Printer import Printer
        Printer.img_print_text(x=x, y=y, text=text, font_size=font_size, board=board)

    def print_map_on_board(self):
        self.__map.print_map(self.__board)
        return self

    def add_frame(self, frames: list):
        frames.append(self.get_board().copy())
        return self

    def print_add_safe(self, frames, name, path: str):
        self.print_map_on_board().add_frame(frames).safe_board(name, path)
        return self

    def print_safe(self, name, path: str):
        self.print_map_on_board().safe_board(name, path)
        return self

    @staticmethod
    def make_dir(path):
        import os
        path_parts = path.split('/')
        bread_crumbs = ''
        for part in path_parts:
            bread_crumbs += part + '/'
            if not os.path.isdir(bread_crumbs):
                os.mkdir(bread_crumbs)

    def safe_board(self, name, path: str):
        from Tools.Printer import Printer
        BoardGame.make_dir(path)
        Printer.save_board(self.__board, name, path)

    def make_gif(self, frames, speed, name, path):
        BoardGame.make_dir(path)
        frames[0].save(
            f'{path}/{name}.gif',
            save_all=True,
            append_images=frames[1:],
            optimize=True,
            duration=speed,
            loop=0
        )
        return self
