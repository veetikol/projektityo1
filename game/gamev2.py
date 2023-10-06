import random
from haeVihje import haevihje
from kuljettumatka import calculateDistance
from maaPicker import maat
from sqlyhteys import yhteys
from Pelaajavalinnat import pelaajavalinta




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
rahat = 1000
sijainti = maalista[listamuuttuja]
listamuuttuja += 1

while True:
    print(f"The first country you land in is: {sijainti}! You have a lot of fun touring the different attractions there.")
    print(f"You have arrived to {sijainti} Airport and now you are to guess the next country.")
    print("Your first clue:")
    print(haevihje(päämäärä))
    pelaajavalinta()

