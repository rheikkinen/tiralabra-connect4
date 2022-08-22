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
poetry run pytest
```

Yksikkötestausta on toteutettu kahdelle luokalle:
- [GameBoard-luokalle](https://github.com/rheikkinen/tiralabra-connect4/blob/85a3ee4cff2e01c8c30b5b4d10c7df38432e1cd5/src/gameboard.py#L6), joka sisältää pelilaudan/peliruudukon käyttämät metodit
- [AI-luokalle](https://github.com/rheikkinen/tiralabra-connect4/blob/85a3ee4cff2e01c8c30b5b4d10c7df38432e1cd5/src/ai.py#L7), joka sisältää pelitekoälyn käyttämät metodit ja algoritmit

### Testikattavuus 
[![codecov](https://codecov.io/gh/rheikkinen/tiralabra-connect4/branch/main/graph/badge.svg?token=HXE9OXQ3R4)](https://codecov.io/gh/rheikkinen/tiralabra-connect4)

Projektin testikattavuusraportti viedään automaattisesti Codecov-palveluun. Testikattavuutta pääsee tarkastelemaan klikkaamalla yllä olevaa codecov-merkkiä.

#### Projektin testikattavuuden visualisointi käyttäen plotlya hyödyntävää [coverage-plot](https://pypi.org/project/coverage-plot/) -kirjastoa
(Päivitetty 22.8.2022)

![tiralabra_coverage_2022-08-22](https://user-images.githubusercontent.com/32366546/185904366-d071e521-5b38-471f-8ad1-567241fbf76c.png)

Huomioitavaa: 
- Komentorivikäyttöliittymän ja osan pelilogiikasta sisältävää [connect4.py](https://github.com/rheikkinen/tiralabra-connect4/blob/85a3ee4cff2e01c8c30b5b4d10c7df38432e1cd5/src/connect4.py) -moduulia ei tällä hetkellä ole yksikkötestattu. Tiedoston peliogiikka hyödyntää kuitenkin täysin GameBoard-olion metodeja, joita on testattu.

### Peliruudukon testaus
Peliruudukon testauksessa tarkastetaan GameBoard-luokan metodien toiminnan oikeellisuus. Peliruudukon dokumentoidut testit löytyvät [täältä](https://github.com/rheikkinen/tiralabra-connect4/blob/main/src/tests/gameboard_test.py).

### Pelitekoälyn testaus
Pelitekoälyn testauksessa tarkastetaan, että AI-luokan olio eli pelitekoäly tekee järkeviä siirtoja sille annetuissa pelitilanteissa, ja osaa pisteyttää pelitilanteet oikein. Tekoälyn dokumentoidut testit löytyvät [täältä](https://github.com/rheikkinen/tiralabra-connect4/blob/main/src/tests/ai_test.py).

## Empiirinen testaus
...
