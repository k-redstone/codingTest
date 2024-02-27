import sys
sys.stdin = open("./input.txt", "r")

T = int(input())
d_row, d_col = [1, 0], [0, 1]

def solution(row, col):
    for idx in range(2):
        new_row, new_col = row+d_row[idx], col+d_col[idx]
        if 0 <= new_row < N and 0 <= new_col < N:
            if visited[new_row][new_col] == 0:
                visited[new_row][new_col] = visited[row][col] + case_matrix[new_row][new_col]
                solution(new_row, new_col)
            else:
                if visited[row][col] + case_matrix[new_row][new_col] < visited[new_row][new_col]:
                    visited[new_row][new_col] = visited[row][col] + case_matrix[new_row][new_col]
                    solution(new_row, new_col)


for tc in range(1, T+1):
    N = int(input())
    case_matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    visited[0][0] = case_matrix[0][0]
    solution(0, 0)
    print(f'#{tc} {visited[N-1][N-1]}')