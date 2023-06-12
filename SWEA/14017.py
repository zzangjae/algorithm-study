import sys
sys.stdin = open("input.txt", "r")

t = int(input())


def preorder(node=1):

    if node not in tree:
        return [node]

    else:
        temp_lst = [node]
        for temp_node in tree[node]:
            temp_lst = temp_lst + preorder(temp_node)

        return temp_lst


for test_case_num in range(1, t+1):
    v = int(input())
    num_lst = list(map(int, input().split()))
    tree = {}

    for idx in range(v-1):
        node1, node2 = num_lst[idx * 2], num_lst[idx * 2 + 1]

        if node1 not in tree:
            tree[node1] = [node2]
        else:
            tree[node1].append(node2)

    print(f'#{test_case_num} {" ".join(map(str, preorder()))}')
