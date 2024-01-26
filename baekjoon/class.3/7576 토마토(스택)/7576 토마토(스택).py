import sys
sys.stdin = open("data.txt", "r")


M, N = map(int, sys.stdin.readline().rstrip().split())
case_list = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
stack_list = []
need_visit = []


def valid_M(number):
    if number < 0:
        return False
    if number >= M:
        return False
    return True


def valid_N(number):
    if number < 0:
        return False
    if number >= N:
        return False
    return True

count_zero = 0

for i in range(N):
    for j in range(M):
        if case_list[i][j] == 1:
            stack_list.append((i, j))
            need_visit.append((i, j))
        if case_list[i][j] == 0:
            count_zero += 1

def rare_tomato(stack_list, need_visit):
    global count_zero
    count = -1
    pointer = len(stack_list)
    while pointer != len(stack_list) -1:
        length = len(stack_list)
        pointer -= length
        # while pointer != len(stack_list):
        # length = len(stack_list)
        for _ in range(length - pointer):
            y, x = stack_list[pointer]
            case_list[y][x] = 1
            for num in range(4):
                col_x = x + dx[num]
                col_y = y + dy[num]
                if valid_M(col_x) and valid_N(col_y):
                    if case_list[col_y][col_x] == 0:
                        # print("넣음")
                        count_zero -= 1
                        stack_list.append((col_y, col_x))
                        pointer += 1
        print(case_list)
        print(stack_list)
        print(pointer)
        count += 1
    # print(count)
    return count

count = rare_tomato(stack_list, need_visit)
# num = -1
# while need_visit:
#     stack_list = need_visit
#     need_visit = []
#     rare_tomato(stack_list)
#     num += 1
    

if count_zero > 0:
    print(-1)
if count == 1:
    print(0)
else:
    print(count)