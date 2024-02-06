import sys
sys.stdin = open('./input.txt', 'r')

T = int(input())


def judge(word):
    if word == word[-1::-1]:
        return 1
    else:
        return 0


for tc in range(1, T+1):
    print(f'#{tc} {judge(input())}')