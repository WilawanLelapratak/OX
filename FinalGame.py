import tkinter
import random
from itertools import permutations

class Player :
    def __init__(self, name, color) :
        self.name = name
        self.color = color
        self.selected_sq = set()
