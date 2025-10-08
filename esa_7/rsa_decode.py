# rsa_verschluesselung.py
# Dieses Programm verschlüsselt und entschlüsselt eine Nachricht mit RSA.
# Vorgabe:
# e = 37, n = 3713 (öffentlicher Schlüssel)
# d = 97 (privater Schlüssel)
# Nachricht: "Geheimtreffen abgesagt"
# Leerzeichen werden nicht verschlüsselt!



# Öffentlicher und privater Schlüssel
e = 37
n = 3713
d = 97

# Die geheime Nachricht
nachricht = "Geheimtreffen abgesagt"

# Funktion zum Verschlüsseln eines Buchstabens
def verschluesseln_buchstabe(buchstabe):
    ascii_wert = ord(buchstabe)  # ASCII-Wert holen
    verschluesselt = pow(ascii_wert, e, n)  # RSA Formel: c = m^e mod n
    return verschluesselt

# Funktion zum Entschlüsseln einer Zahl
def entschluesseln_zahl(zahl):
    ascii_wert = pow(zahl, d, n)  # RSA Formel: m = c^d mod n
    buchstabe = chr(ascii_wert)   # zurück in Buchstaben umwandeln
    return buchstabe

# Nachricht verschlüsseln (Leerzeichen bleiben)
def verschluesseln_text(text):
    woerter = text.split(" ")  # Nachricht in Wörter aufteilen
    verschluesselte_woerter = []

    for wort in woerter:
        zahlen_liste = []
        for buchstabe in wort:
            zahl = verschluesseln_buchstabe(buchstabe)
            zahlen_liste.append(str(zahl))
        verschluesselte_woerter.append("-".join(zahlen_liste))

    # Wörter wieder mit Leerzeichen verbinden
    verschluesselt_text = " ".join(verschluesselte_woerter)
    return verschluesselt_text

# Entschlüsselt nur EIN Wort (zur Kontrolle)
def entschluesseln_wort(verschluesselt_wort):
    zahlen = verschluesselt_wort.split("-")
    entschluesselt = ""

    for zahl in zahlen:
        buchstabe = entschluesseln_zahl(int(zahl))
        entschluesselt += buchstabe

    return entschluesselt


# 1. Verschlüsseln
geheimtext = verschluesseln_text(nachricht)
print("Klartext:   ", nachricht)
print("Geheimtext: ", geheimtext)

# 2. Erstes Wort entschlüsseln zur Kontrolle
erstes_verschluesseltes_wort = geheimtext.split(" ")[0]
entschluesseltes_wort = entschluesseln_wort(erstes_verschluesseltes_wort)
print("Entschlüsseltes erstes Wort:", entschluesseltes_wort)
