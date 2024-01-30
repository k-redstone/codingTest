import sys
sys.stdin = open("input.txt", "r")

T = int(input().strip())

for _ in range(T):
    case_list = list(map(int, input().strip()))
    count_list = [0] * 10
    for x in range(len(case_list)):
        count_list[case_list[x]] += 1
    for num in range(0, len(count_list) - 2, 1):
        if count_list[num] == 0:
            continue
        while count_list[num] >= 1 and count_list[num + 1] >= 1 and count_list[num + 2] >= 1:
            count_list[num] -= 1
            count_list[num + 1] -= 1
            count_list[num + 2] -= 1

    for num in range(len(count_list)):
        while count_list[num] >= 3:
            count_list[num] -= 3
    if sum(count_list) == 0:
        print(f'#{_ + 1} True')
    else:
        print(f'#{_ + 1} False')



