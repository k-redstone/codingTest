import sys
sys.stdin = open("./SW Expert Academy/input.txt", "r")

testSize = int(input())

def move(canMove, endPoint, stationName):
  useCount = 0
  currentPoint = 0
  full = canMove

  for i in range(len(stationName)):

    if i == len(stationName)-1:
      if currentPoint + canMove < endPoint:
        useCount += 1
        canMove = full
      if currentPoint + canMove >= endPoint:
        return useCount
    if currentPoint + full < stationName[i+1]:
      return 0
    if currentPoint + canMove < stationName[i+1]:
      useCount += 1
      canMove = full

    currentPoint = stationName[i+1]
    canMove = canMove - (currentPoint - stationName[i])

  return useCount

for size in range(testSize):
  maxMove, endPoint, stationCount = list(map(int,input().split()))
  stationName = list(map(int, input().split()))
  canMove = maxMove
  stationName.insert(0,0)
  result = move(canMove, endPoint, stationName)
  print(f'#{size+1} {result}')
