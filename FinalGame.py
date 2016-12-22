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
        self.canvas = tkinter.Canvas(self.container, width = self.sq_size * 4, height = self.sq_size * 4)
        self.canvas.grid()

    def get_unused_squares_dict(self) :
        return self.unused_squares_dict

    def reset_unused_squares_dict(self) :
        self.unused_squares_dict = { '00': 1, '10': 2, '20': 3, '30' : 4,
                                     '01': 5, '11': 6, '21': 7, '31' : 8,
                                     '02': 9, '12': 10, '22': 11, '32' : 12,
                                     '03': 13, '13': 14, '23': 15, '33' : 16}

    def draw_board(self) :
        for row in range(4) :
            for(column) in range(4) :
                self.canvas.create_rectangle(self.sq_size * column, self.sq_size * row, self.sq_size * (column + 1), self.sq_size * (row + 1), fill = self.color)

    def get_row_col(self, evt) :
        return evt.x, evt.y

    def floor_of_row_col(self, col, rw) :
        col_flr = col // self.sq_size
        rw_flr = rw // self.sq_size
        return col_flr, rw_flr

    def convert_to_key(self, col_floor, row_floor) :
        return str(col_floor) + str(row_floor)

    def find_coords_of_selected_sq(self, evt):
        column, row = self.get_row_col(evt)
        column_floor, row_floor = self.floor_of_row_col(column, row)
        rowcol_key_str = self.convert_to_key(column_floor, row_floor)
        corner_column = (column_floor * self.sq_size) + self.sq_size
        corner_row =  (row_floor  * self.sq_size) + self.sq_size
        return corner_column, corner_row

    def color_selected_sq(self, evt, second_corner_col, second_corner_row, player_color) :
        self.canvas.create_rectangle(
            (evt.x // self.sq_size) * self.sq_size,
            (evt.y // self.sq_size) * self.sq_size,
            second_corner_col,
            second_corner_row,
            fill = player_color)

    @property
    def victory_ways(self) :
        return self._victory_ways

class GamePlay(object) :
    def __init__(self, parent) :
        self.parent = parent
        self.board = Board(self.parent, 100, "#ECECEC")
        self.board.draw_board()
        self.unused_squares_dict = self.board.get_unused_squares_dict()
        self.player1 = Player("Player 1", "#1DE9B6")
        self.player2 = Player("Player 2", "#FFA726")
        self.initialize_buttons()
        self.show_menu()

    def initialize_buttons(self) :
        self.two_players_button = tkinter.Button(self.board.container, text = "TWO PLAYERS", width = 25, command = self.init_two_players_game)
        self.restart_button  = tkinter.Button(self.board.container, text = "RESTART", width = 25, command = self.restart)

    def show_menu(self) :
        self.two_players_button.grid()

    def init_two_players_game(self) :
        self.board.reset_unused_squares_dict()
        self.player1.selected_sq = set()
        self.player2.selected_sq = set()
        self.player1_turn = True
        self.restart_button.grid()
        self.board.canvas.bind("<Button-1>", self.play)

    def restart(self) :
        self.board.container.destroy()
        self.board = Board(self.parent, 100, "#ECECEC")
        self.board.draw_board()
        self.initialize_buttons()
        self.show_menu()

    def add_to_player_sq(self, key, player_sq) :
        current_selected_sq = self.board.unused_squares_dict[key]
        player_sq.add(current_selected_sq)

    def delete_used_sq(self, key) :
        del self.board.unused_squares_dict[key]

    def play(self, event) :
        colrow_tuple = self.board.find_coords_of_selected_sq(event)
        corner_two_col, corner_two_row = colrow_tuple[0], colrow_tuple[1]
        col_fl, row_fl = self.board.floor_of_row_col(event.x, event.y)
        rowcol_key = self.board.convert_to_key(col_fl, row_fl)

        try :
            self.unused_squares_dict[rowcol_key]
        except KeyError :
            return

        if self.player1_turn == True :
            self.add_to_player_sq(rowcol_key, self.player1.selected_sq)
            self.delete_used_sq(rowcol_key)
            self.board.color_selected_sq(event, corner_two_col, corner_two_row, self.player1.color)
            self.check_for_winner(self.player1.selected_sq, self.player1.name)
            self.player1_turn = False

        else :
            self.board.color_selected_sq(event, corner_two_col, corner_two_row, self.player2.color)
            self.add_to_player_sq(rowcol_key, self.player2.selected_sq)
            self.delete_used_sq(rowcol_key)
            self.check_for_winner(self.player2.selected_sq, self.player2.name)
            self.player1_turn = True

    def check_for_winner(self, player_sq, player_name) :
        if len(self.board.unused_squares_dict) > 0 :
            if len(player_sq) > 2 :
                for combo in permutations(player_sq, 4) :
                    for wc in self.board.victory_ways :
                        if set(combo) == wc :
                            self.show_game_result(player_name + " WIN!")
                            self.restart

        if len(self.board.unused_squares_dict) == 0 :
            self.show_game_result("Game Tie!")
            self.restart

    def show_game_result(self, txt) :
        result_label = tkinter.Label(self.board.container, text = txt, width = 32, height = 10, foreground = "white", background = "black", borderwidth = 3)
        result_label.grid(row = 0, column = 0)
        self.board.canvas.unbind("<Button-1>", self.play)

def main() :
    root = tkinter.Tk()
    root.title("OX Special 4x4")
    ox_game = GamePlay(root)
    root.mainloop()

if __name__ == '__main__' :
    main()
