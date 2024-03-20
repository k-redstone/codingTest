import sys
import heapq
input = sys.stdin.readline



def MST(graph, start):
    mst_cost = 0
    visited = set([start])
    hq = [(cost, end) for end, cost in graph[start]]
    heapq.heapify(hq)
    while hq:
        cost, next_node = heapq.heappop(hq)

        if next_node not in visited:
            mst_cost += cost
            visited.add(next_node)
            for next, cost in graph[next_node]:
                if next not in visited:
                    heapq.heappush(hq, (cost, next))

    return mst_cost

N = int(input().rstrip())
M = int(input().rstrip())

graph = {i: [] for i in range(1, N+1)}
for _ in range(M):
    start, end, cost = map(int, input().rstrip().split())
    graph[start].append((end, cost))
    graph[end].append((start, cost))

result = MST(graph, 1)
print(result)
