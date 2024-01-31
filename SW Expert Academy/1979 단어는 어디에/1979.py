import sys

sys.stdin = open('./input.txt', 'r')
T = int(input())


def solution(N, K, matrix):
    cnt = 0
    result_list = []
    for row in range(N):
        result_list += filter(None, matrix[row].split('0'))
    for col in range(N):
        col_str = ''.join(matrix[row][col] for row in range(N))
        result_list += filter(None, col_str.split('0'))
    for item in result_list:
        if len(item) == K:
            cnt += 1
    return cnt


for tc in range(1, T + 1):
    N, K = map(int, input().split())
    case_matrix = ["".join(input().split()) for _ in range(N)]
    print(f'#{tc} {solution(N, K, case_matrix)}')