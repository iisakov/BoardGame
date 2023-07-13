import random
from math import sqrt

from Components import BoardGameGex
from Components.BoardGameSlot import BoardGameSlot


class BoardGameMap:
    def __init__(self):
        self.__slots = []
        self.__deployed_gex = set()
        self.__available_place = set()
        self.__occupied_place = set()

    def get_slots(self):
        return self.__slots

    def deploy_gex(self, gex: BoardGameGex):
        self.__deployed_gex.add(gex)
        place_x, place_y = gex.get_place()
        current_place = (place_x, place_y, gex.get_direction())
        self.add_occupied_place(current_place)
        self.remove_available_place(current_place)
        field_type = {x.get_direction(): x.get_type() for x in gex.get_fields()}
        if gex.get_direction() == 0:
            self.add_available_place((place_x-1, place_y-1, 1, field_type[2], 2, gex))
            self.add_available_place((place_x-1, place_y+1, 1, field_type[1], 1, gex))
            self.add_available_place((place_x+2, place_y, 1, field_type[0], 0, gex))
        else:
            self.add_available_place((place_x+1, place_y-1, 0, field_type[1], 1, gex))
            self.add_available_place((place_x+1, place_y+1, 0, field_type[2], 2, gex))
            self.add_available_place((place_x-2, place_y, 0, field_type[0], 0, gex))

    def add_available_place(self, place):
        if place not in self.__occupied_place:
            self.__available_place.add(place)

    def remove_available_place(self, place):
        self.__available_place.discard(place)

    def add_occupied_place(self, place):
        self.__occupied_place.add(place)

    def get_occupied_place(self):
        return list(self.__occupied_place)

    def get_deployed_gex(self) -> {tuple:BoardGameGex}:
        return {(*gex.get_place(), int(gex.get_direction())): gex for gex in self.__deployed_gex}

    def get_deployed_gex_by_place(self, place: tuple):
        gexes = {(*gex.get_place(), int(gex.get_direction())): gex for gex in self.__deployed_gex}
        if place in gexes:
            return gexes[place]
        else: False

    def get_available_place(self):
        result = list(self.__available_place)
        random.shuffle(result)
        return result

    def get_random_available_place(self):
        return random.choice(self.get_available_place())

    def get_statistics(self):
        result = {}
        for gex in self.get_deployed_gex().values():
            for field in gex.get_fields():
                f_type = field.get_type()
                result[f_type] = result.setdefault(f_type, 0) + 1
        return result

    class MapGenerator:
        pass
