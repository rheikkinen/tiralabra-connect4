# Toteutusdokumentti
## Ohjelman rakenne
```
src
├── ai.py
├── connect4.py
├── constants.py
├── gameboard.py
├── play.py
└── tests
    ├── ai_test.py
    ├── gameboard_test.py
    └── __init__.py
```
Ohjelma on jaettu sen toiminnan kannalta kolmeen merkittävään moduuliin:
- [`connect4.py`](https://github.com/rheikkinen/tiralabra-connect4/blob/main/src/connect4.py) sisältää komentorivikäyttöliittymän koodin sekä vielä hieman toimintalogiikkaa
  - Toimintalogiikka käyttää kuitenkin lähes kokonaan `GameBoard`-olion metodeja 
- [`gameboard.py`](https://github.com/rheikkinen/tiralabra-connect4/blob/c60adfb997e4172bd5e263598fd00a1d26945109/src/gameboard.py) sisältää pelissä käytettävän pelilautaolion ja sen metodit, jotka toteuttavat suurimman osan pelilogiikasta
- [`ai.py`](https://github.com/rheikkinen/tiralabra-connect4/blob/c60adfb997e4172bd5e263598fd00a1d26945109/src/ai.py) sisältää pelitekoälyn toiminnallisuudet, tärkeimpänä minimax-algoritmi ja alfa-beta -karsinta

Lisäksi erillinen [constants.py](https://github.com/rheikkinen/tiralabra-connect4/blob/c60adfb997e4172bd5e263598fd00a1d26945109/src/constants.py) -tiedosto sisältää ohjelmakoodissa usein käytettävät vakioarvot ja -tietorakenteet:
- Peliruudukon rivien lukumäärä `ROW_COUNT`
- Peliruudukon sarakkeiden lukumäärä `COL_COUNT`
- Tyhjän ruudun arvo peliruudukossa `EMPTY`
- Sarakkeiden läpikäyntijärjestys pelitekoälyä varten `ORDER`
    - Järjestys on keskimmäisestä reunimmaisiin sarakkeisiin, sillä keskimmäiset sarakkeet ovat keskimäärin pelin kannalta hyödyllisemmät. 
- Sarakkeiden numerot `COLUMN_NUMBERS`

Ohjelma käynnistetään komentoriviltä suorittamalla tiedosto [play.py](https://github.com/rheikkinen/tiralabra-connect4/blob/c60adfb997e4172bd5e263598fd00a1d26945109/src/play.py).

## Pelitekoälyn toiminta
Pelitekoälyn toteutuksessa on käytetty minimax-algoritmia ja alfa-beta -karsintaa. Luokan AI metodi `best_column` saa parametrina pelilaudan tilanteen `GameBoard`-oliona sekä laskentasyvyyden (kuinka monen siirron päähän halutaan laskea). Metodi suorittaa alfa-beta -karsintaa käyttävän `minimax`-algoritmin metodin, joka käy pelipuuta rekursiivisesti annettuun laskentasyvyyteen saakka ja palauttaa parhaaksi arvioidun sarakkeen.

Ilman alfa-beta-karsintaa minimax-algoritmi käy läpi koko pelipuun kaikki solmut. Koska läpi käytävän pelipuun solmujen määrä kasvaa eksponentiaalisesti mitä syvemmälle pelipuuta tutkitaan, pelkästään minimax-algoritmia käyttäen laskentasyvyyden tuli olla korkeintaan 4, jotta algoritmi toimi aina tehokkaasti. Tehokkuus määritettiin projektissa niin, että tekoälyn katsottiin toimivan tehokkaasti, kun se valitsee siirtonsa keskimäärin alle 3 sekunnissa. Ehdotonta yläräjaa ei kuitenkaan ollut.

Alfa-beta-karsinnan avulla läpi käytävää pelipuuta saatiin karsittua pienemmäksi, ja algoritmin laskenta-aika parantui merkittävästi. Viimeisimpien tehostusten jälkeen laskentasyvyyden pystyi nostamaan 8:aan laskenta-ajan pahemmin kärsimättä.

### Minimax-algoritmin toteutus
Pelitekoäly on toteutetussa algoritmissa minimoiva pelaaja, eli algoritmi palauttaa sitä pienemmän pisteytyksen mitä parempi siirto on tekoälypelaajan kannalta. 
#### Pseudokoodi toteutetusta minimax-algoritmista:
```
minimax(GameBoard, alpha, beta, depth, maximizing):
    if board_is_full: # Pelilauta täynnä
        # Palauta tasapelin pisteytys

    if player_wins_next_move: # Vuorossa olevalla pelaajalla mahdollisuus voittoon
        # Palauta parhaat pisteet voittajan (min tai max) kannalta

    if depth == 0: # Laskentasyvyys saavutettu
        # Laske ja palauta pelilaudan tilanteen pisteytys

    if maximizing: # Maksimoiva pelaaja
        max_value = -∞
        for each valid move:
            # Tee siirto
            current_value = minimax(...) # Hae siirron pisteytys kutsumalla minimaxia rekursiivisesti

            if current_value > max_value: # Siirron arvo parempi kuin tähänastinen maksimiarvo
                max_value = current_value # Päivitä maksimiarvo

            alpha = max(alpha, max_value)

            if beta <= alpha: # Siirron arvo huonompi kuin paras jo varmistettu arvo
                break # Karsitaan / jätetään käsittelemättä haaran loput solmut
                
        return max_value # Palauta maksimiarvo

    else: # Minimoiva pelaaja (tekoäly)
        min_value = ∞
        for each valid move:
            # Tee siirto
            current_value = minimax(...) # Hae siirron pisteytys kutsumalla minimaxia rekursiivisesti

            if current_value < min_value: # Siirron arvo parempi kuin tähänastinen minimiarvo
                min_value = current_value # Päivitä minimiarvo
                best_move = current_move # Päivitä paras siirto

            beta = min(beta, min_value)

            if beta <= alpha: # Siirron arvo huonompi kuin paras jo varmistettu arvo
                break # Karsitaan / jätetään käsittelemättä haaran loput solmut
                
        # Palauta paras arvo (minimiarvo) ja arvoa vastaava siirto (sarake)
        return min_value, best_move
```

## Kehitysehdotuksia
- Pelille voisi lisätä graafisen käyttöliittymän sen kokeilua helpottamiseksi
- Samalla pelin toimintalogiikan ja käyttöliittymän voisi erotella toisistaan paremmin
