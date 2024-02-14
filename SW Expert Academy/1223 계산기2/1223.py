import sys
sys.stdin = open("./input.txt", "r")


def trans(case):
    sign = []
    trans_exp = []
    for item in case:
        if item != '+' and item != '*':
            trans_exp.append(int(item))
            continue
        if item == '+':
            while sign:
                trans_exp.append(sign.pop())
            sign.append(item)
            continue
        if item == '*':
            sign.append(item)
            continue
    while sign:
        trans_exp.append(sign.pop())
    return trans_exp


def calc(case):
    stack = []
    for item in case:
        if item != '+' and item != '*':
            stack.append(item)
            continue
        if item == '+':
            stack.append(stack.pop() + stack.pop())
            continue
        if item == '*':
            stack.append(stack.pop() * stack.pop())
            continue
    return stack[0]


for tc in range(1, 11):
    case_size = int(input())
    case_list = input()
    exp = trans(case_list)
    print(f'#{tc} {calc(exp)}')
