from Components.BoardGameVector import BoardGameVector


class VectorGenerator:
    @staticmethod
    def gen(coordinates: list[tuple] or tuple, quantity: int = None):
        if type(coordinates) is tuple:
            quantity = 1 if quantity is None else quantity
            coordinates = [coordinates]
        else:
            quantity = len(coordinates)

        coordinates = coordinates*quantity if len(coordinates) == 1 and quantity != 1 else coordinates

        return [BoardGameVector(*x_y) for x_y in coordinates]
