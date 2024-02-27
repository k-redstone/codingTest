import sys
input = sys.stdin.readline


def trans(case_list):
    expression = []
    sign = []
    for item in case_list:
        if item not in signs:
            expression.append(item)
        else:
            if len(sign) == 0:
                sign.append(item)
            else:
                if item == ')':
                    while True:
                        pop_item = sign.pop()
                        if pop_item == '(':
                            break
                        expression.append(pop_item)
                elif icp[item] <= isp[sign[-1]]:
                    while icp[item] <= isp[sign[-1]]:
                        expression.append(sign.pop())
                        if not sign:
                            break
                    sign.append(item)
                else:
                    sign.append(item)
    while sign:
        expression.append(sign.pop())
    return ''.join(expression)


case_list = list(input().rstrip())
signs = ['(', ')', '+', '-', '*', '/']
icp = {'(':3, '*':2, '/':2, '+':1, '-':1}
isp = {'(':0, '*':2, '/':2, '+':1, '-':1}
print(trans(case_list))