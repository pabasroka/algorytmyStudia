def kp(text, phrase, alphabet):
    prime = 79
    texth = 0
    phraseh = 0
    n = len(phrase)
    nA = len(alphabet)

    for i in range(n):
        phraseh = (phraseh * nA + alphabet[key[i]]) % prime
        texth = (texth * nA + alphabet[text[i]]) % prime  
    i = 0
    while i <= len(text) - n:
        if texth == phraseh:
            if text[i:i + n] == phrase:
                return i
        texth = ((texth - (alphabet[text[i]] * pow(nA, n - 1))) * nA + alphabet[text[i + n]]) % prime
        i += 1
    return -1

text = "losowe slowa do wyszukania"
key = "do"
alphabet = {}
for y, x in enumerate(text):
    if x not in alphabet.keys() : alphabet[x] = y

print(kp(text, key, alphabet))
