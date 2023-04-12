liczba10 = 4321
poczatkowaWartosc = liczba10
wynikZDzielenia = 1
liczba2 = ""
while wynikZDzielenia>0:
    reszta = liczba10 % 16
    if reszta<10:
        liczba2 = liczba2 + str(reszta)
    else:
        x = reszta + 55
        liczba2 = liczba2 + chr(x)
    wynikZDzielenia = int(liczba10/16)
    liczba10 = wynikZDzielenia

wynik = ""
dlugosc = len(liczba2)
for i in range(dlugosc):
    j = -i - 1 + dlugosc
    wynik = wynik + liczba2[j]
print("Wynik:")
print(str(poczatkowaWartosc) + " w systemie dwojkowym to " + wynik)