import sys
import heapq
import math
input = sys.stdin.readline


def solution():
    hq = [(0, start_node)]
    weight_list = [math.inf]*(V+1)
    weight_list[start_node] = 0

    while hq:
        weight, node = heapq.heappop(hq)
        if weight > weight_list[node]:
            continue
        for next_node, next_weight in graph[node]:
            if weight_list[next_node] > weight + next_weight:
                weight_list[next_node] = weight + next_weight
                heapq.heappush(hq, (weight + next_weight, next_node))
    return weight_list[1:]
    
V, E = map(int, input().rstrip().split())
start_node = int(input().rstrip())
graph = [[] for _ in range(V+1)]

for _ in range(E):
    start, end, weight = map(int, input().rstrip().split())
    graph[start].append((end, weight))

result = solution()

for answer in result:
    if answer == float('infinity'):
        print('INF')
    else:
        print(answer)