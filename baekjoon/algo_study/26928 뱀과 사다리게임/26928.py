import sys
from collections import deque
input = sys.stdin.readline

def search():
    visited = [0]*101
    visited[1] = 0
    que = deque()
    que.append(1)
    while que:
        cur = que.popleft()
        for dice_num in range(1, 7):
            next = cur + dice_num
            if graph[next] != 0:
                next = graph[next]
            if next == 100:
                return visited[cur] + 1 
            if visited[next] == 0:
                visited[next] = visited[cur] + 1
                que.append(next)


N, M = map(int, input().split())
# 최대 100칸
graph = [0]*101
for _ in range(N+M):
    u, v = map(int, input().split())
    graph[u] = v

print(search())