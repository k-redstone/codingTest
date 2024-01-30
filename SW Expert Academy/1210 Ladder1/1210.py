import sys
sys.stdin = open("./SW Expert Academy/1210 Ladder1/input.txt", "r")

T = 10

for _ in range(T):
    test_num = int(input())
    case_matrix = [ list(map(int, input().split())) for _ in range(100)]
    for i in range(100):
        if case_matrix[99][i] == 2:
            row = 99
            col = i
            break
    direction = ""
    while row != 0:
        # 왼쪽 이동
        if direction == 'left':
            col -= 1
            if case_matrix[row + 1][col] == 1:
                direction = 'top'
                continue
        # 오른쪽 이동
        elif direction == 'right':
            col += 1
            if case_matrix[row + 1][col] == 1:
                direction = 'top'
                continue
        else:
            row -= 1
            if col -1  >= 0:
                if case_matrix[row][col - 1] == 1:
                    direction = 'left'
                    continue
            if col + 1 < 100:
                if case_matrix[row][col + 1] == 1:
                    direction = 'right'
                    continue


    print(f'#{test_num} {col}')

