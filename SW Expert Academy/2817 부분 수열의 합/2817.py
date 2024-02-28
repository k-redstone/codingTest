import sys
sys.stdin = open("./input.txt", "r")

T = int(input())

def make(idx, sum_num):
    global cnt
    if sum_num > K:
        return
    if idx > N:
        if sum_num == K:
            cnt += 1
        return
    for num in range(0, 2):
        visited[idx] = num
        if visited[idx] == 1:
            make(idx+1, sum_num + case_list[idx-1])
        if visited[idx] == 0:
            make(idx + 1, sum_num)
        visited[idx] = -1

for tc in range(1, T+1):
    N, K = map(int, input().split())
    case_list = list(map(int, input().split()))
    cnt = 0
    visited = [0]*(N+1)
    make(1, 0)
    print(f'#{tc} {cnt}')
