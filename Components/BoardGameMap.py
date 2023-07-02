from math import sqrt

from Components.BoardGameSlot import BoardGameSlot


#TODO Добавить сетку гексов или соседей (Лучше всего сетку соседей)
class BoardGameMap:
    def __init__(self, height: int, width: int, size: float = 1):
        self.__slots = []
        for row_num in range(height):
            row = []
            for col_num in range(width):
                row.append(BoardGameSlot.create(col_num if row_num % 2 == 0 else (col_num+0.5),
                                                sqrt(3)/2*row_num, size))
            self.__slots.append(row)

    def get_slots(self):
        return self.__slots

    class MapGenerator:
        pass
