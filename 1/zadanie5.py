file=open("pary_liczb.txt","r")
licznikA = 0
licznikB = 0
licznikC = 0
for i in range(1000):
    zmienna = file.readline()
    x = zmienna.split(" ")[0]
    y = zmienna.split(" ")[1]
    temp = ""
    for i in range(len(y) - 1):
        temp = temp + y[i]

    y = temp

    x2 = int(x)
    y2 = int(y)

    #podpunkt A
    if x2%y2==0 or y2%x2==0:
        licznikA = licznikA + 1

    #podpunkt B
    flaga = 0
    r = 0
    if x2<y2:
        r = x2
    else:
        r = y2
    for j in range(1,r):
        z = j+1
        if x2%z==0 and y2%z==0:
            flaga = 1
            break
    if flaga==0:
        licznikB = licznikB + 1
    
    #podpunkt C
    suma1=0
    suma2=0
    for j in x:
        suma1 = suma1 + int(j)
    for j in y:
        suma2 = suma2 + int(j)
    if suma1==suma2:
        licznikC = licznikC + 1


print("Podpunkt A:")
print("Liczba wierszy, w ktorych jedna z wartosci jest wielokrotnoscia tej drugiej: ", licznikA)

print("Podpunkt B:")
print(licznikB)

print("Podpunkt C:")
print(licznikC)
