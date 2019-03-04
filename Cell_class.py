import random
import sys
import numpy as np


class Cell(object):
    def __init__(self, cell, name):
        self.name = name

        if cell == '.':
            cell = '0'

        try:
            self.type = 'clear'
            self.adj = [cell]
        except ValueError:
            self.type = {'*': 'mine', '?': 'unknown'}[cell]

    def is_mine(self):
        return self.type == 'mine'

    def is_unknown(self):
        return self.type == 'unknown'

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)




