def verknuepfung(a: bool, b: bool) :
    if not (a and b):
        return "wahr"
    else:
        return "falsch"
    
def uebersetzung(b: bool):
    if b:
        return "wahr"
    else:
        return "falsch"
# Ausgabe der Wahrheitstabelle (außerhalb der Funktion)
werte = [[False, False], [False, True], [True, False], [True, True]]
print("A\t B \t Not (A And B)")
for wert in werte:
    a = wert[0];
    b = wert[1];
    e = verknuepfung(a,b)

   # print (str(a) + "\t" + str(b) + "\t" + e)
    
    #Mit übersetzung 

    print(str(uebersetzung(a)) + "\t" +str(uebersetzung(b)) + "\t" + e)


#zahl1 = 0
#zahl = int(input("Bitte Zahl eingeben:"))




