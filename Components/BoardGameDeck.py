from Components import BoardGameField, BoardGameGex
from random import shuffle, randint


class BoardGameDeck:
    def __init__(self, num_field, examples_field: list[dict], size: float):
        self.__size = size
        self.__num_field = num_field
        self.__num_type = len(examples_field)
        self.__examples_field = examples_field
        self.__deck = []

    def create(self):
        import itertools

        for raw_fields in itertools.product(self.__examples_field, repeat=self.__num_field):
            self.__deck.append(BoardGameGex(x=randint(1, 17), y=randint(1, 8), fields_type=raw_fields, size=self.__size))

        shuffle(self.__deck)

    def get_deck(self):
        return self.__deck

    def __str__(self):
        for i in self.__deck:
            print(f"({', '.join([j.get_type() for j in i.get_fields()])})")
        return ''

    def pull_gex(self):
        gex = self.__deck.pop()
        print(f'Карт в колоде: {len(self.__deck)}')
        return gex