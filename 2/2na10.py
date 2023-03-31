liczba2 = "100101"
numerZnaku = len(liczba2)-1
potega = 1
wynik = 0

while numerZnaku>=0:
    wynik = wynik + potega * int(liczba2[numerZnaku])
    potega = potega * 2
    numerZnaku = numerZnaku - 1

print(liczba2 + " w systemie dziesietnym to " + str(wynik))