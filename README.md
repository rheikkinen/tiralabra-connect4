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

1. Lataa [uusin release](https://github.com/rheikkinen/tiralabra-connect4/releases/tag/viikko6) zip-tiedostona koneellesi ja pura tiedosto haluamaasi hakemistoon. Syntyy oletuksena hakemisto nimeltä `tiralabra-connect4-viikko6`. Tämä on projektin juurihakemisto, ja seuraavat komentorivikomennot tulee tehdä tässä hakemistossa.

2. Asenna projektin riippuvuudet suorittamalla komento
```
poetry install
```

3. Käynnistä sovellus suorittamalla komento
```
poetry run invoke play
```

Pelin pelilauta on 2-ulotteinen taulukko, jossa 0 on tyhjä ruutu, 1 on käyttäjän kiekko, ja 2 on pelitekoälyn kiekko. Tällä hetkellä käyttäjä on aina aloittava pelaaja, mutta halutessaan aloitusvuoroa voi vaihtaa muokkaamalla `src/connect4.py`:ssä [tätä riviä](https://github.com/rheikkinen/tiralabra-connect4/blob/1f2020ca339b26a1749be9ecc2980c5a252e25b7/src/connect4.py#L49).

## Yksikkötestit
Yksikkötestit voi suorittaa projektin juurihakemistossa komennolla
```
poetry run invoke test
```
## Testikattavuus
Testikattavuusraportin saa luotua projektin juurihakemistossa komennolla 
```
poetry run invoke coverage
``` 
Testikattavuutta voi tarkastella avaamalla selaimessa hakemistosta **htmlcov** löytyvän tiedoston `index.html`. 
