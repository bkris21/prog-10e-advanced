# Projekt feladat

A feladatban egy város működését kell lemodellezned. Törekedj az eddig tanultak használatára. 

### Feladat
Készíts egy osztályt, ami egy város egy lakóját reprezetálja legyen a neve `Citizen`. Minden lakónak legyen egy neve,
és egy születési dátuma. (Dátumok kezeléséhez javaslom: https://www.w3schools.com/python/python_datetime.asp) <br>

Legyen egy `Building` nevű osztály is, melynek legyen egy címe, amit az `Address` osztály tárol (utca, házszám) és `Citizenek` listája. 

A `main` metódus fogja reprezentálni a város működését, itt legyen egy lista épületekkel. A listát fájlból vagy kézzel töltsd fel.
A következő feladatokat a `main` metóduson kívül oldd meg:
* Készíts egy metódust ami paraméterül vár egy utcanevet és visszaadja a benne lévő épületek listáját.
* Határozd meg, hogy hány nagycsaládos ház van a városban. (legalább 5 lakó)
* Határozd meg, hogy utcánként, hány épület van a városban
* Keresd meg azt az utcát, ahol a legtöbb lakó lakik
* Határozd meg, hogy korcsoportonként hány lakó lakik a városban. (0-18, 19-45, 46-64, 65-)
* Készíts egy metódust amiben megadjuk egy lakó adatait, add vissza a címét.
* Készíts egy metódust ami paraméterül vár egy életkort és visszaadja, hogy hány ilyenkorú ember lakik a városban.

