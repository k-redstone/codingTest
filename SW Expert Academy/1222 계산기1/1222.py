import sys
sys.stdin = open("./input.txt", "r")
# 그래 정석으로 풀자

def calc(case):
    pointer = 2
    stack = [case[0], case[1]]
    while pointer != case_size:
        if case[pointer] != '+':
            stack.append(case[pointer])
        else:
            num1 = int(stack.pop())
            num2 = int(stack.pop())
            stack.append(num1 + num2)
        pointer += 1
    return stack[0]

for tc in range(1, 11):
    case_size = int(input())
    cnt = int((case_size - 1)/2)
    case_list = list(filter(lambda item: item != '+', input()))
    case_list.extend(['+']*cnt)
    print(f'#{tc} {calc(case_list)}')
