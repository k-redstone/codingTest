import sys
sys.stdin = open("input.txt", "r")

T = int(input().strip())

for _ in range(T):
    case_size = int(input().strip())
    case_list = []
    for num in range(case_size):
        case_list.append(tuple(map(int, input().strip().split())))
    stop_count = int(input().strip())
    stop_list = [int(input().strip()) for i in range(stop_count)]
    stop_dict = {}
    result = []

    for item in case_list:
        for i in range(item[0], item[1] + 1):
            if stop_dict.get(i) is None:
                stop_dict[i] = 1
            else:
                stop_dict[i] += 1
    for stop in stop_list:
        if stop_dict.get(stop) is not None:
            result.append(str(stop_dict[stop]))
        else:
            result.append(str(0))

    print(f'#{_ + 1 } {" ".join(result)}')
