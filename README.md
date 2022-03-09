# Pišek priznanja

Koda za generiranje priznanj za mentorje in udeležence Tekmovanja v programiranju z delčki - Pišek.

### Windows

Shranite oz. prenesite si vse datoteke v mapi `dist` ali pa zadnjo različico programa.

Mapa oz. ZIP datoteka vsebuje naslednje datoteke:
* mentor.svg - SVG datoteka z ozadjem priznanja za mentorje
* mentorji.txt - TXT datoteka s podatki o mentorjih (za zgradbo glej spodaj)
* priznanja2022.exe - generator priznanj za tekmovanje 2022
* tekmovalci.txt - TXT datoteka s podatki o tekmovalcih (za zgradbo glej spodaj)
* tekmovalec.svg - SVG datoteka z ozadjem priznanja za tekmovalce

### Mac OS X in Linux

Shranite si ZIP datoteko celotnega Github repozitorija. Poleg zgoraj omenjenih datotek iz podmape `dist` morate imeti še vsaj naslednji dve datoteki v osnovni mapi:
* priznanja.sh - skripta za poganjanje generatorja priznanj (podobno kot priznanja.bat za Windows)
* priznanja.py - generator priznanj napisan v programskem jeziku Python


## Ustvarjanje oz. generiranje priznanj

### Windows

1. V datoteki mentorji.txt in tekmovalci.txt vnesete ustrezne podatke o mentorjih in tekmovalcih (če je tekmovalec nastopal v več kategorijah, vnesete podatke za vsako kategorijo posebej - ena vrstica za vsako kategorijo)
2. Poženete generator priznanja2022.exe

### Mac OS X in Linux

1. Na sistemu morate imeti nameščen Python različice 3.x (testirano z različico 3.8)
2. Nato ustvarite virtualno okolje (_ang. virtual environment_):
   ```$ python -m venv ./venv```
3. Aktivirajte virtualno okolje:
    ```$ source ./venv/Scripts/activate```
4. Preverite ali vaša namestitev Pythona vsebuje `pip`:
   ```$ pip --version```
   sicer ga namestite:
   ```$ python -m pip install```
5. Namestite pythonove knjižnice oz. module v virtualno okolje - potrebne knjižnice so že navedene v datoteki requirements.txt (ki jo uporabite za namestitev modulov):
   ```$ pip install -r requirements.txt```
6. Deaktivirajte virtualno okolje:
   ```$ source ./venv/Scripts/deactivate```
7. Nastavite "execute" pravice datoteki priznanja.sh
8. Poženite datoteko priznanja.sh (ki bo aktivirala virtualno okolje, pognala generator in na koncu deaktivirala virtualno okolje).

Opombe:
* Če ukaza `python` in `pip` ne delujeta, ju poizkusite nadomestiti z ukazoma `python3` in `pip3`.
* Če si boste shranili celoten repozitorij iz Github-a lahko preskočite na korak 7.
* SVG in TXT datoteke z ozadji priznanj in podatki za priznanja morajo ostati v podami `dist`.

## Struktura TXT datotek

### mentorji.txt

Datoteka vsebuje imena in priimke mentorjev. Za vsakega mentorja v svoji vrstici.

Primer:
```
Janez Kranjski
Micka Kovačeva
```

### tekmovalci.txt

Datoteka vsebuje podatke o tekmovalcih v CSV obliki. Za vsakega tekmovalca v svoji vrstici. Če je tekmovalec tekmoval v več kategorijah, mora datoteka vsebovati po eno vrstico s podatki za vsako kategorijo.

Vsaka vrstica vsebuje naslednje podatke:
Ime in priimek tekmovalca, kategorija, številka priznanja

Primer:
```
Janez Novak,46z,12345
Lučka Potebuješ,46n,12346
Miša Kaja Lužar,79z,12347
Živa Šivič,79n,12348
Jona Čujež,SSz,12349
Leon Hrovat,SSn,12350
Janez Novak,46n,12351
```

Možne so naslednje kategorije:
* `46z`: 4. do 6. razred OŠ - začetniki,
* `46n`: 4. do 6. razred OŠ - napredni,
* `79z`: 7. do 9. razred OŠ - začetniki,
* `79n`: 7. do 9. razred OŠ - napredni,
* `SSz`: SŠ - začetniki,
* `SSn`: SŠ - napredni
