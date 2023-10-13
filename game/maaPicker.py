from sqlyhteys import yhteys

def maat():
    sql = "SELECT LOWER(country.name), airport.name FROM country, airport"
    sql += " WHERE airport.iso_country = country.iso_country AND country.continent = 'EU' AND airport.type = 'large_airport' GROUP BY country.name"
    kursori = yhteys.cursor(buffered=True)
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos
