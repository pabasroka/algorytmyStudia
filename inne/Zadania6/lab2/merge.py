arr = [4, 41, 5, 7, -8, -12, 3, 1, 2]
scal1 = [1, 3, 5]
scal2 = [2, 6, 7]


def merge(scal1, scal2):
    scal3 = []
    i = 0
    j = 0
    length = len(scal1) + len(scal2)
    for s in range(0, length):
        if i >= len(scal1):
            scal3.append(scal2[j])
            j += 1
        elif j >= len(scal2):
            scal3.append(scal1[i])
            i += 1

        if i < len(scal1) and j < len(scal2):
            if scal1[i] <= scal2[j]:
                scal3.append(scal1[i])
                i += 1
            else:
                scal3.append(scal2[j])
                j += 1
        print(s, ":", scal3[s])
    return scal3


scal3 = merge(scal1, scal2)
print(scal3)

