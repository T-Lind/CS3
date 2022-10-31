class Player:
    def __init__(self, r, c):
        self.r = r
        self.c = c

    def pos(self):
        pos: tuple = (self.r, self.c)
        return pos
