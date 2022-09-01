import unittest
import numpy as np

from gameboard import GameBoard
from ai import AI, MAX_SCORE, MIN_SCORE

class TestAI(unittest.TestCase):
    """Yksikkötestit, jotka testaavat AI-luokan metodien eli pelitekoälyn toiminnallisuutta.
    Minimax-algoritmin laskentasyvyys testeissä on oletuksena 8."""
    def setUp(self):
        """Alustusmetodi, jossa luodaan oliot pelilaudalle ja pelitekoälylle.
        Suoritetaan ennen jokaista testitapausta."""
        self.board = GameBoard()
        self.ai = AI()

    def test_ai_chooses_winning_move_horizontally(self):
        """Tarkastaa, että tekoälyn metodi best_column palauttaa voittavan sarakkeen, jos
        vaakasuunnassa on mahdollisuus voittoon yhdellä siirrolla."""
        # Alustetaan pelilaudan tilanne
        # 2 = tekoälyn kiekko
        # 1 = vastustajan kiekko
        # 0 = tyhjä ruutu

        # Sarakeindeksit  --->      0 1 2 3 4 5 6
        test_situation = np.array([[0,0,0,0,0,0,0],
                                   [0,0,0,0,0,0,0],
                                   [0,0,0,0,0,0,0],
                                   [0,0,0,0,0,0,0],
                                   [1,1,1,0,0,2,2],
                                   [2,2,2,0,0,1,1]])

        self.board.set_game_situation(test_situation)

        # Tekoälyn pitäisi valita sarakeindeksi 3 (voitto)
        best_column = self.ai.best_column(self.board)[0]
        self.assertEqual(best_column, 3)

    def test_ai_chooses_winning_move_in_positive_diagonal(self):
        """Tarkastaa, että tekoälyn metodi best_column palauttaa voittavan sarakkeen, jos
        vinottain nousevassa suunnassa on mahdollisuus voittoon yhdellä siirrolla."""
        # Alustetaan pelilaudan tilanne
        # 2 = tekoälyn kiekko
        # 1 = vastustajan kiekko
        # 0 = tyhjä ruutu

        # Sarakeindeksit  --->      0 1 2 3 4 5 6
        test_situation = np.array([[0,0,0,0,0,0,0],
                                   [0,0,0,0,0,0,0],
                                   [1,0,0,2,0,0,0],
                                   [1,0,0,1,0,0,0],
                                   [1,2,1,1,0,0,0],
                                   [2,1,2,2,0,0,0]])

        self.board.set_game_situation(test_situation)

        # Tekoälyn pitäisi valita sarakeindeksi 2 (voitto)
        best_column = self.ai.best_column(self.board)[0]
        self.assertEqual(best_column, 2)

    def test_ai_chooses_winning_move_in_negative_diagonal(self):
        """Tarkastaa, että tekoälyn metodi best_column palauttaa voittavan sarakkeen, jos
        vinottain laskevassa suunnassa on mahdollisuus voittoon yhdellä siirrolla."""
        # Alustetaan pelilaudan tilanne
        # 2 = tekoälyn kiekko
        # 1 = vastustajan kiekko
        # 0 = tyhjä ruutu

        # Sarakeindeksit  --->      0 1 2 3 4 5 6
        test_situation = np.array([[0,0,0,0,0,0,0],
                                   [0,0,0,0,0,0,0],
                                   [0,0,0,1,0,0,0],
                                   [1,2,1,1,0,0,0],
                                   [2,1,2,1,0,2,0],
                                   [2,1,1,2,0,2,0]])

        self.board.set_game_situation(test_situation)

        # Tekoälyn pitäisi valita sarakeindeksi 0 (voitto)
        best_column = self.ai.best_column(self.board)[0]
        self.assertEqual(best_column, 0)

    def test_ai_chooses_winning_move_vertically(self):
        """Tarkastaa, että tekoälyn metodi best_column palauttaa voittavan sarakkeen, jos
        pystysuunnassa on mahdollisuus voittoon yhdellä siirrolla."""
        # Alustetaan pelilaudan tilanne
        # 2 = tekoälyn kiekko
        # 1 = vastustajan kiekko
        # 0 = tyhjä ruutu

        # Sarakeindeksit  --->      0 1 2 3 4 5 6
        test_situation = np.array([[0,0,0,0,0,0,0],
                                   [0,0,0,0,0,0,0],
                                   [0,0,0,0,0,0,0],
                                   [2,2,0,0,0,0,0],
                                   [1,2,2,1,0,0,1],
                                   [2,2,1,1,0,0,1]])

        self.board.set_game_situation(test_situation)

        # Tekoälyn pitäisi valita sarakeindeksi 1 (voitto)
        best_column = self.ai.best_column(self.board)[0]
        self.assertEqual(best_column, 1)

    def test_ai_evaluates_draw_game_state_correctly(self):
        """Tarkastaa, että tekoälyn metodi best_column palauttaa viimeisen vapaan sarakkeen
        pisteytyksellä 0, kun jäljellä on vain yksi mahdollinen siirto, joka johtaa tasapeliin."""
        # Alustetaan pelilaudan tilanne
        # 2 = tekoälyn kiekko
        # 1 = vastustajan kiekko
        # 0 = tyhjä ruutu

        # Sarakeindeksit  --->      0 1 2 3 4 5 6
        test_situation = np.array([[1,2,1,2,1,2,0],
                                   [1,2,1,2,1,2,1],
                                   [1,2,1,2,1,2,2],
                                   [2,1,2,1,2,1,1],
                                   [2,1,2,1,2,1,2],
                                   [2,1,2,1,2,1,2]])

        self.board.set_game_situation(test_situation)

        # Tekoälyn pitäisi valita sarakeindeksi 6 (viimeinen vapaa ruutu) pisteytyksellä 0 (tasapeli)
        column, score, _ = self.ai.best_column(self.board)

        self.assertEqual(column, 6)
        self.assertEqual(score, 0)

    def test_ai_blocks_horizontal_win_for_opponent(self):
        """Tarkastaa, että tekoälyn metodi best_column palauttaa siirron, joka estää
        vastustajaa voittamasta vaakasuunnassa seuraavalla siirrolla."""
        # Alustetaan pelilaudan tilanne
        # 2 = tekoälyn kiekko
        # 1 = vastustajan kiekko
        # 0 = tyhjä ruutu

        # Sarakeindeksit  --->      0 1 2 3 4 5 6
        test_situation = np.array([[0,0,0,0,0,0,0],
                                   [0,0,0,0,0,0,0],
                                   [0,0,0,0,0,0,0],
                                   [2,2,0,0,0,0,0],
                                   [1,2,2,1,0,0,1],
                                   [2,1,2,1,1,0,1]])

        self.board.set_game_situation(test_situation)

        # Tekoälyn pitäisi valita sarakeindeksi 5
        best_column = self.ai.best_column(self.board)[0]
        self.assertEqual(best_column, 5)

    def test_ai_blocks_vertical_win_for_opponent(self):
        """Tarkastaa, että tekoälyn metodi best_column palauttaa siirron, joka estää
        vastustajaa voittamasta pystysuunnassa seuraavalla siirrolla."""
        # Alustetaan pelilaudan tilanne
        # 2 = tekoälyn kiekko
        # 1 = vastustajan kiekko
        # 0 = tyhjä ruutu

        # Sarakeindeksit  --->      0 1 2 3 4 5 6
        test_situation = np.array([[0,0,0,0,0,0,0],
                                   [0,0,0,0,0,0,0],
                                   [0,0,0,0,0,1,0],
                                   [1,0,0,2,1,2,0],
                                   [1,0,2,1,2,2,1],
                                   [1,0,2,2,1,2,1]])

        self.board.set_game_situation(test_situation)
        # Tekoälyn pitäisi valita sarakeindeksi 0
        best_column = self.ai.best_column(self.board)[0]
        self.assertEqual(best_column, 0)

    def test_ai_blocks_positive_diagonal_win_for_opponent(self):
        """Tarkastaa, että tekoälyn metodi best_column palauttaa siirron, joka estää
        vastustajaa voittamasta seuraavalla siirrolla vinottain nousevassa suunnassa."""
        # Alustetaan pelilaudan tilanne
        # 2 = tekoälyn kiekko
        # 1 = vastustajan kiekko
        # 0 = tyhjä ruutu

        # Sarakeindeksit  --->      0 1 2 3 4 5 6
        test_situation = np.array([[0,0,0,0,0,0,0],
                                   [0,0,0,0,0,0,0],
                                   [0,0,0,2,0,0,1],
                                   [0,0,0,2,0,0,2],
                                   [0,0,2,1,1,2,1],
                                   [0,0,2,1,1,2,1]])

        self.board.set_game_situation(test_situation)
        # Tekoälyn pitäisi valita sarakeindeksi 5
        best_column = self.ai.best_column(self.board)[0]
        self.assertEqual(best_column, 5)

    def test_ai_blocks_negative_diagonal_win_for_opponent(self):
        """Tarkastaa, että tekoälyn metodi best_column palauttaa siirron, joka estää
        vastustajaa voittamasta seuraavalla siirrolla vinottain laskevassa suunnassa."""
        # Alustetaan pelilaudan tilanne
        # 2 = tekoälyn kiekko
        # 1 = vastustajan kiekko
        # 0 = tyhjä ruutu

        # Sarakeindeksit  --->      0 1 2 3 4 5 6
        test_situation = np.array([[0,0,0,0,0,0,0],
                                   [0,0,0,0,0,0,0],
                                   [0,0,1,2,0,0,0],
                                   [0,0,2,1,0,0,0],
                                   [0,0,2,1,1,0,0],
                                   [0,1,2,2,1,0,0]])

        self.board.set_game_situation(test_situation)
        # Tekoälyn pitäisi valita sarakeindeksi 5
        best_column = self.ai.best_column(self.board)[0]
        self.assertEqual(best_column, 5)

    def test_ai_chooses_last_free_column_even_if_it_results_in_defeat(self):
        """Tarkastaa, että tekoälyn metodi best_column palauttaa viimeisen 
        vapaana olevan sarakkeen, vaikka se johtaa pelin häviämiseen."""
        # Alustetaan pelilaudan tilanne
        # 2 = tekoälyn kiekko
        # 1 = vastustajan kiekko
        # 0 = tyhjä ruutu

        # Sarakeindeksit  --->      0 1 2 3 4 5 6
        test_situation = np.array([[1,0,1,2,2,1,1],
                                   [2,0,2,1,2,2,2],
                                   [1,0,2,2,1,1,1],
                                   [2,0,1,2,2,2,1],
                                   [1,1,2,1,1,1,2],
                                   [1,2,1,2,1,2,2]])

        self.board.set_game_situation(test_situation)
        # Tekoälyn pitäisi valita sarakeindeksi 1
        best_column = self.ai.best_column(self.board)[0]
        self.assertEqual(best_column, 1)

    def test_ai_chooses_column_that_results_in_fastest_win(self):
        """Tarkastaa, että metodi best_column valitsee sarakkeen, joka johtaa
        tekoälyn voittoon nopeiten. Testitilanteessa valitsemalla sarakkeen 6,
        tekoäly saavuttaa varman voiton seuraavalla siirrollaan."""
        # Alustetaan pelilaudan tilanne
        # 2 = tekoälyn kiekko
        # 1 = vastustajan kiekko
        # 0 = tyhjä ruutu

        # Sarakeindeksit  --->      0 1 2 3 4 5 6
        test_situation = np.array([[0,0,0,0,0,0,0],
                                   [0,0,0,2,2,2,0],
                                   [0,0,0,2,1,1,0],
                                   [0,0,0,1,2,2,0],
                                   [1,1,2,1,2,1,2],
                                   [1,2,1,2,2,1,1]])

        self.board.set_game_situation(test_situation)
        # Tekoälyn pitäisi valita sarakeindeksi 6
        best_column = self.ai.best_column(self.board)[0]
        self.assertEqual(best_column, 6)

    def test_ai_chooses_column_that_results_in_certain_win_after_7_moves(self):
        """Tarkastaa, että tekoälyn metodi best_column tunnistaa varman voiton
        7 siirron (3 pelikierroksen) päässä."""
        # Alustetaan pelilaudan tilanne
        # 2 = tekoälyn kiekko
        # 1 = vastustajan kiekko
        # 0 = tyhjä ruutu

        # Sarakeindeksit  --->      0 1 2 3 4 5 6
        test_situation = np.array([[0,0,0,0,0,0,0],
                                   [0,0,0,1,0,0,0],
                                   [0,0,2,2,0,0,0],
                                   [0,0,1,2,0,0,0],
                                   [0,0,2,1,0,0,0],
                                   [1,0,1,2,1,0,0]])

        self.board.set_game_situation(test_situation)
        best_column, score, _ = self.ai.best_column(self.board)
        # Tekoälyn pitäisi valita sarake 4 voittoa vastaavalla pisteytyksellä (< MIN_SCORE)
        self.assertEqual(best_column, 4)
        self.assertLessEqual(score, MIN_SCORE)

    def test_ai_identifies_certain_loss_after_6_moves(self):
        """Tarkastaa, että tekoälyn metodi best_column tunnistaa varman häviön
        6 siirron päässä, ja että tekoäly viivyttää häviötä blokkaamalla voiton, 
        jonka vastustaja saavuttaisi seuraavalla siirrolla. Testitilanne on vastaava kuin
        edellisessä testitapauksessa."""
        # Alustetaan pelilaudan tilanne
        # 2 = tekoälyn kiekko
        # 1 = vastustajan kiekko
        # 0 = tyhjä ruutu

        # Sarakeindeksit  --->      0 1 2 3 4 5 6
        test_situation = np.array([[0,0,0,0,0,0,0],
                                   [0,0,0,2,0,0,0],
                                   [0,0,1,1,0,0,0],
                                   [0,0,2,1,0,0,0],
                                   [0,0,1,2,1,0,0],
                                   [2,0,2,1,2,0,0]])

        self.board.set_game_situation(test_situation)
        best_column, score, _ = self.ai.best_column(self.board)
        # Tekoälyn pitäisi valita sarake 5 häviötä vastaavalla pisteytyksellä (> MAX_SCORE)
        self.assertEqual(best_column, 5)
        self.assertGreaterEqual(score, MAX_SCORE)
