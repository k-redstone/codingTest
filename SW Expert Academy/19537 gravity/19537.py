import sys
sys.stdin = open("input.txt", "r")

T = int(input().rstrip())

for _ in range(T):
    N = int(input().rstrip())
    case_list = list(map(int, input().rstrip().split()))
    max_move = 0

    for cur in range(N):
        count = 0
        for temp in range(cur + 1, N, 1):
            if case_list[cur] > case_list[temp]:
                count += 1
        if max_move < count:
            max_move = count
    print(f'#{_ + 1} {max_move}')
