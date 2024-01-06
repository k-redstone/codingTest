import sys
sys.stdin = open("./SW Expert Academy/input.txt", "r")

testSize = int(input())

for num in range (testSize):
  caseSize = int(input())
  caseList = list(map(int, input()))
  
  caseDic = {}
  maxNum = []
  for i in caseList:
    if caseDic.get(i) is None:
      caseDic[i] = 1
    else:
      caseDic[i] += 1

  for key, value in caseDic.items():
    if value == max(caseDic.values()):
      maxNum.append(key)
  print(f'#{num+1} {max(maxNum)} {max(caseDic.values())}')