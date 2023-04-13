liczba10 = 4321
poczatkowaWartosc = liczba10
wynikZDzielenia = 1
liczba2 = ""
while wynikZDzielenia>0:
    liczba2 = liczba2 + str(liczba10 % 2)
    wynikZDzielenia = int(liczba10/2)
    liczba10 = wynikZDzielenia

wynik = ""
dlugosc = len(liczba2)
for i in range(dlugosc):
    j = -i - 1 + dlugosc
    wynik = wynik + liczba2[j]
print(str(poczatkowaWartosc) + " w systemie dwojkowym to " + wynik)
