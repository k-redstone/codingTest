import sys
sys.stdin = open("./SW Expert Academy/input.txt", "r")

T = int(input())


for _ in range(T):
    N = int(input())
    case_list = sorted(list(map(int,input().split())))
    result = []
    for i in range(5):
        result.append(case_list[-1 - i]) 
        result.append(case_list[0 + i])
    print(f'#{_ + 1} {" ".join(map(str, result))}')