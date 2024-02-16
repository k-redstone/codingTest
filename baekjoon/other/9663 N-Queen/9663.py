import sys
input = sys.stdin.readline

delta =[
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
    (-1, -1),
    (-1, 1),
    (1, -1),
    (1, 1)
]

def check(row, col):
    return_list = []
    for item in delta:
        temp = 1
        while True:
            new_row , new_col = row + (item[0]*temp), col + (item[1]*temp)
            if 0 <= new_row < N and 0 <= new_col < N:
                return_list.append((new_row, new_col))
                temp += 1
            else:
                break
    return return_list

def change(case, num):
    for row, col in case:
        matrix[row][col] = num


def backtrack(idx):
    global cnt
    if idx == N:
        cnt += 1
        return
    for item in matrix:
        if 0 not in item:
            return
    for row in range(N):
        for col in range(N):
            if matrix[row][col] == 0:
                matrix[row][col] = 1
                check_list = check(row, col)
                change(check_list, 1)
                print(check_list)
                backtrack(idx+1)
                matrix[row][col] = 0
                change(check_list, 0)
                print(check_list)
                

cnt = 0
N = int(input())
matrix = [[0]*N for _ in range(N)]
backtrack(0)
print(cnt)
# for i in matrix:
#     print(*i)