def caesar_mit_index(text: str, grundverschiebung: int):

    verschluesselter_text = []

    for index, zeichen in enumerate(text):
        positionsverschiebung = index + 1
        gesamt_verschiebung = (grundverschiebung + positionsverschiebung) % 26

        if 'A' <= zeichen <= 'Z':
            basis_ascii = ord('A')
            neuer_buchstabe = chr((ord(zeichen) - basis_ascii + gesamt_verschiebung) % 26 + basis_ascii)
            verschluesselter_text.append(neuer_buchstabe)

        elif 'a' <= zeichen <= 'z':
            basis_ascii = ord('a')
            neuer_buchstabe = chr((ord(zeichen) - basis_ascii + gesamt_verschiebung) % 26 + basis_ascii)
            verschluesselter_text.append(neuer_buchstabe)

        else:
            verschluesselter_text.append(zeichen)

    return ''.join(verschluesselter_text)

# Beispiel:
text_beispiel = "Aaaaabc xyz"
verschiebung = 0
print(caesar_mit_index(text_beispiel, verschiebung))
