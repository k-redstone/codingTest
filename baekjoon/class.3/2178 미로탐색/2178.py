import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    Q = deque([(0,0)])
    while Q:
        row, col = Q.popleft()
        for idx in range(4):
            new_row, new_col = row+d_row[idx], col+d_col[idx]
            if 0 <= new_row < N and 0 <= new_col < M:
                if case_matrix[new_row][new_col] == 1:
                    case_matrix[new_row][new_col] += case_matrix[row][col]
                    if new_row == N-1 and new_col == M-1:
                        return case_matrix[new_row][new_col]
                    Q.append((new_row, new_col))

d_row, d_col = [-1, 1, 0, 0], [0, 0, -1, 1]
N, M = map(int, input().rstrip().split())
case_matrix = [list(map(int, input().rstrip())) for _ in range(N)]
print(bfs())