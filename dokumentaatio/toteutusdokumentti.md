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
- [`ui/command_line_interface.py`](https://github.com/rheikkinen/tiralabra-connect4/blob/main/src/ui/command_line_interface.py) sisältää pelin komentorivikäyttöliittymän.

Erilliseen [`constants.py`](https://github.com/rheikkinen/tiralabra-connect4/blob/main/src/constants.py) -tiedostoon on talletettu ohjelmakoodissa usein käytettäviä vakioarvoja ja -tietorakenteita.

Ohjelma käynnistetään komentoriviltä suorittamalla tiedosto [`play.py`](https://github.com/rheikkinen/tiralabra-connect4/blob/main/src/play.py).

Yksikkötestit löytyvät hakemistosta `src/tests`.

## Pelitekoälyn toiminta
Pelitekoälyn toteutuksessa on käytetty minimax-algoritmia ja alfa-beta -karsintaa. Luokan AI metodi `best_column` saa parametrina pelilaudan tilanteen `GameBoard`-oliona sekä laskentasyvyyden (kuinka monen siirron päähän halutaan laskea). Metodi suorittaa alfa-beta -karsintaa käyttävän `minimax`-algoritmin metodin, joka käy pelipuuta rekursiivisesti annettuun laskentasyvyyteen saakka ja palauttaa parhaaksi arvioidun sarakkeen.

Ilman alfa-beta-karsintaa minimax-algoritmi käy läpi koko pelipuun kaikki solmut. Koska läpi käytävän pelipuun solmujen määrä kasvaa eksponentiaalisesti mitä syvemmälle pelipuuta tutkitaan[^1], pelkästään minimax-algoritmia käyttäen laskentasyvyyden tuli olla korkeintaan 4, jotta algoritmi toimi aina tehokkaasti. Tehokkuus määritettiin projektissa niin, että tekoälyn katsottiin toimivan tehokkaasti, kun se valitsi siirtonsa keskimäärin alle 3 sekunnissa. Ehdotonta yläräjaa ei kuitenkaan ollut, ja erityisessä asemassa olikin pelaamisen sujuvuus, eli että peliä pelatessa tekoäly valitsee siirtonsa useimmiten parissa sekunnissa, eikä siirron tekemistä tarvitse toistamiseen odotella esimerkiksi yli 5 sekuntia.

Alfa-beta-karsinnan avulla läpi käytävää pelipuuta saatiin karsittua pienemmäksi, ja algoritmin laskenta-aika parantui merkittävästi. Viimeisimpien tehostusten jälkeen laskentasyvyyden pystyi nostamaan 8:aan laskenta-ajan pysyessä keskimäärin 1-3 sekunnissa. Siirron laskemiseen saattaa ajoittain edelleen kulua jopa yli 5 sekuntia, mikä johtunee mm. melko yksinkertaisesta heuristiikka-/pisteytysmetodista, jossa variaatiota pelitilanteiden pisteytyksiin tulee kovin vähän. Kuitenkin viimeisimmän lisäyksen jälkeen, kun pelitilanteen pisteytyksessä nostettiin keskisarakkeen arvoa korkeammaksi (mitä useampi pelaajan/vastustajan kiekko on keskisarakkeessa, sitä korkeammat/matalammat pisteet), algoritmin suoritusaika vaikuttaa pysyvän tasaisesti noin parissa sekunnissa.

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
## Saavutetut aikavaativuudet
Yllä olevan minimax-algoritmin toteutuksessa aikavaativuus riippuu laskentasyvyydestä, ja tässä toteutuksessa päästiin korkeimmillaan laskentasyvyyteen 8. Haarautumiskerroin eli pelivuoron mahdollisten siirtojen lukumäärä on pelin alkuvaiheessa 7 ja pienenee, kun jokin sarakkeista täyttyy. Huonoimmassa tapauksessa, kun karsintaa ei tapahdu juuri ollenkaan, ja kaikki haarat käydään läpi, algoritmin aikavaativuus on O(h^s), missä h on haarautumiskerroin ja s on läpikäytävän pelipuun syvyys. Optimitilanteessa toteutetun alfa-beta -karsinnan avulla haarautumiskerroin pysyy samana, mutta läpikäytävä pelipuu pienenee jonkin verran, kun jokaista haaraa ei tarkasteta. Parhaassa tapauksessa alfa-beta -karsinnan avulla syvyys s pienenisi puoleen (s/2)[^2]. Tässä toteutuksessa optimointia on tehty melko vähän, joten käytännössä ei ole mahdollista päästä täysin parhaaseen tulokseen, missä kaikki siirrot valittaisiin optimaalisessa järjestyksessä niin, että haaroja saataisiin edes lähes jokaisella kerralla karsittua. 

Muita aikavaativuuksia algoritmin toteutuksessa:
- Tasapelin tarkastus (board_is_full)
    - Lineaarinen O(n), missä n on sarakkeiden lukumäärä
    - Tarkastaa huonoimmassa tapauksessa jokaisen sarakkeen ylimmän ruudun
- Pelaajan voiton tarkastus (player_wins_next_move)
    - Lineaarinen O(n), missä n on vapaiden sarakkeiden lukumäärä
- Pelilaudan pisteytys, kun laskentasyvyys on saavutettu (depth = 0)
    - Koko peliruudukko käydään läpi
    - Neliöllinen O(n^2)

## Kehitysehdotuksia
- Pelitekoälyn minimax-algoritmin toiminnan tehostukseen on lukuisia menetelmiä[^3][^4], joista osa voisi olla melko yksinkertaisia toteuttaa, mm:
    - Käsiteltyjen ja pisteytettyjen pelitilanteiden tallettaminen muistiin, millä vältytään saman pelitilanteen toistuvalta pisteyttämiseltä 
    - Pelitilanteiden peilaus
    - Parempi siirtojen optimointi ja järjestäminen paremmuusjärjestykseen
        - Nyt siirrot tarkastetaan aina keskimmäisestä sarakkeesta reunimmaiseen 
    - Iteratiivisesti syventäminen, algoritmin suoritukselle maksimiaika
- Pelille voisi lisätä myös graafisen käyttöliittymän sen kokeilua helpottamiseksi

[^1]: Hautalahti Joona, [Vahvistusoppimis- ja minimax-agentin vertailu ristinollan avulla](https://trepo.tuni.fi/bitstream/handle/10024/131377/HautalahtiJoona.pdf?sequence=2&isAllowed=y), Pro gradu -tutkielma, huhtikuu 2021

[^2]: Hussain Syed, Hameed Usman, [Minimax with alpha-beta pruning (Connect-4 game)](https://www.academia.edu/41561708/Minimax_with_alpha_beta_pruning_connect_4_game_) (haettu 5.9.2022)

[^3]: Wächter Lars, [Improving Minimax performance](https://dev.to/larswaechter/improving-minimax-performance-1924) (haettu 5.9.2022)

[^4]: Kotilainen Jukka, [Hakumenetelmien vertailua myllypelissä](https://www.theseus.fi/bitstream/handle/10024/749051/Kotilainen_Jukka.pdf?sequence=2), Tieto- ja viestintätekniikan insinöörityö, 5.5.2022
