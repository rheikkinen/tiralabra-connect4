from random import randint
from time import time

class AI:
    def __init__(self, game, level=1, player=2):
        self.level = level
        self.player = player
        self.last_row = None
        self.last_col = None
        self.game = game

    def player(self):
        return self.player

    def store_last_move(self, row, column):
        self.last_row = row
        self.last_col = column

    def get_available_columns(self, board):
        valid_columns = []
        for column in range (0, 7):
            if self.game.column_is_available(board, column):
                valid_columns.append(column)
        return valid_columns

    def get_next_available_row(self, board, column):
        for row in range(0, 6):
            if board[row][column] == 0:
                return row

    def best_column(self, game_board):
        if self.level == 0:
            # Palauttaa satunnaisen sarakkeen väliltä [0, sarakkeiden_lkm]
            column = randint(0,6)

        if self.level == 1:
            start_time = time()
            value, column = self.minimax(game_board, self.last_row, self.last_col, depth=4, maximizing=False)
            print(f"Minimax valitsi sarakkeen {column+1} pisteytyksellä {value}")
            end_time = time()
            print(f"Minimax-algoritmin suoritusaika: {end_time - start_time} sekuntia")
        return column

    def minimax(self, board, last_row, last_col, depth, maximizing: bool):
        last_player = 2 if maximizing else 1
        end_state = self.game.end_state(board, last_row, last_col, last_player)
        
        if depth == 0:
            # TODO: PISTETYSMEKANISMI
            return 0, None

        if end_state:
            if end_state == 1:
                return 1, None
            if end_state == 2:
                return -1, None
            elif end_state == 0:
                return 0, None

        if maximizing:
            max_value = -9999
            best_column = None
            valid_columns = self.get_available_columns(board)

            for column in valid_columns:
                row = self.get_next_available_row(board, column)

                self.game.drop_disc(board, row=row, column=column, player=1)
                value = self.minimax(board, row, column, depth-1, maximizing=False)[0]
                
                # Kumotaan siirto
                board[row][column] = 0

                if value > max_value:
                    max_value = value
                    best_column = column
            
            return max_value, best_column

        elif not maximizing:
            min_value = 9999
            best_column = None

            valid_columns = self.get_available_columns(board)

            for column in valid_columns:
                row = self.get_next_available_row(board, column)

                self.game.drop_disc(board, row=row, column=column, player=2)
                value = self.minimax(board, row, column, depth-1, maximizing=True)[0]
                
                # Kumotaan siirto
                board[row][column] = 0

                if value < min_value:
                    min_value = value
                    best_column = column
            
            return min_value, best_column