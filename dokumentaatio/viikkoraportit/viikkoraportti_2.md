# Viikko 2
Projektiin käytetty aika: 16 tuntia.

### Mitä olen tehnyt?
- Toisella viikolla erityisen paljon aikaa meni pelin toimintalogiikan toteuttamiseen, ja juuri muuta en ehtinyt tehdä
  - Tein pelistä komentorivillä toimivan version, jota ei vielä voi pelata tietokonetta vastaan
- Yksikkötestausta sain hieman aloitettua
  - Github Actionsin suoritettavaksi laitettu yksikkötestit ja testikattavuuden keräys
  - Lisäsin projektin testikattavuuden Codecoviin seurattavaksi
- Otin selvää minimax-algoritmin ja alfa-beta-karsinnan laskennallisista vaativuuksista
- Tein lisäyksen aikavaativuuksista määrittelydokumenttiin
- Kirjoitin viikon 2 viikkoraportin

### Ohjelman edistyminen
Connect 4 -pelille on tehty nyt komentorivillä toimiva versio, tekoälyn toteuttamista ei ole vielä aloitettu. 
Pelilauta tai peliruudukko on tässä vaiheessa toteutettu Pythonin numpy-kirjaston 2-ulotteisena taulukkona (ndarray), 
jossa "tyhjät" ruudut ovat nollia, ja pudotetut kiekot ovat arvoiltaan 1 tai 2 vuorossa olevan pelaajan mukaan. 

Taulukon käsittelyyn ei käytetä juurikaan NumPyn valmiita funktioita. 
Taulukkoa manipuloidaan ainoastaan, kun peliruudukko tulostetaan näkyviin, jolloin taulukon y-akseli käännetään toisinpäin flip-funktiolla. 

### Mitä opin?
Tällä viikolla täysin uusia asioita opin vähemmän, mutta Connect 4 -pelin ohjelmoinnista ja numpy-kirjastosta jonkin verran.
Kokonaiskuva projektista on myös selkiytynyt huomattavasti ensimmäisestä viikosta. 

### Epäselvyydet ja haasteet
Pelin toteutus alkoi hitaasti, kun toteutustavassa oli hakemista.
Toteutus vei lopulta yllättävän paljon aikaa tältä viikolta, eikä aikaa jäänyt aivan kaikkeen mitä olin suunnitellut tehdä,
mm. tekoälyn toteutus olisi ollut mukava jo saada aloitettua.

Pelin toteutuksen jälkeen tuli mieleen, että onkohan numpy-kirjaston käyttö missä määrin sallittua. 
Se ei tosin tässä vaiheessa ole tarpeellinenkaan, joten peliruudukon voisin muuttaa Pythonin taulukko-/listatietorakenteeksi.

### Mitä teen seuraavaksi?
- Pelin koodin hiominen
- Mahdollisesti numpy-taulukon muuttaminen Pythonin vastaavaksi tietorakenteeksi
- Pelin tekoälystä ja minimax-algoritmistä jokin versio valmiiksi
- Yksikkötestauksesta kattava
- Pylint käyttöön
