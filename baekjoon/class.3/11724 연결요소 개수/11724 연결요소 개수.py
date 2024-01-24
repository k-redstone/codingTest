import sys
sys.stdin = open("data.txt", "r")


N, M = list(map(int, sys.stdin.readline().rstrip().split()))

graph = [ [] for _ in range(N + 1)]

for _ in range(M):
    start, end = map(int, sys.stdin.readline().rstrip().split())
    graph[start].append(end)
    graph[end].append(start)
    
visited=[0 for _ in range(N+1)]
def dfs():
    while stack:
        node = stack.pop()
        if visited[node] == 0:
            visited[node] = 1
            if len(graph[node]) > 0:
                stack.append(node)
                stack.extend(graph[node])
    return 1


result =0
for check in range(1, N+1, 1):
    if visited[check] == 0:
        stack = [check]
        result += dfs()
    
print(result)