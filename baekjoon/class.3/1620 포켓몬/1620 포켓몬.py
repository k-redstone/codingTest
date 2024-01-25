import sys
sys.stdin = open("data.txt", "r")

N, M = map(int,sys.stdin.readline().rstrip().split())
problem_list = [sys.stdin.readline().rstrip() for _ in range(N)]
your_list = [sys.stdin.readline().rstrip() for _ in range(M)]
problem_dict = {}

for idx, item in enumerate(problem_list):
    problem_dict[item] = idx + 1

for item in your_list:
    if item.isnumeric():
        print(problem_list[int(item) - 1])
    else:
        print(problem_dict[item])