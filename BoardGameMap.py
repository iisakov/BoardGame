from BoardGameDeck import BoardGameDeck
from random import randint

#TODO Добавить сетку гексов или соседей (Лучше всего сетку соседей)
class BoardGameMap:
    map = []
    count_fields = {}

    def __init__(self, sample, num_tile):
        self.map = []
        self.count_fields = {}
        self.init_start_map(sample, num_tile)

    def init_start_map(self, deck: BoardGameDeck, num_tile):
        # Выбираем стартовые тайлы
        while len(self.map) < num_tile:
            rand_i = randint(0, deck.get_num_gex() - 1)
            gex = deck.get_deck()[rand_i]
            if gex not in self.map:
                self.map.append(gex)

        for gex in self.map:
            for field in gex.get_fields():
                self.count_fields[field.get_type()] = self.count_fields.setdefault(field.get_type(), 0) + 1

    def get_map(self):
        return self.map

    def get_stat(self):
        return self.count_fields