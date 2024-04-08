import sys
# from collections import deque
sys.stdin = open("./SW Expert Academy/1949 등산로 조성/input.txt", "r")


def solution(row, col, cnt, can):
    global max_length
    max_length = max(max_length, cnt)
    for n_row, n_col in [(row-1, col), (row+1, col), (row, col+1), (row, col-1)]:
        if 0 <= n_row < N and 0 <= n_col < N:
            if not visited[n_row][n_col]:
                if case_matrix[n_row][n_col] < case_matrix[row][col]:
                    visited[n_row][n_col] = True
                    solution(n_row, n_col, cnt+1, can)
                    visited[n_row][n_col] = False
                elif case_matrix[n_row][n_col]-K < case_matrix[row][col] and can:
                        prev = case_matrix[n_row][n_col]
                        case_matrix[n_row][n_col] = case_matrix[row][col]-1
                        visited[n_row][n_col] = True
                        solution(n_row, n_col, cnt+1, False)
                        case_matrix[n_row][n_col] = prev
                        visited[n_row][n_col] = False

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    case_matrix = [list(map(int, input().split())) for _ in range(N)]

    max_height = max(map(max, case_matrix))
    max_length = 1
    visited = [[False]*N for _ in range(N)]
    
    for row in range(N):
        for col in range(N):
            if case_matrix[row][col] == max_height:
                visited[row][col] = True
                solution(row, col, 1, True)
                visited[row][col] = False

    print(f'#{tc} {max_length}')