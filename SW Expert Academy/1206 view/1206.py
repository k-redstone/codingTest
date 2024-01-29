import sys
sys.stdin = open("input.txt", "r")

T = 10

for _ in range(T):
    N = int(input().rstrip())
    case_list = list(map(int, input().rstrip().split()))

    count = 0
    for num in range(2, N-2, 1):
        near_height = [case_list[num - 2], case_list[num - 1], case_list[num + 1], case_list[num + 2]]
        near_height = sorted(near_height)
        if case_list[num] > near_height[-1]:
            count += case_list[num] - near_height[-1]

    print(f'#{_ + 1} {count}')
