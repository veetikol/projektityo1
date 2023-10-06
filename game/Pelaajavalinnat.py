from haeVihje import haevihje

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


def pelaajavalinta():
    print("Voit joko ostaa uuden vihjeen 100 eurolla, tai veikata maata")
    syöte = input("kirjoita (osta) ostaaksesi vihjeen, tai (veikkaa) veikataksesi kohdetta: ")

    global sijainti
    global rahat
    global päämäärä
    global listamuuttuja
    global vihjeindeksi

    while True:
        if rahat < 100:
            print("Hävisit pelin")
            break
        if syöte == "osta":
            if vihjeindeksi <= 2:
                print("Uusi vihje!")
                haevihje(päämäärä)
                rahat -= 100
                print(f"Rahasi: {rahat} euroa")
            else:
                print(f"Kohdemaasi on {päämäärä}. Sinua sakotetaan 100 euroa")
                rahat -= 100
                print(rahat)
                if rahat < 100:
                    print("Hävisit pelin")
                    break
                print("Lennetään kohteeseen...")
                sijainti = päämäärä
                listamuuttuja += 1
                päämäärä = maalista[listamuuttuja]
                vihjeindeksi = 0
                print("Uusi vihje: ")
                haevihje(päämäärä)
            if rahat < 100:
                print("Rahasi loppuivat, peli päättyy")
                break
            syöte = input("kirjoita (osta) ostaaksesi vihjeen, tai (veikkaa) veikataksesi kohdetta: ")
        elif syöte == "veikkaa":
            syöte2 = input("Kirjoita joko maan nimi, tai kirjoita (lista) tulostaaksesi listan mahdollisista maista: ")
            if syöte2 == "lista":
                print(maalista)
                syöte = input("kirjoita (osta) ostaaksesi vihjeen, tai (veikkaa) veikataksesi kohdetta: ")
                syöte2 = None
            elif syöte2 == päämäärä:
                print("Onneksi olkoon, arvasit oikean valtion")
                print("Lennetään kohteeseen...")
                sijainti = päämäärä
                rahat -= 100
                vihjeindeksi = 0
                listamuuttuja += 1
                päämäärä = maalista[listamuuttuja]
                print(rahat)
                if rahat < 100:
                    print("Pääsit perille, mutta rahasi loppuivat. Peli päättyy")
                    break
                break
            elif syöte2 != päämäärä and syöte2 in maalista:
                print("Arvasit väärin")
                rahat -= 100
                print(f"rahasi:{rahat}")
                print("kirjoita (osta) ostaaksesi vihjeen, tai (veikkaa) veikataksesi kohdetta: ")
            else:
                print("Kirjoittamasi maa ei ole vaihtoeho")
                syöte = input("kirjoita (osta) ostaaksesi vihjeen, tai (veikkaa) veikataksesi kohdetta: ")
        else:
            print("Paska komento")
            syöte = input("kirjoita (osta) ostaaksesi vihjeen, tai (veikkaa) veikataksesi kohdetta: ")
    return

