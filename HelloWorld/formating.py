for i in range(1,13):
    print("No. {0} squared is {1} and cubed is {2}".format(i, i ** 2, i ** 3))

for i in range(1,13):
    print("No. {0:2} squared is {1:4} and cubed is {2:4}".format(i, i ** 2, i ** 3))
#            0 column 2        1 column 4   (vezi afisajul care afiseaza pe coloana 2 respectiv 4

for i in range(1,13):
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i ** 2, i ** 3))
#            0 column 2        1 column 3 etc    (vezi afisajul care afiseaza pe coloana 2 respectiv 4

for i in range(1,13):
    print("No. {0:2} squared is {1:<3} and cubed is {2:<4}".format(i, i ** 2, i ** 3))
#            <Aliniament spre stanga

for i in range(1,13):
    print("No. {0:2} squared is {1:<3} and cubed is {2:^4}".format(i, i ** 2, i ** 3))
#            ^ centrat

print()

print("pi is aproximately {0:12}".format(22 / 7))       #general format 15 decimale
print("pi is aproximately {0:12f}".format(22 / 7))      #floating point,general 6 digits (12 ii width)
print("pi is aproximately {0:12.50f}".format(22 / 7))   #floating format dar cu precizie spusa de noi de 50, 50 decimale dupa punct (Py nu trunchiaza numere, de aceia desi ii specificat 12 ne afiseaza 50 decimale
print("pi is aproximately {0:52.50f}".format(22 / 7))   #afiseaza aceiasi valoare dar in field width diferit (intre 51 si 53 nu poate afisa mai mult)
print("pi is aproximately {0:62.50f}".format(22 / 7))
print("pi is aproximately {0:<72.50f}".format(22 / 7))
print("pi is aproximately {0:<72.54f}".format(22 / 7))  #ce afiseaza in plus cu 0000 defapt nu e numar

for i in range(1,13):
    print("No. {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))