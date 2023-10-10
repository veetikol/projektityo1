import random
import mysql.connector
import sqlyhteys

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='veetikol',
    autocommit=True
    )

def maat():
    for x in listamaista:
        print(x, listamaista[x])
        listamaista.pop(x)
        break



def maaLentoSanakirja():
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
    return countries

listamaista = maaLentoSanakirja()


