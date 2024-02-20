import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())

visited = [0]*100001
visited[N] = 1

Q = deque([N])
def bfs():
    while Q:
        node = Q.popleft()
        if node == K:
            return visited[node]
        for next in [node-1, node+1, node*2]:
            if 0 <= next <= 100000 and visited[next] == 0:
                Q.append(next)
                visited[next] = visited[node] + 1

print(bfs() -1 )

