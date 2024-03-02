import sys
from collections import deque
input = sys.stdin.readline


def bfs(graph, start):
    max_dist = 0
    Q = deque([(start, 0)])
    visted = set([start])
    while Q:
        cur_node, dist = Q.popleft()
        for next_node, next_dist in graph[cur_node]:
            if matrix[start][next_node] == 0 and start != next_node:
                num = matrix[start][cur_node] + next_dist
                matrix[start][next_node] = num
                matrix[next_node][start] = num
                Q.append((next_node, num))
                visted.add(next_node)
                max_dist = max(max_dist, num)
    return max_dist


V = int(input())
graph = {i: [] for i in range(1, V+1)}
matrix = [[0]*(V+1) for _ in range(V+1)]

for node in range(1, V+1):
    info = list(map(int, input().split()))
    graph[node].extend((info[i], info[i+1]) for i in range(1, len(info), 2) if info[i] != -1)

max_num = max(bfs(graph, node) for node in range(1, V+1))
print(max_num)