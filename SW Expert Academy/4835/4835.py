import sys
sys.stdin = open("./SW Expert Academy/input.txt", "r")

testSize = int(input())

for num in range (testSize):
  caseSize, sumLen = list(map(int, input().split()))
  caseList = list(map(int, input().split()))
  sumList = []
  for i in range(caseSize - sumLen+1):
    testList = caseList[i:i+sumLen]
    sumList.append(sum(testList))

  print(f'#{num+1} {max(sumList) - min(sumList)}')