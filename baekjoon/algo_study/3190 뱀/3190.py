import sys
from collections import deque
input = sys.stdin.readline


def change(direction, next):
    if direction == 'R':
        if next == 'L':
            return 'U'
        if next == 'D':
            return 'D'
    if direction == 'L':
        if next == 'L':
            return 'D'
        if next == 'D':
            return 'U'
    if direction == 'U':
        if next == 'L':
            return 'L'
        if next == 'D':
            return 'R'
    if direction == 'D':
        if next == 'L':
            return 'R'
        if next == 'D':
            return 'L'
        

def move(direction):
    row, col = Q[0]
    if direction == 'R':
        new_row, new_col = row, col+1
    if direction == 'L':
        new_row, new_col = row, col-1
    if direction == 'U':
        new_row, new_col = row-1, col
    if direction == 'D':
        new_row, new_col = row+1, col

    if 0 <= new_row < N and 0 <= new_col < N:
        if case_matrix[new_row][new_col] == 1:
            return False
        Q.appendleft((new_row, new_col))
        if case_matrix[new_row][new_col] == 2:
            case_matrix[new_row][new_col] = 1
            return True
        case_matrix[new_row][new_col] = 1
        row, col = Q[-1]
        case_matrix[row][col] = 0
        Q.pop()
    else:
        return False
    
    return True
        


N = int(input())
case_matrix = [[0]*N for _ in range(N)]
case_matrix[0][0] = 1
K = int(input())
apple_list = [list(map(int, input().split())) for _ in range(K)]
for apple in apple_list:
    row, col = apple
    case_matrix[row-1][col-1] = 2
L = int(input())
info_list = [list(input().split()) for _ in range(L)]

Q = deque([(0,0)])
direction = 'R'
total_time = 0
idx = 0

while True:
    if idx < L and int(info_list[idx][0]) == total_time:
        direction = change(direction, info_list[idx][1])
        idx += 1
        continue
    result = move(direction)
    if result:
        total_time += 1
        continue
    else:
        total_time += 1
        print(total_time)
        exit()
