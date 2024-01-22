import sys
sys.stdin = open("./SW Expert Academy/input.txt", "r")

T = int(input())

for _ in range(T):
    str_list= list(map(str, input().split()))
    stack_list = []

    for item in str_list:
        if item.isdecimal():
            stack_list.append(item)
        elif item == '.':
            if len(stack_list) == 1:
                result = stack_list.pop()
                print(f'#{_ + 1} {result}')
            else:
                print(f'#{_ + 1} error')
        else:
            if len(stack_list) >= 2:
                second_num = int(stack_list.pop())
                first_num = int(stack_list.pop())
                if str(first_num).isalpha() or str(second_num).isalpha():
                    print(f'#{_ + 1} error')
                    break
                if item == "/":
                    calc = first_num // second_num
                if item == "*":
                    calc = first_num * second_num
                if item == "+":
                    calc = first_num + second_num
                if item == "-":
                    calc = first_num - second_num
                stack_list.append(calc)
            else:
                print(f'#{_ + 1} error')
                break
   
