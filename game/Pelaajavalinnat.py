rahat = 0

def rahatsekki(rahat):
    print(f"You have currently {rahat} euros")
    return


def maatsekki(rahat, location, goal):
    if location == goal:
        print("Congratulations, you have arrived at the right country!")
        print("You have been awarded 100 euros!")
        rahat += 100
    else:
        print("This country you have arrived at is not the correct country")
        # TÄhän pitänee tehdä, että se hakee seuraavan vihjeen.
    return

def pelaajavalinta(sijainti, maaLista, rahat, tavoite):
    print("You can either buy a new clue for 100 euros, or fly to a new country.")
    syöte = input("Type (buy) to buy a new clue or (fly) to fly to a new country: ")
    while true:
        if syöte == "buy":
            #Tähän se, että haetaan uusi vihje kohdemaasta
        if syöte == "fly":
            maa = input("Type the name of the country you want to fly to: ")
            if maa in #lista maista:
                sijainti = maa
                break
            else:
                syöte = input("You have typed an invalid country, please try again: ")

rahatsekki()