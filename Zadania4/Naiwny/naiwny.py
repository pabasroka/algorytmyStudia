def naiwny(text, phrase):
    i = 0
    j = 0
    while(j < len(phrase) and i < len(text)):
        if text[i] == phrase[j]:
            i += 1
            j += 1
        else:
            i -= (j-1)
            j = 0
    if j == len(phrase):
        print(f"Znaleziono na pozycji: {i - len(phrase)}")
    else:
        print("Nie znaleziono")

naiwny("Jakis smieszny tekst", "kot")
naiwny("Jakis smieszny tekst", "tek")