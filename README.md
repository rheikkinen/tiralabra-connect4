[![CI](https://github.com/rheikkinen/tiralabra-connect4/actions/workflows/main.yml/badge.svg)](https://github.com/rheikkinen/tiralabra-connect4/actions/workflows/main.yml)
[![codecov](https://codecov.io/gh/rheikkinen/tiralabra-connect4/branch/main/graph/badge.svg?token=HXE9OXQ3R4)](https://codecov.io/gh/rheikkinen/tiralabra-connect4)

# Connect Four tekoäly
Harjoitustyö, jonka aiheena on Connect Four -pelille toteutettava tekoäly, jota vastaan voi pelata. Tekoälyn toteutuksessa käytetään minimax-algoritmia, jota tehostetaan alfa-beta-karsinnalla.

## Dokumentaatio
[Määrittelydokumentti](https://github.com/rheikkinen/tiralabra-connect4/blob/main/dokumentaatio/maarittelydokumentti.md)

[Testausdokumentti](https://github.com/rheikkinen/tiralabra-connect4/blob/main/dokumentaatio/testausdokumentti.md)

[Toteutusdokumentti](https://github.com/rheikkinen/tiralabra-connect4/blob/main/dokumentaatio/toteutusdokumentti.md)

[Käyttöohje](https://github.com/rheikkinen/tiralabra-connect4/blob/main/dokumentaatio/kayttoohje.md)

## Viikkoraportit
- [Viikko 1](https://github.com/rheikkinen/tiralabra-connect4/blob/main/dokumentaatio/viikkoraportit/viikkoraportti_1.md)
- [Viikko 2](https://github.com/rheikkinen/tiralabra-connect4/blob/main/dokumentaatio/viikkoraportit/viikkoraportti_2.md)
- [Viikko 3](https://github.com/rheikkinen/tiralabra-connect4/blob/main/dokumentaatio/viikkoraportit/viikkoraportti_3.md)
- [Viikko 4](https://github.com/rheikkinen/tiralabra-connect4/blob/main/dokumentaatio/viikkoraportit/viikkoraportti_4.md)
- [Viikko 5](https://github.com/rheikkinen/tiralabra-connect4/blob/main/dokumentaatio/viikkoraportit/viikkoraportti_5.md)

## Sovelluksen käyttöönotto
Sovellus toimii ainoastaan paikallisesti käyttäjän omalla tietokoneella, ja sitä käytetään komentoriviltä.

Varmista, että koneellesi on asennettu Poetry. Voit tehdä sen komennolla 
`poetry --version`, jolloin pitäisi tulostua asennettu versio. Jos Poetrya ei ole asennettu, voit asentaa sen esimerkiksi [Ohjelmistotekniikka-kurssin ohjeella](https://ohjelmistotekniikka-hy.github.io/python/viikko2#asennus).

1. Lataa [uusin release](https://github.com/rheikkinen/tiralabra-connect4/releases/tag/viikko5) zip-tiedostona koneellesi ja pura tiedosto haluamaasi hakemistoon. Syntyy oletuksena hakemisto nimeltä `tiralabra-connect4-viikko5`. Tämä on projektin juurihakemisto, ja seuraavat komentorivikomennot tulee tehdä tässä hakemistossa.

2. Asenna projektin riippuvuudet suorittamalla komento
```
poetry install
```

3. Käynnistä sovellus suorittamalla komento
```
poetry run python3 src/play.py
```

Pelin pelilauta on 2-ulotteinen taulukko, jossa 0 on tyhjä ruutu, 1 on käyttäjän kiekko, ja 2 on pelitekoälyn kiekko. Tällä hetkellä käyttäjä on aina aloittava pelaaja.

## Yksikkötestit
Yksikkötestit voi suorittaa projektin juurihakemistossa komennolla
```
poetry run pytest
```
## Testikattavuus
Testikattavuusraportin saa luotua projektin juurihakemistossa komennolla 
```
poetry run coverage run --branch -m pytest; poetry run coverage html
``` 
Testikattavuutta voi tarkastella avaamalla selaimessa hakemistoon **htmlcov** ilmestyneen tiedoston `index.html`. 
