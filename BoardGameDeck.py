from BoardGameGex import BoardGameGex
from BoardGameField import BoardGameField


class BoardGameDeck:
    deck = []
    n_type = 0
    m_field = 0
    patt = None
    field_desc = {}
    num_gex = 0
    number_tile_with_current_field = 0

    def __init__(self, n, m, patt=None, field_desc=None):
        self.n_type = n
        self.m_field = m
        self.patt = ''.join([str(x) for x in range(n)]) if patt is None else patt
        self.field_desc = field_desc
        self.render_deck()

    def render_deck(self):
        import itertools

        for tile_num, tile_value in enumerate(itertools.product(self.patt, repeat=self.m_field)):
            field_list = []
            for field in tile_value:
                field_list.append(BoardGameField(field, self.field_desc[field]))
            self.deck.append(BoardGameGex(field_list), )
            self.num_gex += 1
            if self.patt[0] in tile_value:
                self.number_tile_with_current_field += 1

    def get_deck(self):
        return self.deck

    def get_num_gex(self):
        return self.num_gex
