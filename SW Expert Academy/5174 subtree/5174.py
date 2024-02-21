import sys
from collections import deque
sys.stdin = open("./input.txt", "r")

T = int(input())

def bfs():
    cnt = 1
    while Q:
        item = Q.popleft()
        if tree[item]:
            Q.extend(tree[item])
        cnt += 1
    return cnt

for tc in range(1, T+1):
    E, N = map(int, input().split())
    tree = {i: [] for i in range(1, E+2)}
    case_list = list(map(int, input().split()))
    for num in range(0, E*2, 2):
        tree[case_list[num]].append(case_list[num+1])
    Q = deque()
    Q.extend(tree[N])
    print(f'#{tc} {bfs()}')