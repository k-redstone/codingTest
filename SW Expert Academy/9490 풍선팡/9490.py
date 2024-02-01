import sys
sys.stdin = open("./input.txt", "r")


T = int(input())
d_row = [-1, 1, 0, 0]
d_col = [0, 0, -1, 1]


def check(matrix, n, m):
    result_list = []
    for row in range(n):
        for col in range(m):
            count = matrix[row][col]
            power = count
            for d_num in range(4):
                for op in range(1, power + 1):
                    new_row = row + (d_row[d_num] * op)
                    new_col = col + (d_col[d_num] * op)
                    if 0 <= new_row < N and 0 <= new_col < M:
                        count += matrix[new_row][new_col]
                    continue
            result_list.append(count)
    return result_list


for tc in range(1, T+1):
    N, M = map(int, input().split())
    case_matrix = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{tc} {max(check(case_matrix, N, M))}')
