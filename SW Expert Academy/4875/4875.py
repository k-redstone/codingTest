import sys
sys.stdin = open("./SW Expert Academy/input.txt", "r")

T = int(input())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def valid(num):
    if num < 0:
        return False
    if num >= N:
        return False
    return True

# 상하좌우 유효성 검사
def set_point():
    while stack_list:
        x, y = stack_list.pop()
        case_list[x][y] = -1
        for num in range(4):
            if valid(x + dx[num]) and valid(y + dy[num]):
                col_x = x + dx[num]
                col_y = y + dy[num]
                if case_list[col_x][col_y] == 3:
                    return 1
                elif case_list[col_x][col_y] == 0:
                    stack_list.append((col_x, col_y))
    return 0


for _ in range(T):
    N = int(input())
    case_list = [list(map(int, input())) for _ in range(N)]

    # 시작점과 도착점 설정
    start_point = []
    end_point = []
    for i in range(N):
        for j in range(N):
            if case_list[i][j] == 2:
                start_point.append((i, j))
                break
    stack_list = [start_point[0]]

    print(f'#{_ + 1} {set_point()}')

