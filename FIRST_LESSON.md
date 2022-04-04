# 1. Haladó óra

## Python CleanCode (szép,tiszta, jól olvasható kód) alapelvek

### 1. Modul felépítése

1. importok
2. osztályok
3. metódusok
4. main metódus (if \_\_name__ == '\_\_main__':)

### 2. Elnevezések és kódolási konvenciók (https://realpython.com/python-pep8/)

1. Értelmes, lehetőleg angol változó és metódus nevek
2. Változók, függvények kisbetűsek, a szavak _ vannak elválasztva (pl.: my_function())
3. Osztálynevek nagybetűvel kezdődnek és CamelCase írásmód! (pl.: MyClass)
4. Konstans értéket tároló változók csupa nagybetű! (pl.: MY_CONSTANT)

### 3. További betartandó szabályok, tippek

1. Metódusoknál lehetőleg használjunk paramétereket és visszatérési értéket
2. Print utasítás csak a main() metódusban legyen, itt történjen az interakció a felhasználóval
3. Minden metódus lehetőleg egy dologért legyen felelős. Tipp, ha egy mondattal le tudod írni, hogy mit csinál a
   metódusod és nem használod benne az "és" vagy "vagy" kötőszavakat akkor jó vagy.
4. Figyeljünk arra, hogy a metódus ami az osztályon dolgozik az ott is legyen, minden elemnek megvan a maga feladata!

__Elsőre ezekre a dolgokra nehéz lesz figyelni, de próbálj meg törekedni rá. Ezek azok a dolgok, amik miatt ki fogsz
emelkedni a többi fejlesztő közül! Egy idő után ezek a dolgok rutinná fognak válni!__

## Egy kis algoritmizálás
Írj egy adott számról eldönti, hogy bővelkedő szám-e. Nézd meg a Wikipédián, hogy mit jelent a bővelkedő szám. 

## Objektum orientált programozás letisztázása (ismétlés)

    1. Mi az osztály?
    2. Mi az objektum?
    3. Attribútumok (fields), metódusok, \_\_init__ metódus?

Példa: Human osztály, név és életkor attribútummal és bemutatkozás metódussal.

#### Újdonságok
    1. Osztály típusú attribútumok pl.: Address
    2. Referenciák , immutable és mutable objektumok(elmélet)

## Feladat:

Készíts egy `Passenger` nevű osztályt, mely egy repülőgép utasát fogja reprezentálni. Minden utasnak van egy neve, egy
jegyazonsítója (szöveg) és egy szám típusú mezője, ami azt mutatja, hogy milyen osztályon utazhat. (1.- First Class 2.-
Business 3. - Economy)
<br>

Készíts egy `Flight` nevű osztályt, mely egy repülőt reprezentál. Minden repülőnek legyen egy járatszáma (szöveg), egy
uti célja és utasok listája! Ezek közül csak az első kettőt kapja meg az `init` metódusban a passengers attribútum egy
üres lista legyen. Legyen az osztályban egy metódus, amivel utast lehet hozzáadni a listához, de ellenőrízük, hogy ha már van egy jegyszámmal rendelkező utas, akkor még egy ugyanolyat ne adhassunk hozzá <br>


A `main` metódusban készíts egy airport nevű listát. Ebbe vegyél fel pár repülőgépet és azokba pár utast.

A következő részfeladatokat a `main` metóduson kívül oldd meg.<br>
* Készíts egy metódust, ami visszaadja azt a __járatot__ amin a legtöbb utas utazik. 
* Készíts egy metódust, ami visszaadja azokat a járatokat egy listában, amin van első osztály. (Ezt onnan tudjuk, hogy van rajta utas aki 1. értékű)
* Készíts egy metódust, ami egy utas jegykódja alapján visszaadja, hogy az az utas hova utazik. (Tesztelheted úgy hogy a jegykódot a felhasználótól kéred be a `main`-ben)
* Egy repülőgépben mindig a magasabb osztállyal rendelkező utasnak van joga előbb felszálni. Készíts egy metódust, ami bekér egy járatszámot és ellenőrzi, hogy azon a járaton a feltétel teljesült-e.
* Készíts egy metódust, ami az összes járaton ellenőrzi az előző feltételt. 
