import Vihjeet

def haeVihje(maa, monesVihje):
    for country in Vihjeet.countries:
        if country == maa:
            return Vihjeet.countries[maa][monesVihje - 1]

vihje = haeVihje("Lithuania", 2)
print(vihje)

