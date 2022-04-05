# 2. Haladó óra

## Adatszerkezetek és a list comprehension

## Elmélet
Eddig az összetett adatszerkezetek közül csak a listával foglalkoztunk, de van még pár amit érdemes megismernünk
ahhoz, hogy hatékony kódot írjunk. 

### Lista
* Az adatokat egymás után (láncolva) tároljuk
* Az elemek indexelhetők (Tudunk hivatkozni rájuk sorszámmal)
* A lista mutable, ami azt jelenti, hogy megváltoztatható az állapota, azaz tudunk elemet kivenni és hozzáfűzni. 
* Hozzáfűzni az `append()` metódus segítségével tudunk, az utolsó elemet kivenni a `pop()` művelettel. 
* for ciklussal könnyen bejárható

### Tuple
* Hasonló a listához, úgy kell elképzelni min vesszővel elválasztott adatok sorozatát.
* Jelölésben a ( ) zárójeleket használjuk
* A tuple immutable tehát nem megváltoutatható az állapota
* Ha több értékkel térek vissza egy metódusban az is tuple-ként jön vissza. 

### Set
* Hasonló a listához, de egy elemet csak egyszer tartalmazhat
* Jelölésben a {} használjuk.
* Üres halmaz létrehozása: `my_set = set()`

### Dictiorany
* Kulcs érték párokat tartalmaz
* A kulcs az lehet szöveg vagy szám (akár tuple is, de nem javaslom)
* Egy kulcshoz mindig egy érték tartozik
* Létrehozása : `  my_dict = {1:  "John", 2: "Jane"}` vagy `my_dict = {"alma":  5, "körte": 4}`
* Elemre hivatkozás: `my_dict["körte"]`
* Bejárása `for k v in my_dict.items()`
* Üres dictionary létrehozása `my_dict = dict()` vagy `my_dict = {}`
* Kulcsok lekérése a `my_dict.keys()` metódussal lehet az `in` kulcsszóval lehet ellenőrizni, hogy szerepel-e a kulcsok között egy bizonyos elem. 


## Újdonságok
* Pythonban ha be szeretnénk járni egy listát és szükségünk van az index-re és az elemre is akkor azt megtehetjük így 
`for index item in enumerate(lista)`
* Gyors egyzserű feladatok, szűrés és keresés feladatokat tudunk vele megoldani.
Szintaxis: `newlist = [expression for item in iterable if condition == True]`


## Feladatok:
Az alábbi feladatoknál törekedj az újonnan megismert eszközök használatára! Minden feladatot külön python állományban készíts el!<br>

#### 1. feladat
Készíts egy `User` nevű osztályt. Minden felhasználónak legyen egy felhasználó neve, egy e-mail címe
és egy jogosultsága ("admin", "editor" vagy "normal_user") , mindhárom szöveges típusú. A teszteléshez készíthetsz egy fájlt pár minta adattal. 
* Készíts egy metódust ami paraméterül vár egy jogosultság típust és visszaadja egy listában a felhasználóneveket ezzel a jogosultsággal.
* Készíts egy metódust ami eldönti, hogy szerepel-e kétszer ugyanaz a username a listában. 
* Gyűtsd ki egy megfelelő adatszerkezetbe, hogy jogosultságonként hány darab felhasználó van!

### 2. feladat

Írj egy metódust, ami paraméterül vár egy szöveget és meghatározza, hogy hány különböző karakter szerepel a szövegben!
Írj egy másik metódust, ami visszaadja, hogy melyik a leggyakrabban előforduló karakter!

### 3. feladat




