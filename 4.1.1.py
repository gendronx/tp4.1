"""
Xavier Gendron
404
tp4 1.1
"""

from dataclasses import dataclass


@dataclass
class StringFoo:
    def __init__(self):
        self.message = ""

    def set_string(self, msg):
        self.message = msg

    def print_string(self):
        print(self.message.upper())


s = StringFoo()
s.set_string("Je suis un message hyper important.")
s.print_string()

