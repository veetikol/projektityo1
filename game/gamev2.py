import random
from kuljettumatka import calculateDistance
from maaPicker import maat
import Vihjeet

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
    print(f"\033[92mYou had a lot of fun in your journey through Europe.\033[0m")
    print(" ")
    print(f"\033[92mHowever, you ended up flying a total of \033[91m{kuljettumatka} kilometers\033[0m")
    print(" ")
    print(f"\033[92mTravelling with a plane is harmful for the environment, and you ended up using a lot of natural resources\033[0m")
    print(" ")
    print(f"\033[92mFor your future travels, consider using other methods of travelling :)\033[0m")


def pelaajavalinta():
    print(f"\033[96mYou can either buy a new tip for 100 euros or guess a country\033[00m")
    syöte = input("Type \033[94m(buy)\033[00m to buy a tip or \033[94m(guess)\033[00m to guess a country: ")

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
                print("")
                print(f"\033[92mNew tip!\033[00m")
                printtivihje = haevihje(päämäärä)
                print(f"\033[93m{printtivihje}\033[00m")
                rahat -= 100
                print(f"Your money: \033[92m{rahat} euros\033[0m")
                print("")
            #TÄhän alle se calculate
            else:
                print("")
                print(f"\033[91mYour destination is {päämäärä}. You will be fined 100 euros\033[0m")
                rahat -= 100
                if rahat < 100:
                    print(f"\033[91mGame Over\033[0m")
                    break
                print(f"\033[92mFlying to your new destination, the ticket costs 100 euros...\033[0m")
                kuljettumatka += int(calculateDistance(str(lentokenttälista[visitedAirport1]), str(lentokenttälista[visitedAirport2])))
                visitedAirport1 += 1
                visitedAirport2 += 1
                print(f"You have traveled \033[95m{kuljettumatka} kilometers\033[0m so far")
                rahat -= 100
                print(f"Your money: \033[92m{rahat}\033[0m")
                sijainti = päämäärä
                listamuuttuja += 1
                päämäärä = maalista[listamuuttuja]
                vihjeindeksi = 0
                print(f"\033[92mNew tip!\033[0m")
                printtivihje = haevihje(päämäärä)
                print(f"\033[93m{printtivihje}\033[0m")
            if rahat < 100:
                break
            syöte = input(f"Type \033[94m(buy)\033[0m to buy a tip, or \033[94m(guess)\033[0m to guess a country: ")
        elif syöte.capitalize() == "Guess":
            syöte2 = input(f"Either write the name of the country or type \033[94m(list)\033[0m to print a list of possible countries: ")
            if syöte2.capitalize() == "List":
                print(f"\033[95mList of countries:\033[00m")
                for maa in maalista:
                    print(maa)
                print(" ")
                syöte = input("Type \033[94m(buy)\033[00m to buy a tip, or \033[94m(guess)\033[00m to guess a country: ")
                syöte2 = None
            elif syöte2.lower() == päämäärä:
                print(f"\033[92mCongratulations, you guessed the right country!\033[0m")
                print("\033[96mYou were rewarded 100 euros for answering correctly\033[0m")
                print("")
                print("Flying to your new destination...")
                kuljettumatka += int(calculateDistance(str(lentokenttälista[visitedAirport1]), str(lentokenttälista[visitedAirport2])))
                visitedAirport1 += 1
                visitedAirport2 += 1
                print(f"You have traveled \033[95m{kuljettumatka} kilometers\033[0m so far")
                sijainti = päämäärä
                rahat += 100
                vihjeindeksi = 0
                listamuuttuja += 1
                if listamuuttuja == 37:
                    break
                päämäärä = maalista[listamuuttuja]
                print(f"Your money currently: \033[92m{rahat} euros\033[0m")
                print(" ")
                if rahat < 100:
                    print("You have made it to your destination, but your money ran out. Game Over.")
                    break
                break
            elif syöte2.lower() != päämäärä and syöte2.lower() in maalista:
                print("")
                print(f"\033[91mYou guessed the wrong country!\033[0m")
                print(f"\033[91mYou have been fined 100 euros.\033[0m")
                rahat -= 100
                print(f"Your money: \033[92m{rahat} euros\033[0m")
                print(" ")
                syöte = input(f"Type \033[94m(buy)\033[0m to buy a tip, or \033[94m(guess)\033[0m to guess a country: ")
            else:
                print(f"\033[91mThe country you entered is not an option\033[0m")
                print(" ")
                syöte = input("Type \033[94m(buy)\033[0m to buy a tip, or \033[94m(guess)\033[0m to guess a country: ")
        else:
            print(f"\033[91mUnknown command, please try again\033[0m")
            print(" ")
            syöte = input("Type \033[94m(buy)\033[0m to buy a tip, or \033[94m(guess)\033[0m to guess a country: ")
    return

def instructions():
    print("You are travelling in Europe. Your parents have planned a route for you through various countries, "
        "and given you 1000 euros for expenses.")
    print("When you arrive at an airport you are tasked with guessing the name of the next country in your route. ")
    print("You are given one hint at first, and you can buy more hints for 100 euros with the money you've been given.")
    print("After 3 tries, you will be given a sanction of 100 euros and flown to the next country.")

while True:
    instructions()
    readyInput = input(f"Are you ready to begin? (\033[92my\033[0m/\033[91mn\033[0m): ")
    if readyInput == "n":
        print("Here are the instructions again: ")
        instructions()
    else:
        break
print("")
print(f"\033[96mYour journey begins!\033[0m")

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
print(f"The first country you land in is: \033[91m{sijainti}\033[0m! You have a lot of fun touring the different attractions there.")
print(f"You have arrived at \033[94m{lentokenttälista[visitedAirport1]}\033[0m of \033[91m{sijainti}\033[0m and now you are to guess the next country.")
print(" ")
while True:
    if rahat < 100:
        print(f"\033[91mYou have ran out of money. Game over\033[0m")
        break
    if listamuuttuja == 37:
        print(f"\033[92mCongratulations, you have travelled through Europe. You have won the game!\033[0m")
        endmessage()
        break
    printtivihje = haevihje(päämäärä)
    print(f"Your clue for your next country is: ")
    print(f"\033[93m{printtivihje}\033[0m")
    print("")
    pelaajavalinta()
