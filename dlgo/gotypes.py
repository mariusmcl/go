import enum

class Player(enum.Enum):  # Lett måte å holde styr på hvilket tall det er som spiller og som er player
    black = 1
    white = 2

    @property
    def other(self):
        print(self)
        return Player.black if self == Player.white else Player.white  # Fin logikk for hvem som er neste spiller


from collections import namedtuple

class Point(namedtuple('Point', ['row', 'col'])):
    def neighbors(self):
        return [
            Point(self.row - 1, self.col),
            Point(self.row + 1, self.col),
            Point(self.row, self.col - 1),
            Point(self.row, self.col + 1)
        ]

q = Player(1)
z = q.other
x = z.other
p = Player(2)
z=2