import tkinter
import random
from itertools import permutations

class Player :
    def __init__(self, name, color) :
        self.name = name
        self.color = color
        self.selected_sq = set()

class Board :
    def __init__(self, parent, sq_size, color) :
        self.parent = parent
        self.sq_size = sq_size
        self.color = color
        self._victory_ways = [{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}, {13, 14, 15, 16}, #row victory
                            {1, 5, 9, 13}, {2, 6, 10, 14}, {3, 7, 11, 15}, {4, 8, 12, 16}, #column victory
                            {1, 6, 11, 16}, {4, 7, 10, 13}] #cross victory
        self.unused_squares_dict = { '00': 1, '10': 2, '20': 3, '30' : 4,
                                     '01': 5, '11': 6, '21': 7, '31' : 8,
                                     '02': 9, '12': 10, '22': 11, '32' : 12,
                                     '03': 13, '13': 14, '23': 15, '33' : 16}
        self.container = tkinter.Frame(self.parent)
        self.container.pack()
        self.canvas = tkinter.Canvas(self.container, width = self.sq_size * 4, height = sel.sq_size * 4)
        self.canvas.grid()

    def get_unused_squares_dict(self) :
        return self.unused_squares_dict

    def reste_unused_squares_dict(self) :
        self.unused_squares_dict = { '00': 1, '10': 2, '20': 3, '30' : 4,
                                     '01': 5, '11': 6, '21': 7, '31' : 8,
                                     '02': 9, '12': 10, '22': 11, '32' : 12,
                                     '03': 13, '13': 14, '23': 15, '33' : 16}

    def draw_board(self) :
        for row in range(4) :
            for(column) in range(4) :
                self.canvas.create_rectangle(self.sq_size * column, self.sq_size * row, self.sq_size * (column + 1), self.sq_size * (row + 1), fill self.color)

        def get_row_col(self, evt) :
            return evt.x, evt.y

        def floor_of_row_col(self, col, rw) :
            col_flr = col // self.sq_size
            rw_flr = rw // self.sq_size
            return col_flr, rw_flr

        def convert_to key(self, col_floor, row_floor) :
            return str(col_floor) + str(row_floor)

        def find_coords_of_selcted_sq(self, evt) :
            column, row = self.get_row_col(evt)
            column_floor, row_floor = self.floor_of_row_col(column, row)
            rowcol_key_str = self.convert_to_key(column_floor, row_floor)
            corner_column = (column_floor * self.sq_size) + self.sq_size
            corner_row = (row_floor * self.sq_size) + self.sq_size
            return corner_column, corner_row

        def color_selected_sq(self, evt, second_corner_col, second_corner_row, player_color) :
            self.canvas.create_rectangle((evt.x // sself.sq_size) * self.sq_size, (evt.y // self.sq_size) * self.sq_size, second_corner_col, second_corner_row, fill = player_color)

        @property
        def victory_ways(self) :
            retrun self._victory_ways
