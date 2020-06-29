class PlanetMap():
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def get_width(self):
        return self.width
    def get_height(self):
        return self.height

    def is_edge(self, x, y):
        return x == self.width-1