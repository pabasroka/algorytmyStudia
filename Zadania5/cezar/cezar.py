def cezar(text, alphabet, shift = 4):
    for znak in text:
        if znak in alphabet:
            print(alphabet[(alphabet.find(znak) + shift) % (len(alphabet))], end = '')
        else:
            print(znak, end = '')

text = "jakis dlugi tekst"
alphabet = "abcdefghijklmnopqrstuvwxyz";
shift = 4
cezar(text, alphabet, shift)