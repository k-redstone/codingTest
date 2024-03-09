import sys
import heapq
import math
input = sys.stdin.readline


def search(start):
    hq = [(0, start)]
    weight_list = [math.inf]*(N+1)
    weight_list[start] = 0
    while hq:
        weight, node = heapq.heappop(hq)

        if weight > weight_list[node]:
            continue

        for next, weight in graph[node]:
            if weight_list[next] > weight_list[node] + weight:
                weight_list[next] = weight_list[node] + weight
                heapq.heappush(hq, (weight_list[next], next))

    return weight_list

def get_path():
    path_1 = search(1)
    path_2 = search(v_1)
    path_3 = search(v_2)

    result_1 = path_1[v_1] + path_2[v_2] + path_3[N]
    result_2 = path_1[v_2] + path_3[v_1] + path_2[N]

    result = min(result_1, result_2)

    return result if result != float('infinity') else -1

N, E = map(int, input().rstrip().split())

graph = {i: [] for i in range(1, N+1)}

for _ in range(E):
    start, end, weight = map(int, input().rstrip().split())
    graph[start].append((end, weight))
    graph[end].append((start, weight))

v_1, v_2 = map(int, input().rstrip().split())

print(get_path())
