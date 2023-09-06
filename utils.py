class Coordinate:
    X: int
    Y: int

    def __init__(self, x, y):
        self.X, self.Y = x, y

    def tuple(self):
        return self.X, self.Y
