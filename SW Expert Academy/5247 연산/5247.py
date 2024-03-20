import sys
from collections import deque
sys.stdin = open("./input.txt", "r")

def bfs(start, end):
    Q = deque([(start, 0)])
    visit = [None] * 1000001
    visit[start] = 0
    while Q:
        cur, cnt = Q.popleft()
        if cur == end:
            return cnt
        for next_node in [cur - 1, cur + 1, cur * 2, cur - 10]:
            if 0 < next_node <= 1000000 and visit[next_node] is None:
                visit[next_node] = cnt + 1
                Q.append((next_node, cnt+1))

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    result = bfs(N, M)
    print(f'#{tc} {result}')