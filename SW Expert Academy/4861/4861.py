import sys
sys.stdin = open("./SW Expert Academy/input.txt", "r")

T = int(input())

for _ in range(T):
    N, M = list(map(int, input().split()))
    case_list = [ input() for _ in range(N)]
    for x in case_list:
        for num in range(N - M + 1):
            new_str = x[0 + num:]
            if new_str == new_str[-1::-1]:
                result = new_str

    for j in range(N):
        new_str = ""
        for i in range(N):
            new_str += case_list[i][j]
        for num in range(N - M + 1):
            new_strY = new_str[0 + num:]
            if new_strY == new_strY[-1::-1]:
                result = new_strY
    print(f'#{_ + 1} {result}')