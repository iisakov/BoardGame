from Components.BoardGameGex import BoardGameGex
from Components.BoardGameMap import BoardGameMap
from Components.BoardGamePlayer import BoardGamePlayer
from Components.BoardGameDeck import BoardGameDeck

from PIL import Image, ImageDraw
from math import sqrt


class BoardGame:
    __examples = [{"type": 'shop', "color": (100, 100, 200)},
                  {"type": 'house', "color": (200, 100, 100)},
                  {"type": 'warehouse', "color": (100, 100, 100)},
                  {"type": 'park', "color": (100, 200, 100)}]

    def __init__(self, num_players, num_gex_in_hand, size):
        self.__count_slots = 24
        self.__num_players = num_players
        self.__num_gex_in_hand = num_gex_in_hand
        self.__players = [BoardGamePlayer(f'Playr_{num}', num_gex_in_hand) for num in range(1, num_players+1)]
        self.__deck = BoardGameDeck.create(3, self.__examples, size)
        self.__discard = BoardGameDeck(3, self.__examples, size)
        self.__map = BoardGameMap()
        self.__board = Image.new('RGB',
                                 (size*self.__count_slots, int(size*self.__count_slots * sqrt(3) / 2)),
                                 (0, 0, 0))
        self.__draw = ImageDraw.Draw(self.__board)

    def __str__(self):
        return f'Количество игроков: {self.__num_players}' \
               f'\nДоступное количество карт на руках: {self.__num_gex_in_hand}' \
               f'\nКарт в колоде: {self.__deck.get_num_gex_in_deck()}' \
               f'\nКарт в сбросе: {self.__discard.get_num_gex_in_deck()}' \
               f'\nКарт на поле: {self.__map.get_num_deployed_gex()}'
    def start(self):
        self.__deck.pull_gex().rotate(0).deploy(self.__map, self.__count_slots, self.__count_slots/2)
        self.__deck.pull_gex().rotate(0).deploy(self.__map, self.__count_slots-3, self.__count_slots/2+1)
        self.__deck.pull_gex().rotate(0).deploy(self.__map, self.__count_slots-3, self.__count_slots/2-1)
        self.__deck.pull_gex().rotate(0).deploy(self.__map, self.__count_slots, self.__count_slots/2-2)
        self.__deck.pull_gex().rotate(0).deploy(self.__map, self.__count_slots+3, self.__count_slots/2-1)
        self.__deck.pull_gex().rotate(0).deploy(self.__map, self.__count_slots+3, self.__count_slots/2+1)
        self.__deck.pull_gex().rotate(0).deploy(self.__map, self.__count_slots, self.__count_slots/2+2)

        if self.__deck.get_num_gex_in_deck() - (self.__num_players*self.__num_gex_in_hand*7) < 0:
            for _ in range(self.__deck.get_num_gex_in_deck() % (self.__num_players * self.__num_gex_in_hand)):
                self.__discard.push_gex(self.__deck.pull_gex())
        else:
            for _ in range(self.__deck.get_num_gex_in_deck() - (self.__num_players*self.__num_gex_in_hand*7)):
                self.__discard.push_gex(self.__deck.pull_gex())

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

    def get_discard(self) -> BoardGameDeck:
        return self.__discard

    def get_map(self) -> BoardGameMap:
        return self.__map

    def get_board(self) -> Image:
        return self.__board

    def get_draw(self) -> ImageDraw:
        return self.__draw
