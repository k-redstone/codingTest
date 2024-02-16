import sys
from collections import deque
sys.stdin = open("./input.txt", "r")

def bfs():
    while Q:
        row, col = Q.popleft()
        for num in range(4):
            new_row, new_col = row + d_row[num], col + d_col[num]
            if 0 <= new_row < 100 and 0 <= new_col < 100:
                if case_matrix[new_row][new_col] == '0':
                    Q.append((new_row, new_col))
                    case_matrix[row][col] = '1'
                    continue
                if case_matrix[new_row][new_col] == '2':
                    return 1
    return 0

d_row, d_col = [0, 0, -1, 1], [1, -1, 0, 0]
for tc in range(1, 11):
    _ = input()
    case_matrix = [list(input()) for _ in range(100)]
    for row in range(100):
        for col in range(100):
            if case_matrix[row][col] == '3':
                start_row, start_col, Q = row, col, deque([(row, col)])
                break

    print(f'#{tc} {bfs()}')
