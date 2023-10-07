import random
from kuljettumatka import calculateDistance
from maaPicker import maat
from maaPicker import yhteys
import Vihjeet
from geopy.distance import geodesic

def haevihje(päämäärä):
    global vihjeindeksi
    vihjenyt = None
    for a in Vihjeet.countries:
        if a == päämäärä:
            vihjenyt = {Vihjeet.countries[päämäärä][vihjeindeksi]}
            vihjeindeksi += 1
    return vihjenyt

'''def calculateDistance(port1, port2):
    search1 = f"SELECT latitude_deg, longitude_deg FROM airport"
    search1 += f" WHERE name = '{port1}';"
    search2 = f"SELECT latitude_deg, longitude_deg FROM airport"
    search2 += f" WHERE name = '{port2}';"
    kursori = yhteys.cursor()
    kursori.execute(search1)
    tulos1 = kursori.fetchall()
    kursori.execute(search2)
    tulos2 = kursori.fetchall()
    distance = geodesic(tulos1, tulos2).km
    return distance'''


def pelaajavalinta():
    print("You can either buy a new tip for 100 euros or guess a country")
    syöte = input("Type (buy) to buy a tip or (guess) to guess a country: ")

    global sijainti
    global rahat
    global päämäärä
    global listamuuttuja
    global vihjeindeksi

    while True:
        if rahat < 100:
            print("Game Over")
            break
        if syöte.capitalize() == "Buy":
            if vihjeindeksi <= 2:
                print("New tip!")
                printtivihje = haevihje(päämäärä)
                print(f"{printtivihje}")
                rahat -= 100
                print(f"Your money: {rahat} euros")
            #TÄhän alle se calculate
            else:
                print(f"Your destination is {päämäärä}. You will be fined 100 euros")
                rahat -= 100
                if rahat < 100:
                    print("Game Over")
                    break
                print("Flying to your new destination...")
                rahat -= 100
                print(rahat)
                sijainti = päämäärä
                listamuuttuja += 1
                päämäärä = maalista[listamuuttuja]
                vihjeindeksi = 0
                print("New tip: ")
                printtivihje = haevihje(päämäärä)
                print(f"{printtivihje}")
            if rahat < 100:
                print("Your money ran out, game over")
                break
            syöte = input("Type (buy) to buy a tip, or (guess) to guess a country: ")
        elif syöte.capitalize() == "Guess":
            syöte2 = input("Either write the name of the country or type (list) to print a list of possible countries: ")
            if syöte2.capitalize() == "List":
                for maa in maalista:
                    print(maa)
                syöte = input("Type (buy) to buy a tip, or (guess) to guess a country: ")
                syöte2 = None
            elif syöte2.capitalize() == päämäärä:
                print("Congratulations, you guessed the right country!")
                print("Flying to your new destination...")
                sijainti = päämäärä
                rahat += 100
                vihjeindeksi = 0
                listamuuttuja += 1
                päämäärä = maalista[listamuuttuja]
                print(rahat)
                print(f"Your first clue:")
                printtivihje = haevihje(päämäärä)
                print(f"{printtivihje}")
                if rahat < 100:
                    print("You have made it to your destination, but your money ran out. Game Over.")
                    break
                break
            elif syöte2.capitalize() != päämäärä and syöte2.capitalize() in maalista:
                #print("Flying to your new destination...") pitää työstää vielä
                print("You guessed the wrong country!")
                print("You have been fined 100 euros.")
                rahat -= 100
                print(f"Your money:{rahat}")
                print("Type (buy) to buy a tip, or (guess) to guess a country: ")
            else:
                print("The country you entered is not an option")
                syöte = input("Type (buy) to buy a tip, or (guess) to guess a country: ")
        else:
            print("Shitty command")
            syöte = input("Type (buy) to buy a tip, or (guess) to guess a country: ")
    return




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

sqlhaku = maat()
random.shuffle(sqlhaku)
maalista = []
lentokenttälista = []
for x in sqlhaku:
    maalista.append(x[0])

for y in sqlhaku:
    lentokenttälista.append(y[1])

listamuuttuja = 0
vihjeindeksi = 0
kuljettumatka = 0
rahat = 1000
sijainti = maalista[listamuuttuja]
listamuuttuja += 1

print(rahat)
print(maalista)
print(lentokenttälista)
print(sijainti)

päämäärä = maalista[listamuuttuja]

print(päämäärä)
print(f"The first country you land in is: {sijainti}! You have a lot of fun touring the different attractions there.")
print(f"You have arrived to {sijainti} Airport and now you are to guess the next country.")
printtivihje = haevihje(päämäärä)
print(f"Your clue for your next country is: {printtivihje}")
while True:
    if rahat < 100:
        print("You have ran out of money. Game over")
        break
    pelaajavalinta()
    visitedAirport1 = 0
    visitedAirport2 = 1
    kuljettumatka += int(calculateDistance(lentokenttälista[visitedAirport1], lentokenttälista[visitedAirport2]))
    print(kuljettumatka)
    visitedAirport1 += 1
    visitedAirport2 += 1

# While loopin ulkopuolelle sitten se funktio, joka laskee lentomatkat yhteen