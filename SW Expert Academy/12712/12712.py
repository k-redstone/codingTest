import sys
sys.stdin = open("./SW Expert Academy/input.txt", "r")

caseSize = int(input())

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
crosX = [-1,1,-1,1]
crosY = [-1,-1,1,1]

def valid(num, n):
    if num < 0:
        return -1
    if num >= n:
        return -1
    return num

def method1(x,y,n, lists):
    result = lists[x][y]
    for num in range(4):
        for op in range(1, power):
            tempX = valid(x + (dx[num]* op), n)
            tempY = valid(y + (dy[num] * op), n)
            if tempX == -1 or tempY == -1:
                result += 0
            else:
                result += lists[tempX][tempY]
    return result

def method2(x,y,n, lists):
    result = lists[x][y]
    for num in range(4):
        for op in range(1, power):
            tempX = valid(x + (crosX[num] * op), n)
            tempY = valid(y + (crosY[num] * op), n)
            if tempX == -1 or tempY == -1:
                result += 0
            else:
                result += lists[tempX][tempY]
    return result


def check(lists, n):
    resultList = []
    for x in range(n):
        for y in range(n):
            resultList.append(method1(x, y, n, lists))
            resultList.append(method2(x, y, n, lists))
    return resultList                

for count in range(caseSize):
    N, power = list(map(int,input().split()))
    testList = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{count + 1} {max(check(testList,N))}')