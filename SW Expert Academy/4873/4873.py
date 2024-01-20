import sys
sys.stdin = open("./SW Expert Academy/input.txt", "r")

T = int(input())

for _ in range(T):
    str_list= list(map(str, input()))
    stack_list = []

    for item in str_list:
        if len(stack_list) == 0:
            stack_list.append(item)
        else: 
            if stack_list[-1] == item:
                stack_list.pop()
            else:
                stack_list.append(item)
    print(f'#{_ + 1} {len(stack_list)}')