import sys
sys.stdin = open("./SW Expert Academy/input.txt", "r")

count = int(input())
divide = round(count/2 + 0.5)

numList = list(map(int, input().split()))
numList.sort()
print(numList[divide-1])