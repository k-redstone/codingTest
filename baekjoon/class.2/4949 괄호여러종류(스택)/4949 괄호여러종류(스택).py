import sys
sys.stdin = open("data.txt", "r")

str_list = ['(',')','[',']']
def find_str(data_list):
    return list(filter(lambda data: data in str_list, data_list))


def go_stack(data):
    for item in data:
        if item == ")":
            if len(stack) == 0:
                return "no"
            elif stack[-1] == '(':
                stack.pop()
                continue
        if item == "]":
            if len(stack) == 0:
                return "no"
            elif stack[-1] == '[':
                stack.pop()
                continue
        stack.append(item)
    if len(stack) == 0:
        return "yes"
    else:
        return "no"


while True:
    case_list = list(sys.stdin.readline().rstrip())
    if len(case_list) == 0:
        break
    if case_list[0] == ".":
        break
    result_list = find_str(case_list)

    stack = []
    result = go_stack(result_list)
    print(result)