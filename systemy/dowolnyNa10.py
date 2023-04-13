print("Podaj liczbe: ")
liczba2 = input()

print("Podaj system: ")
x = int(input())

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
    potega = potega * x
    numerZnaku = numerZnaku - 1

print(liczba2 + " w systemie " + str(x) + " to " + str(wynik))