"""
Xavier Gendron
404
tp4 2.3
"""

from dataclasses import dataclass
from random import randint


@dataclass
class Npc:
    def __init__(self):
        self.hp = randint(1, 20)
        self.strength = randint(3, 18)
        self.dex = randint(3, 18)
        self.con = randint(3, 18)
        self.intelligence = randint(3, 18)
        self.wis = randint(3, 18)
        self.cha = randint(3, 18)
        self.armure = randint(1, 12)
        self.name = ""
        self.race = ""
        self.species = ""
        self.profession = ""

    def affichernpc(self):
        print(f"Nom: {n.name}"
              f" Race: {n.race}"
              f" Espece: {n.species}"
              f" Profession: {n.profession}"
              f" Points de vie {n.hp}"
              f" Armure: {n.armure}"
              f" Force: {n.strength}"
              f" Agilite: {n.dex}"
              f" Constitution: {n.con}"
              f" Intelligence: {n.intelligence}"
              f" Sagesse: {n.wis}"
              f" Charisme: {n.cha}")

    class Kobold:
        def attaquer(self, target):
            degat = randint(1, 6)

        def subirdammage(self):
            randint(1, 6)


n = Npc()
print(n.affichernpc())
