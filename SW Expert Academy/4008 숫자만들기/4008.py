import sys
import math
from collections import Counter
sys.stdin = open("./SW Expert Academy/4008 숫자만들기/input.txt", "r")

def calc(sign, sum, num):
    if sign == 0:
        return sum + num
    if sign == 1:
        return sum - num
    if sign == 2:
        return sum * num
    if sign == 3:
        return math.trunc(sum / num)


def back(arr, sum_num, path):
    global max_num, min_num
    if len(sign_list) == len(path):
        for idx, item in enumerate(path):
            sum_num = calc(item, sum_num, num_list[idx+1])

        max_num = max(max_num, sum_num)
        min_num = min(min_num, sum_num)
        return
    for item in arr:
        if arr[item] == 0:
            continue
        arr[item] -= 1
        path.append(item)
        back(arr, sum_num, path)
        path.pop()
        arr[item] += 1



T = int(input())


for tc in range(1, T+1):
    N = int(input())
    sign_case = list(map(int, input().split()))
    num_list = list(map(int, input().split()))
    max_num = -100000000
    min_num = 100000000

    sign_list = []
    for idx, cnt in enumerate(sign_case):
        for _ in range(cnt):
            sign_list.append(idx)
    remain = Counter(sign_list)

    back(remain, num_list[0], [])
    res = max_num - min_num
    print(f'#{tc} {res}')