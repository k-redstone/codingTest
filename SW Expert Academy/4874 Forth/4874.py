import sys
sys.stdin = open("./input.txt", "r")
T = int(input())

def calc(case):
    stack = []
    for item in case:
        if item.isdigit():
            stack.append(int(item))
        elif item == '.':
            if len(stack) == 1:
                return stack.pop()
            return 'error'
        else:
            if len(stack) <= 1:
                return 'error'
            elif item == '+':
                stack.append(stack.pop() + stack.pop())
            elif item == '-':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2 - num1)
            elif item == '/':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2 // num1)
            elif item == '*':
                stack.append(stack.pop() * stack.pop())

for tc in range(1, T+1):
    case_list = input().split()
    print(f'#{tc} {calc(case_list)}')
