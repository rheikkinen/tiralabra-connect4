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
- [connect4.py](https://github.com/rheikkinen/tiralabra-connect4/blob/main/src/connect4.py) sisältää komentorivikäyttöliittymän koodin sekä vielä hieman toimintalogiikkaa
  - Toimintalogiikka käyttää kuitenkin lähes kokonaan `GameBoard`-olion metodeja 
- [gameboard.py](https://github.com/rheikkinen/tiralabra-connect4/blob/c60adfb997e4172bd5e263598fd00a1d26945109/src/gameboard.py) sisältää pelissä käytettävän pelilautaolion ja sen metodit, jotka toteuttavat suurimman osan pelilogiikasta
- [ai.py](https://github.com/rheikkinen/tiralabra-connect4/blob/c60adfb997e4172bd5e263598fd00a1d26945109/src/ai.py) sisältää pelitekoälyn toiminnallisuudet, tärkeimpänä minimax-algoritmi ja alfa-beta -karsinta

Lisäksi erillinen [constants.py](https://github.com/rheikkinen/tiralabra-connect4/blob/c60adfb997e4172bd5e263598fd00a1d26945109/src/constants.py) -tiedosto sisältää ohjelmakoodissa usein käytettävät vakioarvot ja -tietorakenteet:
- Peliruudukon rivien lukumäärä `ROW_COUNT`
- Peliruudukon sarakkeiden lukumäärä `COL_COUNT`
- Tyhjän ruudun arvo peliruudukossa `EMPTY`
- Sarakkeiden läpikäyntijärjestys pelitekoälyä varten `ORDER`
- Sarakkeiden numerot `COLUMN_NUMBERS`

Ohjelma käynnistetään komentoriviltä suorittamalla tiedoston [play.py](https://github.com/rheikkinen/tiralabra-connect4/blob/c60adfb997e4172bd5e263598fd00a1d26945109/src/play.py).

## Pelitekoälyn toiminta ja algoritmit
Pelitekoälyn toteutuksessa käytetään minimax-algoritmia ja alfa-beta -karsintaa. `AI`-olion metodi `best_column` saa parametrina pelilaudan `GameBoard`-oliona sekä laskentasyvyyden. Metodi suorittaa alfa-beta -karsintaa käyttävää minimax-algoritmia rekursiivisesti annettuun laskentasyvyyteen saakka, ja palauttaa parhaaksi arvioidun sarakkeen.

Koska läpi käytävän pelipuun syvyys kasvaa eksponentiaalisesti, pelkästään minimax-algoritmia käyttäen laskentasyvyyden tuli olla korkeintaan 4, jotta algoritmi toimi aina tehokkaasti.

Alfa-beta-karsinta tehosti algoritmia jonkin verran, ja laskentasyvyyden pystyi nostamaan ainakin 6:een.

## Kehitysehdotuksia
- Pelille on tarkoitus lisätä graafinen käyttöliittymä sen kokeilua helpottamiseksi
- Samalla pelin toimintalogiikan ja käyttöliittymän voisi erotella toisistaan paremmin
- Pelitekoäly tekee ajottain turhaan siirtoja, vaikka voiton saavuttaisi vähemmillä siirroilla
  - Algoritmi priorisoi keskimmäisen sarakkeen, jos vaihtoehtoja samalla pisteytyksellä on useita
  - Algoritmin pisteytysheuristiikkaan voisi esimerkiksi lisätä lisäarvon, jos voiton saa vähemmillä siirroilla
  - Tätä varten pelilauta-oliolle muuttuja, joka pitää kirjaa jäjellä olevista siirroista
