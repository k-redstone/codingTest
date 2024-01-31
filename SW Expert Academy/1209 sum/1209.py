import sys
sys.stdin = open("./input.txt", "r")

T = 10

for _ in range(T):
    cn = int(input())
    # case 행렬 저장
    case_matrix = [list(map(int, input().split())) for _ in range(100)]
    # 행,열,대각선의 합 리스트 생성
    row_list = [0] * 100
    col_list = [0] * 100
    cross_list = [0, 0]
    # 행렬 반복
    for row in range(100):
        for col in range(100):
            # 오른쪽에서 왼쪽 대각선 범위에 있는경우
            if row + col == 99:
                cross_list[1] += case_matrix[row][col]
            # 왼쪽에서 오른쪽 대각선 범위에 있는경우
            if row == col:
                cross_list[0] += case_matrix[row][col]
            # 행과 열리스트에 합을 추가
            row_list[row] += case_matrix[row][col]
            col_list[col] += case_matrix[row][col]

    print(f'#{cn} {max([max(row_list), max(col_list), max(cross_list)])}')

