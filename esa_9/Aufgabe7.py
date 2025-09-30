""" ************************************************
Lineare Suche
************************************************"""
# der Import der Funktion randrange() aus dem Modul random
from random import randrange
# die maximale Anzahl der Werte
anzahl = 100
# eine leere Liste für die Werte
werte = []
# wurde schon ein Wert gefunden?
gefunden = []
# für die Suche
suchen = 0
print("Lineare Suche")
# die Liste füllen, benutzt werden zufällige Zahlen bis 200
durchlauf = 1
while durchlauf <= anzahl:
    werte.append(randrange(1, 5))
    durchlauf = durchlauf + 1
    # zur Kontrolle ausgeben
print("Die Werte sind: ")
for wert in werte:
    print(wert, end = " ")
    print()
# Abfrage des Suchkriteriums
kriterium = int(input("Wonach soll gesucht werden? "))
# und jetzt suchen, bis das Ende erreicht wurde oder die Zahl
# gefunden wurde
while suchen < anzahl: # and gefunden == False:
    if werte[suchen] == kriterium:
        gefunden.append(suchen)
        suchen = suchen + 1
    else:
        suchen = suchen + 1
    
if len(gefunden) > 0:
# bitte in einer Zeile eingeben
    print("Die Werte zu", str(kriterium), "befinden sich an der Position",  str(gefunden))
else:
    print("Der Wert", kriterium, "wurde nicht gefunden.")