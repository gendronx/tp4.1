"""
Xavier Gendron
404
tp4 4.3
"""

from dataclasses import dataclass
from random import randint
from enum import Enum


class Alignement(Enum):
    Lawful_good = 0
    Lawful_neutral = 1
    Lawful_evil = 2
    Neutral_good = 3
    Neutral = 4
    Neutral_evil = 5
    Chaotic_good = 6
    Chaotic_neutral = 7
    Chaotic_evil = 8
    Non_defini = 9


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
    name: str
    quantite: int


class Inventory:
    def __init__(self):
        self.list_item = []

    def ajouter_item(self, new_item):
        """
        si item présent, additionner la quantité
        sinon si item pas présent, ajouter automatiqurement
        """
        if len(self.list_item) > 0:
            for item in self.list_item:
                if item.name == new_item.name:
                    item.quantite += new_item.quantite
                    return

            if item.name != new_item.name:
                self.list_item.append(new_item)
        else:
            self.list_item.append(new_item)

    def retirer_item(self, delete_item):
        if len(self.list_item) == 0:
            print("Il n'y a rien dans l'inventaire")
        else:
            for item in self.list_item:
                if item.name == delete_item.name:
                    item.quantite -= delete_item.quantite
                    if item.quantite > 0:
                        return

                    else:
                        print("Vous n'avez pas autant d'item dans votre inventaire")

                    if item.name != delete_item.name:
                        print(f"{delete_item} n'est pas dans l'inventaire")


    def voir_contenu(self):
        print("Inventaire: ")
        print(self.list_item)


inv = Inventory()

inv.ajouter_item(Item("Or", 10))
inv.ajouter_item(Item("Or", 10))
inv.ajouter_item(Item("Argent", 10))
inv.ajouter_item(Item("Argent", 100))
print(inv.list_item)
inv.retirer_item(Item("Or", 100))
inv.voir_contenu()


class Npc:
    def __init__(self):
        self.npc_stats = NpcStats()
        self.hp = randint(1, 20)
        self.armure = randint(1, 12)
        self.name = ""
        self.race = ""
        self.species = ""
        self.profession = ""
        self.alignement = ""

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
