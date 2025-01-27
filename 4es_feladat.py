"""4. Feladat
Írj egy programot, amely a felhasználótól bekér 3 szót, ezeket egy listában tárolja, és egy eljárás segítségével meghatározza, és a képernyőre kiírja, melyik a legrövidebb szó!"""


szavak = []

hanyzsor = 4

for i in range(hanyzsor):
    szavak.append(input('Adjon meg egy szót: '))

def legrövidebb(szavak):
    legrovidebb = szavak[0]
    for szo in szavak:
        if len(szo) < len(legrovidebb):
            legrovidebb = szo
    return legrovidebb

print('A legrövidebb szó: ', legrövidebb(szavak))
