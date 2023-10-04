from haeVihje import haeVihje

rahat = 0

"""def rahatsekki(rahat):
    print(f"You have currently {rahat} euros")
    return"""


def maatsekki(rahat, location, goal):
    if location == goal:
        print("Congratulations, you have arrived at the right country!")
        print("You have been awarded 100 euros!")
        rahat += 100
    else:
        print("This country you have arrived at is not the correct country")
        # TÄhän pitänee tehdä, että se hakee seuraavan vihjeen.
    return

def pelaajavalinta(maaLista, päämäärä):
    print("You can either buy a new clue for 100 euros, or fly to a new country.")
    syöte = input("Type (buy) to buy a new clue or (guess) to make a guess: ")
    global rahat
    while True:
        if rahat < 100:
            print("You have ran out of money.")
            print("Game over.")
            break
        if syöte == "buy":
            haeVihje(päämäärä, 1)
        elif syöte == "guess":
            syöte2 = input("type the name of the country, or type (list) to get a full list of possible countries: ")
            if syöte2 == "list":
                print(maaLista)
                syöte = input("Type (buy) to buy a new clue or (guess) to make a guess: ")
            if syöte2 == päämäärä: #Tulostetaan onnitteluviesti, vaihdetaan sijainti ja vähennetään rahoista
                print("Congratulations! You have guessed the correct country")
                print("Flying to your new destination...")
                sijainti = päämäärä

                rahat -= 100
                break
            if syöte2 != päämäärä and syöte2 in maaLista: #Tsekataan, että arvaus on maalistassa, ja vähennetään rahoista.
                print("You have made an incorrect guess.")
                rahat -= 100
                syöte = input("Type (buy) to buy a new clue or (guess) to make a guess: ")
            else:
                print("You have typed an invalid country, please try again: ")
                syöte = input("Type (buy) to buy a new clue or (guess) to make a guess: ")

        else:
                print("You have typed an invalid command, please try again: ")
                syöte = input("Type (buy) to buy a new clue or (guess) to make a guess: ")#Siirrytään suoraan loopin alkuun
    return päämäärä

