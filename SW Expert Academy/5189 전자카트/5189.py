import sys
sys.stdin = open("./input.txt", "r")

T = int(input())

def backtrack(row, num, cnt):
    global min_num
    if num > min_num:
        return
    if cnt >= N+1:
        min_num = num
        return
    for idx in range(1, N+1):
        if row > 0 and idx == 1 and cnt != N:
            continue
        if case_matrix[row][idx-1] == 0:
            continue
        if idx not in path:
            path[row] = idx
            backtrack(idx-1, num+case_matrix[row][idx-1], cnt+1)
            path[row] = 0

for tc in range(1, T+1):
    N = int(input())
    case_matrix = [list(map(int, input().split())) for _ in range(N)]
    min_num = 100*N
    path = [0]*N
    backtrack(0, 0, 1)
    print(f'#{tc} {min_num}')
