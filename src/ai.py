from random import randint
from time import time
from constants import ROW_COUNT, COL_COUNT
from gameboard import GameBoard

class AI:
    def __init__(self, level=1, player=2):
        self.level = level
        self.ai_player = player
        self.opponent = (player % 2) + 1
        self.nodes_visited = 0

    def player(self):
        return self.ai_player

    def end_state(self, board: GameBoard, depth: int):
        """Tarkastaa, onko peli päätöstilassa, eli onko viimeisimmän siirron
        tehnyt pelaaja voittanut tai onko peliruudukko täynnä (tasapeli).

        :param board: Peliruudukko GameBoard-luokan oliona
        :param depth: Jäljellä oleva laskentasyvyys, käytetään kertoimena
        voiton pisteytykselle (voiton arvo on suurempi, jos se saadaan aiemmalla laskentatasolla)

        :rtype: tuple
        :return: Jos on päätöstila, palauttaa True ja tilaa vastaavan pistearvon.
        Muuten palauttaa (False, None).
        """
        if board.check_for_win():
            _, _, player = board.get_last_move()

            if player == self.ai_player:
                value = -10_000_000 # Tekoäly eli minimoiva pelaaja voitti
            else:
                value = 10_000_000 # Vastustaja eli maksimoiva pelaaja voitti
            if depth:
                value *= depth
            return True, value

        if board.board_is_full():
            return True, 0 # Tasapeli

        return False, None

    def best_column(self, board: GameBoard, depth=6):
        if self.level == 0:
            # Palauttaa satunnaisen sarakkeen väliltä [0, sarakkeiden_lkm - 1]
            column = randint(0, COL_COUNT-1)

        if self.level == 1:
            # Asetetaan käsiteltyjen solmujen lukumäärä nollaksi
            self.nodes_visited = 0

            start_time = time()

            # Alfan ja betan alkuarvot
            alpha, beta = -999_999_999, 999_999_999

            value, column = self.minimax(board, alpha, beta, depth, maximizing=False)

            end_time = time()
            runtime = end_time - start_time

            print(f"Minimax valitsi sarakkeen {column + 1} pisteytyksellä {value}")
            print(f"Pelipuun solmuja käsitelty: {self.nodes_visited} kpl")
            print(f"Minimax-algoritmin suoritusaika: {runtime} sekuntia\n")


        return column, value, runtime

    def minimax(self, board: GameBoard, alpha, beta, depth: int, maximizing: bool):
        """Minimax-algoritmi alfa-beta -karsinnalla. Käy rekursiivisesti pelipuuta läpi
        päätössolmuun tai annettuun syvyyteen asti. Tekoäly on algoritmissa minimoiva pelaaja.

        :param board: Peliruudukko GameBoard-luokan oliona
        :param alpha: Alfan arvo
        :param beta: Betan arvo
        :param depth: Jäljellä oleva laskentasyvyys
        :param maximizing: True, jos maksimoiva pelaaja, muuten False

        :rtype: tuple
        :return: Palauttaa pelitilanteen pisteytyksen ja parhaaksi arvioidun sarakkeen
        """
        self.nodes_visited += 1

        end_state, end_state_value = self.end_state(board, depth)

        if end_state: # Päätössolmu (voitto tai tasapeli)
            return end_state_value, None

        if depth == 0: # Laskentasyvyys saavutettu
            value = self.evaluate_board(board)
            return value, None

        if maximizing: # Maksimoiva pelaaja
            max_value = -999_999_999
            valid_columns = board.get_available_columns()
            best_column = None

            for column in valid_columns:
                row = board.get_next_available_row(column)
                board.update_position(row, column, value=self.opponent)
                value = self.minimax(board, alpha, beta, depth-1, maximizing=False)[0]

                # Kumotaan siirto
                board.update_position(row, column, value=0)

                if value > max_value:
                    max_value = value
                    best_column = column

                alpha = max(alpha, max_value)

                if beta <= alpha:
                    break

            return max_value, best_column

        else: # Minimoiva pelaaja (tekoäly)
            min_value = 999_999_999
            valid_columns = board.get_available_columns()
            best_column = None

            for column in valid_columns:
                row = board.get_next_available_row(column)
                board.update_position(row, column, value=self.ai_player)
                value = self.minimax(board, alpha, beta, depth-1, maximizing=True)[0]

                # Kumotaan siirto
                board.update_position(row, column, value=0)

                if value < min_value:
                    min_value = value
                    best_column = column

                beta = min(beta, min_value)

                if beta <= alpha:
                    break

            return min_value, best_column

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
        Lohko on lista, joka sisältää neljän peräkkäisen ruudun arvot vaaka-, pysty- tai vinosuunnassa.

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
