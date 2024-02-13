import sys
sys.stdin = open("./input.txt", "r")

T = int(input())
d_row = [1, -1, 0, 0]
d_col = [0, 0, -1, 1]

def backtrack(row, col, out):
    if case_matrix[row][col] == 3:
        out = 1
        return out
    case_matrix[row][col] = 1
    for num in range(4):
        new_row = row + d_row[num]
        new_col = col + d_col[num]
        if 0 <= new_row < N and 0 <= new_col < N:
            if case_matrix[new_row][new_col] != 1:
                out = backtrack(new_row, new_col, out)
                case_matrix[new_row][new_col] = 0
    return out

for tc in range(1, T+1):
    N = int(input().strip())
    case_matrix = [list(map(int, input().strip())) for _ in range(N)]
    result = 0
    for i in range(N):
        for j in range(N):
            if case_matrix[i][j] == 2:
                start_point = (i, j)
                break
    print(f'#{tc} {backtrack(start_point[0], start_point[1], result)}')
