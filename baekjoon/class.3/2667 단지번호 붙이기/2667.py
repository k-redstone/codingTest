import sys
from collections import deque
# sys.stdin = open("data.txt", "r")
input = sys.stdin.readline



def bfs(row, col):
    Q = deque()
    Q.append((row, col))
    case_matrix[row][col] = 2
    house = 1
    while Q:
        cur_row, cur_col = Q.popleft()
        for idx in range(4):
            new_row, new_col = cur_row+d_row[idx], cur_col+d_col[idx]
            if 0 <= new_row < N and 0 <= new_col < N:
                if case_matrix[new_row][new_col] == 1:
                    case_matrix[new_row][new_col] = 2
                    Q.append((new_row, new_col))
                    house += 1
    return house


d_row, d_col = [-1, 1, 0, 0], [0, 0, -1, 1]

N = int(input())
case_matrix = [list(map(int, input().rstrip())) for _ in range(N)]

total = 0
house_num = []
for row in range(N):
    for col in range(N):
        if case_matrix[row][col] == 1:
            total += 1
            house_num.append(bfs(row, col))

print(total)
house_num.sort()
for num in house_num:
    print(num)