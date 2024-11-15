"""
Xavier Gendron
404
tp4 1.2
"""

from dataclasses import dataclass


@dataclass
class Rectangle:
    def __init__(self):
        longueur = int(input("Longueur: "))
        largeur = int(input("Largeru: "))
        self.clacul_aire = longueur * largeur
        print(f"longueur: {longueur}\nlargeur: {largeur}\nAire: {self.clacul_aire}")


Rectangle()
