import sys
from collections import deque, defaultdict
input = sys.stdin.readline

def bfs():
    parent= [0]*(N+1)
    parent[1] = 1
    Q = deque([1])
    while Q:
        item = Q.popleft()
        for node in graph[item]:
            if parent[node] == 0:
                parent[node] = item
                Q.append(node)
    print(parent)
    return parent[2:]

graph = defaultdict(set)
N = int(input().rstrip())
for _ in range(N-1):
    node_1, node_2 = map(int, input().rstrip().split())
    graph[node_1].add(node_2)
    graph[node_2].add(node_1)
result = bfs()
for item in result:
    print(item)