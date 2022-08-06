# Viikko 3
Projektiin käytetty aika: 21 tuntia

## Mitä olen tehnyt?
Tämä viikko meni lähes kokonaan Minimax-algoritmin kertaukseen ja erityisesti algoritmin toteutukseen. 

Otin käyttöön pylintin koodin laaduntarkastukseen, ja pylint suoritetaan automaattisesti Github Actionsin toimesta.

Lisäksi kirjoitin tämän viikkoraportin.

## Ohjelman edistyminen
Pelillä on edelleen komentorivillä toimiva käyttöliittymä,
ja peliruudukko on toteutettu NumPy-kirjaston 2-ulotteisena taulukkona.

Pelille on tällä viikolla toteutettu (osittain) toimiva minimax-algoritmi, jota vastaan pystyy pelaamaan.
Tekoäly on algoritmissa minimoiva pelaaja. Minimax-algoritmi käy pelipuun läpi 4 solmun syvyyteen asti ja algoritmi osaa valita optimaaliset siirrot jo melko hyvin.
Erityisesti pelitilanteen, jossa pelaaja tai tekoäly voittaa,
algoritmi ottaa huomioon hyvällä menestyksellä. 

Aina kun minimax on saavuttanut syvyyden 4, algoritmi pisteyttää pelilaudan tilanteen.
Tällä hetkellä pisteytysfunktio ottaa huomioon pelilaudan tilanteen vaaka- ja pystysuunnassa seuraavasti:
- Peliruudukko jaetaan neljän ruudun lohkoihin/riveihin, ensin vaaka- ja sen jälkeen pystysuunnassa
- Jokainen lohko käydään läpi
  - Jos lohkossa on 3 omaa kiekkoa ja yksi tyhjä ruutu (mahdollisuus voittoon), pisteitä lisätään suurin määrä
  - Jos lohkossa on 3 vastapelaajan kiekkoa ja tyhjä ruutu, pisteitä vähennetään suurin määrä
  - Jos lohkossa on kaksi omaa kiekkoa ja kaksi tyhjää ruutua, pisteitä lisätään toiseksi suurin määrä
- Lopuksi pisteytysfunktio palauttaa saadun pistemäärän tai sen vastaluvun, jos pelivuorossa on tekoäly eli minimoiva pelaaja.

Valmiita funktioita ei juurikaan käytetä, mutta tekoälyn funktio get_available_columns, 
joka palauttaa vapaat sarakkeet listana, järjestää tällä hetkellä sarakkeet keskimmäisistä reunimmaisiin sorted()-funktiolla.

## Mitä opin?
Minimax-algoritmin toiminnasta ja toteutuksesta opin tällä viikolla erityisen paljon. Osa oli kertausta aiemmilta kursseilta, mutta suuri osa oli myös uutta asiaa,
koska minimaxia en ole itse toteuttanut aiemmin.
Loppujen lopuksi minimax-algoritmi osoittautui yksinkertaisemmaksi toteuttaa kuin ennakkoon ajattelin. 
Lisäksi minimaxin pisteytysperiaatteista sain uusia näkemyksiä, mm. "neljän ruudun lohkot".

## Haasteet
Minimax-algoritmin opettelu ja implementointi vei huomattavan paljon aikaa tältä viikolta. Kun tajusin toteutuksen yleisperiaateen,
niin työläin vaihe oli saada se toimimaan olemassa olevan pelilogiikan kanssa, minkä jälkeen sopivan 
heuristiikan etsimiseen/miettimiseen ja toteutukseen menikin loppuaika. 

Projektin rakenteen kanssa on ajoittain ollut myös haasteita. Peli ja tekoäly ovat nyt omina moduuleina,
ja tekoälylle annetaan konstruktorin parametrina ConnectFour-luokka, jotta se voi käyttää luokan metodeja.
Tämä ei tuntunut järkevältä toteutustavalta, mutta sillä sain ohjelman toimimaan. 
Kenties yritän eriyttää pelilaudan/-ruudukon omaksi luokaksi, kun nyt lukuisille metodeille annetaan parametrina pelilauta taulukkotietorakenteena.

Tällä viikolla harmillisesti testaus jäi olemattomaksi. 
Jonkinlaista empiiristä havainnointia toki tuli tehtyä algoritmia toteutettaessa, 
mutta yksikkötestauksen ja testikattavuuden parantamiseen ei jäänyt aikaa.

## Mitä teen seuraavaksi?
- Varmaankin refaktorointia, sovelluksen pilkkominen hieman eri tavalla
- Yksikkötestaus kuntoon (!)
- Muun testauksen toteutus ja testausdokumentoinnin tekeminen
- Minimax-algoritmin pisteytysmekanismin viimeistely
- (Valmiin käyttöliittymän implementointi, jos ei vie liikaa aikaa)  
  - Helpottaisi erityisesti empiiristä testaamista
- Käyttöohjeen lisäys
