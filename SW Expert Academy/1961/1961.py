import sys
sys.stdin = open("./SW Expert Academy/input.txt", "r")

caseSize = int(input())

def rotate(len, caseList):
  newList = [[0 for j in range(len)] for i in range(len)]
  for i in range(len):
    for j in range(len):
      newList[j][len-i-1] = caseList[i][j]
  return newList

def joinList(caseList):
  newList = []
  for num in caseList:
    newList.append(''.join(list(map(str,num))))
  return newList

def printResult(len, resultList):
  for i in range(len):
    result = ''
    for j in range(3):
      result += f'{resultList[j][i]} '
    print(result)

for count in range(caseSize):
  listLength = int(input())
  caseList = [ list(map(int, input().split())) for _ in range(listLength)]
  resultList = []

  for size in range(3):
    caseList = rotate(listLength, caseList)
    resultList.append(joinList(caseList))

  print(f'#{count+1}')
  printResult(listLength, resultList)
