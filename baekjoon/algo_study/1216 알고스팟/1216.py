import sys
from collections import deque
from math import inf
input = sys.stdin.readline

def solution():
    Q = deque([(0, 0, 0)])
    dist = [[inf] * N for _ in range(M)]
    dist[0][0] = 0
    
    while Q:
        weight, row, col = Q.popleft()
        if dist[row][col] < weight:
            continue
        for idx in range(4):
            new_row, new_col = row+d_row[idx], col+d_col[idx]
            if 0 <= new_row < M and 0 <= new_col < N:
                if case_matrix[new_row][new_col] == 1:
                    if dist[new_row][new_col] > weight+1:
                        dist[new_row][new_col] = weight+1
                        Q.append((weight+1, new_row, new_col))
                else:
                    if dist[new_row][new_col] > weight:
                        dist[new_row][new_col] = weight
                        Q.appendleft((weight, new_row, new_col))
    return dist[-1][-1]




N, M = map(int, input().rstrip().split())
case_matrix = [list(map(int, input().rstrip())) for _ in range(M)]
d_row, d_col = [-1, 1, 0, 0], [0, 0, -1, 1]

print(solution())