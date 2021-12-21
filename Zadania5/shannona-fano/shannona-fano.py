def shannon_fano(symbole):
    if len(symbole) > 1:
        symbole = sorted(symbole, reverse=True)
        left = []
        left_sum = 0
        right = symbole
        right_sum = 0
        for symbol in right:
            right_sum += symbol[0]
        i = 0
        while i < len(symbole):
            if abs((left_sum + right[0][0]) - (right_sum - right[0][0])) < abs(left_sum - right_sum):
                i += 1
                s = right.pop(0)
                left.append(s)
                left_sum += s[0]
                right_sum -= s[0]
            else: 
                break
        for symbol in left:
            kod[symbol[1]] += "0"
        for symbol in right:
            kod[symbol[1]] += "1"
        shannon_fano(left)
        shannon_fano(right)
        
kod = {"A": "", "B": "", "C": ""}
symbole = [(50, "A"), (30, "B"), (20, "C")]
tekst = "ABBACC"

shannon_fano(symbole)
print("Zakodowany tekst: ")
for litera in tekst:
    print(kod[litera], end="")