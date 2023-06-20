from BoardGameField import BoardGameField

class BoardGameGex:
    __fields = []

    def __init__(self, fields: list[BoardGameField]):
        self.fields = fields
        pass

    def get_gex(self):
        # /1/\
        # \3\2
        one, two, tree = self.fields
        return [f' /{one.get_type()}/\\', f' \\{tree.get_type()}\\{two.get_type()}']

    def get_fields(self):
        return self.fields
