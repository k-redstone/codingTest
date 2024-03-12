import sys
import heapq
import math
input = sys.stdin.readline

def solution(start, end):
    pq = [(0, [start])]
    weight_list = [[math.inf, i] for i in range(N+1)]
    weight_list[start][0] = 0

    while pq:
        cost, nodes = heapq.heappop(pq)
        node = int(nodes[-1])
        if cost > weight_list[node][0]:
            continue
        
        for next_cost, next_node in graph[node]:
            if weight_list[next_node][0] > cost + next_cost:
                weight_list[next_node][0] = cost + next_cost
                new = [*nodes, next_node]
                weight_list[next_node][1] = new
                heapq.heappush(pq, (cost + next_cost, new))

    return weight_list[end]




N = int(input().rstrip())
M = int(input().rstrip())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    start, end, cost = map(int, input().rstrip().split())
    graph[start].append((cost, end))

start, end = map(int, input().rstrip().split())
result = solution(start, end)

print(result[0])
print(len(result[1]))
print(*result[1])