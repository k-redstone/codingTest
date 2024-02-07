import sys
sys.stdin = open('./input.txt', 'r')

T = 10


def notuse_func(case_list):
    stack = [0] * int(num_count)
    top = -1
    for item in case_list:
        if top == -1:
            top += 1
            stack[top] = item
            continue
        if item == stack[top]:
            top -= 1
        else:
            top += 1
            stack[top] = item
    print(f'#{tc} {"".join(map(str,stack[0:top+1]))}')


# def use_func(case_list):
#     stack = []
#     for item in case_list:
#         if not stack:
#             stack.append(item)
#         else:
#             if item == stack[-1]:
#                 stack.pop()
#             else:
#                 stack.append(item)
#     return ''.join(stack)

for tc in range(1, T+1):
    num_count, num_list = input().split()
    stack = []
    for item in num_list:
        if stack:
            if item != stack[-1]:
                stack.append(item)
            else:
                stack.pop()
        else:
            stack.append(item)
    print(f'#{tc} {"".join(stack)}')

