from math import sin, cos


class BoardGameVector:
    def __init__(self, x: float, y: float):
        self.__x = round(x, 4)
        self.__y = round(y, 4)

    @staticmethod
    def create(x, y):
        return VectorGenerator.gen(x, y)

    @staticmethod
    def create_polar(rho, theta):
        return VectorGenerator.gen(rho * sin(theta), rho * cos(theta))

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get(self):
        return self.__x, self.__y

    def set_x(self, x: float):
        self.__x = round(x, 4)

    def set_y(self, y: float):
        self.__y = round(y, 4)

    def __str__(self):
        return f'x = {self.__x}, y = {self.__y}'


class VectorGenerator:
    @staticmethod
    def gen(x, y):
        return BoardGameVector(x, y)
