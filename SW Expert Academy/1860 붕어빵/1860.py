import sys
sys.stdin = open("./input.txt", "r")
T = int(input())
def solution():
    prev_fish = prev_remain = 0
    for waiting in set_list:
        fish = (waiting // M) * K - prev_fish + prev_remain
        if fish < count_dict[waiting]:
            return 'Impossible'
        prev_fish = (waiting // M) * K
        prev_remain = fish - count_dict[waiting]
    return 'Possible'

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    case_list = list(map(int, input().split()))
    count_dict = {}
    for item in case_list:
        if count_dict.get(item) is None:
            count_dict[item] = 1
        else:
            count_dict[item] += 1
    set_list = sorted(set(case_list))
    print(f'#{tc} {solution()}')