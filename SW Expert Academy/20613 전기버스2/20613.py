import sys
from collections import deque
sys.stdin = open("./input.txt", "r")

T = int(input())

def solution(start_charge, num):
    visited = [0]*(num+1)
    Q = deque()
    Q.append((1, start_charge, 0))
    while Q:
        cur, can_go, cnt = Q.popleft()
        for go in range(1, can_go+1):
            if cur+go >= len(visited)-1:
                visited[cur + go] = 1
                return cnt
            if visited[cur+go] == 0:
                visited[cur+go] = 1
                Q.append((cur+go, case_list[cur+go-1], cnt+1))



for tc in range(1, T+1):

    case_list = list(map(int, input().split()))
    N = case_list[0]
    case_list = case_list[1:]

    print(f'#{tc} {solution(case_list[0], N)}')