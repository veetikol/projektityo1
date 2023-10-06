import random
import mysql.connector
import sqlyhteys


import random
yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='aitog',
    autocommit=True
    )



def maat():
    sql = "SELECT country.name, airport.name FROM country, airport"
    sql += " WHERE airport.iso_country = country.iso_country AND country.continent = 'EU' AND airport.type = 'large_airport'"
    kursori = yhteys.cursor(buffered=True)
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos



'''def maaLentoSanakirja():
    sql = "SELECT country.name, airport.name FROM country, airport"
    sql += " WHERE airport.iso_country = country.iso_country AND country.continent = 'EU' AND airport.type = 'large_airport'"
    sql += " ORDER by RAND()"
    kursori = yhteys.cursor(buffered=True)
    kursori.execute(sql)
    countries = {}
    while len(countries) < 37:  # tämä järjestää kaikki maat sanakirjaan
        tulos = kursori.fetchone()
        if tulos[0] != countries:
            countries[tulos[0]] = tulos[1]
    return countries'''

'''poistaMaa = maaLentoSanakirja()
tulos = maat()
if tulos in poistaMaa:
    print(tulos)
    poistaMaa.pop(tulos)'''

print(poistaMaa)