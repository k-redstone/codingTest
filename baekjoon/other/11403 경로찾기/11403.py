import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N)]

case_matrix = [list(map(int, input().split())) for _ in range(N)]

for row in range(N):
    for col in range(N):
        if case_matrix[row][col] == 1:
            graph[row].append(col)

find_path = [[] for _ in range(N)]
for idx, item in enumerate(graph):
    Q = deque(graph[idx])
    while Q:
        node = Q.popleft()
        if node in find_path[idx]:
            continue
        find_path[idx].append(node)
        Q.extend(graph[node])
for case in find_path:
    for col in range(N):
        if col in case:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()
