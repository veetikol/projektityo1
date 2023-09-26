from geopy.distance import geodesic
import mysql.connector
import sqlyhteys
from kuljettumatka import calculateDistance

rahat = 0 # Rahan määrää pitänee kontrolloida jokaisen funktion sisällä.
pelaajanimi is None # input
sijainti is None # Tämä määritellään sql-haulla
vihjeet # Tämä on siis lista vihjeitä
tavoitemaa is None # Eli tämä haetaan sql-haulla.

pelaajanimi = input(f"Tervetuloa pelaamaan! Mikä on nimesi?: ")
print(f"Hei {pelaajanimi}!")
def instructions():
    print("Olet matkustamassa Europassa. Vanhempasi ovat suunnitelleet sinulle reitin eri maiden läpi, "
        "ja antaneet sinulle 1000 euroa kustannuksiin.")
    print("Saavuttuasi lentokentälle tehtäväsi on arvata seuraavan kohteen nimi. Saat tehtävän alussa yhden vihjeen,"
      "ja voit halutessasi ostaa lisää vihjeitä sinulle annetuilla rahoilla. 3 yrityksen jälkeen sinulta veloitetaan"
      "sakko (5 euroa)")

readyInput = input("Oletko valmis aloittamaan? (k/e): ")
if readyInput == "e":
    instructions()
else:
    # tähän funktio, joka jatkaa peliä




'''Tähän tulee siis funktio, joka arpoo aloitusmaan'''
'''Tähän tulee funktio, joka arpoo kohdemaan'''
'''Pelaaja etenee vaiheeseen, jossa hän voi ostaa uuden vihjeen, tai lentää kohteeseen'''
'''Eli syötteen perusteella joko funktio, joka antaa uuden vihjeen, tai sitten funktio, joka siirtää pelaajan valittuun maahan'''
'''Siirtymisen jälkeen funktio, joka tsekkaa, onko pelaaja oikeassa maassa.'''


