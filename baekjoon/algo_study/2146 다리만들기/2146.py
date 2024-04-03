import sys
from collections import deque
input = sys.stdin.readline

def get_island():
    idx = 2
    Q_is = deque()
    for row in range(N):
        for col in range(N):
            if case_matrix[row][col] == 1:
                visited[row][col] = -1
                case_matrix[row][col] = idx
                Q_is.append((row,col))
                while Q_is:
                    row, col = Q_is.popleft()
                    for n_row, n_col in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
                        if 0 <= n_row < N and 0 <= n_col < N:
                            if case_matrix[n_row][n_col] == 1:
                                visited[n_row][n_col] = -1
                                case_matrix[n_row][n_col] = idx
                                Q_is.append((n_row, n_col))
                idx +=1

def solution():
    Q = deque()
    for row in range(N):
        for col in range(N):
            if visited[row][col] == -1:
                Q.append((row, col, 0, case_matrix[row][col]))
    ans = 10000
    while Q:
        row, col, dist, island = Q.popleft()
        for n_row, n_col in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
            if 0 <= n_row < N and 0 <= n_col < N:
                if visited[n_row][n_col] != 0 and visited[n_row][n_col] != -1:
                    if case_matrix[n_row][n_col] == island: 
                        continue
                    ans = min(ans, visited[n_row][n_col] + dist)
                else:
                    case_matrix[n_row][n_col] = island
                    visited[n_row][n_col] = dist+1
                    Q.append((n_row, n_col, visited[n_row][n_col], island))
    return ans


N = int(input())
case_matrix = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)] 
get_island()
print(solution())