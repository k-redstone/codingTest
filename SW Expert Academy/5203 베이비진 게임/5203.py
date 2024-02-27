import sys
sys.stdin = open("./input.txt", "r")

T = int(input())


def is_run(arr, num):
    if arr[num] >= 3:
        return True
    return False


def triplet(arr):
    temp = 0
    for num in range(10):
        if arr[num] == 0:
            temp = 0
            continue
        if arr[num] != 0:
            temp += 1
            if temp >= 3:
                return True
    return False

for tc in range(1, T+1):
    case_list = list(map(int, input().split()))
    player_1 = [0]*10
    player_2 = [0]*10
    win = 0

    for idx in range(len(case_list)):
        if idx % 2 == 0:
            player_1[case_list[idx]] += 1
            if triplet(player_1) or is_run(player_1, case_list[idx]):
                win = 1
                break
        else:
            player_2[case_list[idx]] += 1
            if triplet(player_2) or is_run(player_2, case_list[idx]):
                win = 2
                break
    print(f'#{tc} {win}')
