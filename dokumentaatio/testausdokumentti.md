# Testausdokumentti
## Sisältö
#### [Yksikkötestaus](https://github.com/rheikkinen/tiralabra-connect4/blob/main/dokumentaatio/testausdokumentti.md#yksikk%C3%B6testaus)
- [Testikattavuus](https://github.com/rheikkinen/tiralabra-connect4/blob/main/dokumentaatio/testausdokumentti.md#testikattavuus)
  - [Testikattavuusraportti taulukkona](https://github.com/rheikkinen/tiralabra-connect4/blob/main/dokumentaatio/testausdokumentti.md#projektin-testikattavuus-kuvana)
- [Peliruudukon testaus](https://github.com/rheikkinen/tiralabra-connect4/blob/main/dokumentaatio/testausdokumentti.md#peliruudukon-testaus)
- [Pelitekoälyn testaus](https://github.com/rheikkinen/tiralabra-connect4/blob/main/dokumentaatio/testausdokumentti.md#peliteko%C3%A4lyn-testaus)

## Yksikkötestaus
Yksikkötestit suoritetaan käyttäen pytestiä ja ne sijaitsevat hakemistossa [src/tests/](https://github.com/rheikkinen/tiralabra-connect4/tree/main/src/tests). Yksikkötestien suorittaminen onnistuu projektin juurihakemistossa komennolla
```
poetry run inv test
```

Yksikkötestausta on toteutettu kahdelle luokalle:
- [GameBoard-luokalle](https://github.com/rheikkinen/tiralabra-connect4/blob/main/src/gameboard.py), joka sisältää pelilautaan/peliruudukkoon kohdistuvat ja suuren osan pelilogiikasta toteuttavat metodit.
- [AI-luokalle](https://github.com/rheikkinen/tiralabra-connect4/blob/main/src/ai.py), joka sisältää pelitekoälyn käyttämät metodit ja algoritmin.

### Testikattavuus 
[![codecov](https://codecov.io/gh/rheikkinen/tiralabra-connect4/branch/main/graph/badge.svg?token=HXE9OXQ3R4)](https://codecov.io/gh/rheikkinen/tiralabra-connect4)

Projektin testikattavuusraportti viedään automaattisesti Codecov-palveluun. Testikattavuutta pääsee tarkastelemaan klikkaamalla yllä olevaa codecov-merkkiä.

#### Projektin testikattavuusraportti
![tiralabra_coverage_2022-09-04](https://user-images.githubusercontent.com/32366546/188325445-a340170c-49c8-4025-a794-4bf901308287.png)

Huomioitavaa:
- Pelilogiikan sisältävää [connect4.py](https://github.com/rheikkinen/tiralabra-connect4/blob/85a3ee4cff2e01c8c30b5b4d10c7df38432e1cd5/src/connect4.py) -moduulia ei tällä hetkellä ole yksikkötestattu, koska tiedoston peliogiikka hyödyntää enimmäkseen GameBoard-olion metodeja, jotka on testattu. Ja muut metodit on settereinä jätetty pois testeistä.

### Peliruudukon yksikkötestit
Peliruudukon yksikkötestauksessa tarkastetaan GameBoard-luokan metodien toiminnan oikeellisuus. Testitapauksissa pelilaudalle asetetaan valmis pelitilanne GameBoard-luokan metodilla `set_game_situation`. Peliruudukon dokumentoidut testit löytyvät [täältä](https://github.com/rheikkinen/tiralabra-connect4/blob/main/src/tests/gameboard_test.py).

### Pelitekoälyn yksikkötestit
Pelitekoälyn yksikkötestauksessa tarkastetaan, että pelitekoäly eli AI-luokan metodit ja minimax-algoritmi toimivat oikein. Tekoälyn oikeellisuuden testauksessa tekoälylle annetaan valmiita pelitilanteita, joissa sen odotetaan valitsevan tietynlainen siirto. Joissakin testitilanteissa myös tarkastetaan, että tekoäly antaa tekemälleen siirrolle oikean pisteytyksen. Tekoälyn dokumentoidut testit löytyvät [täältä](https://github.com/rheikkinen/tiralabra-connect4/blob/main/src/tests/ai_test.py).

#### Testisyötteet
Pelitekoälyn yksikkötesteissä tekoälypelaajan seuraava siirto haetaan pelissäkin käytettävällä best_column-metodilla, joka suorittaa minimax-algoritmin metodin. Testitapausten alussa GameBoard-oliolle asetetaan pelitilanne metodilla `set_game_situation`, minkä jälkeen testitilanteen sisältävä GameBoard-olio annetaan parametrina AI-luokan metodille best_column.
