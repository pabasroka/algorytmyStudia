import heapq 
def dijkstra(matrix):
    p = [-1] * len(matrix)
    dist = [float('inf')] * len(matrix)
    q = [(float('inf'), i) for i in range(len(matrix))]
    q_nodes = [x[1] for x in q]
    s = 0
    dist[s] = 0
    q[q_nodes.index(s)] = (0, s)
    heapq.heapify(q)
    
    while len(q) > 0:
        v = heapq.heappop(q)[1]
        q_nodes.remove(v)
        for u, weight in enumerate(matrix[v]):
            if weight != 0.0 and weight != float('inf'):
                d = dist[v] + matrix[v][u]
                if d < dist[u]:
                    dist[u] = d
                    p[u] = v
    return p, dist

matrix = [[float(x) for x in line.split()] for line in open("dane.txt").readlines()]
print(f"p: {dijkstra(matrix)[0]}, d: {dijkstra(matrix)[1]}")