import sys
sys.stdin = open("./SW Expert Academy/input.txt", "r")

T = int(input())

for _ in range(T):
    V, E = list(map(int, input().split()))
    new_dict = {}
    for num in range(E):
        start, end = list(map(int, input().split()))
        if new_dict.get(start) == None:
            temp = [end]
            new_dict[start] = temp
        else:
            temp = new_dict.get(start)
            temp.append(end)
            new_dict[start] = temp

    goal_start, goal_end = list(map(int,input().split()))

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

    if goal_end in  visit_list:
        print(f'#{_ +1} 1')
    else:
        print(f'#{_ +1} 0')

