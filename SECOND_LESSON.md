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

### 1. feladat

Írj egy metódust, ami paraméterül vár egy szöveget és meghatározza, hogy hány különböző karakter szerepel a szövegben!
Írj egy másik metódust, ami visszaadja, hogy melyik a leggyakrabban előforduló karakter!


#### 2. feladat
Készíts egy `User` nevű osztályt. Minden felhasználónak legyen egy felhasználó neve, egy e-mail címe
és egy jogosultsága ("admin", "editor" vagy "normal_user") , mindhárom szöveges típusú. A teszteléshez a fájlt a resources könyvtárban találod.
* Készíts egy metódust, ami beolvassa a felhasználkat egy listába
* Készíts egy metódust ami paraméterül vár egy jogosultság típust és visszaadja egy listában a felhasználóneveket ezzel a jogosultsággal.
* Készíts egy metódust ami eldönti, hogy szerepel-e kétszer ugyanaz a username a listában. 
* Gyűtsd ki egy megfelelő adatszerkezetbe, hogy jogosultságonként hány darab felhasználó van!

Készíts egy `Product` nevű osztályt. Minden terméknek legyen egy egyedi azonosítója és egy neve.<br>
Fejleszd tovább úgy a `User` osztályt, hogy legyen benne egy `dictionary` aminek kulcsai termék kódok lesznek értékei
pedig darabszám. Készíts továbbá egy `add_product(self, product)` nevű metódust, ami a paraméterül kapott 
termékről eldönti, hogy szerepel, e már a felhasználó "kosarában", és ha igen akkor csak a darabszámot növeli, ha nem
akkor új termékként hozzáadja. 

* Készíts egy metódust, aminek segítségével előkészíthetjük a "normal_user"-ek rendeléseit. Azaz add vissza, hogy az összes normal user melyik termékből hányat rendelt.
* Készíts egy metódust, ami paraméterül vár egy számot és egy termékkódot és visszaadja azokat a felhasználókat, akik legalább a megadott mennyiséget rendelték a termékből.  










