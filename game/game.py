from geopy.distance import geodesic
import mysql.connector
import sqlyhteys
from kuljettumatka import calculateDistance
from maaPicker import maat, maaLentoSanakirja
from Pelaajavalinnat import maatsekki, pelaajavalinta, maatsekki
import Vihjeet
import haeVihje

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='veetik',
    autocommit=True
    )

rahat = 1000 # Rahan määrää pitänee kontrolloida jokaisen funktion sisällä.
sijainti = maat()[0]

pelaajanimi = input(f"Welcome! What's your name?: ")
print(f"Hello {pelaajanimi}!")

def instructions():
    print("You are travelling in Europe. Your parents have planned a route for you through various countries, "
        "and given you 1000 euros for expenses.")
    print("When you arrive at an airport you are tasked with guessing the name of the next country in your route. ")
    print("You are given one hint at first, and you can buy more hints with the money you've been given.")
    print("After 3 tries, you will be given a sanction of 5 euros and flown to the next country.")

while True:
    instructions()
    readyInput = input("Are you ready to begin? (y/n): ")
    if readyInput == "n":
        print("Here are the instructions again: ")
        instructions()
    else:
        break

print("Your journey begins!")

while True:
    #sijainti = maat()
    print(f"The first country you land in is: {sijainti}! You have a lot of fun touring the different attractions there.")
    print(f"You have arrived to {sijainti} Airport and now you are to guess the next country.")
    päämäärä = maat()
    poistaMaa.pop(päämäärä)
    if päämäärä in poistaMaa:
        päämäärä = maat()
        poistaMaa.pop(päämäärä)
    else:
        print("Congratulations, you have successfully completed your journey through Europe!")
    vihje = haeVihje(sijainti, 1)
    pelaajavalinta(sijainti, Vihjeet.country_names, rahat, päämäärä)







'''Tähän tulee siis funktio, joka arpoo aloitusmaan'''
'''Tähän tulee funktio, joka arpoo kohdemaan'''
'''Pelaaja etenee vaiheeseen, jossa hän voi ostaa uuden vihjeen, tai lentää kohteeseen'''
'''Eli syötteen perusteella joko funktio, joka antaa uuden vihjeen, tai sitten funktio, joka siirtää pelaajan valittuun maahan'''
'''Siirtymisen jälkeen funktio, joka tsekkaa, onko pelaaja oikeassa maassa.'''


