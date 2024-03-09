import sys
import heapq
import math
input = sys.stdin.readline

def solution(start_point, end_point):
    hq = []
    heapq.heappush(hq, (0, start_point))
    weight = [math.inf]*(N+1)
    weight[start_point] = 0
    while hq:
        dist, node = heapq.heappop(hq)
        if dist > weight[node]:
            continue

        for cost, end in graph[node]:
            if weight[end] > weight[node] + cost:
                weight[end] = weight[node] + cost
                heapq.heappush(hq, (weight[end], end))
    return weight[end_point]

N = int(input().rstrip())
M = int(input().rstrip())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    start, end, weight = map(int, input().rstrip().split())
    graph[start].append((weight, end))
start_point, end_point = map(int, input().rstrip().split())
print(solution(start_point, end_point))