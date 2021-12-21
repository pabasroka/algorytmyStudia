def huffman(kod, symbole):
    while len(symbole) > 1:
        s1 = symbole.pop()
        s2 = symbole.pop()
        for i in s1[1]:
            kod[i] = "0" + kod[i]
        for i in s2[1]:
            kod[i] = "1" + kod[i]
        s1s2 = (s1[0] + s2[0], s1[1] + s2[1])
        symbole.append(s1s2)
        symbole = sorted(symbole, reverse=True)

kod = {"A":"", "B":"", "C":""}
symbole = [(50, "A"), (30, "B"), (20, "C")]
symbole = sorted(symbole, reverse=True)
huffman(kod, symbole)
tekst = "BACA"
print("Zakodowany tekst: ", end="")
for litera in tekst:
    print(kod[litera], end="")