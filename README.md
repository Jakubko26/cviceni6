Python projekt zameraný na prácu s funkciami, modulmi, testovaním a vizualizáciou dát.
Program analyzuje dve kružnice a určí, či sa pretínajú a koľko majú prienikov.

Okrem výpočtu program dokáže kružnice aj vykresliť do grafu pomocou knižnice matplotlib.

⸻

Funkcionalita

Program dokáže:
	•	vypočítať Euklidovskú vzdialenosť medzi stredmi kružníc
	•	porovnať vzdialenosť so súčtom a rozdielom polomerov
	•	určiť počet prienikov:
	•	0 – kružnice sa nepretínajú
	•	1 – kružnice sa dotýkajú
	•	2 – kružnice sa pretínajú
	•	vypísať výsledok do terminálu
	•	vykresliť kružnice do grafu

Štruktúra projektu: 

cviceni6
│
├── circle_stats.py
├── circle_intersection.py
├── circles_intersection_draw.py
│
├── tests
│   └── test_circle_stats.py

Súbory

circle_stats.py
Obsahuje matematické funkcie:
	•	radius_sum(r1, r2)
	•	euclid_distance(x1, y1, x2, y2)
	•	has_intersection(circle_1, circle_2)

Tieto funkcie určujú, či sa kružnice pretínajú.

⸻

circle_intersection.py
Hlavný skript programu.

Program:
	•	definuje dve kružnice
	•	zavolá funkciu has_intersection
	•	vypíše výsledok do terminálu
	•	zobrazí graf kružníc

⸻

circles_intersection_draw.py
Obsahuje funkciu:
draw_data(circle_1, circle_2)

Funkcia vykreslí kružnice pomocou knižnice matplotlib.

⸻

tests/test_circle_stats.py
Obsahuje testy funkcií pomocou knižnice pytest.
Testy overujú správnosť funkcií:
	•	has_intersection
	•	radius_sum

Autor :
Jakub Michalík
