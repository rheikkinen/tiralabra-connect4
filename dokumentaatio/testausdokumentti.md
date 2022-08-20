# Testausdokumentti
## Sisältö
#### [Yksikkötestaus](https://github.com/rheikkinen/tiralabra-connect4/blob/main/dokumentaatio/testausdokumentti.md#yksikk%C3%B6testaus)
- [Testikattavuus](https://github.com/rheikkinen/tiralabra-connect4/blob/main/dokumentaatio/testausdokumentti.md#testikattavuus)
  - [Testikattavuus visualisoituna](https://github.com/rheikkinen/tiralabra-connect4/blob/main/dokumentaatio/testausdokumentti.md#projektin-testikattavuuden-visualisointi-k%C3%A4ytt%C3%A4en-plotlya-hy%C3%B6dynt%C3%A4v%C3%A4%C3%A4-coverage-plot--kirjastoa)
  - [Testikattavuuden kehitys](https://github.com/rheikkinen/tiralabra-connect4/blob/main/dokumentaatio/testausdokumentti.md#testikattavuuden-kehitys-kaaviona)
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
(Päivitetty 20.8.2022)

![tiralabra_coverage_vko5](https://user-images.githubusercontent.com/32366546/185762152-d3efae94-40f4-4a19-ba1c-fd32ad246fec.png)

Huomioitavaa: 
- Komentorivikäyttöliittymän ja osan pelilogiikasta sisältävää [connect4.py](https://github.com/rheikkinen/tiralabra-connect4/blob/85a3ee4cff2e01c8c30b5b4d10c7df38432e1cd5/src/connect4.py) -moduulia ei tällä hetkellä ole yksikkötestattu. Tiedoston peliogiikka hyödyntää täysin GameBoard-olion metodeja, joita on testattu.
- Moduulin ai.py testikattavuus on huonontunut tehtyjen muutosten jälkeen, koska yksikkötestit, joissa tarkastetaan valitseeko tekoäly varmasti voittavan siirron, eivät vaadi enää pelipuun syvempää tarkastelua. 


#### Testikattavuuden kehitys kaaviona
(Päivitetty 20.8.2022)

![9kmfaelik](https://user-images.githubusercontent.com/32366546/185762502-7af58099-8ccf-4580-be58-6523748e263b.png)

- x-akseli: päivämäärä
- y-akseli: testikattavuus prosentteina
- Kuvaajan pisteet kuvaavat kattavuuden pienintä arvoa kyseisenä ajankohtana

### Peliruudukon testaus
Peliruudukon testauksessa tarkastetaan GameBoard-luokan metodien toiminnan oikeellisuus. Peliruudukon dokumentoidut testit löytyvät [täältä](https://github.com/rheikkinen/tiralabra-connect4/blob/main/src/tests/gameboard_test.py).

### Pelitekoälyn testaus
Pelitekoälyn testauksessa tarkastetaan, että AI-luokan olio eli pelitekoäly tekee järkeviä siirtoja sille annetuissa pelitilanteissa, ja osaa pisteyttää pelitilanteet oikein. Tekoälyn dokumentoidut testit löytyvät [täältä](https://github.com/rheikkinen/tiralabra-connect4/blob/main/src/tests/ai_test.py).

## Empiirinen testaus
