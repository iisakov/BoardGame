from random import randint, sample
from Components.BoardGameGex import BoardGameGex


class BoardGamePlayer:
    def __init__(self, player_name, num_gex_in_hand):
        self.__name = player_name
        self.__available_num_gex_in_hand = num_gex_in_hand
        self.__num_gex_in_hand = 0
        self.__hand = set()
        self.__active_gex = None

    def take_gex_in_hand(self, gex: BoardGameGex):
        if self.__num_gex_in_hand < self.__available_num_gex_in_hand:
            if self.__active_gex is None:
                self.__active_gex = gex
                self.__num_gex_in_hand += 1
            else:
                self.__hand.add(gex)
                self.__num_gex_in_hand += 1
                gex.set_status('in hand')
            return self
        else:
            print('gex not take - is', 'hand overflowing.')
            return False

    def pull_random_gex_from_hand(self) -> BoardGameGex or None:
        if len(self.__hand) > 0:
            return self.__hand.pop()
        else:
            return None

    def set_active_gex(self, gex: BoardGameGex):
        self.__active_gex = gex

    def get_active_gex(self) -> BoardGameGex:
        return self.__active_gex

    def get_name(self):
        return self.__name

    def get_num_gex_in_hand(self):
        return self.__num_gex_in_hand

    def chang_active_gex(self):
        if len(self.__hand) > 0:
            if self.__active_gex is None:
                self.__active_gex = self.pull_random_gex_from_hand()
            else:
                current_active_gex = self.__active_gex
                self.__active_gex = self.pull_random_gex_from_hand()
                self.__hand.add(current_active_gex)
        else:
            return False

    def deploy_gex(self, bg_map):
        deployed = False
        for i, place in enumerate(bg_map.get_available_place()):
            if i == 0:
                self.__active_gex.rotate(place[2] * 60)

            if self.__active_gex.get_direction() == 0:
                possible_places = [{'x': place[0] - 1, 'y': place[1] - 1, 'gex_direction': 1, 'field_direction': 2},
                                   {'x': place[0] - 1, 'y': place[1] + 1, 'gex_direction': 1, 'field_direction': 1},
                                   {'x': place[0] + 2, 'y': place[1], 'gex_direction': 1, 'field_direction': 0}]
            else:
                possible_places = [{'x': place[0] + 1, 'y': place[1] - 1, 'gex_direction': 0, 'field_direction': 1},
                                   {'x': place[0] + 1, 'y': place[1] + 1, 'gex_direction': 0, 'field_direction': 2},
                                   {'x': place[0] - 2, 'y': place[1], 'gex_direction': 0, 'field_direction': 0}]
            fields = [bg_map.get_deployed_gex_by_place((place['x'], place['y'], place['gex_direction'])).get_field_by_direction(place['field_direction']) for place in possible_places if bg_map.get_deployed_gex_by_place((place['x'], place['y'], place['gex_direction']))]

            if self.__active_gex.get_field_by_direction(place[4]).get_type() == place[3] and (place[0], place[1]) not in [(opl[0], opl[1]) for opl in bg_map.get_occupied_place()] and self.__active_gex.get_direction() == place[2] and len(fields) < 3:
                for field in fields:
                    field.set_type('COVERED', (10, 10, 10))
                self.__active_gex.deploy(bg_map, place[0], place[1])
                deployed = True
                self.__num_gex_in_hand -= 1
                self.set_active_gex(self.pull_random_gex_from_hand())
                break
            else:
                self.__active_gex.rotate(60)
            if not deployed:
                self.chang_active_gex()

    def __str__(self):
        return f'{"-"*100}' \
               f'\nname: {self.__name}' \
               f'\nhand (count {self.__num_gex_in_hand},{len(self.__hand)}): {self.__hand}' \
               f'\nactive_gex: {self.__active_gex}'

