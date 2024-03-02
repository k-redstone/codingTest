import sys
from collections import deque

input = sys.stdin.readline

def bfs(start, graph):
    max_distance = 0
    max_node = 0
    visited = [False] * (V + 1)
    Q = deque([(start, 0)])

    while Q:
        current, distance = Q.popleft()

        if distance > max_distance:
            max_distance = distance
            max_node = current

        visited[current] = True

        for neighbor, weight in graph[current]:
            if not visited[neighbor]:
                Q.append((neighbor, distance + weight))

    return max_node, max_distance

V = int(input())
graph = [[] for _ in range(V + 1)]

for _ in range(V):
    data = list(map(int, input().split()))
    node = data[0]
    for i in range(1, len(data) - 1, 2):
        graph[node].append((data[i], data[i + 1]))

start_node, _ = bfs(1, graph)
_, result = bfs(start_node, graph)

print(result)