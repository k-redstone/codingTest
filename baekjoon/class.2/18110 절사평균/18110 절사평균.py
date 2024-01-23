import sys
sys.stdin = open("data.txt", "r")

T = int(sys.stdin.readline().rstrip())
case_list = sorted([int(sys.stdin.readline().rstrip()) for _ in range(T)])

def round_up(num):
    if num - int(num) >= 0.5:
        return int(num) + 1
    else:
        return int(num)
    

def calc_score():
    if T == 0:
        return 0
    cut_num = T * 0.15
    cut_off = round_up(cut_num)
    if cut_off == 0:
        result = sum(case_list) / len(case_list)
        return round_up(result)
    else:
        result_list = case_list[cut_off:(cut_off * (-1))]
        result = sum(result_list) / len(result_list)
        return round_up(result)
    
print(calc_score())