def fw(matrix):
    p = [row[:] for row in matrix]
    for row, i in enumerate(p):
        for column, j in enumerate(i):
            if p[row][column] != 0.0 and p[row][column] != float('inf'):
                p[row][column] = row
            else:
                p[row][column] = -1
    for u in range(len(matrix)):
        for v in range(len(matrix)):
            for w in range(len(matrix)):
                if u != v and v != w and u != w:
                    l = matrix[v][u] + matrix[u][w]
                    if l < matrix[v][w]:
                        matrix[v][w] = l
                        p[v][w] = p[u][w]
    return matrix, p


matrix = [[float(x) for x in line.split()] for line in open("dane.txt").readlines()]
dp = fw(matrix)

for row in dp[0]:
    print(row)

print("")

for row in dp[1]:
    print(row)