# Legrövidebb út egy aknamezőn
Adott egy n*m-es pálya és azon tetszőleges mennyiségű akna. Úgy kell eljutni a pálya bal oldaláról a jobb oldalára hogy ne lépjünk egy akna, vagy annak közelébe se. 
(Az akna csak akkor robban, hogy ha egy felette, alatta vagy egy tőle jobbra, balra lévő mezőn állunk.)

Két algoritmus segítségével oldjuk meg:
* nyers backtracking algoritmus -> értékadások száma: 13034
* backtracking + MVR + forward checking algoritmus -> értékadások száma: 8846

Készítették:
* Dániel Zsombor
* Hegyi Botond - Sámuel