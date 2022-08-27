from math import inf
from time import time
from constants import ROW_COUNT, COL_COUNT
from gameboard import GameBoard

MAX_SCORE = 10_000_000
MIN_SCORE = -10_000_000

class AI:
    def __init__(self, level=3, player=2):
        self.level = level
        self.ai_player = player
        self.opponent = (player % 2) + 1
        self.nodes_visited = 0
        self._winning_move = None

    def player(self):
        return self.ai_player

    def best_column(self, board: GameBoard, depth: int = 7):
        """Valitsee pelitekoälylle seuraavaksi tehtävän siirron käyttäen
        minimax-algoritmia. Tekoälylle määritetty vaikeustaso (level) vaikuttaa
        laskentasyvyyteen eli siihen, kuinka monta siirtoa algoritmi laskee eteenpäin.

        :param board: Peliruudukko GameBoard-luokan oliona
        :param depth: Laskentasyvyys minimax algoritmille. Jos tyhjä, käytetään oletussyvyyttä 7.

        :rtype: tuple
        :return: Palauttaa valitun sarakkeen indeksin, siirrolle lasketun pisteytyksen
        ja laskennan suoritusajan sekunteina.
        """
        if self.level == 1:
            depth = 1
        if self.level == 2:
            depth = 4

        self.nodes_visited = 0

        alpha, beta = -inf, inf # Alfan ja betan alkuarvot

        start_time = time()
        value, column = self.minimax(board, alpha, beta, depth, maximizing=False)
        runtime = time() - start_time

        print(f"Pelipuun solmuja käsitelty: {self.nodes_visited} kpl")
        print(f"Minimax-algoritmin suoritusaika: {runtime} sekuntia\n")
        print(f"Minimax valitsi sarakkeen {column + 1} pisteytyksellä {value}\n")

        return column, value, runtime

    def minimax(self, board: GameBoard, alpha, beta, depth: int, maximizing: bool):
        """Minimax-algoritmi alfa-beta -karsinnalla. Käy rekursiivisesti pelipuuta läpi
        päätössolmuun (havaittu voitto tai tasapeli) tai annettuun syvyyteen asti.
        Pelitekoäly on algoritmissa minimoiva pelaaja, eli algoritmi palauttaa sitä
        pienemmän pisteytyksen mitä parempi pelitilanne on tekoälypelaajan kannalta.

        :param board: Peliruudukko GameBoard-luokan oliona
        :param alpha: Alfan arvo
        :param beta: Betan arvo
        :param depth: Jäljellä oleva laskentasyvyys
        :param maximizing: True, jos maksimoiva pelaaja, muuten False

        :rtype: tuple
        :return: Palauttaa pelitilanteen pisteytyksen ja parhaaksi arvioidun sarakkeen
        """
        self.nodes_visited += 1

        if board.board_is_full(): # Päätössolmu, tasapeli
            return 0, None

        player_in_turn = self.opponent if maximizing else self.ai_player

        if self.player_wins_next_move(board, player_in_turn):
            if maximizing:
                # Maksimoivan pelaajan voitto
                win_value = MAX_SCORE * (depth+1)
            else:
                # Minimoivan pelaajan voitto
                win_value = MIN_SCORE * (depth+1)
            return win_value, self._winning_move

        if depth == 0: # Laskentasyvyys saavutettu
            value = self.evaluate_board(board)
            return value, None

        if maximizing: # Maksimoiva pelaaja
            max_value = -inf
            valid_columns = board.get_available_columns()
            best_column = valid_columns[0]

            for column in valid_columns:
                row = board.get_next_available_row(column)
                board.update_position(row, column, value=self.opponent)
                value = self.minimax(board, alpha, beta, depth-1, maximizing=False)[0]

                # Kumotaan siirto
                board.clear_position(row, column)

                if value > max_value:
                    max_value = value
                    best_column = column

                alpha = max(alpha, max_value)

                if beta <= alpha:
                    break

            return max_value, best_column

        # Minimoiva pelaaja (tekoäly)
        min_value = inf
        valid_columns = board.get_available_columns()
        best_column = valid_columns[0]

        for column in valid_columns:
            row = board.get_next_available_row(column)
            board.update_position(row, column, value=self.ai_player)
            value = self.minimax(board, alpha, beta, depth-1, maximizing=True)[0]

            # Kumotaan siirto
            board.clear_position(row, column)

            if value < min_value:
                min_value = value
                best_column = column

            beta = min(beta, min_value)

            if beta <= alpha:
                break

        return min_value, best_column

    def player_wins_next_move(self, board: GameBoard, player: int):
        """Tarkastaa, onko pelaajalla mahdollisuus voittaa seuraavalla siirrolla.

        :param board: Peliruudukko GameBoard-luokan oliona
        :param player: Vuorossa oleva pelaaja, 1 tai 2

        :rtype: bool
        :return: Palauttaa True, jos pelaaja voi voittaa seuraavalla siirrolla.
        Muuten palauttaa False.
        """
        valid_moves = board.get_available_columns()
        for column in valid_moves:
            self.nodes_visited += 1
            row = board.get_next_available_row(column)
            if board.check_for_win(row, column, player):
                self._winning_move = column
                return True
        return False

    def evaluate_board(self, board: GameBoard):
        """Pisteytysfunktio, joka käy läpi koko peliruudukon ja pisteyttää pelitilanteen
        tekoälypelaajan (minimoiva pelaaja) kannalta.

        :param board: Peliruudukko GameBoard-luokan oliona

        :rtype: int
        :return: Palauttaa pelitilanteelle lasketun pisteytyksen
        """
        value = 0

        # VAAKASUUNTAISET NELJÄN RUUDUN LOHKOT

        for row in range(ROW_COUNT):
            for column in range(COL_COUNT - 3):
                evaluation_block = [board.get_position(row, val) for val in range(column, column+4)]

                value += self.get_block_value(evaluation_block)

        # PYSTYSUUNTAISET NELJÄN RUUDUN LOHKOT

        for column in range(COL_COUNT):
            for row in range(ROW_COUNT - 3):
                evaluation_block = [board.get_position(val, column) for val in range(row, row + 4)]

                value += self.get_block_value(evaluation_block)

        # VINOTTAISET NELJÄN RUUDUN LOHKOT

        # Nouseva suunta (/)
        for row in range(ROW_COUNT - 3):
            for col in range(COL_COUNT - 3):
                evaluation_block = [board.get_position(row+val, col+val) for val in range(4)]

                value += self.get_block_value(evaluation_block)

        # Laskeva suunta (\)
        for row in range(ROW_COUNT - 1, ROW_COUNT - 4, -1):
            for col in range(COL_COUNT - 3):
                evaluation_block = [board.get_position(row-val, col+val) for val in range(4)]

                value += self.get_block_value(evaluation_block)

        return -value

    def get_block_value(self, block: list):
        """Pisteyttää neljän ruudun kokoisen lohkon tekoälypelaajan kannalta.
        Lohko on lista, joka sisältää neljän peräkkäisen ruudun arvot vaaka-, pysty-
        tai vinosuunnassa.

        :param block: Pisteytettävä lohko

        :rtype: int
        :return: Palauttaa lohkon pisteytyksen
        """
        ai_discs = 0
        opponent_discs = 0
        empty_count = 0

        for disc in block:
            if disc == self.ai_player:
                ai_discs +=1
            elif disc == self.opponent:
                opponent_discs += 1
            else: # Ruutu on tyhjä
                empty_count += 1

        if ai_discs == 3 and empty_count == 1:
            return 10
        if ai_discs == 2 and empty_count == 2:
            return 4
        if opponent_discs == 3 and empty_count == 1:
            return -10
        if opponent_discs == 2 and empty_count == 2:
            return -4

        return 0
