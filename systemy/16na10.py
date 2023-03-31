liczba2 = "B3F"
numerZnaku = len(liczba2)-1
potega = 1
wynik = 0

while numerZnaku>=0:
    znak = liczba2[numerZnaku]
    numerZnaku2 = ord(znak)
    if numerZnaku2>=48 and numerZnaku2<=57:
        numer = numerZnaku2-48
    else:
        numer = numerZnaku2-55


    wynik = wynik + potega * numer
    potega = potega * 16
    numerZnaku = numerZnaku - 1

print(liczba2 + " w systemie dziesietnym to " + str(wynik))