import heapq

def prima(matrix):
    p = [-1 for _ in range(len(matrix))]
    k = [float('inf')] * len(matrix)
    s = 0
    k[s] = 0
    pq = []
    for v in range(len(matrix)):
        heapq.heappush(pq, (float(k[v]), v))
    pq_nodes = [x[1] for x in pq]

    while len(pq) > 0:
        u = heapq.heappop(pq)[1]
        pq_nodes.remove(u)
        for v, weight in enumerate(matrix[u]):
            if weight != 0.0 and weight != float('inf'):
                if v in pq_nodes:
                    if weight < k[v]:
                        p[v] = u
                        k[v] = weight
                        pq[pq_nodes.index(v)] = (weight, v)
                        heapq.heapify(pq)
    return p, k


matrix = [[float(x) for x in line.split()] for line in open("dane.txt").readlines()]
print(prima(matrix))