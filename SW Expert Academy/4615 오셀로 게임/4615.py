import sys
sys.stdin = open("./input.txt", "r")

T = int(input())
d_row = [0, 0, -1, 1, -1, 1, 1, -1]
d_col = [-1, 1, 0, 0, 1, 1, -1, -1]

def init(N):
    default_point = N // 2 - 1
    board = [[0] * N for _ in range(N)]
    board[default_point][default_point] = 2
    board[default_point][default_point + 1] = 1
    board[default_point + 1][default_point] = 1
    board[default_point + 1][default_point + 1] = 2
    return board

def start(board, case):
    for item in case:
        color = item[2]
        row = item[1] - 1
        col = item[0] - 1
        board[row][col] = color
        for num in range(8):
            new_row = row + d_row[num]
            new_col = col + d_col[num]
            spread = 1
            stack = []
            while 0 <= new_row < N and 0 <= new_col < N and board[new_row][new_col] == 3 - color:
                new_row = row + (d_row[num] * spread)
                new_col = col + (d_col[num] * spread)
                if 0 <= new_row < N and 0 <= new_col < N:
                    if board[new_row][new_col] == 0:
                        break
                    spread += 1
                    stack.append((new_row, new_col))
                else:
                    stack.clear()
                    break
            else:
                for point in stack:
                    board[point[0]][point[1]] = color


for tc in range(1, T+1):
    N, M = map(int, input().split())
    board = init(N)
    put_list = [list(map(int, input().split())) for _ in range(M)]
    start(board, put_list)
    black_cnt = sum(row.count(1) for row in board)
    white_cnt = sum(row.count(2) for row in board)
    print(f'#{tc} {black_cnt} {white_cnt}')