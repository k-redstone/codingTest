import sys

sys.stdin = open("./input.txt", "r")
T = int(input())

for tc in range(1, T+1):
    case_list = input().replace('()', 'R')
    stack = []
    cnt = 0
    for item in case_list:
        if item == 'R':
            cnt += len(stack)
            continue
        else:
            if item == '(':
                stack.append(item)
            else:
                stack.pop()
                cnt += 1
    print(f'#{tc} {cnt}')
