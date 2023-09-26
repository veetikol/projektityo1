from geopy.distance import geodesic
import mysql.connector
import sqlyhteys
from kuljettumatka import calculateDistance
from SqlKoodiMaaRand import maat
from Pelaajavalinnat import maatsekki, pelaajavalinta, maatsekki
import Vihjeet


rahat = 0 # Rahan määrää pitänee kontrolloida jokaisen funktion sisällä.
tavoite = maat() # Tämä määritellään sql-haulla
vihjeet # Tämä on siis lista vihjeitä
tavoitemaa is None # Eli tämä haetaan sql-haulla.

pelaajanimi = input(f"Welcome! What's your name?: ")
print(f"Hello {pelaajanimi}!")

def instructions():
    print("You are travelling in Europe. Your parents have planned a route for you through various countries, "
        "and given you 1000 euros for expenses.")
    print("When you arrive at an airport you are tasked with guessing the name of the next country in your route. ")
    print("You are given one hint at first, and you can buy more hints with the money you've been given.")
    print("After 3 tries, you will be given a sanction of 5 euros and flown to the next country.")

while True:
    readyInput = input("Are you ready to begin? (y/n): ")
    if readyInput == "n":
        print("Here are the instructions again: ")
        instructions()
    else:
        break

print("Your journey begins!")
print(f"The first country you land in is: {sijainti}! You have a lot of fun touring the different attractions there.")

while True:
    print(f"")





'''Tähän tulee siis funktio, joka arpoo aloitusmaan'''
'''Tähän tulee funktio, joka arpoo kohdemaan'''
'''Pelaaja etenee vaiheeseen, jossa hän voi ostaa uuden vihjeen, tai lentää kohteeseen'''
'''Eli syötteen perusteella joko funktio, joka antaa uuden vihjeen, tai sitten funktio, joka siirtää pelaajan valittuun maahan'''
'''Siirtymisen jälkeen funktio, joka tsekkaa, onko pelaaja oikeassa maassa.'''


