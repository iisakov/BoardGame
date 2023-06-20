class BoardGameField:

    def __init__(self, f_type: str = 'default', color: str = 'red'):
        self.__f_type = f_type
        self.__color = color
        self.__siblings = []

    def get_type(self):
        return self.__f_type

    def get_color(self):
        return self.__color

    def get_siblings(self):
        return self.__siblings
