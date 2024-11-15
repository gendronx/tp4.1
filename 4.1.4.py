"""
Xavier Gendron
404
tp4 1.2
"""

from dataclasses import dataclass
from random import randint


@dataclass
class Hero:
    def __init__(self, name):
        self.hp = randint(1, 10) + randint(1, 10)
        self.force = randint(1, 6)
        self.defense = randint(1, 6)
        self.name = name
        self.playerstats = 0

    def attaquer(self):
        return self.force + randint(1, 6)

    def dommage(self, attaquer):
        self.hp -= self.attaquer() - self.defense

    def vivant(self):
        if self.hp > 0:
            return True
        else:
            return False

    def playerstats(self):
        self.strength: int
        self.dex: int
        self.con: int
        self.intelligence: int
        self.wis: int
        self.cha: int

        self.playerstats = (randint(1, 20),
                            randint(1, 20),
                            randint(1, 20),
                            randint(1, 20),
                            randint(1, 20),
                            randint(1, 20))
