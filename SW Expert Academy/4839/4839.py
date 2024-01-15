import sys
sys.stdin = open("input.txt", "r")

caseSize = int(input())

def binary(num, goal):
    finish = goal
    count = 0
    first = 1
    while True:
        count += 1
        mod = int((first+finish)/2)
        if mod < num :
            first = mod
        if mod > num:
            finish = mod
        if mod == num:
            break
    return count

for count in range(caseSize):
    goal, A, B = list(map(int, input().split()))
    resultList = list(set([binary(A, goal), binary(B, goal)]))
    if len(resultList) == 1:
        result = 0
    elif resultList[0] > resultList[1]:
        result = "B"
    else:
        result = "A"
    print(f'#{count + 1} {result}')

        