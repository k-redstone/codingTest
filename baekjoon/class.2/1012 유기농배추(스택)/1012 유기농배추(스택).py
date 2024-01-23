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
        print(f'기준점 {x, y}')
        for num in range(4):
            if valid_N(x + dx[num]) and valid_M(y + dy[num]):
                col_x = x + dx[num]
                col_y = y + dy[num]
                print(col_x, col_y)
                if case_dict.get((col_x, col_y)) is False:
                    stack.append((col_x, col_y))
                    print("스택넣기")
            print('상하좌우')
        print(stack)
        print(case_dict)
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
            print(f"{key} 뭔가 진행됨")
        print()
    print(f'#{_ +1} {group_count}')
