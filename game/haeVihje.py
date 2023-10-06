import Vihjeet

def haevihje(päämäärä):
    global vihjeindeksi
    for a in Vihjeet.countries:
        if a == päämäärä:
            print(Vihjeet.countries[päämäärä][vihjeindeksi])
            vihjeindeksi += 1
    return


