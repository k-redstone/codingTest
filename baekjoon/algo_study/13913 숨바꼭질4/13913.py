import sys
from collections import deque
input = sys.stdin.readline

def bfs(N, K):
    Q = deque([N])
    visited[N] = N
    while Q:
        node = Q.popleft()
        if node == K:
            return node
        
        for next in [node-1, node+1, node*2]:
            if 0 <= next <= 100000 and next not in visited:
                visited[next] = node
                Q.append(next)

N, K = map(int, input().split())
visited = dict()
result = bfs(N, K)
answer = deque()
cnt = 0

while visited[result] != result:
    answer.appendleft(result)
    result = visited[result]
    cnt += 1
answer.appendleft(result)
print(cnt)
print(*answer)