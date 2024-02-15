import sys
from collections import deque
sys.stdin = open("./input.txt", "r")

T = int(input())
def cooking(case):
    cnt = 0
    fire = [[0, 0] for _ in range(N)]
    fire_pit = deque(fire)
    while True:
        if len(fire_pit) == 1:
            break
        check = fire_pit.popleft()
        check[1] = check[1] // 2
        if check[1] == 0:
            if cnt < len(case):
                fire_pit.append(case[cnt])
                cnt += 1
                continue
            continue
        fire_pit.append(check)
    return fire_pit[0]
for tc in range(1, T+1):
    N, M = map(int, input().split())
    case_list = list(map(int, input().split()))
    case_list = [[idx+1, item] for idx, item in enumerate(case_list)]
    result = cooking(case_list)
    print(f'#{tc} {result[0]}')