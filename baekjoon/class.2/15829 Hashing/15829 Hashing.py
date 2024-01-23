import sys
sys.stdin = open("data.txt", "r")


L = int(sys.stdin.readline().rstrip())
R = 31
M = 1234567891
case_list = sys.stdin.readline().rstrip()


alpha_dict ={}
for num in range(1, 27):
    alpha_dict[chr(96 + num)] = num

def hashing():
    num = 0
    for idx, item in enumerate(case_list):
        calc = alpha_dict[item] * (R**idx)
        num += calc
    if num > M:
        num = num % M
    return num

print(hashing())