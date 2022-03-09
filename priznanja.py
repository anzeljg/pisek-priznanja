"""
Program za generiranje priznanj za sodelovanje na tekmovanju v programiranju
z delčki Pišek.

Ta program je prilagojen za pyinstaller bundle s katerim naredimo izvršljivo
.exe datoteko. To pomeni, da so poti zunanjih datotek nastavljene tako, da so
v isti mapi kot samostojni .exe, ki ga zgenerira pyinstaler.

Zunanje datoteke:
- mentor.svg      (SVG priznanje za mentorje)
- mentorji.txt    (CSV datoteka s podatki o mentorjih)
- tekmovalec.svg  (SVG priznanje za tekmovalce)
- tekmovalci.txt  (CSV datoteka s podatki o tekmovalcih)

"""

from svglib.svglib import SvgRenderer
from reportlab.graphics import renderPDF
from lxml import etree
import csv
import sys # za argument

prefix = ''
if len(sys.argv) > 1:
    prefix = '.\\' + sys.argv[1] + '\\'

def ustvari_priznanje(sola, oseba, mentor=False):
    if mentor:
        # naloži SVG datoteko
        path = prefix + 'mentor.svg'
        svg = open(path, 'r', encoding='utf-8').read()
        # zamenjaj privzete vrednosti
        svg = svg.replace('Osnovna šola z zelo dolgim imenom', sola)
        svg = svg.replace('Ime in Priimek', oseba)
        svg = svg.replace('1. do 12. februar 2021', termin)
        svg = svg.replace('1234567890', '')
        # nastavi ime PDF datoteke = ime mentorja
        filename = oseba
    else:
        # naloži SVG datoteko
        path = prefix + 'tekmovalec.svg'
        svg = open(path, 'r', encoding='utf-8').read()
        # zamenjaj privzete vrednosti
        svg = svg.replace('Osnovna šola z zelo dolgim imenom', sola)
        svg = svg.replace('Ime in Priimek', oseba[0])
        svg = svg.replace('9. razred', kategorija[oseba[1]])
        svg = svg.replace('1. do 12. februar 2021', termin)
        svg = svg.replace('1234567890', oseba[2])
        # nastavi ime PDF datoteke = ime tekmovalca
        filename = oseba[0] + " " + oseba[2]

    # razčleni XML/SVG iz besedilnega niza
    parser = etree.XMLParser(
        remove_comments=True, recover=True, resolve_entities=False
    )
    svg_root = etree.fromstring(bytes(svg, encoding='utf-8'), parser=parser)

    # pretvori v RLG risbo
    svgRenderer = SvgRenderer(path)
    priznanje = svgRenderer.render(svg_root)

    # risbo izriši v PDF datoteko
    renderPDF.drawToFile(priznanje, prefix + filename + '.pdf')


# tekmovalne kategorije
kategorija = {
    '46z': '4. do 6. razred OŠ - začetniki',
    '46n': '4. do 6. razred OŠ - napredni',
    '79z': '7. do 9. razred OŠ - začetniki',
    '79n': '7. do 9. razred OŠ - napredni',
    'SSz': 'SŠ - začetniki',
    'SSn': 'SŠ - napredni',
}

sola   = input('Vnesite polno ime šole: ')
termin = '31. januar do 11. februar 2022'


# preberi podatke o mentorjih iz datoteke 'mentorji.txt'
mentorji = []
with open(prefix + 'mentorji.txt', encoding='utf-8', newline='') as file:
    reader = csv.reader(file)
    mentorji = list(reader)

# ustvari priznanje za mentorje
print('Ustvarjam priznanje za mentorja ...')
for mentor in mentorji:
    print(" - ", mentor[0])
    ustvari_priznanje(sola, mentor[0], True)


# preberi podatke o tekmovalcih iz datoteke 'tekmovalci.txt'
tekmovalci = []
with open(prefix + 'tekmovalci.txt', encoding='utf-8', newline='') as file:
    reader = csv.reader(file)
    tekmovalci = list(reader)

# ustvari priznanja za tekmovalce
print('Ustvarjam priznanja za tekmovalce ...')
for tekmovalec in tekmovalci:
    print(" - ", tekmovalec[0], tekmovalec[2])
    ustvari_priznanje(sola, tekmovalec)


print('Končano. Vsa priznanja so ustvarjena.')
