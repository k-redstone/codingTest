import sys
sys.stdin = open("data.txt", "r")


T = int(sys.stdin.readline().rstrip())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def valid_N(num):
    if num < 0:
        return False
    if num > N:
        return False
    return True

def valid_M(num):
    if num < 0:
        return False
    if num > M:
        return False
    return True


def find_group():
    num = 0
    while stack:
        pop_value = stack.pop()
        case_dict[pop_value] = True
        x,y = pop_value
        for num in range(4):
            col_x = x + dx[num]
            col_y = y + dy[num]
            if valid_M(col_x) and valid_N(col_y):
                if case_dict.get((col_x, col_y)) is False:
                    stack.append((col_x, col_y))
        num += 1
    return 1

for _ in range(T):
    M, N, K = list(map(int, sys.stdin.readline().rstrip().split()))
    case_list = [ tuple(map(int, sys.stdin.readline().rstrip().split())) for _ in range(K)]
    case_dict = {}

    for item in case_list:
        case_dict[item] = False

    stack =[]
    group_count = 0

    for key, value in case_dict.items():
        if value is True:
            continue
        else:
            stack.append(key)
            group_count += find_group()
    print(f'{group_count}')
