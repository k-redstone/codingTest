import sys
from collections import deque
sys.stdin = open("./input.txt", "r")

T = int(input())

def bfs():
    while Q:
        item = Q.popleft()
        for node in graph[item]:
            if node == end_node:
                return visited[item] + 1
            if visited[node] == 0:
                Q.append(node)
                visited[node] = visited[item] + 1
    return 0
for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    for num in range(E):
        start, end = map(int, input().split())
        graph[start].append(end)
        graph[end].append(start)
    start_node, end_node = map(int, input().split())
    Q = deque([start_node])
    visited = [0]*(V+1)
    print(f'#{tc} {bfs()}')
