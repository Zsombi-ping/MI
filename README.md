# Legrövidebb út egy aknamezőn
Adott egy n*m-es pálya és azon tetszőleges mennyiségű akna. Úgy kell eljutni a pálya bal oldaláról a jobb oldalára hogy ne lépjünk egy akna, vagy annak közelébe se. 
(Az akna csak akkor robban, hogy ha egy felette, alatta vagy egy tőle jobbra, balra lévő mezőn állunk.)

Két algoritmus segítségével oldjuk meg:
* nyers backtracking algoritmus -> futási idő: 0,135 ms
* backtracking + MVR + forward checking algoritmus -> futási idő: 0,06 ms

Készítették:
* Dániel Zsombor
* Hegyi Botond - Sámuel