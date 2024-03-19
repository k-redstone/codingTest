import sys
sys.stdin = open("./input.txt", "r")


def get_min_cost(idx, result):
    global min_cost
    if min_cost <= result:
        return
    if idx >= N:
        min_cost = result
        return
    for num in range(N):
        if temp[num] == 1:
            continue
        temp[num] = 1
        get_min_cost(idx+1, result+case_matrix[idx][num])
        temp[num] = 0


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    case_matrix = [list(map(int, input().split())) for _ in range(N)]
    temp = [0]*N
    min_cost = float('infinity')
    get_min_cost(0, 0)
    print(f'#{tc} {min_cost}')