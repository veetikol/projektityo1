import random
from haeVihje import haevihje
from kuljettumatka import calculateDistance
from maaPicker import maat
from maaPicker import yhteys
import Vihjeet

def haevihje(päämäärä):
    global vihjeindeksi
    for a in Vihjeet.countries:
        if a == päämäärä:
            print(Vihjeet.countries[päämäärä][vihjeindeksi])
            vihjeindeksi += 1
    return


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
                haevihje(päämäärä)
                rahat -= 100
                print(f"Your money: {rahat} euros")
            else:
                print(f"Your destination is {päämäärä}. You will be fined 100 euros")
                rahat -= 100
                print(rahat)
                if rahat < 100:
                    print("Game Over")
                    break
                print("Flying to your new destination...")
                sijainti = päämäärä
                listamuuttuja += 1
                päämäärä = maalista[listamuuttuja]
                vihjeindeksi = 0
                print("New tip: ")
                haevihje(päämäärä)
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
                if rahat < 100:
                    print("You have made it to your destination, but your money ran out. Peli päättyy")
                    break
                break
            elif syöte2 != päämäärä and syöte2 in maalista:
                print("Flying to your new destination...")
                print("You guessed the wrong country!")
                rahat -= 100
                print(f"Your money:{rahat}")
                print("Type (buy) to buy a tip, or (guess) to guess a country: ")
            else:
                print("The country you entered is not an option")
                syöte = input("Type (buy) to buy a tip, or (guess) to guess a country: ")
        else:
            print("Shitty function")
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
while True:
    print(f"The first country you land in is: {sijainti}! You have a lot of fun touring the different attractions there.")
    print(f"You have arrived to {sijainti} Airport and now you are to guess the next country.")
    print("Your first clue:")
    print(haevihje(päämäärä))
    pelaajavalinta()

