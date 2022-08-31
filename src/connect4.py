from gameboard import GameBoard
from ai import AI

class ConnectFour:
    """Luokan vastuulla on pelilogiikkaa suorittavat metodit."""
    def __init__(self):
        self.board = GameBoard()
        self.ai = AI() # pylint: disable=invalid-name
        self.ai_level = 2
        self.starting_player = 1
        self.player_in_turn = 1
        self.game_over = False

        self.results = [0]*3
        self.ai_times = [] # Listaa tekoälyn suoritusajat

    def quit_game(self):
        self.game_over = True

    def change_turn(self):
        self.player_in_turn = (self.player_in_turn % 2) + 1

    def change_starting_player(self):
        self.starting_player = (self.starting_player % 2) + 1

    def set_ai_level(self, level):
        self.ai_level = level
        if level == 0:
            self.ai.depth = 1
        if level == 1:
            self.ai.depth = 4
        if level == 2:
            self.ai.depth = 8

    def drop_disc(self, column, player):
        row = self.board.get_next_available_row(column)
        self.board.update_position(row, column, value=player)

    def column_is_available(self, column):
        """Palauttaa True, jos sarake on vapaa. Muuten palauttaa False."""
        return self.board.column_is_available(column)

    def game_ended_in_tie(self):
        """Palauttaa True, jos kaikki sarakkeet ovat täynnä, muuten palauttaa False."""
        if self.board.board_is_full():
            self.results[0] += 1
            return True
        return False

    def player_won(self):
        """Palauttaa True, jos viimeksi pudotettu kiekko muodostaa lähellä olevien
        kiekkojen kanssa voittavan kiekkojonon. Muuten palauttaa False."""
        row, column, player = self.board.get_last_move()
        if self.board.check_for_win(row, column, player):
            self.results[player] += 1
            return True
        return False

connect_four = ConnectFour()
