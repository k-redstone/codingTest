import sys
from collections import deque
input = sys.stdin.readline


def solution(start):
    weight = [-1]*(N+1)
    weight[start] = 0
    Q = deque()
    Q.extend(graph[start])
    while Q:
        cur, next_node = Q.popleft()

        if weight[next_node] == -1:
            weight[next_node] = weight[cur] + 1
            Q.extend(graph[next_node])
    return sum(weight)+1



N, M = map(int, input().rstrip().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    start, end = map(int, input().rstrip().split())
    graph[start].append((start, end))
    graph[end].append((end, start))

min_num = float('infinity')
people = []
for num in range(1, N+1):
    people.append(solution(num))

print(people.index(min(people)) + 1)