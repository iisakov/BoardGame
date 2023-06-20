class BoardGameField:
    f_type = 'default'
    color = 'red'

    def __init__(self, f_type: str, color: str):
        self.f_type = f_type
        self.color = color

    def get_type(self):
        return self.f_type

    def get_color(self):
        return self.color
