# Käyttöohje
Peli toimii ainoastaan paikallisesti käyttäjän omalla koneella, ja sitä käytetään koomentoriviltä. Ohjeet Connect 4 -pelin asentamiseen löytyvät [README:sta](https://github.com/rheikkinen/tiralabra-connect4#sovelluksen-k%C3%A4ytt%C3%B6%C3%B6notto).
## Käynnistys
Peli käynnistetään komentoriviltä juurihakemistossa komennolla:
```
poetry run inv play
```
## Pelin toiminta
### Päävalikko
Kun peli on käynnistetty tulee näkyviin pelin päävalikko, missä hyväksyttyjä komentoja on kolme:
- Komento "1" --> Aloita peli
- Komento "2" --> Aseta tekoälypelaajan vaikestaso
- Komento "q" --> Lopeta peli

Komennot suoritetaan syöttämällä ensin komentoa vastaava numero/kirjain ja painamalla tämän jälkeen Enteriä.
```
$ poetry run inv play

Tervetuloa Connect 4 -peliin!


============== Komennot ==============
[1] - aloita peli
[2] - aseta vaikeustaso (valittu: vaikea)
[q] - lopeta peli
======================================

Syötä komento >> 
```
Muilla syötteillä ohjelma ilmoittaa syötteen/komennon olevan virheellinen.

### Pelitekoälyn vaikeustaso
Pelitekoälylle on tällä hetkellä valittavissa kolme vaikeustasoa: "helpoin", "keskitaso" ja "vaikea". Oletuksena on valittuna "vaikea". Vaikeustason pääsee valitsemaan päävalikosta syöttämällä komennon "2".
```
Syötä komento >> 2

Valitse tekoälypelaajan vaikeustaso:
>> 1 = helpoin
>> 2 = keskitaso
>> 3 = vaikea

>> 
```

### Pelaaminen
1. Peli aloitetaan päävalikosta komennolla "1". Kun peli aloitetaan, käyttäjää pyydetään ensin valitsemaan pelitapa kahdesta vaihtoehdosta:
- Kaksinpeli (ihminen vastaan ihminen)
- Peli tietokonetta vastaan (ihminen vastaan tekoäly)
(_Huom: pelitekoälyn vaikeustaso määritetään alkuvalikossa._)
```
Syötä komento >> 1

Valitse pelitapa:
>> 1 = ihminen vs ihminen
>> 2 = ihminen vs tekoäly

>> 
```
2. Tämän jälkeen ohjelma pyytää valitsemaan pelaajan, joka aloittaa pelin.
```
Valitse aloittava pelaaja (1 = ihminen, 2 = tekoäly)

>> 
```
3. Kun aloittava pelaaja on valittu, peli alkaa, ja tulostuu pelilauta. Vuorossa oleva pelaaja valitsee haluamansa sarakkeen väliltä 1-7 syöttämällä ohjelmaan saraketta vastaavan numeron. Tällöin pelaajan oma "pelikiekko" tulostuu pelilaudalle valitun sarakkeen alimpaan vapaaseen ruutuun. Pelin voi myös lopettaa kesken syöttämällä komennon "q" sarakenumeron sijaan.
```
Peli alkoi. Tekoäly on pelaaja nro 2

|1|2|3|4|5|6|7|
|_|_|_|_|_|_|_|
|_|_|_|_|_|_|_|
|_|_|_|_|_|_|_|
|_|_|_|_|_|_|_|
|_|_|_|_|_|_|_|
|_|_|_|_|_|_|_|
|1|2|3|4|5|6|7|


Pelaaja 1 ('X'), valitse sarake väliltä 1-7:
(Lopeta peli komennolla q)

>> 4

|1|2|3|4|5|6|7|
|_|_|_|_|_|_|_|
|_|_|_|_|_|_|_|
|_|_|_|_|_|_|_|
|_|_|_|_|_|_|_|
|_|_|_|_|_|_|_|
|_|_|_|X|_|_|_|
|1|2|3|4|5|6|7|
```
4. Tekoälypelaajan vuorolla algoritmi laskee ja valitsee tekoälyn kannalta hyödyllisen sarakkeen, jolloin ohjelma tulostaa tekoälyn käyttämän minimax-algoritmin laskentatulokset, ja pelilaudalle tulostuu tekoälyn pelikiekko.
```
Pelaaja 2 (tekoäly) valitsee sarakkeen.

Pelipuun solmuja käsitelty: 138129 kpl
Algoritmin suoritusaika: 2.05584168 sekuntia

Tekoäly valitsi sarakkeen 4 pisteytyksellä 12

|1|2|3|4|5|6|7|
|_|_|_|_|_|_|_|
|_|_|_|_|_|_|_|
|_|_|_|_|_|_|_|
|_|_|_|_|_|_|_|
|_|_|_|O|_|_|_|
|_|_|_|X|_|_|_|
|1|2|3|4|5|6|7|
```
Tekoäly pisteyttää siirron siten, että mitä hyödyllisempi siirto on tekoälypelaajan kannalta, sitä pienempi on pisteytys. Esimerkiksi, jos tekoälyn algoritmi havaitsee taatun voiton, niin pisteytys on hyvin pieni, -10 000 000 tai vähemmän.
### Pelin lopettaminen
Pelin voi lopettaa kesken syöttämällä sarakenumeron sijaan komennon "q". Muuten peli päättyy, kun pelilauta täyttyy (tasapeli), tai toinen pelaajista saa aikaan neljän kiekon jonon vaakasuunnassa, pystysuunnassa tai vinottain (voitto). Tällöin ohjelma tulostaa tilaston, jossa näkyy tasapelien ja pelaajien voittojen lukumäärät.

Pelin päätyttyä käyttäjä voi aloittaa heti uuden pelin komennolla "y" tai lopettaa pelin ja palata päävalikkoon komennolla "n".
```
Tekoäly valitsi sarakkeen 3 pisteytyksellä -90000000

Pelaaja 2 voitti pelin!

|1|2|3|4|5|6|7|
|_|_|_|_|X|_|_|
|_|_|_|X|O|_|_|
|_|O|_|O|O|X|_|
|_|X|O|X|O|X|_|
|_|O|O|O|X|X|_|
|_|O|X|X|X|O|_|
|1|2|3|4|5|6|7|


P1 voitot: 0
P2 voitot: 1
Tasapelit: 0

Uusi peli (y = kyllä / n = ei)?

>> 
```
