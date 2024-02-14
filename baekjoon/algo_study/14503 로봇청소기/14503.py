import sys
input = sys.stdin.readline

d_row, d_col = [-1, 0, 1, 0], [0, 1, 0, -1]

def can_clean(row, col):
    return 0 <= row < N and 0 <= col < M and case_matrix[row][col] == 0

def rotate_left(direction):
    return (direction - 1) % 4

def move_back(row, col, direction):
    return row + d_row[(direction + 2) % 4], col + d_col[(direction + 2) % 4]

N, M = map(int, input().split())
start_row, start_col, direction = map(int, input().split())
case_matrix = [list(map(int, input().split())) for _ in range(N)]
cnt = 0

while True:
    if case_matrix[start_row][start_col] == 0:
        cnt += 1
        case_matrix[start_row][start_col] = 2

    cleaned = False
    for _ in range(4):
        next_direction = rotate_left(direction)
        next_row, next_col = start_row + d_row[next_direction], start_col + d_col[next_direction]
        if can_clean(next_row, next_col):
            start_row, start_col, direction = next_row, next_col, next_direction
            cleaned = True
            break
        direction = next_direction

    if not cleaned:
        back_row, back_col = move_back(start_row, start_col, direction)
        if case_matrix[back_row][back_col] == 1:
            break
        start_row, start_col = back_row, back_col

print(cnt)