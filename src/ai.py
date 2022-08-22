from random import randint
from time import time
from constants import ROW_COUNT, COL_COUNT
from gameboard import GameBoard

MAX_SCORE = 10_000_000
MIN_SCORE = -10_000_000

class AI:
    def __init__(self, level=1, player=2):
        self.level = level
        self.ai_player = player
        self.opponent = (player % 2) + 1
        self.nodes_visited = 0
        self._winning_move = None

    def player(self):
        return self.ai_player

    def best_column(self, board: GameBoard, depth=7):
        """Valitsee pelitekoälylle seuraavaksi tehtävän siirron
        määritetyn vaikeustason (level) mukaisella menetelmällä.

        :param board: Peliruudukko GameBoard-luokan oliona

        :rtype: tuple
        :return: Palauttaa valitun sarakkeen indeksin, siirrolle lasketun pisteytyksen
        ja laskennan suoritusajan sekunteina.
        """
        if self.level == 0:
            # Palauttaa satunnaisen sarakkeen väliltä [0, sarakkeiden_lkm - 1]
            column = randint(0, COL_COUNT-1)

        if self.level == 1:
            # Asetetaan käsiteltyjen solmujen lukumäärä nollaksi
            self.nodes_visited = 0
            start_time = time()

            # Alfan ja betan alkuarvot
            alpha, beta = MIN_SCORE, MAX_SCORE

            value, column = self.minimax(board, alpha, beta, depth, maximizing=False)

            end_time = time()
            runtime = end_time - start_time

            print(f"Minimax valitsi sarakkeen {column + 1} pisteytyksellä {value}")
            print(f"Pelipuun solmuja käsitelty: {self.nodes_visited} kpl")
            print(f"Minimax-algoritmin suoritusaika: {runtime} sekuntia\n")

        return column, value, runtime

    def minimax(self, board: GameBoard, alpha, beta, depth: int, maximizing: bool):
        """Minimax-algoritmi alfa-beta -karsinnalla. Käy rekursiivisesti pelipuuta läpi
        päätössolmuun tai annettuun syvyyteen asti. Pelitekoäly on algoritmissa minimoiva
        pelaaja, eli algoritmi palauttaa sitä pienemmän pisteytyksen mitä parempi pelitilanne
        on tekoälypelaajan kannalta.

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

        if depth == 0: # Laskentasyvyys saavutettu
            value = self.evaluate_board(board)
            return value, None

        if maximizing: # Maksimoiva pelaaja
            if self.player_wins_next_move(board, self.opponent):
                return MAX_SCORE, self._winning_move

            max_value = MIN_SCORE
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
        if self.player_wins_next_move(board, self.ai_player):
            return MIN_SCORE, self._winning_move

        min_value = MAX_SCORE
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
            row = board.get_next_available_row(column)
            # Peliruudukkoon ei tehdä muutoksia, riittää tallettaa siirron tiedot GameBoard-oliolle
            board.store_last_move(row, column, player)
            if board.check_for_win():
                self._winning_move = column
                return True
        return False

    def evaluate_board(self, board: GameBoard):
        """Pisteytysfunktio, joka käy läpi koko peliruudukon ja pisteyttää pelitilanteen vuorossa
        olevan pelaajan kannalta.

        :param board: Peliruudukko GameBoard-luokan oliona

        :rtype: int
        :return: Palauttaa pelitilanteelle lasketun pisteytyksen
        """
        # Viimeisimmän siirron tehnyt pelaaja
        _, _, player = board.get_last_move()

        value = 0

        # VAAKASUUNTAISET NELJÄN RUUDUN LOHKOT

        for row in range(ROW_COUNT):
            for column in range(COL_COUNT - 3):
                evaluation_block = [board.get_position(row, val) for val in range(column, column+4)]

                value += self.get_block_value(evaluation_block, player)

        # PYSTYSUUNTAISET NELJÄN RUUDUN LOHKOT

        for column in range(COL_COUNT):
            for row in range(ROW_COUNT - 3):
                evaluation_block = [board.get_position(val, column) for val in range(row, row + 4)]

                value += self.get_block_value(evaluation_block, player)

        # VINOTTAISET NELJÄN RUUDUN LOHKOT

        # Nouseva suunta (/)
        for row in range(ROW_COUNT - 3):
            for col in range(COL_COUNT - 3):
                evaluation_block = [board.get_position(row+val, col+val) for val in range(4)]

                value += self.get_block_value(evaluation_block, player)

        # Laskeva suunta (\)
        for row in range(ROW_COUNT - 1, ROW_COUNT - 4, -1):
            for col in range(COL_COUNT - 3):
                evaluation_block = [board.get_position(row-val, col+val) for val in range(4)]

                value += self.get_block_value(evaluation_block, player)

        # Jos pelaaja on tekoäly eli minimoiva pelaaja, palautetaan saadun arvon vastaluku
        if player == self.ai_player:
            return -value

        return value

    def get_block_value(self, block: list, player: int):
        """Pisteyttää neljän ruudun mittaisen lohkon vuorossa olevan pelaajan kannalta.
        Lohko on lista, joka sisältää neljän peräkkäisen ruudun arvot vaaka-, pysty-
        tai vinosuunnassa.

        :param block: Pisteytettävä lohko
        :param player: Vuorossa oleva pelaaja, 1 tai 2

        :rtype: int
        :return: Palauttaa lohkon pisteytyksen
        """
        opponent = (player % 2) + 1

        player_discs = 0
        opponent_discs = 0
        empty_count = 0

        for disc in block:
            if disc == player:
                player_discs +=1
            elif disc == opponent:
                opponent_discs += 1
            else: # Ruutu on tyhjä
                empty_count += 1

        if player_discs == 3 and empty_count == 1:
            return 10
        if player_discs == 2 and empty_count == 2:
            return 4
        if opponent_discs == 3 and empty_count == 1:
            return -10

        return 0
