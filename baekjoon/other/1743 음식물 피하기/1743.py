import sys
input = sys.stdin.readline
from collections import deque


d_row, d_col = [0, 0, -1, 1], [1, -1, 0, 0]

def bfs(row, col):
    Q = deque([(row, col)])
    trash = 0
    while Q:
        row, col = Q.popleft()
        for num in range(4):
            new_row, new_col = row+d_row[num], col+d_col[num]
            if 0 <= new_row < N and 0 <= new_col < M:
                if case_matrix[new_row][new_col] == 1:
                    trash +=1
                    case_matrix[new_row][new_col] = 0
                    Q.append((new_row, new_col))
    return trash


N, M, K = map(int, input().split())
case_matrix = [[0]*M for _ in range(N)]
case_list = []
max_trash = 0
for _ in range(K):
    row, col = map(int, input().split())
    case_matrix[row-1][col-1] = 1
    case_list.append((row-1, col-1))

for item in case_list:
    row, col = item
    if case_matrix[row][col] == 0:
        continue
    max_trash = max(max_trash, bfs(row, col))

print(max_trash)
    

