import Vihjeet

def haeVihje(päämäärä, monesVihje):
    for country in Vihjeet.countries:
        if country == päämäärä:
            return Vihjeet.countries[päämäärä][monesVihje - 1]

vihje = haeVihje("Sweden", 2)
print(vihje)

