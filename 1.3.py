"""
Xavier Gendron
404
tp4 1.2
"""

from dataclasses import dataclass
from math import pi


@dataclass
class Cercle:
    def __init__(self):
        rayon = int(input("Rayon:"))
        self.clacul_aire = pi * rayon**2
        self.clacul_circonference = 2 * pi * rayon
        print(f"circonference: {self.clacul_circonference}\nAire: {self.clacul_aire}")


Cercle()
