import sys
sys.stdin = open("./input.txt", "r")
T = int(input())
filter_word = ['(', ')', '{', '}']


def solution(string):
    stack = []
    for item in string:
        if stack:
            if item == ')':
                if stack[-1] == '(':
                    stack.pop()
                    continue
            if item == '}':
                if stack[-1] == '{':
                    stack.pop()
                    continue
        stack.append(item)
    if stack:
        return 0
    else:
        return 1

for tc in range(1, T+1):
    case_list = filter(lambda item: item in filter_word, input())
    print(f'#{tc} {solution(case_list)}')

