print("Podaj liczbe: ")
liczba10 = int(input())

print("Podaj system: ")
x = int(input())

poczatkowaWartosc = liczba10
wynikZDzielenia = 1
liczba2 = ""
while wynikZDzielenia>0:
    reszta = liczba10 % x
    if reszta<10:
        liczba2 = liczba2 + str(reszta)
    else:
        xx = reszta + 55
        liczba2 = liczba2 + chr(xx)
    wynikZDzielenia = int(liczba10/x)
    liczba10 = wynikZDzielenia

wynik = ""
dlugosc = len(liczba2)
for i in range(dlugosc):
    j = -i - 1 + dlugosc
    wynik = wynik + liczba2[j]
print("Wynik:")
print(str(poczatkowaWartosc) + " w systemie " + str(x) + " to " + wynik)