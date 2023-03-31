file=open("napisy.txt","r")
tablicaLicznikow = []
for i in range(15):
    tablicaLicznikow.append(0)

x=0
p=0
napisyC = 0
napisyC2 = 0
for i in range(1000):
    napis=file.readline()

    #podpunkt D
    dlugosc2=len(napis)
    for j in range(2,17):
        if dlugosc2==j:
            tablicaLicznikow[j-2] = tablicaLicznikow[j-2] + 1
            break

    #potrzebne do podpunktow A i B
    dlugosc=len(napis)-1

    #podpunkt B
    y=0
    v=0
    for j in range(dlugosc):
        if napis[j]=="1":
            y=y+1
        if napis[j]=="0":
            v=v+1
    if y==v:
        p=p+1

    #podpunkt A
    if dlugosc%2==0:
        x=x+1

    #podpunkt C
    flaga = 1
    for j in range(dlugosc):
        if napis[j]!="0":
            flaga = 0
            break
    if flaga==1:
        napisyC = napisyC + 1

    flaga = 1
    for j in range(dlugosc):
        if napis[j]!="1":
            flaga = 0
            break
    if flaga==1:
        napisyC2 = napisyC2 + 1

#wyswietlanie podpunktu D
for i in range(15):
    print("Liczba wyrazow o dlugosci rownej ", i+2, ": ", tablicaLicznikow[i])

print("Ilosc napisow skladajacych sie z samych zer: ", napisyC)
print("Ilosc napisow skladajacych sie z samych jedynek: ", napisyC2)
    
print("Ilosc napisow o parzystej ilosci liter: ",x)
print("Ilosc napisow o takiej samej ilosci jedynek, co zer: ",p)