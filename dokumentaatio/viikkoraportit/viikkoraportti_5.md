# Viikko 5
Käytetty aika: 21 tuntia

## Mitä olen tehnyt?
Viikon alkupuolella ehdin tutkia vertaisarvioitavaa
projektia melko pintapuolisesti, ja syvemmän tarkastelun ja vertaisarvioinnin kirjoittamisen
aloitin keskiviikkona. Siihen mennessä omaa projektia en ollut vielä työstänyt juuri ollenkaan. Oman projektin parissa 
työskentelemään pääsin kunnolla vasta loppuviikosta.

Loppuviikko menikin korjatessa paria merkittävintä ongelmaa edelliseltä viikolta:
- Tekoäly teki turhia siirtoja, vaikka olisi mahdollisuus varmaan voittoon.
- Tekoälyn algoritmilla kesti tarpeettoman pitkään valita siirto, jos
jommalla kummalla pelaajista oli voittomahdollisuus reunimmaisissa sarakkeissa.

Ensimmäistä ongelmaa varten lisäsin voiton pisteytykselle kertoimen, joka otti huomioon sen hetkisen laskentatason. Kuitenkaan tämä ei ratkaissut
jälkimmäistä ongelmaa, ja kerroin osoittautuikin tarpeettomaksi, kun sain jälkimmäisen ongelman korjattua. Sen ratkaiseminen aiheuttikin 
yllättäviä haasteita, joten aikaa ei juuri muuhun jäänytkään, esimerkiksi testaamisen parantamiseen. 
Nyt algoritmi toimii kuitenkin huomattavasti tehokkaammin ja vaikuttaa osaavan valita seuraavat siirrot järkevämmin.

Lisäksi kirjoitin tämän viikkoraportin.

## Ohjelman edistyminen
Tällä viikolla ohjelmaan ei ole tehty paljon muutoksia, eikä testausta ole lisätty. Ohjelmakoodia on refaktoroitu jonkin verran.
Lisäksi algoritmin suoritusta on tehostettu seuraavasti:
- Algoritmille lisättiin metodi `player_wins_next_move`, joka aina ennen pelipuussa syvemmälle etenemistä tarkastaa voiko 
jollakin mahdollisista siirroista saada varman voiton.
  - Jos on mahdollisuus voittoon, palautetaan voittoa vastaava pisteytys
  - Pelipuuta sai huomattavasti karsittua, koska varman voiton tunnistettua ei ole järkeä tarkastaa puuta syvemmälle
- Samalla alkuperäinen metodi päätössolmun eli voiton ja tasapelin tarkastukselle poistettiin
  - Tasapeli tarkastetaan ja pisteytetään minimax-algoritmin suorituksen alussa

Laskentasyvyyttä pystyi 6:sta kasvattamaan suoritusajan pahemmin kärsimättä 7 ja jopa 8 solmun syvyyteen.

## Mitä opin?
Tällä viikolla opitut uudet asiat liittyivät oikeastaan vain minimax-algoritmin tehostusmenetelmiin. Vaikka olin aiemmillakin viikoilla
niitä tutkinut, niin vasta tällä vikolla syvemmin asiaan perehdyttyä niistä löytyi paljon uutta. 
Tehostustapoja tuli tutkittua runsaasti myös vertaisarvioitavan projektin yhteydessä.

## Haasteet
Tällä viikolla algoritmin tehostus aiheutti haasteita. Tarkoituksena oli korjata erityisesti ongelma, jossa algoritmilla
kesti huomattavan pitkään esim. blokata voitto reunimmaisissa sarakkeissa, välillä aikaa meni jopa yli 10 sekuntia.
Tapaukselle olisi pitänyt luoda testejä sen toimivuuden varmistamiseksi, mutta nyt testasin itse pelaamalla peliä.
Muutaman toteutustavan jälkeen vaikutti siltä, että ongelma oli ratkennut, ja tekoäly toimi tehokkaasti myös reunasarakkeissa, mutta
jostain tuntemattomaksi jääneestä syystä muutama tekoälyn yksikkötesti ei mennyt läpi, vaikka itse pelissä tekoäly vaikutti
toimivan odotetulla tavalla. Debugggaamisella en saanut selvyyttä, joten kumosin muutaman viimeksi tehdyn muutoksen kunnes testit 
alkoivat toimimaan, ja kuitenkin loppujen lopuksi viimeisin koodi vaikutti varsin samalta kuin ongelmien ilmaantuessa.

Muuten haasteita aiheutti oma aikataulu, minkä vuoksi suurin osa kurssin työskentelystä kasaantui viimeisille päiville, ja piti 
priorisoida projektiin tehtäviä muutoksia jonkin verran eri tavalla.
Ainakin käyttöliittymän jätin ennalleen tällä viikolla, ja testausta en saanut lisättyä. Kuitenkin koska ohjelman toiminta vaikuttaa olevan
nyt hyvällä tasolla, seuraavalle viikolle pitäisi jäädä hyvin aikaa testaukseen, dokumentointiin sekä muihin tarvittaviin lisäyksiin. 

## Mitä teen seuraavaksi?
- Toinen vertaisarviointi
- Yksikkötestauksen lisäys, ainakin:
  - Tekoälylle syvempiä testejä, eli mm. useammalla siirrolla saavutettavat voitot
  - Voiton blokkaavien siirtojen testaaminen
- Sopivien muiden testaustapojen miettiminen ja toteutus
- Oikeastaan kaiken dokumentoinnin päivittäminen
- Aika- ja tilavaativuuksien tutkiminen

Ja mahdollisesti ajan riittäessä:
- Luultavasti jonkin verran refaktorointia selkeyden parantamiseksi
- Pieni käyttöliittymän kohennus
