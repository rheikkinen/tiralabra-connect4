# Testausdokumentti
## Sisältö
#### [Yksikkötestaus](https://github.com/rheikkinen/tiralabra-connect4/blob/main/dokumentaatio/testausdokumentti.md#yksikk%C3%B6testaus)
- [Testikattavuus](https://github.com/rheikkinen/tiralabra-connect4/blob/main/dokumentaatio/testausdokumentti.md#testikattavuus)
  - [Testikattavuus visualisoituna](https://github.com/rheikkinen/tiralabra-connect4/blob/main/dokumentaatio/testausdokumentti.md#projektin-testikattavuuden-visualisointi-k%C3%A4ytt%C3%A4en-plotlya-hy%C3%B6dynt%C3%A4v%C3%A4%C3%A4-coverage-plot--kirjastoa)
- [Peliruudukon testaus](https://github.com/rheikkinen/tiralabra-connect4/blob/main/dokumentaatio/testausdokumentti.md#peliruudukon-testaus)
- [Pelitekoälyn testaus](https://github.com/rheikkinen/tiralabra-connect4/blob/main/dokumentaatio/testausdokumentti.md#peliteko%C3%A4lyn-testaus)

## Yksikkötestaus
Yksikkötestit suoritetaan käyttäen pytestiä. Testit sijaitsevat hakemistossa [src/tests/](https://github.com/rheikkinen/tiralabra-connect4/tree/main/src/tests). Testien suorittaminen onnistuu projektin juurihakemistossa komennolla
```
poetry run inv test
```

Yksikkötestausta on toteutettu kahdelle luokalle:
- [GameBoard-luokalle](https://github.com/rheikkinen/tiralabra-connect4/blob/main/src/gameboard.py), joka sisältää pelilautaan/peliruudukkoon kohdistuvat ja suuren osan pelilogiikasta toteuttavat metodit.
- [AI-luokalle](https://github.com/rheikkinen/tiralabra-connect4/blob/main/src/ai.py), joka sisältää pelitekoälyn käyttämät metodit ja algoritmin.

### Testikattavuus 
[![codecov](https://codecov.io/gh/rheikkinen/tiralabra-connect4/branch/main/graph/badge.svg?token=HXE9OXQ3R4)](https://codecov.io/gh/rheikkinen/tiralabra-connect4)

Projektin testikattavuusraportti viedään automaattisesti Codecov-palveluun. Testikattavuutta pääsee tarkastelemaan klikkaamalla yllä olevaa codecov-merkkiä.

#### Projektin testikattavuus kuvana
![tiralabra_coverage_2022-09-04](https://user-images.githubusercontent.com/32366546/188325445-a340170c-49c8-4025-a794-4bf901308287.png)

Huomioitavaa:
- Pelilogiikan sisältävää [connect4.py](https://github.com/rheikkinen/tiralabra-connect4/blob/85a3ee4cff2e01c8c30b5b4d10c7df38432e1cd5/src/connect4.py) -moduulia ei tällä ole yksikkötestattu. Tiedoston peliogiikka hyödyntää enimmäkseen GameBoard-olion metodeja, jotka on testattu. Ja muut metodit on settereinä jätetty pois testeistä.

### Peliruudukon testaus
Peliruudukon testauksessa tarkastetaan GameBoard-luokan metodien toiminnan oikeellisuus. Peliruudukon dokumentoidut testit löytyvät [täältä](https://github.com/rheikkinen/tiralabra-connect4/blob/main/src/tests/gameboard_test.py).

### Pelitekoälyn testaus
Pelitekoälyn testauksessa tarkastetaan, että AI-luokan olio eli pelitekoäly tekee järkeviä siirtoja sille annetuissa pelitilanteissa, ja osaa pisteyttää pelitilanteet oikein. Tekoälyn dokumentoidut testit löytyvät [täältä](https://github.com/rheikkinen/tiralabra-connect4/blob/main/src/tests/ai_test.py).
