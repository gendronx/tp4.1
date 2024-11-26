"""
Xavier Gendron
404
tp4 2.3
"""

from dataclasses import dataclass
from random import randint


@dataclass
class NpcStats:
    def __init__(self):
        self.strength: int = randint(3, 18)
        self.dex: int = randint(3, 18)
        self.con: int = randint(3, 18)
        self.intelligence: int = randint(3, 18)
        self.wis: int = randint(3, 18)
        self.cha: int = randint(3, 18)


class Npc:
    def __init__(self):
        self.npc_stats = NpcStats()
        self.hp = randint(1, 20)
        self.armure = randint(1, 12)
        self.name = ""
        self.race = ""
        self.species = ""
        self.profession = ""

    def afficher_npc(self):
        print(f"Nom: {self.name}"
              f" Race: {self.race}"
              f" Espece: {self.species}"
              f" Profession: {self.profession}"
              f" Points de vie {self.hp}"
              f" Armure: {self.armure}"
              f" Force: {self.npc_stats.strength}"
              f" Agilite: {self.npc_stats.dex}"
              f" Constitution: {self.npc_stats.con}"
              f" Intelligence: {self.npc_stats.intelligence}"
              f" Sagesse: {self.npc_stats.wis}"
              f" Charisme: {self.npc_stats.cha}")


class Kobold(Npc):
    def __init__(self):
        super().__init__()

    def attaquer(self):
        degat_roll = randint(1, 6)

    def subir_dommage(self, degat):
        self.hp = self.hp - degat


class Hero(Npc):

    def __init__(self):
        super().__init__()

    def attaquer(self):
        degat_roll = randint(1, 20)
        if degat_roll == 20:
            degat = randint(1, 8)

        elif degat_roll == 1:
            degat = 0

        else:
            if degat_roll >= k.armure:
                degat = randint(1, 6)

            else:
                degat = 0

    def subir_dommage(self, degat):
        self.hp = self.hp - degat


k = Kobold()
