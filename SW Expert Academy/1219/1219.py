import sys
sys.stdin = open("./SW Expert Academy/input.txt", "r")

T = 10

while T > 0:
    V, E = list(map(int, input().split()))
    node = list(map(int,input().split()))
    new_dict = {}
    for num in range(0,len(node), 2):
        start = node[num]
        end = node[num + 1]
        if new_dict.get(start) == None:
                temp = [end]
                new_dict[start] = temp
        else:
            temp = new_dict.get(start)
            temp.append(end)
            new_dict[start] = temp

    goal_start = 0
    goal_end = 99
    visit_list = []
    stack_list = []

    point = goal_start
    visit_list.append(goal_start)
    stack_list.append(goal_start)


    while len(stack_list) > 0:
        if new_dict.get(point) == None or len(new_dict.get(point)) == 0:
            point = stack_list.pop()
            if new_dict.get(point) != None:
                if len(new_dict.get(point)) != 0:
                    stack_list.append(point)

        else:
            point = new_dict[point].pop(0)
            visit_list.append(point)
            stack_list.append(point)

    if goal_end in visit_list:
        print(f'#{V} 1')
    else:
        print(f'#{V} 0')

    T -= 1

