# 3. Haladó Óra

A mai órán egy olyan alkalmazást fogunk készíteni, ahol az adatokat az internetről szedjük össze. 

## Elmélet
* Szerver-Kliens kommunikáció
* HTTP kérések (GET, POST, PUT, DELETE), mai órán csak GET
* Json formátum

## Gyakorlat
1. Menj fel a `https://openweathermap.org/` oldalra és regisztrálj
2. Másold ki az API kulcsodat
3. Minta kód:

```python
import requests

API_KEY = "my-api-key"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f'{BASE_URL}?appid={API_KEY}&q={city}'
response = requests.get(request_url)
if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = data['main']['temp'] - 273.15
    print(weather,temperature)
else:
    print("An error occured.")
```

### Feladat
1. Készíts egy listát 10 általad kedvelt város nevével és írd ki a képernyőre, hogy melyik városban volt a legmelegebb!
2. Az `https://apifootball.com/` api segítségével számold össze, hogy a kedvenc csapatod, hány gólt szerzett 2022-ben! VIgyázz először le kell kérned a country id-t majd leauge_id-t! 
3. (Nehéz) Számold ki, hogy mennyi pontott szerzett a kedvenc csapatod és ellenőrizd a standings-ben, hogy jól számoltál-e!
