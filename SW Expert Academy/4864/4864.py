import sys
sys.stdin = open("./SW Expert Academy/input.txt", "r")

T = int(input())

for _ in range(T):
    str1 =  input()
    str2 = input()

    result = 0
    for num in range(len(str2) - len(str1) + 1):
        if str1 == str2[num:num + len(str1)]:
            result = 1
    print(f'#{_ + 1} {result}')