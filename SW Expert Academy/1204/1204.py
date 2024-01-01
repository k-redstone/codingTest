import sys
sys.stdin = open("./SW Expert Academy/input.txt", "r")

testCount = int(input())

def getMode(list):
  testDic = {}
  modeList = []

  for num in list:
    if testDic.get(num) is None:
      testDic[num] = 1
    else:
      testDic[num] += 1
  for key, value in testDic.items():
    if value == max(testDic.values()):
      modeList.append(key)
  return max(modeList)
  

for count in range(testCount):
  testNum = input()
  testList = list(map(int, input().split()))
  print(f'#{count+1} {getMode(testList)}')

