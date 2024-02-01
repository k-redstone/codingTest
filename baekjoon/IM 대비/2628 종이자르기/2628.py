import sys
sys.stdin = open("./baekjoon/IM 대비/2628 종이자르기/input.txt", "r")



col, row = map(int, sys.stdin.readline().split())
cut_count = int(sys.stdin.readline())
width = [0, col]
height = [0, row]
result = 0

for _ in range(cut_count):
    condition, line_num = map(int, sys.stdin.readline().split())
    if condition == 0:
        height.append(line_num)
    else:
        width.append(line_num)
        
width.sort()
height.sort()

for i in range(len(width)-1):
    for j in range(len(height)-1):
        x = width[i+1] - width[i]
        y = height[j+1] - height[j]
        result = max(result, x*y)
 
print(result)


