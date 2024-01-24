import sys
sys.stdin = open("data.txt", "r")


T = int(sys.stdin.readline().rstrip())
network_number = int(sys.stdin.readline().rstrip())
case_list = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(network_number)]

case_dict = {}
for item in case_list:
    if case_dict.get(item[0]) is None:
        case_dict[item[0]] = [item[1]]
    else:
        case_dict[item[0]].append(item[1])
    if case_dict.get(item[1]) is None:
        case_dict[item[1]] = [item[0]]
    else:
        case_dict[item[1]].append(item[0])

# print(case_dict)


stack_list = [1]
visited_list = []

while stack_list:
    node = stack_list.pop()
    # print(node)
    if node not in visited_list:
        visited_list.append(node)
        if case_dict.get(node) is not None:
            stack_list.append(node)
            stack_list.extend(case_dict[node])
    # print(stack_list)
print(len(visited_list) - 1)