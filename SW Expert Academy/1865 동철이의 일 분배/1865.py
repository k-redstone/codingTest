import sys
sys.stdin = open("./input.txt", "r")


def get_max_percent(idx, result):
    global max_percent
    if max_percent >= result:
        # print(max_percent, result)
        return
    if idx >= N:
        max_percent = result
        return

    for num in range(N):
        if temp[num] == 1:
            continue
        temp[num] = 1
        get_max_percent(idx+1, result*case_matrix[idx][num])
        temp[num] = 0


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    case_matrix = [list(map(lambda x: x * 0.01, map(int, input().split()))) for _ in range(N)]
    temp = [0]*N
    max_percent = 0
    get_max_percent(0, 100)

    print(f'#{tc} {max_percent:.6f}')