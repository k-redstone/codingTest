import sys
sys.stdin = open("./baekjoon/IM 대비/10157 자리배정/input.txt", "r")


given_col, given_row = map(int, sys.stdin.readline().split())
wait_num = int(sys.stdin.readline())
new_matrix = [[0]*given_col for _ in range(given_row)]

def solution(wait_num, new_matrix):
    row = given_row - 1
    col = 0
    cnt = new_matrix[row][col] = 1
    d_row = [-1, 0, 1, 0]
    d_col = [0, 1, 0, -1]

    return_row = return_col = 0
    rotate_num = 0
    while cnt <= given_row*given_col:
        if cnt == wait_num:
            return (return_col + 1, abs(return_row) + 1)

        new_row = row + d_row[rotate_num]
        new_col = col + d_col[rotate_num]
        if 0 <= new_row < given_row and 0 <= new_col < given_col:
            if new_matrix[new_row][new_col] == 0:
                cnt += 1
                new_matrix[new_row][new_col] = cnt
                row = new_row
                col = new_col
                return_row += d_row[rotate_num]
                return_col += d_col[rotate_num]
            else:
                rotate_num = (rotate_num + 1) % 4
        else:
            rotate_num = (rotate_num + 1) % 4

if given_col * given_row < wait_num:
    print(0)
elif wait_num == 1:
       print(1, 1)
else:
    print(*solution(wait_num,new_matrix))