import sys
sys.stdin = open("./SW Expert Academy/input.txt", "r")

caseSize = int(input())

def checkWidth(lists):
    for list in lists:
        temp = set(list)
        if len(temp) != 9:
          return 0
    return 1

def checkLen(lists):
    for i in range(9):
        numList = []
        for j in range(9):
            numList.append(lists[j][i])
        temp = set(numList)
        if len(temp) != 9:
            return 0
    return 1

def checkSquare(lists):
    for j in range(0,9,3):
        for i in range(0,9,3):
            numList = []
            for j2 in range(3):
                for i2 in range(3):
                    numList.append(lists[i+i2][j+j2])
            temp = set(numList)
            if len(temp) != 9:
                return 0
    return 1
            
for count in range(caseSize):
    caseList = [ list(map(int, input().split())) for _ in range(9)]
    a = checkWidth(caseList)
    b = checkLen(caseList)
    c = checkSquare(caseList)
    result = a+b+c
    if result == 3:
        result = 1
    else:
        result = 0
    print(f'#{count+1} {result}')