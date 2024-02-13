import sys
from collections import deque
# sys.stdin = open("data.txt", "r")
input = sys.stdin.readline

M, N = map(int, input().split())
case_list = [list(map(int, input().split())) for _ in range(N)]
d_row = [0, 0, -1, 1]
d_col = [-1, 1, 0, 0]
que = deque()

for row in range(N):
    for col in range(M):
        if case_list[row][col] == 1:
            que.append((row, col))

def rare_tomato(Q):
    while Q:
        item = Q.popleft()
        for num in range(4):
            new_row = item[0] + d_row[num]
            new_col = item[1] + d_col[num]
            if 0 <= new_row < N and 0 <= new_col < M:
                if case_list[new_row][new_col] == 0:
                    case_list[new_row][new_col] = case_list[item[0]][item[1]] + 1
                    Q.append((new_row, new_col))
    return que
matrix = rare_tomato(que)



print(cnt)