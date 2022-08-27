# Viikko 6
Projektiin käytetty aika: noin 26 tuntia

## Mitä olen tehnyt?
Aloitin viikon lisäämällä voiton blokkaavia testejä tekoälylle. Testien myötä ilmeni ongelma, että tekoäly 
ei aina palauttanut saraketta ollenkaan, jos se johti häviöön, mikä korjaantui asettamalla sarakkeelle jonkin alkuarvon, 
aiemmin se oli aluksi vain ‘None’. 

Toiseksi, havaitsin että todella olin tehnyt virheellisen tulkinnan ohjelman toiminnasta, ja tekoäly teki välillä edelleen
turhia siirtoja, vaikka mahdollisuus varmaan voittoon olisi saavutettavissa aiemmin. 
Onnistuin luomaan nopeimman voiton testaukselle hyvinkin sopivan pelitilanteen, jossa tekoälyllä 
oli mahdollisuus voittaa varmasti 2:lla siirrolla, mutta tilannetta itse pelissä kokeiltuani tekoäly 
viivytti voittoa tekemällä jopa 8 ylimääräistä siirtoa. 

Ratkaisuna lisäsin jälleen jo kertaalleen poistamani “syvyysbonuksen” eli kertoimen voiton pisteytykselle, 
niin että voitto on arvokkaampi aiemmilla tasoilla, mutta ongelma ei heti korjaantunut. 
Pelkän kertoimen lisäyksen jälkeen tekoäly toimi melko kummallisesti, ja tapaukselle lisäämäni yksikkötesti ei mennyt läpi. 
Turhankin pitkän debuggauksen ja eri toteutustapojen jälkeen syyksi ilmeni alfan ja betan alkuarvot, joita en tajunnut muuttaa samalla. 
Ne olivat liian pienet, joten muutin ne nyt suoraan “äärettömiksi” -inf ja inf, ja saman tein algoritmissa minimoivan pelaajan 
alkuarvolle min_value ja maksimoivan pelaajan max_valuelle. Tämän jälkeen algoritmi toimikin halutulla tavalla. 

Lisäksi lisäsin invoke-kirjaston projektin riippuvuudeksi, jotta saisin mm. ohjelman suorituksen ja testien ajamisen komentoja yhtenäisemmiksi. 
Tein tämän jälkeen uuden releasen, koska ohjelmaan oli tullut merkittäviä muutoksia. Releasen jälkeen havaitsin ohjelman käyttöliittymän
toimivan erikoisesti invoke-komennoilla; käyttäjän tekemä siirto ei enää tulostunut heti pelilaudalle, vaan vasta samaan aikaan 
tekoälyn tekemän siirron kanssa, mikä osoittautui ärsyttäväksi bugiksi peliä pelatessa. 
Tämän kanssa taistelin myös tarpeettoman pitkään, kunnes huomasin, että ongelma johtui vain invoken taskeista task.py:ssä.
Hieman tutkailtuani ja pienellä muutoksella sain ohjelman toimimaan jälleen normaalisti.

Keskiviikona ja torstaina kävin läpi vertaisarvoitavaa projektia ja kirjoitin toisen vertaisarvioinnin. 

Loppuviikolla tein hyödyllisen havainnon GameBoard-luokan voiton tarkastusmetodista `check_for_win`. 
- Metodi on alusta lähtien tarkastanut vain viimeksi tehdyn siirron sijainnin viereiset ruudut, tarvitsematta käydä läpi koko pelilautaa.
- Metodi siis tarkastaa onko sille parametrina annettu siirto voittava siirto.
- Tämä osoittautui näin yllättävänkin myöhään hyväksi ominaisuudeksi, sillä minimaxissa voi helposti tarkistaa, 
voiko jollakin siirrolla saavuttaa voiton, ilman että pelilautaan tarvitsee tehdä muutoksia.

Muutin minimax-algoritmin rakennetta siirtämällä voiton tarkistuksen minimaxin alkuun ennen syvyyden tarkastusta niin,
että vaikka laskentasyvyys on saavutettu, algoritmi vielä tarkastaa, voisiko vuorossa oleva pelaaja voittaa, 
minkä myötä ainakin voiton tarkistuksessa pääsee ikään kuin vielä yhtä tasoa syvemmälle. 
Aiemmin laskentasyyvyden saavutettua, algoritmi vain pisteytti sen hetkisen pelitilanteen.

Ensimmäisestä vertaisarvioinnista saamani kommentin myötä päädyin muuttamaan pisteytysfunktiota laskemaan pelitilanteen
arvon aina tekoälypelaajan kannalta, koska tekoälyhän kyseistä metodia käyttää. Olin aiemmin ajatellut ja toteuttanut 
muitakin koodin osia ehkä turhankin kompleksisesti, mutta nyt sain koodia siistittyä melko paljon.

Vielä lauantaina monipuolistin hieman pelin toimintaa ja refaktoroin käyttöliittymän koodia. 
Pelin alussa käyttäjä voi asettaa nyt tekoälyn vaikeustason, joista helpoin käyttää syvyyden 1 minimaxia ja vaikein syvyyttä 7. Näihin
luultavasti tulee vielä tehtyä muutoksia. Lisäsin myös mahdollisuuden pelata uudelleen pelin päätyttyä ja mahdollisuuden valita aloittava pelaaja. 
Vielä on tarkoitus eritellä käyttöliittymän toiminnot paremmin omaan moduuliin.

Lisäsin myös tekoälylle pari syvempää yksikkötestiä, jotka testaavat, että
- Tekoäly tunnistaa varman voiton 7 siirron (3 pelikierroksen) päässä
- Vastaavasti tekoäly tunnistaa varman häviön 6 siirron päässä vastaavassa mutta päinvastaisessa pelitilanteessa


## Ohjelman edistyminen
Tällä viikolla on pääosin korjattu pelitekoälyn toiminnassa havaittuja bugeja ja lisätty testausta. 
Pelitekoälyn toiminta vaikuttaa olevan nyt hyvällä tasolla. Ohjelman toimintaa on myös hiottu hieman.
Pidempi selostus muutoksista edellä.

## Mitä opin?
Opin toistamiseen, että testaaminen tosiaan kannattaisi aloittaa mahdollisimman aikaisessa vaiheessa. Nyt esimerkiksi voiton
blokkausta testattaessa esiin tuli ainakin yksi uusi bugi, jossa minimax ei aina palauttanut saraketta ollenkaan.

## Haasteet
Haasteita riitti tällä viikolla, en jaksanut viikkoselotuksesta niitä eritellä, koska ne kytkeytyvät vahvasti viikon tekemisiin.

Harmillisesti en saanut aikaa riittämään dokumentaation lisäämiseen, mutta tällä viikolla tuli 
suunniteltua to-do lista sen suhteen, mitä asioita dokumentaatioihin lisään.

En koe, että loppupalautukseen olisi oikeastaan epäselvyyksiä, ainakaan tällä hetkellä.

## Mitä teen seuraavaksi?
Viimeisellä viikolla:
- Testausdokumentin päivitys
- Toteutusdokumentin päivitys
- Käyttöohjeen lisäys
- Viimeiset hiomiset ohjelmakoodille
- Käyttöliittymälle pieni hiominen
