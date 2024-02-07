import sys
sys.stdin = open('./input.txt', 'r')


def judge(text):
    return int(text == text[::-1])


for tc in range(1, 11):
    T = int(input())
    case_matrix = [list(input()) for _ in range(8)]
    cnt = 0
    for row in range(8):
        for col in range(8-T+1):
            cnt += judge(case_matrix[row][col:col+T])
    for col in range(8):
        for row in range(8-T+1):
            cnt += judge(''.join(case_matrix[num][col] for num in range(row, row+T)))
    print(f'#{tc} {cnt}')
