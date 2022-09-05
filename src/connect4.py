from gameboard import GameBoard
from ai import AI

class ConnectFour:
    """Luokan vastuulla on pelilogiikkaa suorittavat metodit."""
    def __init__(self):
        self.board = GameBoard()
        self.ai = AI() # pylint: disable=invalid-name
        self.ai_level = 3
        self.starting_player = 1
        self.player_in_turn = 1

        self.results = [0]*3 # Listaa pelin tulokset [tasapelit, p1 voitot, p2 voitot]
        self.ai_times = [] # Listaa tekoälyn suoritusajat

    def change_turn(self):
        """Vaihtaa pelivuorossa olevan pelaajan."""
        self.player_in_turn = (self.player_in_turn % 2) + 1

    def change_starting_player(self):
        """Vaihtaa pelin aloittavan pelaajan."""
        self.starting_player = (self.starting_player % 2) + 1

    def set_ai_level(self, level):
        """Asettaa vaikeustason (laskentasyvyyden) tekoälypelaajalle."""
        self.ai_level = level
        if level == 1:
            self.ai.depth = 2
        if level == 2:
            self.ai.depth = 4
        if level == 3:
            self.ai.depth = 8

    def drop_disc(self, column, player):
        """Pudottaa pelaajan pelikiekon annetun sarakkeen alimpaan vapaaseen ruutuun."""
        row = self.board.get_next_available_row(column)
        self.board.update_position(row, column, value=player)

    def column_is_available(self, column):
        """Palauttaa True, jos sarake on vapaa. Muuten palauttaa False."""
        return self.board.column_is_available(column)

    def game_ended_in_tie(self):
        """Palauttaa True, jos pelilaudan kaikki sarakkeet ovat täynnä.
        Muuten palauttaa False."""
        if self.board.board_is_full():
            self.results[0] += 1 # Lisätään tuloksiin tasapeli (indeksi 0)
            return True
        return False

    def player_won(self):
        """Palauttaa True, jos viimeksi pudotettu kiekko muodostaa lähellä olevien
        kiekkojen kanssa voittavan kiekkojonon. Muuten palauttaa False."""
        row, column, player = self.board.get_last_move()
        if self.board.check_for_win(row, column, player):
            self.results[player] += 1 # Lisätään tuloksiin pelaajan voitto (indeksi pelaajan nro)
            return True
        return False

connect_four = ConnectFour()
