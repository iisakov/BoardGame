import random
from math import sqrt

from Components import BoardGameGex
from Components.BoardGameSlot import BoardGameSlot


class BoardGameMap:
    def __init__(self, height: int, width: int, size: float = 1):
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
        if gex.get_direction() == 0:
            self.add_available_place((place_x-1, place_y-1, 1))
            self.add_available_place((place_x-1, place_y+1, 1))
            self.add_available_place((place_x+2, place_y, 1))
        else:
            self.add_available_place((place_x+1, place_y-1, 0))
            self.add_available_place((place_x+1, place_y+1, 0))
            self.add_available_place((place_x-2, place_y, 0))

    def add_available_place(self, place):
        if place not in self.__occupied_place:
            self.__available_place.add(place)

    def remove_available_place(self, place):
        self.__available_place.discard(place)

    def add_occupied_place(self, place):
        self.__occupied_place.add(place)

    def get_deployed_gex(self):
        return self.__deployed_gex

    def get_available_place(self):
        return list(self.__available_place)

    def get_random_available_place(self):
        return random.choice(self.get_available_place())

    class MapGenerator:
        pass
