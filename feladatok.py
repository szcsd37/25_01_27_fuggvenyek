"""2. Feladat
Írj eljárást, amely paraméterül kapott számról eldönti, és a képernyőre kiírja, hogy negatív, pozitív vagy nulla-e!
"""
def masodik_feladat(szam):
    if szam > 0:
        print('Pozitív')
    elif szam < 0:  
        print('Negatív')
    else:
        print('Nulla')



"""addig lehessen számokat megadni ameddig a felhasználó nem ad meg üres sztringet"""

megyen = True

while megyen:
    szam = input('Adjon meg egy számot: ')
    if szam == '':
        megyen = False

masodik_feladat(szam)   