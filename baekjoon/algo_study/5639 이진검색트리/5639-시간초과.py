import sys
sys.stdin = open("./baekjoon/algo_study/5639 이진검색트리/input.txt", "r")
# input = sys.stdin.readline


def make_binary_tree(root, node):
    if node:
        if root > node:
            if dict_tree[root][0] == 0:
                dict_tree[root][0] = node
                return
            else:
                make_binary_tree(dict_tree[root][0], node)
        if root < node:
            if dict_tree[root][1] == 0:
                dict_tree[root][1] = node
                return
            else:
                make_binary_tree(dict_tree[root][1], node)

def post_order(node):   
    if node:
        post_order(dict_tree[node][0])
        post_order(dict_tree[node][1])
        print(node, sep="\n")

case_list = []
while True:
    try:
        node = int(input())
        case_list.append(node)
    except:
        break
dict_tree = {i: [0, 0] for i in case_list}
root = case_list[0]
for item in case_list:
    make_binary_tree(root, item)
post_order(root)