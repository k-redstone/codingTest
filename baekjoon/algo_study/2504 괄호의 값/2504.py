import sys
input = sys.stdin.readline


def calc():
    for item in case_list:
        temp = 0
        if item == ")" and len(stack) >= 1:
            while True:
                if len(stack) == 0:
                    stack.clear()
                    return 0
                pop_item = stack.pop()
                if pop_item == '(':
                    stack.append(str(temp*2))
                    break
                if pop_item == '[':
                    stack.clear()
                    return 0
                if pop_item.isdecimal():
                    temp += int(pop_item)
                    continue

        elif item == "]" and len(stack) >= 1:
            while True:
                if len(stack) == 0:
                    stack.clear()
                    return 0
                pop_item = stack.pop()
                if pop_item == '[':
                    stack.append(str(temp*3))
                    break
                if pop_item == '(':
                    stack.clear()
                    return 0
                if pop_item.isdecimal():
                    temp += int(pop_item)
                    continue
        else:
            stack.append(item)

    return stack

def judge():
    result = calc()
    if stack:
        for item in result:
            if not item.isdecimal():
                return print(0)
    if result:
        return print(sum(map(int, result)))
    else:
        return print(result)

case_list = list(input().strip().replace('()' , '2').replace('[]' , '3'))
stack = []
judge()