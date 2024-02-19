import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
case_matrix = [list(input().split()) for _ in range(N)]


def bfs():
    while Q:
        row, col = Q.popleft()
        for idx in range(4):
            new_row, new_col = row+d_row[idx], col+d_col[idx]
            if 0 <= new_row < N and 0 <= new_col < M:
                if case_matrix[new_row][new_col] == -1:
                    case_matrix[new_row][new_col] = case_matrix[row][col] + 1
                    Q.append([new_row, new_col])
                    
Q = deque()
for row in range(N):
    for col in range(M):
        if case_matrix[row][col] == '2':
            start_row, start_col = row, col
            case_matrix[row][col] = 0
            Q.append([row, col])
        if case_matrix[row][col] == '1':
            case_matrix[row][col] = -1
d_row, d_col = [0, 0, -1, 1], [ -1, 1, 0, 0]
bfs()


for case in case_matrix:
    print(*case)