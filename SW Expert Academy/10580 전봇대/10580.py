import sys
sys.stdin = open("./input.txt", "r")
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    case_list = [list(map(int, input().split())) for _ in range(N)]
    case_list = sorted(case_list, key=lambda x: x[0])
    visited = [0]*10001
    cnt = 0
    for item in case_list:
        A, B = item
        visited[A] = B
        for idx in range(1, A):
            if visited[idx] > B:
                cnt += 1
    print(f'#{tc} {cnt}')
