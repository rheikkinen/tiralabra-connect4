# Toteutusdokumentti
## Ohjelman rakenne
```
src
├── ai.py
├── connect4.py
├── constants.py
├── gameboard.py
├── play.py
├── tests
│   ├── ai_test.py
│   ├── gameboard_test.py
│   └── __init__.py
└── ui
    └── command_line_interface.py
```
Ohjelma on jaettu sen toiminnan kannalta neljään merkittävään moduuliin:
- [`connect4.py`](https://github.com/rheikkinen/tiralabra-connect4/blob/main/src/connect4.py) keskittyy pelilogiikkaa suorittaviin metodeihin, joista suurin osa käyttää `GameBoard`-olion metodeja pelilaudan päivittämiseen ja pelitilanteen hakemiseen.
- [`gameboard.py`](https://github.com/rheikkinen/tiralabra-connect4/blob/main/src/gameboard.py) sisältää pelissä käytettävän pelilautaolion ja sen metodit, jotka pitävät yllä pelilaudan tilannetta ja toteuttavat suurimman osan pelilogiikasta.
- [`ai.py`](https://github.com/rheikkinen/tiralabra-connect4/blob/main/src/ai.py) sisältää pelitekoälyn toiminnallisuudet, joista tärkeimpänä minimax-algoritmi, jonka avulla lasketaan tekoälypelaajan seuraavaksi tehtävä siirto.
- [`ui/command_line_interface.py`] sisältää pelin komentorivikäyttöliittymän.

Erilliseen [`constants.py`](https://github.com/rheikkinen/tiralabra-connect4/blob/c60adfb997e4172bd5e263598fd00a1d26945109/src/constants.py) -tiedostoon on talletettu ohjelmakoodissa usein käytettäviä vakioarvoja ja -tietorakenteita.

Ohjelma käynnistetään komentoriviltä suorittamalla tiedosto [`play.py`](https://github.com/rheikkinen/tiralabra-connect4/blob/c60adfb997e4172bd5e263598fd00a1d26945109/src/play.py).

## Pelitekoälyn toiminta
Pelitekoälyn toteutuksessa on käytetty minimax-algoritmia ja alfa-beta -karsintaa. Luokan AI metodi `best_column` saa parametrina pelilaudan tilanteen `GameBoard`-oliona sekä laskentasyvyyden (kuinka monen siirron päähän halutaan laskea). Metodi suorittaa alfa-beta -karsintaa käyttävän `minimax`-algoritmin metodin, joka käy pelipuuta rekursiivisesti annettuun laskentasyvyyteen saakka ja palauttaa parhaaksi arvioidun sarakkeen.

Ilman alfa-beta-karsintaa minimax-algoritmi käy läpi koko pelipuun kaikki solmut. Koska läpi käytävän pelipuun solmujen määrä kasvaa eksponentiaalisesti mitä syvemmälle pelipuuta tutkitaan[^1], pelkästään minimax-algoritmia käyttäen laskentasyvyyden tuli olla korkeintaan 4, jotta algoritmi toimi aina tehokkaasti. Tehokkuus määritettiin projektissa niin, että tekoälyn katsottiin toimivan tehokkaasti, kun se valitsi siirtonsa keskimäärin alle 3 sekunnissa. Ehdotonta yläräjaa ei kuitenkaan ollut, ja erityisessä asemassa olikin pelaamisen sujuvuus, eli että peliä pelatessa tekoäly valitsee siirtonsa useimmiten parissa sekunnissa, eikä siirron tekemistä tarvitse toistamiseen odotella esimerkiksi yli 5 sekuntia.

Alfa-beta-karsinnan avulla läpi käytävää pelipuuta saatiin karsittua pienemmäksi, ja algoritmin laskenta-aika parantui merkittävästi. Viimeisimpien tehostusten jälkeen laskentasyvyyden pystyi nostamaan 8:aan laskenta-ajan pysyessä keskimäärin 2-3 sekunnissa. Satunnaisesti jonkin siirron laskemiseen saattaa algoritmilta kulua 5-8 sekuntia, mikä johtuu mm. melko yksinkertaisesta heuristiikka-/pisteytysmetodista, jossa variaatiota pelitilanteiden pisteytyksiin tulee kovin vähän.

### Minimax-algoritmin toteutus
Huomioitavaa:
- Pelitekoäly on toteutetussa algoritmissa minimoiva pelaaja, eli algoritmi palauttaa sitä pienemmän pisteytyksen mitä hyödyllisempi siirto on tekoälypelaajan kannalta.
    - Tekoälyn varman voiton pisteytys on -10 000 000 tai vähemmän, ja taatun häviön vastaavasti 10 000 000 tai enemmän, riippuen siitä kuinka nopeasti voitto tai häviö saavutetaan. 
- Koska vielä laskentasyyvyden saavutettua algoritmi tarkastaa voisiko vuorossa oleva pelaaja voittaa, tekoäly pystyy laskentasyvyydella 8 tunnistamaan taatun voiton jopa 9 siirron päässä. 
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


[^1]: Hautalahti Joona, [Vahvistusoppimis- ja minimax-agentin vertailu ristinollan avulla](https://trepo.tuni.fi/bitstream/handle/10024/131377/HautalahtiJoona.pdf?sequence=2&isAllowed=y), Pro gradu -tutkielma, huhtikuu 2021
