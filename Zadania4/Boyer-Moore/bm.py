def letter(l):
    for i in p.keys():
        if i == l:
            return p[l]
    return -1
    
def bm(text, phrase):
    n = len(phrase)
    i = n - 1
    j = n - 1
    while i < len(text):
        while text[i] == phrase[j]:
            i -= 1
            j -= 1
        if j == -1:
            return i + 1
        else:
            i += n - min(j, 1 + letter(text[i]))
            j = n - 1
    return -1


phrase = "za"
p = {letter:index for index, letter in enumerate(phrase)}
print(bm("kolejny zabawny tekst", phrase))
