[![CI](https://github.com/rheikkinen/tiralabra-connect4/actions/workflows/main.yml/badge.svg)](https://github.com/rheikkinen/tiralabra-connect4/actions/workflows/main.yml)
[![codecov](https://codecov.io/gh/rheikkinen/tiralabra-connect4/branch/main/graph/badge.svg?token=HXE9OXQ3R4)](https://codecov.io/gh/rheikkinen/tiralabra-connect4)

# Connect Four tekoäly
Harjoitustyö, jonka aiheena on Connect Four -pelille toteutettava tekoäly, jota vastaan voi pelata. Tekoälyn toteutuksessa käytetään minimax-algoritmia, jota tehostetaan alfa-beta-karsinnalla.

## Dokumentaatio
[Määrittelydokumentti](https://github.com/rheikkinen/tiralabra-connect4/blob/main/dokumentaatio/maarittelydokumentti.md)

[Testausdokumentti](https://github.com/rheikkinen/tiralabra-connect4/blob/main/dokumentaatio/testausdokumentti.md)

[Toteutusdokumentti](https://github.com/rheikkinen/tiralabra-connect4/blob/main/dokumentaatio/toteutusdokumentti.md)

## Viikkoraportit
- [Viikko 1](https://github.com/rheikkinen/tiralabra-connect4/blob/main/dokumentaatio/viikkoraportit/viikkoraportti_1.md)
- [Viikko 2](https://github.com/rheikkinen/tiralabra-connect4/blob/main/dokumentaatio/viikkoraportit/viikkoraportti_2.md)
- [Viikko 3](https://github.com/rheikkinen/tiralabra-connect4/blob/main/dokumentaatio/viikkoraportit/viikkoraportti_3.md)

## Käyttöohje
Sovellus toimii ainoastaan paikallsesti käyttäjän omalla tietokoneella, ja sitä käytetään komentoriviltä.

Varmista, että koneellesi on asennettu Poetry. Voit tehdä sen komennolla 
`poetry --version`, jolloin pitäisi tulostua asennettu versio. Jos Poetrya ei ole asennettu, voit asentaa sen esimerkiksi [Ohjelmistotekniikka-kurssin ohjeella](https://ohjelmistotekniikka-hy.github.io/python/viikko2#asennus).

1. Lataa [uusin release](https://github.com/rheikkinen/tiralabra-connect4/releases/tag/viikko4) esim. zip-tiedostona koneellesi ja pura tiedosto haluamaasi hakemistoon.

2. Syntyy oletuksena hakemisto nimeltä `tiralabra-connect4-viikko4`. Tämä on projektin juurihakemisto, ja seuraavat komentorivikomennot tulee tehdä tässä hakemistossa.

3. Asenna projektin käyttämät riippuvuudet suorittamalla komento
```
poetry install
```

4. Käynnistä sovellus suorittamalla komento
```
poetry run python3 src/play.py
```
