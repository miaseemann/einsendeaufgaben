

def fakultaet(n):
    ergebnis = 1
    i = 1
    while i <= n:
        ergebnis = ergebnis * i
        i = i + 1
    return ergebnis


n = 49
k = 6

oben = fakultaet(n)
unten = fakultaet(k) * fakultaet(n - k)

ergebnis = oben / unten  

print("Es ist eine Warscheinlichkeit von 1 zu " + str(int(ergebnis)))
