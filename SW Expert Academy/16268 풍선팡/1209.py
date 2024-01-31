import sys
sys.stdin = open('./input.txt', 'r')

T = int(input())

d_row = [-1, 1, 0, 0]
d_col = [0, 0, -1, 1]

for _ in range(T):
    N, M = list(map(int, input().split()))
    case_matrix = [list(map(int, input().split())) for _ in range(N)]
    max_sum = 0
    for row in range(N):
        for col in range(M):
            sum_value = case_matrix[row][col]
            for idx in range(4):
                new_row = row + d_row[idx]
                new_col = col + d_col[idx]
                if 0 <= new_row < N and 0 <= new_col < M:
                    sum_value += case_matrix[new_row][new_col]
            if sum_value > max_sum:
                max_sum = sum_value
    print(f'#{_ + 1} {max_sum}')
