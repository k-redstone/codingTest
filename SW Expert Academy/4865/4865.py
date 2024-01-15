import sys
sys.stdin = open("./SW Expert Academy/input.txt", "r")

T = int(input())

for _ in range(T):
    str1 =  input()
    str2 = input()
    test_dic = {}
    for num in range(len(str1)):
        test_dic[str1[num]] = 0
    for num in range(len(str2)):
        if test_dic.get(str2[num]) is not None:
            test_dic[str2[num]] += 1
    
    print(f'#{_ + 1} {max(test_dic.values())}')