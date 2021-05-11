class Road:
    WEIGHT = 25

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def weight(self, depth):
        return depth * self.WEIGHT * self._width * self._length


road = Road(1500, 20)
print(road.weight(5))
print(road._length)
print(road._width)