import math
from random import randint

from Components import BoardGameDeck


#TODO Добавить сетку гексов или соседей (Лучше всего сетку соседей)
class BoardGameMap:
    def __init__(self, sample, num_tile):
        self.__map = []
        self.count_fields = {}
        self.init_start_map(sample, num_tile)

    def init_start_map(self, deck: BoardGameDeck, num_tile):
        # Выбираем и выкладываем стартовые тайлы
        while len(self.__map) < num_tile:
            rand_i = randint(0, deck.get_num_gex() - 1)
            gex = deck.get_deck()[rand_i]
            if gex not in self.__map:
                self.__map.append(gex)
                # Выдаём центр первому(центральному) гексу
                gex.set_center((0, 0))
                if len(self.__map) > 1:
                    # Задружили текущий гекс с центральным
                    self.__map[0].add_siblings(gex)
                    gex.add_siblings(self.__map[0])

                    # Задружили текущий гекс с предыдущим (возможно и с центральным)
                    self.__map[-1].add_siblings(gex)
                    gex.add_siblings(self.__map[-1])

                    # Выдаём центр текущему гексу:
                    angle_degree = 60 * len(self.__map) + 30
                    angle_radian = math.pi / 180 * angle_degree

                    gex.set_center((round(gex.get_size() * math.cos(angle_radian), 4),
                                    round(gex.get_size() * math.sin(angle_radian), 4)))

        for gex in self.__map:
            for field in gex.get_fields():
                self.count_fields[field.get_type()] = self.count_fields.setdefault(field.get_type(), 0) + 1

    def get_map(self):
        return self.__map

    def get_stat(self):
        return self.count_fields