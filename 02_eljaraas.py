
'''
Az argumentum (aktuális paraméter) lehet érték, kifejezés, változó is!
Az 'x', 'y' és 'eredmeny' nevű változók LOKÁLISAK, csak az eljáráson belül érhetők el! 
'''
def osszead(x, y):
        eredmeny = x + y
        print('A két szám összege: ', eredmeny)


osszead(10, 9)
osszead(5+5, 5+4)

# a = 10
# b = 9
# osszead(a, b)

