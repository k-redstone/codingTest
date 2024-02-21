import sys
from collections import deque
sys.stdin = open("./input.txt", "r")

T = int(input())

def search():
    for row, col in point:
        for idx in range(4):
            temp_row, temp_col = row, col
            cnt = 1
            while True:
                temp_row, temp_col = temp_row+d_row[idx], temp_col+d_col[idx]
                if 0 <= temp_row < N and 0 <= temp_col < N:
                    if case_matrix[temp_row][temp_col] == 'o':
                        cnt += 1
                        if cnt >= 5:
                            return 'YES'
                    else:
                        break
                else:
                    break
    return 'NO'



d_row, d_col = [0, 1, 1, 1], [1, 0, 1, -1]
for tc in range(1, T+1):
    N = int(input())
    case_matrix = [list(input()) for _ in range(N)]
    result = ''
    point = []
    for row in range(N):
        for col in range(N):
            if case_matrix[row][col] == 'o':
                point.append((row, col))
    result = search()

    print(f'#{tc} {result}')