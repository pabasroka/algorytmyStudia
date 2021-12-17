import heapq

h = {0: 4, 1:8, 2:3, 3:4, 4:5, 5:2, 6:1, 7:0}

def a(matrix):
    q = []
    qn = []
    s = []
    pred = [-1] * len(matrix)
    start = 0
    end = 7
    cost = 0
    v = None
    heapq.heappush(q, (0, start))
    qn.append(start)
    while len(q) > 0:
        n = heapq.heappop(q)
        if v is not None:
            cost += matrix[v][n[1]]
        v = n[1]
        qn.remove(v)
        s.append(v)
        for node, weight in enumerate(matrix[v]):
            if weight != 0.0 and weight != float('inf'):
                if not node in s:
                    if not node in qn:
                        heapq.heappush(q, (cost + weight + h[node], node))
                        qn.append(node)
                        pred[node] = v   
                    
        if v == end: break
    return pred, s

matrix = [[float(x) for x in line.split()] for line in open("dane.txt").readlines()]
res = a(matrix)
print(f"p: {res[0]}") 
print(f"s: {res[1]}")