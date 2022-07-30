## Määrittelydokumentti
**Opinto-ohjelma**: Tietojenkäsittelytieteen kandidaatti

**Ohjelmointikieli**: Python

**Dokumentaatiossa käytettävä kieli**: suomi

Vertaisarvioinnissa myöskään Javalla toteutettujen tai englanniksi dokumentoitujen töiden arvioinnin ei pitäisi tuottaa liikaa vaikeuksia.

### Aihe
Aiheena on kehittää Connect Four peliin tehokas tekoäly, jota vastaan voi pelata. Pelille käytetään 7x6-kokoista pelilautaa (7 saraketta, 6 riviä). Peli ja tekoäly toteutetaan Pythonilla. Tarkoituksena on hyödyntää tekoälyssä minimax-algoritmia, jota tehostetaan alfa-beta -karsinnalla. Tekoälylle toteutetaan myös sopiva määrä projektin kannalta mielekkäitä vaikeustasoja.

### Connect Four
Connect Four (tai Neljän suora) on kahden pelaajan lautapeli, jota pelataan perinteisesti pelilaudalla, jonka koko on 7x6 "ruutua". Peliä pelataan kiekoilla, joita on kahta eri väriä, kummallekin pelaajalle omansa. Pelilaudan sarakkeisiin pudotetaan vuorotellen yksi omista pelikiekoista. Voittaja on se pelaaja, joka saa aikaan “neljän suoran” eli neljän kiekon jonon vaakasuunnassa, pystysuunnassa tai vinottain. Jos pelilauta täyttyy ilman että kumpikaan pelaajista saa neljän suoraa, peli päättyy tasapeliin.[^1]

### Algoritmit
Connect Four on vuorottain pelattava peli, joten hyvin pelaavan tekoälyn pitää suunnitella siirtonsa useamman siirron päähän saavuttaakseen optimaalisen tuloksen ja samalla minimoidakseen mahdollisen häviön, jos vastustaja tekee myös mahdollisimman optimaalisia siirtoja[^2]. Tämän vuoksi projektissa käytetään tähän hyvin soveltuvaa minimax-algoritmia. Todennäköisesti minimax ei ole kuitenkaan tarpeeksi tehokas, sillä mahdollisia siirtoja on valtava määrä, jolloin pelipuun solmujen läpi käyminen vie minimax-algoritmilta liian kauan aikaa. Alfa-beta karsinnalla halutaan vähentää läpi käytävien solmujen määrää, jolloin tekoäly voi myös suunnitella siirtoja huomattavasti pidemmälle eli syvemmälle pelipuussa kuin minimax-algoritmia käyttäen.

### Aikavaativuudet
Minimax-algoritmilla aikavaativuus on $O(h^s)$[^3], missä $h$ on haarautumiskerroin eli pelivuorolla tehtävien mahdollisten siirtojen lukumäärä, ja $s$ on läpi käytävän pelipuun syvyys eli pelissä tehtävien siirtojen kokonaismäärä. Perinteisellä Connect 4 -pelilaudalla siis suurimmillaan $h=7$, ja arvo pienenee, kun jokin sarakkeista täyttyy. Läpi käytävän pelipuun syvyys on korkeimmillaan pelin alussa, jolloin $s=42$. Minimax-algoritmin aikavaativuus on sama kuin alfa-beta -karsinnan aikavaativuus huonoimmassa tapauksessa, kun kaikki pelipuun solmut käydään läpi.

Parhaassa tapauksessa, kun kaikki siirrot ovat optimaalisia, alfa-beta -karsinnan aikavaativuus on $O(h^{s/2})$[^3].

### Lähteet
[^1]: Wikipedia (FI), [Neljän suora](https://fi.wikipedia.org/wiki/Nelj%C3%A4n_suora)

[^2]: Karhunen Jaakko, [Minimax ja alfa-beta-karsinta](https://jyx.jyu.fi/bitstream/handle/123456789/58204/1/URN%3ANBN%3Afi%3Ajyu-201805292875.pdf), 28.5.2018, Tietotekniikan kandidaatintutkielma.

[^3]: Hussain Syed, Hameed Usman, [Minimax with alpha-beta pruning (Connect-4 game)](https://www.academia.edu/41561708/Minimax_with_alpha_beta_pruning_connect_4_game_)
