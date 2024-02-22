import sys
sys.stdin = open("./baekjoon/algo_study/2206 벽 부수고 이동/input.txt", "r")

from collections import deque
# input = sys.stdin.readline

def bfs():
    while Q:
        print(case_matrix)
        row, col = Q.popleft()
        for idx in range(4):
            new_row, new_col = row+d_row[idx], col+d_col[idx]
            if 0 <= new_row < N and 0 <= new_col < M:
                if case_matrix[new_row][new_col] == '0':
                    case_matrix[new_row][new_col] = case_matrix[row][col] + 1
                    Q.append((new_row, new_col))
                    if new_row == end_row and new_col == end_col:
                        return case_matrix[new_row][new_col]
    if new_row != end_row or new_col != end_col:
        return re(row, col)
    return -1

def re(row, col):
    global can_break
    if can_break == 1:
        for idx in range(4):
            new_row, new_col = row+d_row[idx], col+d_col[idx]
            if 0 <= new_row < N and 0 <= new_col < M:
                if case_matrix[new_row][new_col] == '1':
                    case_matrix[new_row][new_col] = case_matrix[row][col] + 1
                    Q.append((new_row, new_col))
        can_break -= 1
        return bfs()
    else:
        return -1


d_row, d_col = [0,0,-1,1], [-1,1,0,0]
N, M = map(int, input().split())
end_row, end_col = N-1, M-1
case_matrix = [list(input()) for _ in range(N)]

can_break = 1

case_matrix[0][0] = 1
Q = deque()
Q.append((0,0,))
print(bfs())