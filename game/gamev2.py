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
            vihjenyt = str({Vihjeet.countries[päämäärä][vihjeindeksi]})
            vihjeindeksi += 1
    return vihjenyt

def endmessage():
    print(" ")
    print("You had a lot of fun in your journey through Europe.")
    print(" ")
    print(f"However, you ended up flying a total of {kuljettumatka} kilometers")
    print(" ")
    print("Travelling with a plane is harmful for the environment, and you ended up using a lot of natural resources")
    print(" ")
    print("For your future travels, consider using other methods of travelling :)")


def pelaajavalinta():
    print("You can either buy a new tip for 100 euros or guess a country")
    syöte = input("Type (buy) to buy a tip or (guess) to guess a country: ")

    global sijainti
    global rahat
    global päämäärä
    global listamuuttuja
    global vihjeindeksi
    global visitedAirport1
    global visitedAirport2
    global kuljettumatka

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
                print("Flying to your new destination, the ticket costs 100 euros...")
                kuljettumatka += int(calculateDistance(str(lentokenttälista[visitedAirport1]), str(lentokenttälista[visitedAirport2])))
                visitedAirport1 += 1
                visitedAirport2 += 1
                print(f"You have traveled {kuljettumatka} kilometers so far")
                rahat -= 100
                print(f"Your money: {rahat}")
                sijainti = päämäärä
                listamuuttuja += 1
                päämäärä = maalista[listamuuttuja]
                vihjeindeksi = 0
                print("New tip: ")
                printtivihje = haevihje(päämäärä)
                print(f"{printtivihje}")
            if rahat < 100:
                break
            syöte = input("Type (buy) to buy a tip, or (guess) to guess a country: ")
        elif syöte.capitalize() == "Guess":
            syöte2 = input("Either write the name of the country or type (list) to print a list of possible countries: ")
            if syöte2.capitalize() == "List":
                for maa in maalista:
                    print(maa)
                print(" ")
                syöte = input("Type (buy) to buy a tip, or (guess) to guess a country: ")
                syöte2 = None
            elif syöte2.lower() == päämäärä:
                print("Congratulations, you guessed the right country!")
                print("You were rewarded 100 euros for answering correctly")
                print("")
                print("Flying to your new destination...")
                kuljettumatka += int(calculateDistance(str(lentokenttälista[visitedAirport1]), str(lentokenttälista[visitedAirport2])))
                visitedAirport1 += 1
                visitedAirport2 += 1
                print(f"You have traveled {kuljettumatka} kilometers so far")
                sijainti = päämäärä
                rahat += 100
                vihjeindeksi = 0
                listamuuttuja += 1
                if listamuuttuja == 37:
                    break
                päämäärä = maalista[listamuuttuja]
                print(f"Your money currently: {rahat}")
                print(" ")
                if rahat < 100:
                    print("You have made it to your destination, but your money ran out. Game Over.")
                    break
                break
            elif syöte2.lower() != päämäärä and syöte2.lower() in maalista:
                #print("Flying to your new destination...") pitää työstää vielä
                print("You guessed the wrong country!")
                print("You have been fined 100 euros.")
                rahat -= 100
                print(f"Your money:{rahat}")
                print(" ")
                syöte = input("Type (buy) to buy a tip, or (guess) to guess a country: ")
            else:
                print("The country you entered is not an option")
                print(" ")
                syöte = input("Type (buy) to buy a tip, or (guess) to guess a country: ")
        else:
            print("Unknown commnd, please try again")
            print(" ")
            syöte = input("Type (buy) to buy a tip, or (guess) to guess a country: ")
    return




def instructions():
    print("You are travelling in Europe. Your parents have planned a route for you through various countries, "
        "and given you 1000 euros for expenses.")
    print("When you arrive at an airport you are tasked with guessing the name of the next country in your route. ")
    print("You are given one hint at first, and you can buy more hints for 100 euros with the money you've been given.")
    print("After 3 tries, you will be given a sanction of 100 euros and flown to the next country.")

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
visitedAirport1 = 0
visitedAirport2 = 1
sijainti = maalista[listamuuttuja]
listamuuttuja += 1


päämäärä = maalista[listamuuttuja]

'''print(päämäärä)'''
print(f"The first country you land in is: {sijainti}! You have a lot of fun touring the different attractions there.")
print(f"You have arrived at {lentokenttälista[visitedAirport1]} of {sijainti} and now you are to guess the next country.")
print(" ")
while True:
    if rahat < 100:
        print("You have ran out of money. Game over")
        break
    if listamuuttuja == 37:
        print("Congratulations, you have travelled through Europe. You have won the game!")
        endmessage()
        break
    printtivihje = haevihje(päämäärä)
    print(f"Your clue for your next country is: ")
    print(f"{printtivihje}")
    print("")
    pelaajavalinta()



# While loopin ulkopuolelle sitten se funktio, joka laskee lentomatkat yhteen
# Eli tehtävänä vielä pelaajavalinta-funktion läpikäyminen, lasketun matkan ilmoittaminen järkevästi
# Lisäksi pitää ratkoa se UK ja pohjois-macedonia-ongelma