from itertools import combinations
import sys
sys.stdin = open('./input.txt', 'r')

T = int(input())

d_row = [0, 1, 0, -1]
d_col = [1, 0, -1, 0]


for tc in range(1, T+1):
    N = int(input())
    row = col = 0
    cnt = 1
    new_matrix = [[0]*N for _ in range(N)]
    new_matrix[row][col] = 1

    if N == 1:
        print(f'#1')
        print(new_matrix[0][0])
        continue

    while cnt < N**2:
        for num in range(4):
            for _ in range(N):
                if 0 <= row + d_row[num] < N and 0 <= col + d_col[num] < N:
                    if new_matrix[row + d_row[num]][col + d_col[num]] == 0:
                        cnt += 1
                        row = row + d_row[num]
                        col = col + d_col[num]
                        new_matrix[row][col] = cnt
                    else:
                        continue
                else:
                    continue
    print(f'#{tc}')
    for item in new_matrix:
        print(' '.join(map(str, item)))



