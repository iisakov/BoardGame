from math import sqrt
from random import randint

from Components import BoardGameDeck
from Components import BoardGameVector


#TODO Добавить сетку гексов или соседей (Лучше всего сетку соседей)
class BoardGameMap:
    def __init__(self, size: tuple[int]):
        height = size[0]
        width = size[1]
        self.__slots = []
        for r in range(height):
            row = []
            for c in range(width):
                row.append(BoardGameVector.create(c if r % 2 == 0 else c+0.5, sqrt(3)/2*r))
            self.__slots.append(row)

    def get_slots(self):
        return self.__slots

    class MapGenerator:
        pass
