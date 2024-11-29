"""
Xavier Gendron
404
tp4 4.3
"""

from dataclasses import dataclass
from random import randint
from enum import Enum


class Alignement(Enum):
    Lawful_good = 1
    Lawful_neutral = 2
    Lawful_evil = 3
    Neutral_good = 4
    Neutral = 5
    Neutral_evil = 6
    Chaotic_good = 7
    Chaotic_neutral = 8
    Chaotic_evil = 9


@dataclass
class NpcStats:
    def __init__(self):
        self.strength: int = randint(3, 18)
        self.dex: int = randint(3, 18)
        self.con: int = randint(3, 18)
        self.intelligence: int = randint(3, 18)
        self.wis: int = randint(3, 18)
        self.cha: int = randint(3, 18)


@dataclass
class Item:
    quantite: int
    name: str


class Inventory:
    def __init__(self):
        self.list_item = []
        self.name_item = Item.name
        self.quantite_item = Item.quantite

    def ajouter_item(self, item):
        """
        si item présent, additionner la quantité
        sinon si item pas présent, ajouter automatiqurement
        """
        self.list_item.index(self.name_item)
        if self.name_item in self.list_item:
            self.list_item.append(item)

        elif self.name_item not in self.list_item:
            self.list_item.append(item)

    def retirer_item(self, item):
        self.list_item.remove(item)

    def voir_contenu(self):
        print(self.list_item)


inv = Inventory()

inv.ajouter_item(Item(10, "Or"))
inv.ajouter_item(Item(10, "Or"))
print(inv.list_item)


class Npc:
    def __init__(self):
        self.npc_stats = NpcStats()
        self.hp = randint(1, 20)
        self.armure = randint(1, 12)
        self.name = ""
        self.race = ""
        self.species = ""
        self.profession = ""
        self.alignement = "Non defini"

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
              f" Charisme: {self.npc_stats.cha}"
              f" Alignement: {self.alignement}")

    def alive(self):
        if self.hp > 0:
            pass

        else:
            print("Vous etes mort")
            exit()

    def attaquer(self):
        degat_roll = 0


class Kobold(Npc):
    def __init__(self):
        super().__init__()

    def attaquer(self):
        degat_roll = randint(1, 6)

    def subir_dommage(self, degat):
        self.hp = self.hp - degat


class Hero(Npc, Inventory):

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
