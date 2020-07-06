class PlanetMap():
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def get_width(self):
        return self.width
    def get_height(self):
        return self.height
    def get_max_y(self):
        return self.get_height() - 1
    def get_max_x(self):
        return self.get_width() - 1
    