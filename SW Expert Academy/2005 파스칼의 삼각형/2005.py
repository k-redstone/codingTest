import sys
sys.stdin = open("./input.txt", "r")
T = int(input())
def pascal(num):
    stack = []
    for count in range(1, num+1):
        result = '1'
        if count == 1:
            print(result)
            continue
        else:
            while len(stack) > 1:
                item = stack.pop()
                result += f' {int(item) + int(stack[-1])}'
        result += ' 1'
        print(result)
        stack = list(result.split())

for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc}')
    pascal(N)

