import random
import mysql.connector
import sqlyhteys


def maat():
    sql = "SELECT country.name, airport.name FROM country, airport"
    sql += " WHERE airport.iso_country = country.iso_country AND country.continent = 'EU' AND airport.type = 'large_airport'"
    sql += " ORDER by RAND()"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchone()
    maalista = []
    return tulos

