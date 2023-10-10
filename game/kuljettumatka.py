from geopy.distance import geodesic
from sqlyhteys import yhteys

def calculateDistance(port1, port2):
    search1 = f"SELECT latitude_deg, longitude_deg FROM airport"
    search1 += f" WHERE name = '{port1}' AND type = 'large_airport';"
    search2 = f"SELECT latitude_deg, longitude_deg FROM airport"
    search2 += f" WHERE name = '{port2}' AND type = 'large_airport';"
    kursori = yhteys.cursor()
    kursori.execute(search1)
    tulos1 = kursori.fetchone()
    kursori.execute(search2)
    tulos2 = kursori.fetchone()
    distance = geodesic(tulos1, tulos2).km
    return distance