# Viikko 4
Projektiin käytetty aika: 27 tuntia

## Mitä olen tehnyt?
Tällä viikolla projektiin huomattavan paljon aikaa. Viikko alkoi ohjelman rakenteen refaktoroinnilla. Pelilaudan toiminnallisuudet siirsin omaan 
GameBoard-olioon. Refaktoroinnin jälkeen ohjelma ei täysin toiminut, joten sitä 
joutui jonkin verran korjaamaan.

Lisäsin myös minimax-algoritmiin alfa-beta-karsinnan, ja tein yksikkötestejä tekoälyn toiminnalle ja
pelilaudan metodeille. Algoritmin pisteytystä tuli myös korjattua, sillä 
tasapelitilanteen algoritmi pisteytti väärin.

Lisäksi dokumentointia lisäsin projektille runsaasti:
- Aloitin testaus- ja toteutusdokumentin kirjoittamisen
- Lisäsin dokumentointia ohjelmakoodille ja testeille
- Lisäsin käyttöohjeen README:hen

## Ohjelman edistyminen
Ohjelman rakennetta on refaktoroitu huomattavasti. Pelilaudan tarvitsemat metodit on eroteltu omaksi luokakseen. 

Pelin tekoälyn algoritmia on kehitetty; minimax-algoritmi käyttää nyt alfa-beta -karsintaa,
joka paransi laskentasyvyyttä 4:stä solmusta 6 solmun syvyyteen.

Ohjelmaa on myös dokumentoitu.

## Mitä opin?
- Eniten Alfa-beta- karsinnan toiminnasta ja toteutuksesta
- Pythonin dokumentointikäytännöistä

## Haasteet
Haasteita syntyi tällä viikolla erityisesti ohjelman refaktoroinnin yhteydessä. Kuitenkin nyt 
ohjelman rakenne tuntuu järkevämmältä ja selkeämmältä, ja refaktorointi helpotti yskikkötestausta.

Lisäksi alfa-beta -karsinnan toteutus oli hankalahkoa aluksi, koska oli vaikea todeta sen
toiminnan oikeellisuus. Laskentanopeus parani melkein heti, mutta pisteytys ei toiminut toivotulla tavalla. Ongelmat johtuivat
osittain siitä, että tekoälyssä päätössolmun tunnistusmetodissa tasapelin tarkistus oli toteutettu huonosti; metodi palautti arvon 0, 
joka vastaa pythonissa boolean-arvoa False, mikä aiheutti sekaannuksia solmujen pisteytyksessä.

Loppuviikolla havaitsin vielä, että tekoäly tekee ajoittain turhaan ylimääräisiä siirtoja, 
ilmeisesti koska algoritmi priorisoi keskimmäisen sarakkeen, jos vaihtoehtoja samalla pisteytyksellä on 
useita, vaikka reunimmainen sarake toisi voiton vähemmille siirroilla. Algoritmin suoritusaika myös kasvoi usealla sekunnilla, 
jos toinen pelaaja on lähellä voittoa reunimmaisissa sarakkeissa, mikä liittynee samaan ongelmaan.

## Mitä teen seuraavaksi?
- Heuristiikkaan lisäarvo, jos voiton saa vähemmillä siirroilla + mahdollisesti muuta päivitystä
- Pelille graafinen käyttöliittymä esim. pygame
- Pelin logiikan erottaminen paremmin käyttöliittymästä
  - Testikattavuusraportista käyttöliittymän tiedosto pois
- Empiiristä testausta
- Dokumentoinnin päivitystä
