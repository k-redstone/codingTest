import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

def bfs():
    global result, cnt
    Q = deque()
    visited = set()
    for vi in virus:
        visited.add(vi)
        Q.append(vi)
    while Q:
        row, col = Q.popleft()

        for n_row, n_col in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
            if 0 <= n_row < N and 0 <= n_col < M:
                if matrix[n_row][n_col] == 0 and (n_row, n_col) not in visited:
                    visited.add((n_row, n_col))
                    Q.append((n_row, n_col))
    
    result = max(result, cnt - len(visited))

def solution():
    wall_combi = list(combinations(empty, 3))
    for wall in wall_combi:
        for row, col in wall:
            matrix[row][col] = 1
        bfs()
        for row, col in wall:
            matrix[row][col] = 0

N, M = map(int, input().rstrip().split())
matrix = [list(map(int, input().rstrip().split())) for _ in range(N)]
cnt = N*M
result = 0
wall = []
empty = []
virus = []

for row in range(N):
    for col in range(M):
        if matrix[row][col] == 0:
            empty.append((row, col))
        elif matrix[row][col] == 1:
            wall.append((row, col))
        elif matrix[row][col] == 2:
            virus.append((row, col))

cnt -= (len(wall)+3)

solution()

print(result)