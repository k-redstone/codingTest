import sys
from collections import deque
sys.stdin = open("./input.txt", "r")

T = int(input())
d_row, d_col = [0, 0, -1, 1], [1, -1, 0, 0]


def bfs():
    while Q:
        row, col = Q.popleft()
        for num in range(4):
            new_row, new_col = row + d_row[num], col + d_col[num]
            if 0 <= new_row < N and 0 <= new_col < N:
                if case_matrix[new_row][new_col] == '3':
                    return case_matrix[row][col] - 1
                if case_matrix[new_row][new_col] == '0':
                    Q.append((new_row, new_col))
                    case_matrix[new_row][new_col] = case_matrix[row][col] + 1
    return 0
for tc in range(1, T+1):
    N = int(input())
    case_matrix = [list(input()) for _ in range(N)]
    for row in range(N):
        for col in range(N):
            if case_matrix[row][col] == '2':
                start_row, start_col, Q = row, col, deque([(row, col)])
                case_matrix[row][col] = 1
                break
    print(f'#{tc} {bfs()}')
