import sys
sys.stdin = open('./input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N, M = list(map(int, input().split()))
    case_matrix = [list(map(int, input().split())) for _ in range(N)]
    sum_max = 0

    for row in range(N - M + 1):
        for col in range(N - M + 1):
            sum_value = 0
            for row_idx in range(M):
                for col_idx in range(M):
                    sum_value += case_matrix[row + row_idx][col + col_idx]
            sum_max = max(sum_max, sum_value)

    print(f'#{tc} {sum_max}')
