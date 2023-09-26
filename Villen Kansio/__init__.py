rahat = 0

def rahatsekki():
    print(f"Your current money: {rahat}")


def maatsekki(rahat, location, goal):
    if location == goal:
        print("Congratulations, you have arrived at the right country!")
        print("You have been awarded 100 euros!")
        rahat += 100
    else:
        print("This country you have arrived at is not the correct country")
    return

def pelaajavalinta():
    syöte = input("Voit joko ostaa uuden vihdeen 100 eurolla, tai valita seuraavan kohteen")

rahatsekki()