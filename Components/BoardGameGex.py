from Components import BoardGameField, BoardGameVector


class BoardGameGex:

    def __init__(self, fields: list[BoardGameField], size=50):
        self.__step_angle = 0
        self.__center = 0
        self.__size = size
        self.__fields = fields
        self.__is_put = False
        self.__siblings = set()
        self.__coordinates = [BoardGameVector(0, 0)]

    def get_info(self):
        return f'{len(self.get_siblings())} {self.get_siblings() = }' \
               f'\n{self.get_center() = }' \
               f'\n{len(self.get_fields())} {self.get_fields() = }' \
               f'\n{self.is_putted() = }\n'


    def get_gex(self):
        # /1/\
        # \3\2
        one, two, tree = self.__fields
        return [f' /{one.get_type()}/\\', f' \\{tree.get_type()}\\{two.get_type()}']

    def get_fields(self):
        return self.__fields

    def get_center(self):
        return self.__center

    def get_siblings(self):
        return self.__siblings

    def get_size(self):
        return self.__size

    def get_step_angel(self):
        return self.__step_angle

    def is_putted(self):
        return self.__is_put

    def set_fields(self, fields: list[BoardGameField]):
        self.__fields = fields

    def set_center(self, center: tuple):
        self.__center = center

    def set_step_angel(self, step: int):
       self.__step_angle = step

    def add_siblings(self, sibling_gex):
        self.__siblings.add(sibling_gex)

    def put(self):
        self.__is_put = True

    def remove(self):
        self.__is_put = False


class GexGenerator:
    pass