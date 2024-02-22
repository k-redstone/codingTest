import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    visited = [[[0, 0] for _ in range(M)] for _ in range(N)]
    Q = deque()
    Q.append((0, 0, 0))
    visited[0][0][0] = 1

    while Q:
        row, col, broken = Q.popleft()
        if row == N-1 and col == M-1:
            return visited[row][col][broken]

        for idx in range(4):
            new_row, new_col = row + d_row[idx], col + d_col[idx]
            if 0 <= new_row < N and 0 <= new_col < M:
                if case_matrix[new_row][new_col] == '0' and visited[new_row][new_col][broken] == 0:
                    visited[new_row][new_col][broken] = visited[row][col][broken] + 1
                    Q.append((new_row, new_col, broken))
                elif broken == 0 and case_matrix[new_row][new_col] == '1' and visited[new_row][new_col][1] == 0:
                    visited[new_row][new_col][1] = visited[row][col][broken] + 1
                    Q.append((new_row, new_col, 1))

    return -1

d_row, d_col = [0, 0, -1, 1], [-1, 1, 0, 0]
N, M = map(int, input().split())
case_matrix = [input().rstrip() for _ in range(N)]

print(bfs())