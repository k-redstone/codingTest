import sys
from collections import deque
input = sys.stdin.readline

'''
1.현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
2.현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우,
    1.바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
    2.바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우,
    1. 반시계 방향으로 90도 회전한다.
    2. 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
    3. 1번으로 돌아간다.
'''

d_row, d_col = [1, 0, -1, 0], [0, 1, 0, -1]
N, M = map(int, input().split())
start_row, start_col, direction = map(int, input().split())
case_matrix = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
temp = 0


def method_1(arr, direction):
    if direction == 0:
        if case_matrix[arr[2][0]][arr[2][1]] == 1:
            return False
        return arr[2]
    if direction == 1:
        if case_matrix[arr[3][0]][arr[3][1]] == 1:
            return False
        return arr[3]
    if direction == 2:
        if case_matrix[arr[0][0]][arr[0][1]] == 1:
            return False
        return arr[0]
    if direction == 3:
        if case_matrix[arr[1][0]][arr[1][1]] == 1:
            return False
        return arr[1]
    
def method_2(row, col, direction):
    if direction == 0:
        if case_matrix[row + d_row[1]][col +d_col[1]] == 0:
            return (row + d_row[1], col +d_col[1], 1)
        return (row, col, 1)
    if direction == 1:
        if case_matrix[row + d_row[2]][col +d_col[2]] == 0:
            return (row + d_row[2], col +d_col[2], 2)
        return (row, col, 2)
    if direction == 2:
        if case_matrix[row + d_row[3]][col +d_col[3]] == 0:
            return (row + d_row[3], col +d_col[3], 3)
        return (row, col, 3)
    if direction == 3:
        if case_matrix[row + d_row[0]][col +d_col[0]] == 0:
            return (row + d_row[0], col +d_col[0], 0)
        return (row, col, 0)

while True:
    if case_matrix[start_row][start_col] == 0:
        cnt += 1
        print(cnt)
        case_matrix[start_row][start_col] = 2
    change =False
    check_list = []
    for num in range(4):
        new_row = start_row + d_row[num]
        new_col = start_col + d_col[num]
        if 0 <= new_row < N and 0 <= new_col < M:
            check_list.append((new_row,new_col))
            if case_matrix[new_row][new_col] == 0:
                change = True
    if not change:
        result = method_1(check_list, direction)
        if not result:
            break
        start_row, start_col = result
    else:
        print('change')
        start_row, start_col, direction = method_2(start_row, start_col, direction)

    print('--------------------')
    print(start_row, start_col)
print(cnt)