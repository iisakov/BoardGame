from Components import BoardGameField, BoardGameGex
from random import shuffle, randint


class BoardGameDeck:
    def __init__(self, num_field, examples_field: list[dict], size: float):
        self.__size = size
        self.__num_field = num_field
        self.__num_type = len(examples_field)
        self.__examples_field = examples_field
        self.__deck: list[BoardGameGex] = []

    def create(self):
        import itertools

        for raw_fields in itertools.product(self.__examples_field, repeat=self.__num_field):
            gex = BoardGameGex.BoardGameGex(x=0, y=0, fields_type=raw_fields, size=self.__size)
            gex.set_status('in deck')
            self.__deck.append(gex)

        shuffle(self.__deck)

    def get_deck(self):
        return self.__deck

    def __str__(self):
        for i in self.__deck:
            print(f"({', '.join([j.get_type() for j in i.get_fields()])})")
        return ''

    def pull_gex(self):
        gex = self.__deck.pop()
        gex.set_status('pulled')
        # print(f'Карт в колоде: {len(self.__deck)}')
        return gex

    def push_gex(self, gex):
        self.__deck.append(gex)
        gex.set_status('in deck')
        shuffle(self.__deck)
        # print(f'Карт в колоде: {len(self.__deck)}')

class DeckGenerator:
    pass