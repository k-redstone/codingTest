import sys
sys.stdin = open("./baekjoon/algo_study/2206 벽 부수고 이동/input.txt", "r")
from collections import deque
# input = sys.stdin.readline

def bfs():
    while Q:
        row, col, broken = Q.popleft()
        if row == end_row and col == end_col:
            return case_matrix[row][col][broken][1]
        for idx in range(4):
            new_row, new_col = row + d_row[idx], col + d_col[idx]
            if 0 <= new_row < N and 0 <= new_col < M:
                if case_matrix[new_row][new_col][broken][0] == '0' and case_matrix[new_row][new_col][broken][1] == 0:
                    case_matrix[new_row][new_col][broken][1] = case_matrix[row][col][broken][1] + 1
                    Q.append((new_row, new_col, broken))
                elif broken == 0 and case_matrix[new_row][new_col][1][0] == '1' and case_matrix[new_row][new_col][1][1] == 0:
                    case_matrix[new_row][new_col][1][1] = case_matrix[row][col][broken][1] + 1
                    Q.append((new_row, new_col, 1))
    return -1

d_row, d_col = [0,0,-1,1], [-1,1,0,0]
N, M = map(int, input().split())
end_row, end_col = N-1, M-1

case_matrix = [ [[[item, 0],[item, 0]] for item in list(input())] for _ in range(N)]


case_matrix[0][0][0][0] = 1
case_matrix[0][0][1][0] = 1
case_matrix[0][0][0][1] = 1

Q = deque()
Q.append((0, 0, 0))
print(bfs())