from math import sqrt

from Components.BoardGameSlot import BoardGameSlot


#TODO Добавить сетку гексов или соседей (Лучше всего сетку соседей)
class BoardGameMap:
    def __init__(self, height: int, width: int, size: float = 1):
        self.__slots = []
        for r in range(height):
            row = []
            for c in range(width):
                row.append(BoardGameSlot.create(c if r % 2 == 0 else (c+0.5),
                                                sqrt(3)/2*r, size))
            self.__slots.append(row)

    def get_slots(self):
        return self.__slots

    class MapGenerator:
        pass
