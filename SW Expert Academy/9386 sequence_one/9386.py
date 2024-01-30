import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for _ in range(T):
    case_size = int(input())
    case_list = list(map(int, input()))
    count = 0
    max_count = 0
    for item in case_list:
        if item == 1:
            count += 1
        if item == 0:
            count = 0
        if max_count < count:
            max_count = count

    print(f'#{_ + 1} {max_count}')
